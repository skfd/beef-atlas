"""Build the anatomical cow and export it as one GLB the page can layer.

    blender -b --python blender/build_anatomy.py -- [--only skeleton] [--preview]
                                       [--part longissimus] [--lod 1.0] [--raw]

Unlike the cut models there is only one of these: the animal's insides do not change
when the butchery tradition does, which is the point -- the same longissimus becomes
the American ribeye, the French entrecote and the Korean kkotdeungsim.

Every part ships as its own named object with its system in `extras`, so the page can
show or hide a whole layer, pick one muscle, or light up the muscles that make up the
cut currently selected in the schematic atlas.
"""

import bpy
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import anatomy as anat       # noqa: E402
import cow as cowmod         # noqa: E402
import render as rendermod   # noqa: E402


def parse_args(argv):
    args = argv[argv.index("--") + 1:] if "--" in argv else []
    out = {"out": os.path.join(ROOT, "web", "models"), "only": None, "part": None,
           "preview": False, "lod": 1.0, "noclip": False, "tag": None,
           "raw": False}
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--out":
            out["out"] = args[i + 1]; i += 2
        elif a == "--only":
            out["only"] = args[i + 1].split(","); i += 2
        elif a == "--part":
            out["part"] = args[i + 1].split(","); i += 2
        elif a == "--tag":
            out["tag"] = args[i + 1]; i += 2
        elif a == "--lod":
            out["lod"] = float(args[i + 1]); i += 2
        elif a == "--preview":
            out["preview"] = True; i += 1
        elif a == "--raw":
            out["raw"] = True; i += 1
        elif a == "--noclip":
            out["noclip"] = True; i += 1
        else:
            i += 1
    return out


def material(name, colour):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = colour
    bsdf.inputs["Roughness"].default_value = 0.52
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.3
    mat.diffuse_color = colour
    return mat


def hex_rgba(value, fallback):
    if not value:
        return fallback
    v = value.lstrip("#")
    return (int(v[0:2], 16) / 255.0, int(v[2:4], 16) / 255.0,
            int(v[4:6], 16) / 255.0, 1.0)


def shrink(obj):
    obj.scale = (1.0 / anat.SCALE,) * 3
    return anat._apply(obj)


def decimate(obj, ratio):
    # Small parts are left alone: a bladder is one 448-face sphere, and halving that
    # is the difference between an organ and a die.
    if ratio >= 1.0 or len(obj.data.polygons) < 1500:
        return obj
    m = obj.modifiers.new("decimate", 'DECIMATE')
    m.decimate_type = 'COLLAPSE'
    m.ratio = ratio
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=m.name)
    return obj


def halve(cow):
    """A copy of the hide with the camera-side half removed, for cutaway previews."""
    dup = cow.copy()
    dup.data = cow.data.copy()
    bpy.context.collection.objects.link(dup)
    dup.name = "__halfskin"
    bpy.ops.mesh.primitive_cube_add(size=4.0, location=(0.5, -2.0, 0.5))
    box = bpy.context.active_object
    m = dup.modifiers.new("half", 'BOOLEAN')
    m.operation = 'DIFFERENCE'
    m.solver = 'EXACT'
    m.object = box
    bpy.context.view_layer.objects.active = dup
    bpy.ops.object.modifier_apply(modifier=m.name)
    bpy.data.objects.remove(box, do_unlink=True)
    mat = material("__hide", (0.74, 0.72, 0.70, 1.0))
    dup.data.materials.clear()
    dup.data.materials.append(mat)
    dup.color = (0.74, 0.72, 0.70, 1.0)
    return dup


