import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// The cow is exported in the normalized frame of data/FRAME.md, converted to
// glTF's Y-up on the way out: x still runs tail to nose, y is up, z is across.
// Blender's -y -- the animal's left -- becomes glTF +z, which is the side the
// camera starts on and therefore the side the cutaway takes off.
const BODY_CENTRE = new THREE.Vector3(0.49, 0.46, 0);
const EXPLODE_REACH = 0.32;

const canvas = document.getElementById('view');
const tooltip = document.getElementById('tooltip');
const loading = document.getElementById('loading');

let cultures = [];
let current = null;          // the culture spec on screen
let cutsById = new Map();    // cut id -> spec, for the culture on screen
const models = new Map();    // culture id -> THREE.Group, loaded once and kept
let meshes = [];             // the pickable cut meshes of the culture on screen
let hovered = null;
let selected = null;

// The atlas has two models of one animal. `cuts` is the schematic: the carcass as a
// butcher's chart, every block a named cut. `anatomy` is what those blocks are made
// of. They share the frame, so a cut selected in one lights up the muscles it
// contains in the other, and a muscle picked in the other says which cut it lands in.
let mode = 'cuts';
let anatomy = null;          // { group, parts, byId, skin }
let anatomyLoading = null;
let anatomyMeshes = [];
let hoveredPart = null;
let selectedPart = null;

/* ------------------------------------------------------------------ scene */

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.15;
renderer.localClippingEnabled = true;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x15100e);
scene.fog = new THREE.Fog(0x15100e, 4.2, 8.5);

const camera = new THREE.PerspectiveCamera(36, 1, 0.05, 40);
camera.position.set(1.9, 1.25, 2.15);

const controls = new OrbitControls(camera, canvas);
controls.target.copy(BODY_CENTRE);
controls.enableDamping = true;
controls.dampingFactor = 0.06;
controls.minDistance = 0.85;
controls.maxDistance = 6;
controls.maxPolarAngle = Math.PI * 0.52;
controls.autoRotateSpeed = 0.9;

scene.add(new THREE.HemisphereLight(0xcfe0ff, 0x3a2a20, 0.85));

const key = new THREE.DirectionalLight(0xfff2e4, 2.1);
key.position.set(2.2, 3.4, 2.0);
key.castShadow = true;
key.shadow.mapSize.set(2048, 2048);
key.shadow.camera.near = 0.5;
key.shadow.camera.far = 12;
key.shadow.camera.left = -1.6;
key.shadow.camera.right = 1.6;
key.shadow.camera.top = 1.6;
key.shadow.camera.bottom = -1.6;
key.shadow.bias = -0.0012;
key.shadow.normalBias = 0.012;
scene.add(key);

const fill = new THREE.DirectionalLight(0x9fb6d8, 0.55);
fill.position.set(-2.4, 1.2, -1.6);
scene.add(fill);

const rim = new THREE.DirectionalLight(0xffd9b0, 0.7);
rim.position.set(-1.4, 0.8, 2.4);
scene.add(rim);

const ground = new THREE.Mesh(
  new THREE.CircleGeometry(4.5, 64).rotateX(-Math.PI / 2),
  new THREE.ShadowMaterial({ opacity: 0.42 })
);
ground.position.set(0.49, 0, 0);
ground.receiveShadow = true;
scene.add(ground);

// One plane shared by every anatomy material, so the cutaway slider is a single
// number rather than per-mesh state. Parked outside the body means "off".
const CLIP_OPEN = 0.40;
const clipPlane = new THREE.Plane(new THREE.Vector3(0, 0, -1), CLIP_OPEN);

function resize() {
  const w = canvas.clientWidth, h = canvas.clientHeight;
  if (canvas.width === w && canvas.height === h) return;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}

/* ------------------------------------------------------------ model load */

const loader = new GLTFLoader();

