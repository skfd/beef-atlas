"""Build the cow mesh, directly in the normalized frame documented in data/FRAME.md.

x 0 = tail, 1 = nose.  y = 0 spine plane, +/-0.5 flanks.  z 0 = ground, 1 = withers.

The body is a loft: a run of cross-sections swept from the buttock to the nose,
each one an ellipse with its own top line, belly line and width above and below
the midline. Metaballs were the obvious tool and the wrong one -- their fields
sum, so lobes dense enough to avoid scalloping balloon the silhouette, and lobes
sparse enough to hold the silhouette scallop. A loft is smooth by construction
and every number in PROFILE is a measurement you can read off the animal.

The legs, ears, horns and tail are ordinary primitives welded on afterwards: a cow
really does have a crease where the leg leaves the body, so a seam there reads
correctly. The result is voxel-remeshed into one manifold shell, because the
boolean solver that carves the cuts needs a watertight body.

Everything is built at SCALE times life size and shrunk at the end: the remesh
voxel size is an absolute length, and at a body length of 1.0 the useful values
fall below what Blender will tessellate -- it returns an empty mesh rather than
complaining.
"""

import bpy
import bmesh
import math
import os
from mathutils import Vector

SCALE = 10.0

# If an external model has been fitted into the frame by blender/import_model.py,
# every build uses it instead of the procedural animal below. The cut data is
# written against the frame rather than against a particular mesh, so swapping
# the cow really is a drop-in -- see the landmark check that import_model prints.
IMPORTED = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "assets", "cow_normalized.blend")


def _load_imported(path):
    bpy.ops.wm.append(filepath=os.path.join(path, "Object", "cow"),
                      directory=os.path.join(path, "Object"), filename="cow")
    meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
    if not meshes:
        raise RuntimeError(f"{path} contained no object named 'cow'")
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    if len(meshes) > 1:
        bpy.ops.object.join()
    cow = bpy.context.active_object
    cow.name = "cow"
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.shade_smooth()
    return cow

# (x, top of back, belly line, half-width above the midline, half-width below)
# Read it as a side view plus a width: the first three numbers are the silhouette,
# the last two let the hindquarter carry its thighs and the barrel its gut.
PROFILE = [
    (0.020, 0.830, 0.610, 0.060, 0.070),   # rear face of the buttock
    (0.045, 0.870, 0.555, 0.105, 0.122),
    (0.080, 0.890, 0.520, 0.140, 0.162),
    (0.130, 0.900, 0.500, 0.163, 0.182),   # widest point of the round
    (0.190, 0.898, 0.495, 0.165, 0.178),
    (0.250, 0.893, 0.492, 0.155, 0.160),   # flank, the narrowest of the barrel
    (0.330, 0.890, 0.490, 0.152, 0.158),
    (0.420, 0.892, 0.488, 0.158, 0.166),
    (0.500, 0.898, 0.487, 0.168, 0.173),
    (0.560, 0.910, 0.490, 0.174, 0.175),   # heart girth, the deepest section
    (0.610, 0.930, 0.498, 0.170, 0.168),   # withers
    (0.655, 0.922, 0.520, 0.150, 0.148),
    (0.690, 0.898, 0.556, 0.120, 0.122),   # point of shoulder, brisket below
    (0.720, 0.872, 0.600, 0.104, 0.108),
    (0.755, 0.856, 0.648, 0.094, 0.100),   # throat and dewlap
    (0.795, 0.846, 0.694, 0.084, 0.090),
    (0.830, 0.840, 0.714, 0.072, 0.076),
    (0.868, 0.838, 0.722, 0.062, 0.064),   # head
    (0.905, 0.822, 0.716, 0.055, 0.055),
    (0.945, 0.796, 0.712, 0.046, 0.046),   # muzzle
    (0.980, 0.778, 0.720, 0.036, 0.034),
]

RINGS = 88          # cross-sections swept along the body
RING_VERTS = 40     # vertices around each cross-section


def _wipe():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def _apply(obj):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    return obj


def ball(location, scale, segments=24, rings=14):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1.0)
    o = bpy.context.active_object
    o.location = Vector(location) * SCALE
    o.scale = Vector(scale) * SCALE
    return _apply(o)


def strut(p0, p1, r1, r2, verts=18):
    """A tapered cylinder running from point p0 to point p1."""
    p0, p1 = Vector(p0) * SCALE, Vector(p1) * SCALE
    axis = p1 - p0
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1 * SCALE,
                                    radius2=r2 * SCALE, depth=axis.length)
    o = bpy.context.active_object
    o.location = (p0 + p1) / 2.0
    o.rotation_mode = 'QUATERNION'
    o.rotation_quaternion = axis.to_track_quat('Z', 'Y')
    return _apply(o)


