"""Build the cow's insides: bones, muscles and viscera, in the frame of data/FRAME.md.

The schematic atlas carves the animal into axis-aligned blocks. That is honest about
butchery lines and says nothing about what the block is *made of*. This module builds
the other half: named anatomical parts -- 13 rib pairs, the longissimus that becomes
the ribeye, the rumen that fills the left flank -- so a cut can be shown as the muscles
it actually contains.

Nothing here is modelled by hand. Every part is a few entries in data/anatomy/*.json
made of four primitives, because a vocabulary small enough to keep in your head is what
lets sixty parts get authored against the same landmarks:

    tube     a swept polyline with a per-point radius and an optionally flattened
             cross-section -- long bones, vertebrae, ribs, the tail, the gut coil
    fusiform sugar over tube: a spindle bowed from origin to insertion. Nearly every
             skeletal muscle is this shape, which is the whole realism lever; a muscle
             drawn as a spindle reads as a muscle, and one drawn as a box does not
    plate    a polygon in the side view given a thickness and a dome -- scapula,
             ilium, the flat of the skull, the diaphragm
    blob     an ellipsoid plus lumps, remeshed into one smooth shell -- every organ

Two things then make it anatomical rather than a bag of shapes:

  * superficial muscles are intersected with the skin shrunk inward, exactly as
    blender/cuts.py intersects boxes with the body. The outer surface of the muscle
    layer is then the real animal's contour instead of a row of bulges.
  * every part is checked to lie inside the skin, because a limb bone that pokes out
    through the elbow is invisible in a side render and obvious the moment the page
    lets you orbit.

Same SCALE trap as cow.py: remesh voxel size is an absolute length, so everything is
built ten times life size and shrunk at the end.
"""

import bmesh
import bpy
import json
import math
import os
from mathutils import Vector

SCALE = 10.0

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "anatomy")

# How far inside the hide the muscle layer is allowed to reach. A beef animal wears
# 8-15mm of subcutaneous fat and hide over the round and loin; on a 2.4m frame that is
# about 0.005, and 0.012 also buys room for the error in a procedural muscle.
SKIN_INSET = 0.012

SYSTEMS = ("skeleton", "muscle", "viscera")

SYSTEM_COLOUR = {
    "skeleton": (0.898, 0.871, 0.796, 1.0),
    "muscle": (0.604, 0.169, 0.153, 1.0),
    "viscera": (0.686, 0.404, 0.408, 1.0),
}


# --------------------------------------------------------------------- helpers

def _link(bm, name):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    obj = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(obj)
    return obj


