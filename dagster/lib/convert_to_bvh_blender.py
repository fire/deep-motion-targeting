import sys
import bpy

argv = sys.argv
argv = argv[argv.index("--") + 1:]
path = argv[0]
bpy.ops.import_scene.gltf(filepath=path)
armature_count = 0
for i in range(len(bpy.context.scene.objects)):
    element = bpy.context.scene.objects[i]
    if element.type != "ARMATURE":
        continue
    armature_count += 1

if armature_count > 1:
    raise AssertionError

for i in range(len(bpy.context.scene.objects)):
    element = bpy.context.scene.objects[i]
    if element.type != "ARMATURE":
        continue
    bpy.ops.export_anim.bvh(filepath=f'{path}.bvh',
                            check_existing=True, filter_glob="*.bvh",
                            global_scale=1, frame_start=0, frame_end=0, rotate_mode='NATIVE', root_transform_only=True)
    break