def _catmull_rom(points, t):
    """Interpolate the PROFILE channels at body position t, smoothly in x."""
    xs = [p[0] for p in points]
    if t <= xs[0]:
        return points[0][1:]
    if t >= xs[-1]:
        return points[-1][1:]
    i = max(j for j in range(len(xs) - 1) if xs[j] <= t)
    u = (t - xs[i]) / (xs[i + 1] - xs[i])
    p0 = points[max(i - 1, 0)]
    p1, p2 = points[i], points[i + 1]
    p3 = points[min(i + 2, len(points) - 1)]
    out = []
    for c in range(1, 5):
        a, b, cc, d = p0[c], p1[c], p2[c], p3[c]
        out.append(0.5 * ((2 * b) + (-a + cc) * u +
                          (2 * a - 5 * b + 4 * cc - d) * u * u +
                          (-a + 3 * b - 3 * cc + d) * u * u * u))
    return out


def _build_body():
    bm = bmesh.new()
    rings = []
    for i in range(RINGS):
        t = PROFILE[0][0] + (PROFILE[-1][0] - PROFILE[0][0]) * i / (RINGS - 1)
        top, bot, hy_up, hy_lo = _catmull_rom(PROFILE, t)
        zc, hz = (top + bot) / 2.0, (top - bot) / 2.0
        ring = []
        for j in range(RING_VERTS):
            a = 2.0 * math.pi * j / RING_VERTS
            s, c = math.sin(a), math.cos(a)
            hy = hy_lo + (hy_up - hy_lo) * (s + 1.0) / 2.0
            ring.append(bm.verts.new((t * SCALE, hy * c * SCALE, (zc + hz * s) * SCALE)))
        rings.append(ring)

    for i in range(RINGS - 1):
        for j in range(RING_VERTS):
            k = (j + 1) % RING_VERTS
            bm.faces.new((rings[i][j], rings[i][k], rings[i + 1][k], rings[i + 1][j]))
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])

    me = bpy.data.meshes.new("body")
    bm.to_mesh(me)
    bm.free()
    obj = bpy.data.objects.new("body", me)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    return obj


def build_cow(voxel=0.038, smooth_iterations=3, decimate_ratio=0.28):
    _wipe()
    if os.path.exists(IMPORTED):
        return _load_imported(IMPORTED)
    parts = [_build_body()]

    for side in (1, -1):
        y_f, y_r = side * 0.092, side * 0.102
        # foreleg: the top of the strut is buried inside the chest so the flat
        # cap of the cone never shows through the brisket
        parts.append(strut((0.622, y_f, 0.700), (0.616, y_f, 0.300), 0.056, 0.032))
        parts.append(strut((0.616, y_f, 0.310), (0.614, y_f, 0.050), 0.032, 0.025))
        parts.append(ball((0.616, y_f, 0.032), (0.038, 0.029, 0.032)))
        # hind leg: the gaskin down to the hock, then the cannon bone, with the bend
        parts.append(strut((0.150, y_r, 0.690), (0.198, y_r, 0.310), 0.070, 0.031))
        parts.append(strut((0.198, y_r, 0.320), (0.176, y_r, 0.050), 0.031, 0.025))
        parts.append(ball((0.176, y_r, 0.032), (0.038, 0.029, 0.032)))
        # ear, carried out and back
        parts.append(ball((0.858, side * 0.072, 0.826), (0.030, 0.026, 0.013)))
        # horn
        parts.append(strut((0.882, side * 0.034, 0.838), (0.866, side * 0.080, 0.890),
                           0.012, 0.004, verts=10))

    # tail, hanging down the back of the round
    parts.append(strut((0.040, 0.0, 0.830), (0.012, 0.0, 0.520), 0.020, 0.009, verts=12))
    parts.append(ball((0.011, 0.0, 0.498), (0.016, 0.014, 0.032)))

    for o in parts:
        o.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.join()
    cow = bpy.context.active_object
    cow.name = "cow"

    m = cow.modifiers.new("remesh", 'REMESH')
    m.mode = 'VOXEL'
    m.voxel_size = voxel
    m.adaptivity = 0.0
    bpy.ops.object.modifier_apply(modifier=m.name)

    m = cow.modifiers.new("smooth", 'SMOOTH')
    m.factor = 1.0
    m.iterations = smooth_iterations
    bpy.ops.object.modifier_apply(modifier=m.name)

    m = cow.modifiers.new("decimate", 'DECIMATE')
    m.decimate_type = 'COLLAPSE'
    m.ratio = decimate_ratio
    bpy.ops.object.modifier_apply(modifier=m.name)

    # back down into the normalized frame the cut boxes are written in
    cow.scale = (1.0 / SCALE,) * 3
    _apply(cow)

    bpy.ops.object.shade_smooth()
    return cow


def mesh_stats(obj):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    non_manifold = sum(1 for e in bm.edges if not e.is_manifold)
    bm.free()
    return {
        "verts": len(obj.data.vertices),
        "faces": len(obj.data.polygons),
        "non_manifold_edges": non_manifold,
        "bbox_min": tuple(round(min(v.co[i] for v in obj.data.vertices), 3) for i in range(3)),
        "bbox_max": tuple(round(max(v.co[i] for v in obj.data.vertices), 3) for i in range(3)),
    }
