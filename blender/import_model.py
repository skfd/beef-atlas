"""Fit an external cow model into the atlas frame, so a downloaded mesh can replace
the procedural one without touching a single cut rectangle.

    blender -b --python blender/import_model.py -- --input downloaded-cow.glb
    blender -b --python blender/import_model.py -- --input cow.obj --keep-largest
    blender -b --python blender/import_model.py -- --input cow.fbx --forward +X --up +Z

Reads .glb/.gltf/.obj/.fbx/.stl/.ply/.blend, works out which way the animal is
facing, scales it into the normalized frame of data/FRAME.md, welds it into one
manifold shell and writes assets/cow_normalized.blend. blender/cow.py picks that
file up automatically on the next build and every tradition is carved against the
new animal.

Orientation is detected rather than declared, because the flags are the easy thing
to get wrong and a wrong flag produces a cow lying on its side that still exports
happily. For a standing quadruped the bounding box is unambiguous -- longest axis
is nose-to-tail, shortest is across, the remaining one is up -- and the two sign
questions have reliable tells: the body is a heavy mass above thin legs, so the
centroid sits above the mid-height; and the nose end is far narrower than the
buttock. --forward/--up override the detection if it ever gets it wrong.

Whatever happens, the result is validated and the anatomy is printed against the
landmarks in FRAME.md, because a new model will not have identical proportions and
the cut data assumes those landmarks.
"""

import bpy
import bmesh
import json
import os
import sys
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

AXES = {"+X": Vector((1, 0, 0)), "-X": Vector((-1, 0, 0)),
        "+Y": Vector((0, 1, 0)), "-Y": Vector((0, -1, 0)),
        "+Z": Vector((0, 0, 1)), "-Z": Vector((0, 0, -1))}

# The frame the cut rectangles live in: nose at x=1, hooves at z=0, withers ~0.93.
TARGET_LENGTH = 1.0
TARGET_WITHERS = 0.93


def parse_args(argv):
    args = argv[argv.index("--") + 1:] if "--" in argv else []
    out = {"input": None, "forward": None, "up": None, "voxel": 0.005, "decimate": 0.0,
           "out": os.path.join(ROOT, "assets", "cow_normalized.glb"),
           "keep_largest": False}
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("--input", "--forward", "--up", "--out"):
            out[a[2:]] = args[i + 1]; i += 2
        elif a in ("--voxel", "--decimate"):
            out[a[2:]] = float(args[i + 1]); i += 2
        elif a == "--keep-largest":
            out["keep_largest"] = True; i += 1
        else:
            i += 1
    if out["forward"]:
        out["forward"] = out["forward"].upper()
    if out["up"]:
        out["up"] = out["up"].upper()
    return out


def import_any(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".blend":
        bpy.ops.wm.open_mainfile(filepath=path)
        return [o for o in bpy.context.scene.objects if o.type == 'MESH']
    bpy.ops.wm.read_factory_settings(use_empty=True)
    if ext in (".glb", ".gltf"):
        bpy.ops.import_scene.gltf(filepath=path)
    elif ext == ".obj":
        bpy.ops.wm.obj_import(filepath=path)
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=path)
    elif ext == ".stl":
        bpy.ops.wm.stl_import(filepath=path)
    elif ext == ".ply":
        bpy.ops.wm.ply_import(filepath=path)
    else:
        raise SystemExit(f"unsupported input {ext}; convert to glb/obj/fbx/stl/ply first")
    return [o for o in bpy.context.scene.objects if o.type == 'MESH']


def keep_largest_island(obj):
    """Drop all but the biggest connected piece.

    Scans arrive with plinths, ground planes and bystanders -- the CC0 Vienna
    slaughterhouse bull, for instance, is scanned together with its herdsman.
    """
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    seen, islands = set(), []
    for f in bm.faces:
        if f.index in seen:
            continue
        stack, group = [f], []
        seen.add(f.index)
        while stack:
            cur = stack.pop()
            group.append(cur)
            for e in cur.edges:
                for nf in e.link_faces:
                    if nf.index not in seen:
                        seen.add(nf.index)
                        stack.append(nf)
        islands.append(group)
    if len(islands) > 1:
        islands.sort(key=len, reverse=True)
        bmesh.ops.delete(bm, geom=[f for g in islands[1:] for f in g], context='FACES')
        bm.to_mesh(obj.data)
    bm.free()
    return len(islands)


