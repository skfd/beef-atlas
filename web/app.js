import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// The cow is exported in the normalized frame of data/FRAME.md, converted to
// glTF's Y-up on the way out: x still runs tail to nose, y is up, z is across.
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

/* ------------------------------------------------------------------ scene */

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.15;

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

/* ------------------------------------------------------------------- UI */

function esc(s) {
  return String(s ?? '').replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

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
    (cut.full_width === false
      ? `<p class="d-note">In life this is a thin sheet of muscle rather than a block.
         The atlas carves it the full width of the body, so treat the slab as
         "whereabouts", not as the shape of the cut.</p>` : '') +
    (elsewhere ? `<p class="d-label">The same place, elsewhere</p>
                  <ul class="elsewhere">${elsewhere}</ul>` : '');

  panel.querySelectorAll('.elsewhere li').forEach(li => {
    li.onclick = () => showCulture(li.dataset.culture, li.dataset.cut);
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

function select(id) {
  selected = id;
  renderDetail(id ? cutsById.get(id) : null);
  applyAppearance();
}

/* ------------------------------------------------------------- switching */

async function showCulture(id, focusCut = null) {
  const spec = cultures.find(c => c.id === id);
  if (!spec) return;
  const group = await loadCulture(id);

  for (const [key, g] of models) g.visible = (key === id);
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

/* --------------------------------------------------------------- explode */

const explodeInput = document.getElementById('explode');

function applyExplode() {
  const t = explodeInput.value / 100;
  for (const m of meshes) {
    m.position.copy(m.userData.home).addScaledVector(m.userData.push, t * EXPLODE_REACH);
  }
}

explodeInput.oninput = applyExplode;

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
canvas.addEventListener('pointerleave', () => { pointerOnCanvas = false; setHover(null); });

let downAt = null;
canvas.addEventListener('pointerdown', e => { downAt = { x: e.clientX, y: e.clientY }; });
canvas.addEventListener('pointerup', e => {
  if (!downAt) return;
  const moved = Math.hypot(e.clientX - downAt.x, e.clientY - downAt.y);
  downAt = null;
  if (moved > 5) return;               // a drag to orbit, not a click on a cut
  const hit = pick();
  select(hit ? hit.object.name : null);
});

function pick() {
  raycaster.setFromCamera(pointer, camera);
  return raycaster.intersectObjects(meshes, false)[0] || null;
}

document.getElementById('detail-close').onclick = () => select(null);
document.getElementById('reset').onclick = () => {
  camera.position.set(1.9, 1.25, 2.15);
  controls.target.copy(BODY_CENTRE);
  explodeInput.value = 0;
  applyExplode();
};
document.getElementById('spin').onchange = e => { controls.autoRotate = e.target.checked; };
document.getElementById('legend-toggle').onclick = e => {
  const panel = document.getElementById('legend');
  const open = panel.classList.toggle('collapsed');
  e.target.textContent = open ? '+' : '–';
  e.target.setAttribute('aria-expanded', String(!open));
};
document.getElementById('about-btn').onclick = () => document.getElementById('about').showModal();
addEventListener('keydown', e => { if (e.key === 'Escape') select(null); });

/* ------------------------------------------------------------------ loop */

function tick() {
  requestAnimationFrame(tick);
  resize();
  controls.update();
  if (pointerOnCanvas && meshes.length) {
    const hit = pick();
    setHover(hit ? hit.object.name : null, true);
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
     <p>Two honest simplifications. Boundaries are axis-aligned blocks, while a real
     chart has some diagonal and seam-following lines. And a cut that is really a thin
     sheet of muscle — skirt, flank, hanger — is carved the full width of the body,
     because carving it thin would make it invisible. The panel says so when it applies.</p>
     <p>The model is procedural: a lofted cross-section profile built in Blender, then
     partitioned by each tradition's boundaries. Nothing is hand-sculpted, so the same
     animal really is underneath all six.</p>
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
