import bpy

def apply_pose_from_library(emotion):
    obj = bpy.context.object
    if not obj or obj.type != 'ARMATURE':
        return

    pose_lib = obj.pose_library
    if not pose_lib:
        return

    for pose in pose_lib.pose_markers:
        if pose.name.lower() == emotion.lower():
            bpy.ops.poselib.apply_pose(pose_index=pose_lib.pose_markers.find(pose.name))
            break