function loadCulture(id) {
  if (models.has(id)) return Promise.resolve(models.get(id));
  return loader.loadAsync(`models/${id}.glb`).then(gltf => {
    const group = gltf.scene;
    group.visible = false;
    group.traverse(o => {
      if (!o.isMesh) return;
      o.castShadow = true;
      o.receiveShadow = true;
      o.material = o.material.clone();
      o.material.roughness = 0.62;
      o.material.metalness = 0.0;
      o.userData.baseColour = o.material.color.clone();
      // Where the piece should fly to when the carcass is exploded: straight
      // out from the middle of the body, so neighbouring cuts separate instead
      // of sliding past each other.
      const box = new THREE.Box3().setFromObject(o);
      const centre = box.getCenter(new THREE.Vector3());
      o.userData.home = o.position.clone();
      o.userData.push = centre.sub(BODY_CENTRE).normalize();
    });
    scene.add(group);
    models.set(id, group);
    return group;
  });
}

function loadAnatomy() {
  if (anatomy) return Promise.resolve(anatomy);
  if (anatomyLoading) return anatomyLoading;
  anatomyLoading = Promise.all([
    loader.loadAsync('models/anatomy.glb'),
    fetch('data/anatomy.json').then(r => r.json()),
  ]).then(([gltf, data]) => {
    const group = gltf.scene;
    group.visible = false;
    const byId = new Map(data.parts.map(p => [p.id, p]));
    let skin = null;
    group.traverse(o => {
      if (!o.isMesh) return;
      o.material = o.material.clone();
      o.material.metalness = 0.0;
      if (o.name === 'skin') {
        skin = o;
        // Drawn last and writing no depth, so the hide is a window rather than
        // fog: every organ behind it stays fully lit and fully solid.
        o.material.transparent = true;
        o.material.opacity = 0.13;
        o.material.depthWrite = false;
        o.material.roughness = 0.85;
        o.material.side = THREE.DoubleSide;
        o.material.color.setHex(0xd8cec4);
        o.renderOrder = 20;
        o.material.clippingPlanes = [clipPlane];
        return;
      }
      const part = byId.get(o.name);
      o.castShadow = true;
      o.receiveShadow = true;
      o.material.roughness = part && part.system === 'skeleton' ? 0.42 : 0.58;
      // The cutaway slices the body open; without DoubleSide you look through an
      // opened muscle into an invisible hollow instead of at its cross-section.
      o.material.side = THREE.DoubleSide;
      o.material.clippingPlanes = [clipPlane];
      o.userData.baseColour = o.material.color.clone();
      o.userData.part = part || null;
      anatomyMeshes.push(o);
    });
    scene.add(group);
    anatomy = { group, parts: data.parts, byId, skin, missing: data.missing || [] };
    buildPartList();
    return anatomy;
  });
  return anatomyLoading;
}

/* ------------------------------------------------------------------- UI */