def main():
    opts = parse_args(sys.argv)
    started = time.time()

    cow = cowmod.build_cow(decimate_ratio=0.16)
    cow.name = "skin"
    cow.data.name = "skin"
    skin = anat.skin_at_scale(cow)
    inner = anat.inset(skin, anat.SKIN_INSET)

    specs = anat.load_specs(opts["only"] or anat.SYSTEMS)
    if opts["part"]:
        specs = [s for s in specs if s["id"] in opts["part"]]

    made, report = [], []
    for spec in specs:
        t0 = time.time()
        obj = anat.build_part(spec)
        if spec.get("clip", spec.get("system") == "muscle") and not opts["noclip"]:
            anat.clip(obj, inner)
        if not obj.data.vertices:
            print(f"EMPTY {spec['id']} -- clipped away entirely")
            bpy.data.objects.remove(obj, do_unlink=True)
            continue
        outside = anat.outside_fraction(obj, skin)
        colour = hex_rgba(spec.get("colour"),
                          anat.SYSTEM_COLOUR.get(spec.get("system"), (0.7, 0.4, 0.4, 1)))
        mat = material(spec["id"], colour)
        obj.data.materials.clear()
        obj.data.materials.append(mat)
        obj.color = colour
        shrink(obj)
        decimate(obj, opts["lod"])
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.shade_smooth()
        obj["system"] = spec.get("system", "")
        obj["depth"] = spec.get("depth", 0)
        made.append(obj)
        vs = obj.data.vertices
        # Where the part actually ended up, in frame units. The page needs this to
        # work out which cuts a muscle falls inside, using the same rectangle
        # overlap it already uses to line up one tradition against another -- so
        # the muscle-to-cut correspondence is measured off the model rather than
        # typed in and left to rot.
        bbox = [[round(min(v.co[i] for v in vs), 4) for i in range(3)],
                [round(max(v.co[i] for v in vs), 4) for i in range(3)]]
        report.append({"id": spec["id"], "system": spec.get("system"),
                       "faces": len(obj.data.polygons),
                       "outside": round(outside, 4), "bbox": bbox,
                       "seconds": round(time.time() - t0, 1)})
        flag = "  <-- OUTSIDE THE HIDE" if outside > 0.02 else ""
        print(f"PART {spec['id']:<26} {report[-1]['faces']:>6} faces  "
              f"outside {outside * 100:5.1f}%{flag}")

    bpy.data.objects.remove(inner, do_unlink=True)
    bpy.data.objects.remove(skin, do_unlink=True)

    if opts["preview"]:
        prev = os.path.join(ROOT, "build", "preview")
        os.makedirs(prev, exist_ok=True)
        # Every preview camera looks from -y, so taking that half of the hide away
        # gives the cutaway a real anatomical plate uses. A part is only right or
        # wrong relative to the animal around it; a lung floating on grey tells you
        # nothing about whether it is inside the chest. (display_type = WIRE does
        # not survive into a Workbench render, which is the obvious thing to try.)
        half = halve(cow)
        cow.hide_render = True
        cam = rendermod.setup_scene()
        tag = opts["tag"] or ("-".join(opts["only"]) if opts["only"] else "all")
        for view in ("side", "threeq", "front"):
            rendermod.render(cam, view, os.path.join(prev, f"anat_{tag}_{view}.png"))
        bpy.data.objects.remove(half, do_unlink=True)
        cow.hide_render = False

    os.makedirs(opts["out"], exist_ok=True)
    path = os.path.join(opts["out"], "anatomy.glb")
    bpy.ops.object.select_all(action='DESELECT')
    for o in made:
        o.select_set(True)
    cow.select_set(True)
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
        export_extras=True,
        # A hundred and fifteen parts at a detail the muscle bellies deserve is
        # 14 MB raw, against about 1.1 MB for a whole tradition's cut model.
        # Decimating it down to that size would cost the thing being shown;
        # Draco gets the same geometry to a comparable download, and the page
        # already loads three.js itself from the same CDN as the decoder.
        export_draco_mesh_compression_enable=not opts["raw"],
        export_draco_mesh_compression_level=6,
    )

    out = {"parts": len(made), "faces": sum(r["faces"] for r in report),
           "glb_bytes": os.path.getsize(path),
           "outside_worst": max([r["outside"] for r in report] or [0]),
           "seconds": round(time.time() - started, 1), "detail": report}
    manifest = os.path.join(ROOT, "build", "anatomy_report.json")
    os.makedirs(os.path.dirname(manifest), exist_ok=True)
    open(manifest, "w", encoding="utf-8").write(json.dumps(out, indent=2))
    if not opts["only"] and not opts["part"]:
        sys.path.insert(0, os.path.join(ROOT, "tools"))
        import make_anatomy_data
        make_anatomy_data.write(ROOT)
    print("ANATOMY_DONE " + json.dumps({k: v for k, v in out.items() if k != "detail"}))


main()
