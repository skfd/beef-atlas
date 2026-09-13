import bpy, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cow as cowmod, render as rendermod

c = cowmod.build_cow()
stats = cowmod.mesh_stats(c)
print("COWSTATS " + json.dumps(stats))

mat = bpy.data.materials.new("hide")
mat.diffuse_color = (0.80, 0.42, 0.38, 1.0)
c.data.materials.append(mat)
c.color = (0.80, 0.42, 0.38, 1.0)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "build", "preview")
os.makedirs(out, exist_ok=True)
cam = rendermod.setup_scene()
rendermod.render(cam, "side", os.path.join(out, "cow_side.png"))
rendermod.render(cam, "front", os.path.join(out, "cow_front.png"))
rendermod.render(cam, "threeq", os.path.join(out, "cow_3q.png"), ortho_scale=1.62)
print("PREVIEW_DONE")
