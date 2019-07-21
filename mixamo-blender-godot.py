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

'''

# THE PURPOSE OF THE SCRIPT BELOW IS TO ATTEMPT TO RESIZE THE ARMATURE AND
# SCALE CORRESPONDING KEYFRAMES OF THE HIP BONE ALONG THE Y-AXIS.

bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.select_all(action = 'DESELECT')
context = bpy.context
areatype = context.area.type
context.area.type = 'GRAPH_EDITOR'
ob = context.object
bpy.context.space_data.pivot_point = 'CURSOR'
bpy.context.scene.frame_current = 1
bpy.context.space_data.cursor_position_y = 0

for action in bpy.data.actions:


    hip_bone=bpy.context.object.pose.bones['Hips']
    print('HIP BONE', hip_bone)

    dpath = hip_bone.path_from_id("location")
    hip_fcurves = [False, False, False]
    hip_fcurves[0] = action.fcurves.find(dpath, index=0)
    hip_fcurves[1] = action.fcurves.find(dpath, index=1)
    hip_fcurves[2] = action.fcurves.find(dpath, index=2)

    #action = ob.animation_data.action
    #fcurve = action.fcurves[0]
    #fcurve.select = True
    #bpy.ops.graph.handle_type(type='VECTOR')
    #context.area.type = areatype

    for hip_fcurve in hip_fcurves:
        print(hip_fcurve)
        hip_fcurve.select = True
        bpy.ops.transform.resize(value=(1, 0.01, 1), orient_type='GLOBAL', \
                orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', \
                constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, \
                proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, \
                use_proportional_projected=False)

    #for curve in action.fcurves:
    #
    #    if curve.data_path[-len("location"):] == "location":
    #        print('CURVE', curve)

'''



###############
'''
myaction = bpy.context.active_object.animation_data.action
fcurves = myaction.fcurves
rot = Euler(0,0,8)
myquat = rot.to_quaternion()


pinkyb = bpy.data.objects['MyArmature'].pose.bones['pinky02_L']
dpath = pinkyb.path_from_id("rotation_quaternion")
fc = fcurves.find(dpath, index=0)
keyframePoints = fc.keyframe_points
for keyframe in keyframePoints:
    keyframe.co[1] = myquat.w

fc = fcurves.find(dpath, index=1)
keyframePoints = fc.keyframe_points
for keyframe in keyframePoints:
    keyframe.co[1] = myquat.x

fc = fcurves.find(dpath, index=2)
keyframePoints = fc.keyframe_points
for keyframe in keyframePoints:
    keyframe.co[1] = myquat.y

fc = fcurves.find(dpath, index=3)
keyframePoints = fc.keyframe_points
for keyframe in keyframePoints:
    keyframe.co[1] = myquat.z
'''


'''
#---------------------------------------
# Clear animation frames from Bone
#
# myBone: Bone to clear
# typ: Loc/Rot/Scale
#---------------------------------------
def clearBoneAnimation(myBone,typ,fromFrame,toFrame):
     # Get current action name
    ob = bpy.context.object
    try:
        action_name = ob.animation_data.action.name
    except:
        return {'FINISHED'}

    if (action_name != None):
        a = bpy.data.actions.get(action_name)
        # Loop all f-curves
        for curve in a.fcurves:
            if curve.lock == False and curve.data_path[-len(typ):] == typ:
                if "[\"" + myBone.name in curve.data_path:
                    keyframePoints = curve.keyframe_points
                    for keyframe in keyframePoints:
                        x = keyframe.co[0] # get frame number

                        # only delete frame range
                        #if x &gt;= fromFrame and x &lt;= toFrame:
                        #    print("Removing keyframe")
                            #keyframePoints.remove(keyframe)  &lt;&lt;&lt;&lt;&lt; HOW DELETE?


# Call funcion
#print("========= Running ==================")
#clearBoneAnimation(bpy.context.active_bone,"location",5,45)

    bpy.context.space_data.dopesheet.filter_text = "hips"
    bpy.context.space_data.pivot_point = 'CURSOR'
    bpy.context.scene.frame_current = 1
    bpy.context.space_data.cursor_position_y = 0

    bpy.ops.transform.resize(value=(1, 0.01, 1), orient_type='GLOBAL', \
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', \
        constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, \
        proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
'''