def _apply(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    obj.select_set(False)
    return obj


def _cr(p0, p1, p2, p3, u):
    """Catmull-Rom; works on Vectors and on floats, both support the arithmetic."""
    return 0.5 * ((2.0 * p1) + (-p0 + p2) * u +
                  (2.0 * p0 - 5.0 * p1 + 4.0 * p2 - p3) * u * u +
                  (-p0 + 3.0 * p1 - 3.0 * p2 + p3) * u * u * u)


def _resample(points, radii, n):
    pts = [Vector(p) * SCALE for p in points]
    rad = [float(r) * SCALE for r in radii]
    m = len(pts)
    if m < 2:
        raise ValueError("a tube needs at least two points")
    if m == 2:
        pts = [pts[0], pts[0].lerp(pts[1], 0.5), pts[1]]
        rad = [rad[0], (rad[0] + rad[1]) / 2.0, rad[1]]
        m = 3
    segs = m - 1
    out_p, out_r = [], []
    for i in range(n):
        t = (i / (n - 1)) * segs
        k = min(int(t), segs - 1)
        u = t - k
        a, b = max(k - 1, 0), min(k + 2, m - 1)
        out_p.append(_cr(pts[a], pts[k], pts[k + 1], pts[b], u))
        out_r.append(max(_cr(rad[a], rad[k], rad[k + 1], rad[b], u), 1e-4))
    return out_p, out_r


def _frames(pts, ref):
    """Cross-section axes along the sweep, taken from a fixed world direction.

    Parallel transport would twist freely, which is fine for a round bone and wrong
    for a flat one: a rib has to keep its flat faces pointing fore and aft the whole
    way round the chest. Deriving the frame from a reference each step keeps a
    flattened section aimed where the data says.
    """
    n = len(pts)
    ref = Vector(ref).normalized()
    alt = Vector((0.0, 0.0, 1.0)) if abs(ref.z) < 0.9 else Vector((1.0, 0.0, 0.0))
    us, vs = [], []
    for i in range(n):
        if i == 0:
            t = pts[1] - pts[0]
        elif i == n - 1:
            t = pts[-1] - pts[-2]
        else:
            t = pts[i + 1] - pts[i - 1]
        t.normalize()
        r = ref if abs(t.dot(ref)) < 0.94 else alt
        u = r - t * r.dot(t)
        u.normalize()
        us.append(u)
        vs.append(t.cross(u).normalized())
    return us, vs


def _sweep(bm, pts, rad, us, vs, flat, seg, cap):
    rings = []
    for i, p in enumerate(pts):
        ring = []
        for j in range(seg):
            a = 2.0 * math.pi * j / seg
            off = (us[i] * (math.cos(a) * rad[i] * flat[0]) +
                   vs[i] * (math.sin(a) * rad[i] * flat[1]))
            ring.append(bm.verts.new(p + off))
        rings.append(ring)
    for i in range(len(rings) - 1):
        for j in range(seg):
            k = (j + 1) % seg
            bm.faces.new((rings[i][j], rings[i][k], rings[i + 1][k], rings[i + 1][j]))

    for end in (0, 1):
        i = 0 if end == 0 else len(pts) - 1
        ring = rings[i]
        if cap != "round":
            bm.faces.new(list(reversed(ring)) if end == 0 else ring)
            continue
        # A dome rather than a lid: bone ends are bulbous, and a flat disc on the end
        # of a femur reads as a pipe.
        axis = (pts[0] - pts[1]) if end == 0 else (pts[-1] - pts[-2])
        axis = axis.normalized()
        prev = ring
        for shrink, push in ((0.80, 0.40), (0.48, 0.68)):
            cur = []
            for j in range(seg):
                a = 2.0 * math.pi * j / seg
                off = (us[i] * (math.cos(a) * rad[i] * flat[0] * shrink) +
                       vs[i] * (math.sin(a) * rad[i] * flat[1] * shrink))
                cur.append(bm.verts.new(pts[i] + off + axis * rad[i] * push))
            for j in range(seg):
                k = (j + 1) % seg
                quad = (prev[j], prev[k], cur[k], cur[j])
                bm.faces.new(reversed(quad) if end == 0 else quad)
            prev = cur
        tip = bm.verts.new(pts[i] + axis * rad[i] * 0.86)
        for j in range(seg):
            k = (j + 1) % seg
            tri = (prev[j], prev[k], tip)
            bm.faces.new(reversed(tri) if end == 0 else tri)


# ------------------------------------------------------------------ primitives

def tube(pts, r, flat=(1.0, 1.0), ref=(0.0, 1.0, 0.0), seg=14, samples=None,
         cap="round", name="tube"):
    """A swept polyline. `r` is one radius per point; `flat` squashes the section."""
    if isinstance(r, (int, float)):
        r = [r] * len(pts)
    n = samples or max(9, 6 * (len(pts) - 1) + 3)
    p, rr = _resample(pts, r, n)
    us, vs = _frames(p, ref)
    bm = bmesh.new()
    _sweep(bm, p, rr, us, vs, tuple(flat), seg, cap)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _link(bm, name)


def fusiform(a, b, w, d=None, bow=(0.0, 0.0, 0.0), ends=0.18, bulge=0.5,
             ref=(0.0, 1.0, 0.0), seg=14, name="muscle"):
    """A spindle from origin to insertion: thin at both tendons, thick in the belly.

    `bow` displaces the middle of the run, so a muscle can wrap the rib cage instead
    of tunnelling through it. `bulge` slides the fattest point along the run -- limb
    muscles are fattest near the body, so theirs sits below 0.5.
    """
    a, b = Vector(a), Vector(b)
    d = w if d is None else d
    bow = Vector(bow)
    bulge = min(max(bulge, 0.08), 0.92)
    power = math.log(0.5) / math.log(bulge)
    pts, rad = [], []
    n = 11
    for i in range(n):
        t = i / (n - 1)
        # a hump peaking at t == bulge and falling to `ends` at either tendon
        s = math.sin(math.pi * (t ** power))
        pts.append(a.lerp(b, t) + bow * (4.0 * t * (1.0 - t)))
        rad.append(ends + (1.0 - ends) * s)
    big = max(w, d)
    return tube(pts, [x * big for x in rad], flat=(w / big, d / big), ref=ref, seg=seg,
                cap="round", samples=34, name=name)


def plate(poly, y, thick, dome=0.0, name="plate"):
    """A polygon in the side view -- (x, z) pairs -- given a thickness across the body.

    `dome` bows the faces outward in the middle, which is what turns a flat cutout
    into a scapula rather than a coin.
    """
    pts = [Vector((p[0], 0.0, p[1])) * SCALE for p in poly]
    cx = sum(p.x for p in pts) / len(pts)
    cz = sum(p.z for p in pts) / len(pts)
    spread = max(max(abs(p.x - cx) for p in pts),
                 max(abs(p.z - cz) for p in pts)) or 1.0
    bm = bmesh.new()
    rings = []
    for sign in (1, -1):
        ring = []
        for p in pts:
            d = math.hypot(p.x - cx, p.z - cz) / spread
            lift = dome * SCALE * max(0.0, 1.0 - d * d)
            ring.append(bm.verts.new((p.x,
                                      y * SCALE + sign * (thick * SCALE / 2.0 + lift),
                                      p.z)))
        rings.append(ring)
    bm.faces.new(rings[0])
    bm.faces.new(list(reversed(rings[1])))
    n = len(pts)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((rings[0][i], rings[0][j], rings[1][j], rings[1][i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _link(bm, name)


def blob(lumps, name="organ", voxel=0.0042, smooth=3):
    """An ellipsoid, or several, fused into one smooth shell.

    Metaballs are the obvious tool for an organ and cow.py already records why they
    are the wrong one: their fields sum, so a second lobe swells the first. Spheres
    plus a voxel remesh give the same smooth union at the sizes you asked for.

    `voxel` is in frame units, so 0.0042 is about a centimetre on a real animal --
    coarse enough to stay cheap, fine enough that a stomach is not a football.

    Each lump is [cx, cy, cz, rx, ry, rz] with optional [rot_x, rot_y, rot_z] degrees.
    """
    parts = []
    for lump in lumps:
        cx, cy, cz, rx, ry, rz = lump[:6]
        bpy.ops.mesh.primitive_uv_sphere_add(segments=28, ring_count=16, radius=1.0)
        o = bpy.context.active_object
        o.location = Vector((cx, cy, cz)) * SCALE
        o.scale = Vector((rx, ry, rz)) * SCALE
        if len(lump) > 6:
            o.rotation_euler = [math.radians(a) for a in (list(lump[6:9]) + [0, 0, 0])[:3]]
        parts.append(_apply(o))
    bpy.ops.object.select_all(action='DESELECT')
    for o in parts:
        o.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    if len(parts) > 1:
        bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = name
    if len(parts) > 1:
        m = obj.modifiers.new("remesh", 'REMESH')
        m.mode = 'VOXEL'
        m.voxel_size = voxel * SCALE
        m.adaptivity = 0.0
        bpy.ops.object.modifier_apply(modifier=m.name)
        if smooth:
            m = obj.modifiers.new("smooth", 'SMOOTH')
            m.factor = 1.0
            m.iterations = smooth
            bpy.ops.object.modifier_apply(modifier=m.name)
    obj.select_set(False)
    return obj


PRIMITIVES = {"tube": tube, "fusiform": fusiform, "plate": plate, "blob": blob}


# ------------------------------------------------------------ part assembly

def _join(objs, name):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    if len(objs) > 1:
        bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = name
    obj.data.name = name
    obj.select_set(False)
    return obj


def _mirror(obj):
    """Add the other side of a paired part into the same object.

    One object per part rather than two, because the page highlights a muscle, not a
    left muscle: picking either side should light both.
    """
    dup = obj.copy()
    dup.data = obj.data.copy()
    bpy.context.collection.objects.link(dup)
    dup.scale = (1.0, -1.0, 1.0)
    _apply(dup)
    bpy.context.view_layer.objects.active = dup
    bpy.ops.object.select_all(action='DESELECT')
    dup.select_set(True)
    bpy.ops.mesh.customdata_custom_splitnormals_clear()
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.flip_normals()
    bpy.ops.object.mode_set(mode='OBJECT')
    dup.select_set(False)
    return _join([obj, dup], obj.name)


def build_part(spec):
    """Turn one JSON entry into one named object, still at SCALE."""
    pieces = []
    for n, shape in enumerate(spec["shape"]):
        kind = shape["t"]
        fn = PRIMITIVES.get(kind)
        if fn is None:
            raise ValueError(f"{spec['id']}: unknown primitive {kind!r}")
        kwargs = {k: v for k, v in shape.items() if k != "t"}
        kwargs["name"] = f"{spec['id']}_{n}"
        pieces.append(fn(**kwargs))
    obj = _join(pieces, spec["id"])
    if spec.get("weld") or len(pieces) > 1:
        # Overlapping shells confuse the boolean solver and shade badly. A voxel pass
        # is the cheapest way to make a multi-piece part one surface; parts that are
        # a single primitive skip it and keep their clean topology.
        if len(pieces) > 1:
            m = obj.modifiers.new("weld", 'REMESH')
            m.mode = 'VOXEL'
            m.voxel_size = float(spec.get("weld", 0.0042)) * SCALE
            m.adaptivity = 0.0
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier=m.name)
            m = obj.modifiers.new("smooth", 'SMOOTH')
            m.factor = 1.0
            m.iterations = int(spec.get("smooth", 3))
            bpy.ops.object.modifier_apply(modifier=m.name)
    if spec.get("mirror"):
        obj = _mirror(obj)
    return obj


def load_specs(systems=SYSTEMS):
    """Read data/anatomy/*.json, in the order the files declare."""
    out = []
    for system in systems:
        path = os.path.join(DATA, f"{system}.json")
        if not os.path.exists(path):
            continue
        doc = json.load(open(path, encoding="utf-8"))
        for part in doc["parts"]:
            part.setdefault("system", system)
            out.append(part)
    return out


# ------------------------------------------------------------- skin and fit

def skin_at_scale(cow):
    """A copy of the animal blown up to SCALE, to boolean the parts against."""
    dup = cow.copy()
    dup.data = cow.data.copy()
    bpy.context.collection.objects.link(dup)
    dup.name = "__skin"
    dup.scale = (SCALE, SCALE, SCALE)
    return _apply(dup)


def inset(obj, amount, name="__inner"):
    """Shrink a closed mesh along its own normals -- the inside face of the hide."""
    dup = obj.copy()
    dup.data = obj.data.copy()
    bpy.context.collection.objects.link(dup)
    dup.name = name
    bm = bmesh.new()
    bm.from_mesh(dup.data)
    bm.normal_update()
    for v in bm.verts:
        v.co -= v.normal * (amount * SCALE)
    bm.to_mesh(dup.data)
    bm.free()
    return dup


def clip(obj, cutter):
    """Intersect a part with the inner face of the hide, as cuts.py does with boxes."""
    mod = obj.modifiers.new("clip", 'BOOLEAN')
    mod.operation = 'INTERSECT'
    mod.solver = 'EXACT'
    mod.object = cutter
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=mod.name)
    return obj


def outside_fraction(obj, skin):
    """How much of a part sticks out through the hide.

    A side render cannot show this -- a femur poking through the elbow looks fine from
    the side and is the first thing you see when the page lets you orbit. The skin is
    watertight, so the sign of (hit - point) . normal settles each vertex.
    """
    verts = obj.data.vertices
    if not verts:
        return 1.0
    step = max(1, len(verts) // 900)
    out = 0
    tested = 0
    for i in range(0, len(verts), step):
        p = verts[i].co
        ok, loc, nrm, _ = skin.closest_point_on_mesh(p)
        tested += 1
        if not ok or (p - loc).dot(nrm) > 0.004 * SCALE:
            out += 1
    return out / max(tested, 1)
