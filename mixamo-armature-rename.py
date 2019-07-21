import bpy

# ORIGINAL MIXAMO RENAME CODE FETCHED FROM BLENDER ANSWERS (I THINK), IF YOU ARE THE AUTHOR OF THIS
# CODE, PLEASE LET ME KNOW SO THAT I CAN CREDIT YOU HERE.

print('Running Mixamo Armature Renaming Script.')
bpy.ops.object.mode_set(mode = 'OBJECT')

if not bpy.ops.object:
    print('Please select the armature')

bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
bpy.context.object.show_in_front = True

for rig in bpy.context.selected_objects:
    if rig.type == 'ARMATURE':
        for mesh in rig.children:
            for vg in mesh.vertex_groups:
                #print(vg.name)
                new_name = vg.name
                new_name = new_name.replace("mixamorig:","")
                #print(new_name)
                rig.pose.bones[vg.name].name = new_name
                vg.name = new_name
        for bone in rig.pose.bones:
            #print(bone.name.replace("mixamorig:",""))
            bone.name = bone.name.replace("mixamorig:","")



for action in bpy.data.actions:
    print(action.name)
    fc = action.fcurves
    for f in fc:
        #print(f.data_path)
        f.data_path = f.data_path.replace("mixamorig:","")