function esc(s) {
  return String(s ?? '').replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

// What fraction of rectangle `a` lies inside rectangle `b`, in the shared frame.
// Read three ways now: one tradition against another, a cut against the muscles
// inside it, and a muscle against the cut that contains it.
function overlapFraction(a, b) {
  const ox = Math.max(0, Math.min(a.x[1], b.x[1]) - Math.max(a.x[0], b.x[0]));
  const oz = Math.max(0, Math.min(a.z[1], b.z[1]) - Math.max(a.z[0], b.z[0]));
  const area = (a.x[1] - a.x[0]) * (a.z[1] - a.z[0]);
  return area > 0 ? (ox * oz) / area : 0;
}

function buildCultureTabs() {
  const nav = document.getElementById('cultures');
  nav.innerHTML = '';
  for (const c of cultures) {
    const b = document.createElement('button');
    b.textContent = c.culture;
    b.onclick = () => showCulture(c.id);
    b.dataset.id = c.id;
    nav.appendChild(b);
  }
}

function buildLegend() {
  document.getElementById('legend-title').textContent =
    `${current.culture} — ${current.cuts.length} cuts`;
  document.getElementById('blurb').textContent = current.blurb || '';
  const list = document.getElementById('cut-list');
  list.innerHTML = '';
  for (const cut of current.cuts) {
    const li = document.createElement('li');
    li.dataset.id = cut.id;
    const romaji = cut.romanized ? ` <span class="cut-en">${esc(cut.romanized)} · ${esc(cut.name)}</span>`
                                 : `<span class="cut-en">${esc(cut.name)}</span>`;
    const showEn = cut.native !== cut.name || cut.romanized;
    if (cut.absent) li.classList.add('absent');
    li.title = cut.absent ? 'Not carved on this model — see the panel' : '';
    li.innerHTML =
      `<span class="swatch" style="background:${esc(cut.colour)}"></span>` +
      `<span class="cut-names"><span class="cut-native">${esc(cut.native)}</span>` +
      (showEn ? romaji : '') + `</span>`;
    li.onmouseenter = () => setHover(cut.id);
    li.onmouseleave = () => setHover(null);
    li.onclick = () => select(cut.id);
    list.appendChild(li);
  }
}

const SYSTEM_LABEL = { muscle: 'Muscle', viscera: 'Organs', skeleton: 'Bone' };
const SYSTEM_ORDER = ['muscle', 'viscera', 'skeleton'];

function buildPartList() {
  const list = document.getElementById('part-list');
  list.innerHTML = '';
  for (const system of SYSTEM_ORDER) {
    const parts = anatomy.parts.filter(p => p.system === system);
    if (!parts.length) continue;
    const head = document.createElement('li');
    head.className = 'part-head';
    head.textContent = `${SYSTEM_LABEL[system] || system} — ${parts.length}`;
    list.appendChild(head);
    for (const part of parts) {
      const li = document.createElement('li');
      li.dataset.id = part.id;
      li.dataset.system = system;
      li.innerHTML =
        `<span class="swatch" style="background:${esc(part.colour || '#8e3028')}"></span>` +
        `<span class="cut-names"><span class="cut-native">${esc(part.name)}</span>` +
        (part.latin ? `<span class="cut-en">${esc(part.latin)}</span>` : '') + `</span>`;
      li.onmouseenter = () => setHoverPart(part.id);
      li.onmouseleave = () => setHoverPart(null);
      li.onclick = () => selectPart(part.id);
      list.appendChild(li);
    }
  }
  document.getElementById('part-count').textContent =
    `Anatomy — ${anatomy.parts.length} parts`;
}

// The muscles that make up a cut, and the cuts that contain a muscle, are the same
// rectangle overlap read in the two directions.
function musclesIn(cut) {
  if (!anatomy) return [];
  return anatomy.parts
    .filter(p => p.system === 'muscle')
    .map(part => ({ part, f: overlapFraction(part, cut) }))
    .filter(m => m.f >= 0.3)
    .sort((a, b) => b.f - a.f);
}

function cutsFor(part) {
  const out = [];
  for (const c of cultures) {
    const best = c.cuts
      .map(cut => ({ cut, f: overlapFraction(part, cut) }))
      .filter(o => o.f >= 0.2)
      .sort((a, b) => b.f - a.f)[0];
    if (best) out.push({ culture: c, ...best });
  }
  return out;
}

function renderDetail(cut) {
  const panel = document.getElementById('detail');
  if (!cut) { panel.hidden = true; return; }
  panel.hidden = false;

  const others = [];
  for (const c of cultures) {
    if (c.id === current.id) continue;
    const best = c.cuts
      .map(o => ({ cut: o, f: overlapFraction(cut, o) }))
      .filter(o => o.f >= 0.16)
      .sort((a, b) => b.f - a.f)
      .slice(0, 2);
    for (const b of best) others.push({ culture: c, ...b });
  }
  others.sort((a, b) => b.f - a.f);

  const dishes = (cut.dishes || []).map(d => `<span class="chip">${esc(d)}</span>`).join('');
  const elsewhere = others.map(o =>
    `<li data-culture="${esc(o.culture.id)}" data-cut="${esc(o.cut.id)}">` +
    `<span class="el-flag">${esc(o.culture.id.toUpperCase())}</span>` +
    `<span class="el-name">${esc(o.cut.native)}</span>` +
    `<span class="el-pct">${Math.round(o.f * 100)}%</span></li>`).join('');

  const madeOf = musclesIn(cut).slice(0, 8).map(m =>
    `<li data-part="${esc(m.part.id)}"><span class="el-flag">${Math.round(m.f * 100)}%` +
    `</span><span class="el-name">${esc(m.part.name)}</span>` +
    `<span class="el-pct">${esc(m.part.latin || '')}</span></li>`).join('');

  document.getElementById('detail-body').innerHTML =
    `<h3 class="d-native">${esc(cut.native)}</h3>` +
    (cut.romanized ? `<p class="d-en"><span class="d-romaji">${esc(cut.romanized)}</span> — ${esc(cut.name)}</p>`
                   : (cut.native !== cut.name ? `<p class="d-en">${esc(cut.name)}</p>` : '')) +
    `<div class="d-rule" style="background:${esc(cut.colour)}"></div>` +
    `<p class="d-body">${esc(cut.description)}</p>` +
    `<p class="d-label">Where it sits</p><p class="d-region">${esc(cut.region)}</p>` +
    (dishes ? `<p class="d-label">Known for</p><div class="chips">${dishes}</div>` : '') +
    (cut.note_no_hump
      ? `<p class="d-note">This model is a European-type animal. Cupim is the fatty
         hump of zebu cattle, which sits on top of the withers — so the shape here
         marks the spot, but the hump itself is missing.</p>` : '') +
    (cut.absent
      ? `<p class="d-note">This cut is named in the data but has no shape on the
         model: the region it was given falls outside the silhouette of this
         animal, so there was nothing there to carve. The description still
         applies.</p>` : '') +
    (cut.full_width === false
      ? `<p class="d-note">In life this is a thin sheet of muscle rather than a block.
         The atlas carves it the full width of the body, so treat the slab as
         "whereabouts", not as the shape of the cut.</p>` : '') +
    (madeOf ? `<p class="d-label">What it is made of</p>
               <ul class="elsewhere muscles">${madeOf}</ul>
               <button class="text-btn see-anatomy">Open it on the animal →</button>` : '') +
    (elsewhere ? `<p class="d-label">The same place, elsewhere</p>
                  <ul class="elsewhere">${elsewhere}</ul>` : '');

  panel.querySelectorAll('.elsewhere li[data-culture]').forEach(li => {
    li.onclick = () => showCulture(li.dataset.culture, li.dataset.cut);
  });
  panel.querySelectorAll('.elsewhere li[data-part]').forEach(li => {
    li.onclick = () => setMode('anatomy', li.dataset.part);
  });
  const jump = panel.querySelector('.see-anatomy');
  if (jump) jump.onclick = () => setMode('anatomy');
  panel.scrollTop = 0;
}

function renderPartDetail(part) {
  const panel = document.getElementById('detail');
  if (!part) { panel.hidden = true; return; }
  panel.hidden = false;

  const becomes = part.system === 'muscle' ? cutsFor(part) : [];
  const list = becomes.map(o =>
    `<li data-culture="${esc(o.culture.id)}" data-cut="${esc(o.cut.id)}">` +
    `<span class="el-flag">${esc(o.culture.id.toUpperCase())}</span>` +
    `<span class="el-name">${esc(o.cut.native)}</span>` +
    `<span class="el-pct">${Math.round(o.f * 100)}%</span></li>`).join('');

  document.getElementById('detail-body').innerHTML =
    `<h3 class="d-native">${esc(part.name)}</h3>` +
    (part.latin ? `<p class="d-en"><em>${esc(part.latin)}</em></p>` : '') +
    `<div class="d-rule" style="background:${esc(part.colour || '#8e3028')}"></div>` +
    `<p class="d-body">${esc(part.blurb)}</p>` +
    (part.beef ? `<p class="d-label">On the plate</p><p class="d-region">${esc(part.beef)}</p>` : '') +
    (list ? `<p class="d-label">Which cut it lands in</p>
             <ul class="elsewhere">${list}</ul>
             <p class="d-note">Matched by where the muscle actually sits against each
             tradition's rectangles — the same overlap the atlas uses to line one
             tradition up against another, rather than a hand-written correspondence.</p>`
          : '') +
    (part.system !== 'muscle'
      ? `<p class="d-note">Bones and organs are here for orientation, and because the
         offal is food in every tradition the atlas covers — they are not carved into
         the schematic cut models.</p>` : '');

  panel.querySelectorAll('.elsewhere li[data-culture]').forEach(li => {
    li.onclick = async () => {
      await setMode('cuts');
      showCulture(li.dataset.culture, li.dataset.cut);
    };
  });
  panel.scrollTop = 0;
}

/* ------------------------------------------------------- hover / select */

const DIMMED = new THREE.Color(0x2b2320);

function applyAppearance() {
  for (const m of meshes) {
    const isHover = hovered === m.name;
    const isSelected = selected === m.name;
    const dim = selected && !isSelected;
    m.material.color.copy(m.userData.baseColour);
    if (isHover || isSelected) m.material.color.offsetHSL(0, 0.06, 0.09);
    // Dimming by opacity looked like fog: you saw straight through to the
    // interior faces of every other cut. Darkening keeps the silhouette solid.
    if (dim) m.material.color.lerp(DIMMED, 0.8);
    m.material.emissive.setHex(isSelected ? 0x2a0d06 : 0x000000);
  }
  document.querySelectorAll('#cut-list li').forEach(li => {
    li.setAttribute('aria-selected', String(li.dataset.id === selected));
  });
}

// Which muscles are lit because a cut is selected, rather than because the part was
// picked itself. It survives the mode switch, which is the whole point of it.
let litByCut = new Set();

function applyAnatomyAppearance() {
  for (const m of anatomyMeshes) {
    const isHover = hoveredPart === m.name;
    const isSelected = selectedPart === m.name;
    const lit = litByCut.has(m.name);
    const dim = (selectedPart && !isSelected) ||
                (litByCut.size > 0 && !lit && !isSelected);
    m.material.color.copy(m.userData.baseColour);
    if (isHover || isSelected) m.material.color.offsetHSL(0, 0.06, 0.10);
    else if (lit) m.material.color.offsetHSL(0.02, 0.12, 0.06);
    if (dim) m.material.color.lerp(DIMMED, 0.72);
    m.material.emissive.setHex(isSelected ? 0x2a0d06 : (lit ? 0x1c0a06 : 0x000000));
  }
  document.querySelectorAll('#part-list li').forEach(li => {
    li.setAttribute('aria-selected', String(li.dataset.id === selectedPart));
    li.classList.toggle('lit', litByCut.has(li.dataset.id));
  });
}

function setHover(id, fromPointer = false) {
  if (hovered === id) return;
  hovered = id;
  applyAppearance();
  const cut = fromPointer && id && cutsById.get(id);
  if (!cut) { tooltip.hidden = true; return; }
  tooltip.hidden = false;
  tooltip.innerHTML = esc(cut.native) +
    (cut.native !== cut.name ? `<span class="tt-en">${esc(cut.name)}</span>` : '');
}

function setHoverPart(id, fromPointer = false) {
  if (hoveredPart === id) return;
  hoveredPart = id;
  if (anatomy) applyAnatomyAppearance();
  const part = fromPointer && id && anatomy && anatomy.byId.get(id);
  if (!part) { tooltip.hidden = true; return; }
  tooltip.hidden = false;
  tooltip.innerHTML = esc(part.name) +
    (part.latin ? `<span class="tt-en">${esc(part.latin)}</span>` : '');
}

function select(id) {
  selected = id;
  const cut = id ? cutsById.get(id) : null;
  litByCut = new Set(cut ? musclesIn(cut).map(m => m.part.id) : []);
  renderDetail(cut);
  applyAppearance();
  if (anatomy) applyAnatomyAppearance();
}

function selectPart(id) {
  selectedPart = id;
  renderPartDetail(id ? anatomy.byId.get(id) : null);
  applyAnatomyAppearance();
}

/* ------------------------------------------------------------- switching */

async function showCulture(id, focusCut = null) {
  const spec = cultures.find(c => c.id === id);
  if (!spec) return;
  const group = await loadCulture(id);

  for (const [key, g] of models) g.visible = (key === id && mode === 'cuts');
  current = spec;
  cutsById = new Map(spec.cuts.map(c => [c.id, c]));
  meshes = [];
  group.traverse(o => { if (o.isMesh) meshes.push(o); });

  document.querySelectorAll('#cultures button').forEach(b =>
    b.setAttribute('aria-current', String(b.dataset.id === id)));
  buildLegend();
  selected = null;
  hovered = null;
  tooltip.hidden = true;
  applyExplode();
  select(focusCut && cutsById.has(focusCut) ? focusCut : null);
}

async function setMode(next, focusPart = null) {
  if (next === 'anatomy' && !anatomy) {
    const note = document.getElementById('anatomy-loading');
    note.hidden = false;
    try {
      await loadAnatomy();
    } catch (err) {
      note.textContent = 'The anatomy model could not be loaded.';
      return;
    }
    note.hidden = true;
    if (selected) select(selected);       // now there is an anatomy to light up
  }
  mode = next;
  for (const [id, g] of models) {
    g.visible = (mode === 'cuts' && current !== null && id === current.id);
  }
  if (anatomy) anatomy.group.visible = (mode === 'anatomy');
  document.body.dataset.mode = mode;
  document.querySelectorAll('#modes button').forEach(b =>
    b.setAttribute('aria-current', String(b.dataset.mode === mode)));
  tooltip.hidden = true;
  hovered = null;
  hoveredPart = null;
  if (mode === 'anatomy') {
    applyLayers();
    if (focusPart) selectPart(focusPart);
    else if (selectedPart) renderPartDetail(anatomy.byId.get(selectedPart));
    else renderDetail(selected ? cutsById.get(selected) : null);
  } else {
    renderDetail(selected ? cutsById.get(selected) : null);
  }
}

/* --------------------------------------------------------------- explode */

const explodeInput = document.getElementById('explode');

function applyExplode() {
  const t = explodeInput.value / 100;
  for (const m of meshes) {
    m.position.copy(m.userData.home).addScaledVector(m.userData.push, t * EXPLODE_REACH);
  }
}

explodeInput.oninput = applyExplode;

/* ------------------------------------------------------ anatomy controls */

// Peel: 0 shows everything, 1 strips the superficial muscles, 2 leaves only the deep
// ones. Forty-odd muscles drawn at once is a red blob; being able to take the outer
// layer off is the difference between a picture and a dissection.
function applyLayers() {
  if (!anatomy) return;
  const show = {
    skin: document.getElementById('layer-skin').checked,
    muscle: document.getElementById('layer-muscle').checked,
    viscera: document.getElementById('layer-viscera').checked,
    skeleton: document.getElementById('layer-skeleton').checked,
  };
  const peel = Number(document.getElementById('peel').value);
  if (anatomy.skin) anatomy.skin.visible = show.skin;
  for (const m of anatomyMeshes) {
    const part = m.userData.part;
    const system = part ? part.system : 'muscle';
    const depth = part ? part.depth : 0;
    m.visible = !!show[system] && !(system === 'muscle' && depth < peel);
  }
  applyAnatomyAppearance();
}

function applyClip() {
  const t = Number(document.getElementById('cutaway').value) / 100;
  clipPlane.constant = CLIP_OPEN - t * 0.60;
}

for (const id of ['layer-skin', 'layer-muscle', 'layer-viscera', 'layer-skeleton']) {
  document.getElementById(id).onchange = applyLayers;
}
document.getElementById('peel').oninput = applyLayers;
document.getElementById('cutaway').oninput = applyClip;

/* ---------------------------------------------------------------- events */

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
let pointerOnCanvas = false;

canvas.addEventListener('pointermove', e => {
  pointer.set((e.clientX / innerWidth) * 2 - 1, -(e.clientY / innerHeight) * 2 + 1);
  pointerOnCanvas = true;
  tooltip.style.left = `${e.clientX}px`;
  tooltip.style.top = `${e.clientY}px`;
});
canvas.addEventListener('pointerleave', () => {
  pointerOnCanvas = false;
  setHover(null);
  setHoverPart(null);
});

let downAt = null;
canvas.addEventListener('pointerdown', e => { downAt = { x: e.clientX, y: e.clientY }; });
canvas.addEventListener('pointerup', e => {
  if (!downAt) return;
  const moved = Math.hypot(e.clientX - downAt.x, e.clientY - downAt.y);
  downAt = null;
  if (moved > 5) return;               // a drag to orbit, not a click on a cut
  const hit = pick();
  if (mode === 'anatomy') selectPart(hit ? hit.object.name : null);
  else select(hit ? hit.object.name : null);
});

function pick() {
  raycaster.setFromCamera(pointer, camera);
  if (mode !== 'anatomy') return raycaster.intersectObjects(meshes, false)[0] || null;
  // The raycaster knows nothing about clipping planes, so a part the cutaway has
  // sliced away would still answer the cursor. Drop the hits it cannot see.
  const hits = raycaster.intersectObjects(anatomyMeshes.filter(m => m.visible), false);
  return hits.find(h => clipPlane.distanceToPoint(h.point) >= 0) || null;
}

document.getElementById('detail-close').onclick = () => {
  if (mode === 'anatomy') selectPart(null); else select(null);
};
document.getElementById('reset').onclick = () => {
  camera.position.set(1.9, 1.25, 2.15);
  controls.target.copy(BODY_CENTRE);
  explodeInput.value = 0;
  applyExplode();
  document.getElementById('cutaway').value = 0;
  applyClip();
};
document.getElementById('spin').onchange = e => { controls.autoRotate = e.target.checked; };
document.getElementById('legend-toggle').onclick = e => {
  const panel = document.getElementById('legend');
  const open = panel.classList.toggle('collapsed');
  e.target.textContent = open ? '+' : '–';
  e.target.setAttribute('aria-expanded', String(!open));
};
document.getElementById('about-btn').onclick = () => document.getElementById('about').showModal();
addEventListener('keydown', e => {
  if (e.key !== 'Escape') return;
  if (mode === 'anatomy') selectPart(null); else select(null);
});
document.querySelectorAll('#modes button').forEach(b => {
  b.onclick = () => setMode(b.dataset.mode);
});

/* ------------------------------------------------------------------ loop */

function tick() {
  requestAnimationFrame(tick);
  resize();
  controls.update();
  if (pointerOnCanvas) {
    if (mode === 'anatomy' && anatomyMeshes.length) {
      const hit = pick();
      setHoverPart(hit ? hit.object.name : null, true);
    } else if (mode === 'cuts' && meshes.length) {
      const hit = pick();
      setHover(hit ? hit.object.name : null, true);
    }
  }
  renderer.render(scene, camera);
}

/* ------------------------------------------------------------------ boot */

function buildAbout() {
  const sources = cultures.map(c =>
    `<li><strong>${esc(c.culture)}</strong> — ` +
    (c.sources || []).map(u =>
      `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(new URL(u).hostname.replace(/^www\./, ''))}</a>`
    ).join(', ') + '</li>').join('');
  document.getElementById('about-body').innerHTML =
    `<p>Every tradition here is drawn on the <em>same</em> cow, in one shared coordinate
     frame, so the shapes can be compared directly. Pick a cut and the panel shows
     which cuts sit in that same piece of animal elsewhere in the world.</p>
     <p>There are two models of that animal. <strong>Cuts</strong> is the schematic one:
     the carcass as a butcher's chart, each block a named cut — honest about butchery
     lines and silent about what a block is made of. <strong>Anatomy</strong> is what
     those blocks are made of: bones, muscles and organs placed in the same frame, so
     selecting a cut lights up the muscles inside it, and picking a muscle says which
     cut it lands in everywhere.</p>
     <p>Two honest simplifications in the schematic model. Boundaries are axis-aligned
     blocks, while a real chart has some diagonal and seam-following lines. And a cut
     that is really a thin sheet of muscle — skirt, flank, hanger — is carved the full
     width of the body, because carving it thin would make it invisible. The panel says
     so when it applies.</p>
     <p>The anatomy is built procedurally from published bovine anatomy rather than
     scanned from an animal: it is right about place, proportion and arrangement, and
     it is not a dissection reference. The muscle-to-cut correspondence is measured off
     the model rather than typed in, so it cannot drift from what you are looking at.</p>
     <p>The animal is <a href="https://sketchfab.com/3d-models/cow-14e616e26823472c809a03042a94b990"
     target="_blank" rel="noopener">&ldquo;Cow&rdquo; by nandakishor.irnv</a>, used under
     <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC&nbsp;BY&nbsp;4.0</a>
     and modified: fitted to a shared coordinate frame, made watertight, and cut into
     pieces. Every tradition is carved from that same mesh, which is what lets the
     shapes be compared at all.</p>
     <p>There is a longer writeup on where the six traditions agree and disagree —
     the British false friend, the shoulder, the diaphragm —
     <a href="https://github.com/skfd/beef-atlas/blob/main/docs/differences.md"
        target="_blank" rel="noopener">here</a>.</p>
     <p class="d-label">Sources fetched for the cut data</p><ul>${sources}</ul>`;
}

fetch('data/cultures.json')
  .then(r => r.json())
  .then(async data => {
    cultures = data;
    buildCultureTabs();
    buildAbout();
    await showCulture(cultures[0].id);
    loading.classList.add('fading');
    setTimeout(() => { loading.hidden = true; }, 520);
    tick();
  })
  .catch(err => {
    loading.innerHTML = `<p>Could not load the atlas data.<br><small>${esc(err.message)}</small></p>`;
  });
