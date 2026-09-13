"""Carve the cow into each culture's cuts and export one GLB per culture.

    blender -b --python blender/build.py -- --out web/models [--only us] [--preview]

Every cut becomes its own named object inside the GLB. That is what lets the web
page raycast a single cut under the cursor, colour it, and push it out of the body
for the exploded view -- none of which works if the cultures ship as one mesh.
"""

import bpy
import bmesh
import glob
import io
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import cow as cowmod          # noqa: E402
import cuts as cutsmod        # noqa: E402
import render as rendermod    # noqa: E402


def parse_args(argv):
    args = argv[argv.index("--") + 1:] if "--" in argv else []
    out = {"out": os.path.join(ROOT, "web", "models"), "only": None, "preview": False}
    i = 0
    while i < len(args):
        if args[i] == "--out":
            out["out"] = args[i + 1]; i += 2
        elif args[i] == "--only":
            out["only"] = args[i + 1]; i += 2
        elif args[i] == "--preview":
            out["preview"] = True; i += 1
        else:
            i += 1
    return out


def make_material(name, colour):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = colour
    bsdf.inputs["Roughness"].default_value = 0.62
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.25
    mat.diffuse_color = colour
    return mat


def box_object(name, x0, x1, z0, z1, y_half=0.6):
    bpy.ops.mesh.primitive_cube_add(size=1.0)
    o = bpy.context.active_object
    o.name = name
    o.location = ((x0 + x1) / 2.0, 0.0, (z0 + z1) / 2.0)
    o.scale = (x1 - x0, y_half * 2.0, z1 - z0)
    bpy.context.view_layer.objects.active = o
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    return o


def carve(cow, name, boxes):
    """Intersect the cow with a union of boxes, returning one named object."""
    pieces = []
    for n, (x0, x1, z0, z1) in enumerate(boxes):
        piece = cow.copy()
        piece.data = cow.data.copy()
        bpy.context.collection.objects.link(piece)
        cutter = box_object(f"__cutter_{name}_{n}", x0, x1, z0, z1)

        mod = piece.modifiers.new("cut", 'BOOLEAN')
        mod.operation = 'INTERSECT'
        mod.solver = 'EXACT'
        mod.object = cutter
        bpy.context.view_layer.objects.active = piece
        bpy.ops.object.modifier_apply(modifier=mod.name)

        bpy.data.objects.remove(cutter, do_unlink=True)
        if len(piece.data.vertices) == 0:
            bpy.data.objects.remove(piece, do_unlink=True)
            continue
        pieces.append(piece)

    if not pieces:
        return None
    if len(pieces) > 1:
        bpy.ops.object.select_all(action='DESELECT')
        for p in pieces:
            p.select_set(True)
        bpy.context.view_layer.objects.active = pieces[0]
        bpy.ops.object.join()
    obj = pieces[0]
    obj.name = name
    obj.data.name = name
    bpy.ops.object.select_all(action='DESELECT')
    return obj


def build_culture(spec, out_dir, do_preview):
    started = time.time()
    cow = cowmod.build_cow(decimate_ratio=0.16)
    cow.name = "__source"
    stats_mesh = cowmod.mesh_stats(cow)

    boxes, stats = cutsmod.partition(spec["cuts"])
    colours = cutsmod.palette(len(spec["cuts"]))

    made, missing = [], []
    for idx, cut in enumerate(spec["cuts"]):
        cut_boxes = boxes.get(cut["id"])
        if not cut_boxes:
            missing.append(cut["id"])
            continue
        obj = carve(cow, cut["id"], cut_boxes)
        if obj is None:
            missing.append(cut["id"])
            continue
        mat = make_material(cut["id"], colours[idx])
        obj.data.materials.clear()
        obj.data.materials.append(mat)
        obj.color = colours[idx]
        bpy.ops.object.shade_smooth()
        made.append(obj)

    bpy.data.objects.remove(cow, do_unlink=True)

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{spec['id']}.glb")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.gltf(
        filepath=path,
        export_format='GLB',
        use_selection=True,
        export_apply=True,
        export_yup=True,
        export_materials='EXPORT',
        export_normals=True,
        export_texcoords=False,
        export_cameras=False,
        export_lights=False,
    )

    if do_preview:
        cam = rendermod.setup_scene()
        prev = os.path.join(ROOT, "build", "preview")
        os.makedirs(prev, exist_ok=True)
        rendermod.render(cam, "side", os.path.join(prev, f"cuts_{spec['id']}_side.png"))
        rendermod.render(cam, "threeq", os.path.join(prev, f"cuts_{spec['id']}_3q.png"))

    report = {
        "culture": spec["id"],
        "cuts_in_data": len(spec["cuts"]),
        "objects_exported": len(made),
        "missing": missing,
        "faces": sum(len(o.data.polygons) for o in made),
        "source_mesh": stats_mesh,
        "partition": stats,
        "glb_bytes": os.path.getsize(path),
        "seconds": round(time.time() - started, 1),
    }
    print("CULTURE " + json.dumps(report))
    return report


def main():
    opts = parse_args(sys.argv)
    specs = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "cuts_*.json"))):
        spec = json.load(io.open(f, encoding="utf-8"))
        if opts["only"] and spec["id"] != opts["only"]:
            continue
        specs.append(spec)

    reports = [build_culture(s, opts["out"], opts["preview"]) for s in specs]

    # One combined file for the page, so it makes a single fetch and its legend
    # colours are the same objects the GLB materials were built from.
    if not opts["only"]:
        sys.path.insert(0, os.path.join(ROOT, "tools"))
        import make_web_data
        make_web_data.write(ROOT)

    manifest_path = os.path.join(ROOT, "build", "build_report.json")
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    io.open(manifest_path, "w", encoding="utf-8").write(
        json.dumps(reports, indent=2, ensure_ascii=False))
    print("BUILD_DONE " + json.dumps({"cultures": len(reports)}))


main()