def _bounds(obj):
    co = [v.co for v in obj.data.vertices]
    lo = Vector((min(c.x for c in co), min(c.y for c in co), min(c.z for c in co)))
    hi = Vector((max(c.x for c in co), max(c.y for c in co), max(c.z for c in co)))
    return lo, hi, hi - lo


def detect_orientation(obj):
    """Work out which model axis is nose-to-tail, which is up, and their signs."""
    lo, hi, size = _bounds(obj)
    order = sorted(range(3), key=lambda i: size[i], reverse=True)
    long_axis, up_axis, width_axis = order[0], order[1], order[2]

    verts = obj.data.vertices
    # Up sign: a standing animal is a heavy barrel carried on thin legs, so the
    # centroid sits above the middle of the bounding box.
    mid = (lo[up_axis] + hi[up_axis]) / 2.0
    centroid = sum(v.co[up_axis] for v in verts) / len(verts)
    up_sign = 1 if centroid > mid else -1

    # Nose sign: the muzzle end is far narrower than the buttock. Measure the
    # spread across the width axis in the outer eighth at each end.
    span = size[long_axis]
    lo_edge, hi_edge = lo[long_axis] + span * 0.12, hi[long_axis] - span * 0.12
    low = [abs(v.co[width_axis]) for v in verts if v.co[long_axis] <= lo_edge]
    high = [abs(v.co[width_axis]) for v in verts if v.co[long_axis] >= hi_edge]
    low_w = sum(low) / len(low) if low else 0.0
    high_w = sum(high) / len(high) if high else 0.0
    nose_sign = 1 if high_w < low_w else -1

    names = ["X", "Y", "Z"]
    return (f"{'+' if nose_sign > 0 else '-'}{names[long_axis]}",
            f"{'+' if up_sign > 0 else '-'}{names[up_axis]}",
            {"bbox": [round(v, 4) for v in size],
             "rear_mean_halfwidth": round(max(low_w, high_w), 4),
             "nose_mean_halfwidth": round(min(low_w, high_w), 4)})


def orient(obj, forward, up):
    fwd, upv = AXES[forward], AXES[up]
    if abs(fwd.dot(upv)) > 1e-6:
        raise SystemExit(f"--forward {forward} and --up {up} are not perpendicular")
    right = upv.cross(fwd)
    # Rows are the model's forward/right/up, so the product reads off a model
    # vector's components along them -- which is exactly the frame's X/Y/Z.
    obj.data.transform(Matrix((fwd, right, upv)).to_4x4())


def fit(obj):
    """Sit the animal in the frame: hooves on z=0, nose at x=1, spine on y=0."""
    lo, hi, size = _bounds(obj)
    obj.data.transform(Matrix.Translation(
        Vector((-lo.x, -(lo.y + hi.y) / 2.0, -lo.z))))
    # Uniform first, on height, so the animal is not distorted...
    s = TARGET_WITHERS / size.z
    obj.data.transform(Matrix.Diagonal((s, s, s, 1.0)))
    # ...then x alone, because the frame pins both nose and withers and a real
    # animal will not hit both at once. The stretch is reported; a few percent is
    # invisible, and anything large means the model is not a standing bovine.
    _, _, size2 = _bounds(obj)
    stretch = TARGET_LENGTH / size2.x
    obj.data.transform(Matrix.Diagonal((stretch, 1.0, 1.0, 1.0)))
    return {"uniform_scale": round(s, 5), "x_stretch": round(stretch, 4)}


def solidify(obj, voxel, decimate):
    m = obj.modifiers.new("remesh", 'REMESH')
    m.mode = 'VOXEL'
    m.voxel_size = voxel
    m.adaptivity = 0.0
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=m.name)
    if decimate and decimate < 1.0:
        m = obj.modifiers.new("decimate", 'DECIMATE')
        m.decimate_type = 'COLLAPSE'
        m.ratio = decimate
        bpy.ops.object.modifier_apply(modifier=m.name)


def landmarks(obj):
    def ray(origin, direction, comp):
        hit, loc, _, _ = obj.ray_cast(Vector(origin), Vector(direction))
        return round(loc[comp], 3) if hit else None
    rows = []
    for x in (0.05, 0.13, 0.25, 0.38, 0.50, 0.60, 0.70, 0.80, 0.90):
        rows.append({
            "x": x,
            "top": ray((x, 0, 3), (0, 0, -1), 2),
            "belly": ray((x, 0, -2), (0, 0, 1), 2),
            "half_width": ray((x, 3, 0.70), (0, -1, 0), 1),
        })
    return rows


