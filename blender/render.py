"""Workbench preview renders, so the mesh and the cuts can actually be looked at.

Cameras are placed by direction and always aimed at the middle of the frame, so a
new angle is one vector rather than a set of Euler angles guessed by hand.
"""

import bpy
from mathutils import Vector

CENTRE = Vector((0.5, 0.0, 0.5))

VIEWS = {
    "side":   Vector((0.0, -1.0, 0.0)),
    "threeq": Vector((-0.85, -1.0, 0.42)),
    "front":  Vector((1.0, -0.55, 0.30)),
    "rear":   Vector((-1.0, -0.55, 0.30)),
    # The animal's right. Half a cow's organs -- liver, omasum, abomasum, the whole
    # gut -- are on that side and are invisible from every other camera here.
    "rside":  Vector((0.0, 1.0, 0.0)),
    "rthreeq": Vector((-0.85, 1.0, 0.42)),
    "top":    Vector((0.0, -0.001, 1.0)),
}


def setup_scene(resolution=(1400, 900), ortho_scale=1.62):
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.render.resolution_x, scene.render.resolution_y = resolution
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False
    if not scene.world:
        scene.world = bpy.data.worlds.new("w")
    scene.world.use_nodes = False
    scene.world.color = (0.13, 0.13, 0.15)

    shading = scene.display.shading
    shading.light = 'STUDIO'
    shading.color_type = 'OBJECT'
    shading.show_shadows = False
    shading.show_cavity = True
    shading.cavity_type = 'BOTH'

    cam_data = bpy.data.cameras.new("cam")
    cam_data.type = 'ORTHO'
    cam_data.ortho_scale = ortho_scale
    cam = bpy.data.objects.new("cam", cam_data)
    bpy.context.collection.objects.link(cam)
    scene.camera = cam
    return cam


def render(cam, view, path, ortho_scale=None, distance=6.0):
    direction = VIEWS[view].normalized()
    cam.location = CENTRE + direction * distance
    cam.rotation_mode = 'QUATERNION'
    cam.rotation_quaternion = direction.to_track_quat('Z', 'Y')
    if ortho_scale:
        cam.data.ortho_scale = ortho_scale
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    return path
