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

Which cuts a muscle belongs to is **not** authored: `tools/make_anatomy_data.py`
derives it from the part's own bounding box against each tradition's rectangles, the
same overlap test the page already uses for "the same place, elsewhere". Put the part
in the right place and the cross-reference follows.

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
difference between a scapula and a coin. Wind the polygon consistently; it may be
concave.

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

Each part prints its face count and `outside`, the fraction of it poking through the
hide. Anything over 2% is flagged and is a bug: it is invisible in a side render and
the first thing you see when the page lets you orbit.

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