def validate(obj, rows):
    """Catch the failures that still export happily as a valid file."""
    problems = []
    _, _, size = _bounds(obj)
    if not (0.98 <= size.x <= 1.02):
        problems.append(f"length is {size.x:.3f}, expected 1.00")
    if not (0.90 <= size.z <= 0.96):
        problems.append(f"height is {size.z:.3f}, expected {TARGET_WITHERS}")
    if size.y > 0.55 * size.z:
        problems.append(f"width {size.y:.3f} is more than half the height "
                        f"{size.z:.3f} -- the model is probably lying on its side "
                        f"or is not a standing animal")
    mid = next((r for r in rows if r["x"] == 0.50), None)
    if not mid or mid["belly"] is None or mid["top"] is None:
        problems.append("a ray down the middle of the body hit nothing at x=0.50")
    else:
        if not (0.30 <= mid["belly"] <= 0.66):
            problems.append(f"belly line at x=0.50 is {mid['belly']}, "
                            f"expected near 0.49 -- the animal may be upside down")
        if mid["top"] < 0.75:
            problems.append(f"topline at x=0.50 is {mid['top']}, expected near 0.89")
    return problems


def main():
    opts = parse_args(sys.argv)
    if not opts["input"]:
        raise SystemExit(__doc__)
    src = os.path.abspath(opts["input"])
    if not os.path.exists(src):
        raise SystemExit(f"no such file: {src}")

    meshes = import_any(src)
    if not meshes:
        raise SystemExit("the file contained no mesh objects")
    bpy.ops.object.select_all(action='DESELECT')
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    if len(meshes) > 1:
        bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "cow"
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    islands = keep_largest_island(obj) if opts["keep_largest"] else None

    guess_f, guess_u, evidence = detect_orientation(obj)
    forward = opts["forward"] or guess_f
    up = opts["up"] or guess_u
    orient(obj, forward, up)
    scaling = fit(obj)
    solidify(obj, opts["voxel"], opts["decimate"])
    refit = fit(obj)                     # the remesh moves the surface by up to a voxel
    bpy.ops.object.shade_smooth()

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    non_manifold = sum(1 for e in bm.edges if not e.is_manifold)
    bm.free()

    rows = landmarks(obj)
    problems = validate(obj, rows)

    out_glb = opts["out"] if os.path.isabs(opts["out"]) else os.path.join(ROOT, opts["out"])
    os.makedirs(os.path.dirname(out_glb), exist_ok=True)
    blend_path = os.path.splitext(out_glb)[0] + ".blend"
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    # The .blend is the handoff to cow.py, not the .glb: glTF is Y-up, so writing
    # and re-reading one would quietly stand the animal on its side. The .glb is
    # written as well, purely so the result can be checked in any 3D viewer.
    bpy.ops.wm.save_as_mainfile(filepath=blend_path, copy=True)
    bpy.ops.export_scene.gltf(filepath=out_glb, export_format='GLB',
                              use_selection=True, export_apply=True)

    print("IMPORT " + json.dumps({
        "source": src, "islands_found": islands,
        "orientation": {"used_forward": forward, "used_up": up,
                        "detected_forward": guess_f, "detected_up": guess_u,
                        "overridden": bool(opts["forward"] or opts["up"]),
                        "evidence": evidence},
        "scaling": scaling, "refit_after_remesh": refit,
        "faces": len(obj.data.polygons), "non_manifold_edges": non_manifold,
        "problems": problems, "written": [out_glb, blend_path],
    }))

    print(f"\nOriented as forward={forward} up={up} "
          f"({'given' if opts['forward'] or opts['up'] else 'detected'})")
    print("FRAME.md expects: belly ~0.49, topline ~0.89, withers ~0.93, half-width ~0.17")
    for r in rows:
        print(f"  x={r['x']:.2f}  top={r['top']}  belly={r['belly']}  "
              f"half_width={r['half_width']}")
    if problems:
        print("\nPROBLEMS -- do not build with this mesh until they are resolved:")
        for p in problems:
            print("  ! " + p)
        print("  Try --forward/--up explicitly, or --keep-largest if the file has extras.")
    else:
        print("\nOK: the mesh sits in the frame. Rebuild to carve every tradition "
              "against it.")


main()
