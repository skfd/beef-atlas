# Authoring an anatomical part

Every bone, muscle and organ in the atlas is a JSON entry in this folder, built by
`blender/anatomy.py` out of four primitives. There is no hand-modelling and no mesh
to edit: if a part is wrong, the numbers are wrong.

Read [`../FRAME.md`](../FRAME.md) first. Every coordinate here is in that frame —
`x` 0 tail to 1 nose, `y` 0 spine plane to ±0.5 flanks, `z` 0 ground to 1 withers —
which is the whole reason a muscle can be compared against a cut.

## The files

| File | Holds |
|---|---|
| `skeleton.json` | bones, from the skull to the distal phalanges |
| `muscle.json` | skeletal muscle, plus the diaphragm |
| `viscera.json` | the four stomachs, gut, and the thoracic and abdominal organs |

Each is `{"system": "...", "sources": [...], "parts": [ ... ]}`.

## A part

```json
{
  "id": "longissimus",
  "name": "Longissimus dorsi",
  "latin": "M. longissimus thoracis et lumborum",
  "system": "muscle",
  "group": "back",
  "depth": 2,
  "mirror": true,
  "clip": true,
  "colour": "#9c2b26",
  "blurb": "The long back muscle, and the single most valuable one on the animal.",
  "beef": "Ribeye, striploin, entrecôte, 채끝 — the loin eye in every tradition.",
  "shape": [ { "t": "fusiform", ... } ]
}
```

| Key | Meaning |
|---|---|
| `id` | unique, kebab-case, the GLB object name and the page's handle on it |
| `name` / `latin` | what the panel shows; `latin` may be omitted for organs |
| `group` | for grouping in the legend: `axial`, `forelimb`, `hindlimb`, `head`, `thorax`, `abdomen`, … |
| `depth` | 0 = touching the hide, 1 = intermediate, 2 = deep. The page peels by depth. |
| `mirror` | build once for `y > 0`, then add the mirrored copy into the same object |
| `clip` | intersect with the hide shrunk inward by 12 mm. Defaults **true** for muscles. Set it for limb bones too — legs are thin. |
| `colour` | hex; omitted falls back to the system colour |
| `blurb` | one or two sentences: what it does on the living animal |
| `beef` | what it is on the plate, across traditions — omit for bone and most organs |
| `weld` | voxel size for fusing a multi-piece part, frame units, default 0.0042 |
| `shape` | one or more primitives, unioned |

Which cuts a muscle belongs to is **not** authored. `build_anatomy.py` measures each
part's bounding box after it has been carved and clipped, `tools/make_anatomy_data.py`
writes that measurement into `web/data/anatomy.json`, and the page overlaps it with
each tradition's rectangles — the same test it already uses for "the same place,
elsewhere", with one difference. A cut and a muscle are nothing like the same size,
so the page gates on the *smaller* of the two rectangles and then ranks by how much of
the *cut* the muscle fills. Dividing by the muscle instead rewards short straps: the
longissimus runs x 0.11 to 0.70 and only a fifth of it is in the US short loin, so it
would drop out of its own headline cut. Put the part in the right place and the
cross-reference follows.

## The four primitives

### `tube` — long bones, vertebrae, ribs, gut

```json
{"t": "tube",
 "pts": [[0.152,0.050,0.718], [0.185,0.064,0.610], [0.228,0.078,0.458]],
 "r":   [0.030, 0.020, 0.030],
 "flat": [1.0, 0.45],
 "ref":  [1, 0, 0],
 "seg": 14}
```

A Catmull-Rom sweep through `pts` with radius `r` at each point (a single number
applies to all). Ends are domed, so a bone end is bulbous rather than a cut pipe.

`flat` squashes the cross-section: `[1.0, 0.45]` is a flat bar. Which way it is flat
is set by `ref`, the world direction the first axis is derived from. A rib is thin
fore-and-aft, so a rib uses `"ref": [1,0,0]` with `"flat": [0.4, 1.0]`, and keeps its
flat faces aimed correctly the whole way round the chest. Round bones can ignore both.

### `fusiform` — nearly every muscle

```json
{"t": "fusiform",
 "a": [0.115,0.052,0.805], "b": [0.700,0.050,0.790],
 "w": 0.055, "d": 0.062,
 "bow": [0, 0.012, 0.018],
 "ends": 0.42, "bulge": 0.42}
```

A spindle from origin `a` to insertion `b`: `w` across the body, `d` the other way,
`ends` the fraction of that width left at each tendon (0.15 for a limb muscle with
long tendons, 0.5 for a fleshy one), `bulge` where along the run the belly is fattest
(limb muscles are proximal, so 0.35–0.45). `bow` pushes the middle sideways, which is
how a muscle wraps the rib cage instead of tunnelling through it.

**This is the shape that makes the model read as anatomy.** A muscle drawn as a
spindle looks like a muscle. Resist the urge to draw one as a box.

### `plate` — scapula, ilium, skull, diaphragm

```json
{"t": "plate",
 "poly": [[0.58,0.90], [0.68,0.88], [0.70,0.62], [0.60,0.60]],
 "y": 0.11, "thick": 0.012, "dome": 0.018}
```

A polygon given as `(x, z)` pairs in the side view, extruded across the body to
`thick`, centred on `y`. `dome` bows both faces outward in the middle, which is the
difference between a scapula and a coin — each face is built as the outline, a ring
pulled in towards the centroid and the centroid itself, and only the inner two move,
so the part still occupies exactly the rectangle you authored. Wind the polygon
consistently; it may be concave.

### `blob` — every organ

```json
{"t": "blob", "lumps": [
   [0.250,-0.055,0.640, 0.115,0.105,0.140],
   [0.380,-0.050,0.650, 0.105,0.100,0.135, 0,15,0]
]}
```

Ellipsoids — centre then radii, with optional Euler degrees — fused by a voxel remesh
into one smooth shell. Two or three lumps give a stomach its lobes. Metaballs are the
obvious tool and `blender/cow.py` records why they are the wrong one.

**Make the lumps overlap hard.** The union of two spheres of radius `r` whose centres
are `s` apart dips by about `(s/2r)²` at the join, and `smooth` will not take that out
— it sands the whole organ down instead. A chain where `r` is barely wider than `s`
comes out as a caterpillar, which is how the rumen looked for three rounds. Aim for
`r` around three times the spacing and pull the end lumps inward so the sac still
spans what you meant it to.

## Building and looking at it

One system, into a scratch folder so it does not clobber the shipped model:

```sh
~/Tools/blender-4.5/blender.exe -b --python blender/build_anatomy.py -- \
    --only muscle --preview --tag muscle --out build/test-anat/muscle
```

That writes `build/preview/anat_muscle_{side,threeq,front}.png` — a **cutaway**, with
the near half of the hide removed, so a part is always seen against the animal that
contains it. Look at the renders. A part that is never rendered is not finished.

`--part semitendinosus,biceps-femoris` builds a subset, which is much faster while
iterating on one region.

`--cut left|right|both` chooses which half of the hide comes off; `both` is the
default and also renders `anat_<tag>_rside.png` and `_rthreeq.png`. Which half matters
more than it sounds: a ruminant is not symmetric inside. The rumen fills the left of
the abdomen, and the liver, omasum, abomasum, spiral colon, caecum and both kidneys
are on the right — author those against the right-side pair or you are working blind.

Each part prints its face count and `outside`, the fraction of it poking through the
hide. Anything over 2% is flagged and is a bug: it is invisible in a side render and
the first thing you see when the page lets you orbit.

**Two things `outside` will not tell you.** It runs *after* the clip, so for anything
with `clip` on — every muscle by default — it is trivially 0.0% and means nothing. And
the clip does not trim a badly placed part so much as delete it: the EXACT boolean
against the inset hide returns a mesh with no vertices when a part is substantially
outside, and the build prints `EMPTY <id> -- clipped away entirely` and drops it. For
a clipped part, **`EMPTY` is the health signal, not `outside`.** Fit the part inside
the hide yourself and let the clip be a near-no-op.

The hide is also not the shape `FRAME.md` describes. Measured off the mesh the atlas
actually ships: the belly floor is at z ≈ 0.40 inside, not 0.49; the abdomen is
±0.155 at rumen height and ±0.185 lower down; at z 0.46 the belly is only ±0.10 wide;
the neck floor climbs steeply, with nothing below z 0.64 at x 0.78; and the cavity is
about 0.01 wider on the right all the way from x 0.34 to 0.74. The legs are posed
staggered, too — hind hooves at x 0.08 and 0.22, fore at 0.62 and 0.67, with different
y offsets — so `mirror: true` on a limb bone puts one side outside its own leg. Limb
parts carry two explicit shapes instead.

## The landmarks worth knowing

From `FRAME.md`, plus the ones a skeleton needs:

| | |
|---|---|
| pin bone (ischium) | x 0.08 |
| hip joint (acetabulum) | x 0.16, z ≈ 0.72 |
| hook bone (tuber coxae) | x 0.24, z ≈ 0.86 |
| last rib | x 0.46 |
| 5th rib | x 0.56 |
| elbow | x 0.62, z ≈ 0.55 |
| point of shoulder | x 0.72 |
| poll | x 0.80 |
| knee (carpus) and hock (tarsus) | z 0.28 |
| belly line | z ≈ 0.49 |
| topline | z ≈ 0.89, withers z ≈ 0.93 at x ≈ 0.61 |
| barrel half-width | ≈ 0.17 at the heart girth, less at the flank |

The vertebral column runs at about z 0.78–0.82 through the trunk, with the thoracic
spinous processes rising to 0.90 and highest over the withers. Cattle have 7 cervical,
13 thoracic, 6 lumbar, 5 fused sacral and about 18 caudal vertebrae, and 13 pairs of
ribs.
