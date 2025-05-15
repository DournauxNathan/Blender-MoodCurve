import bpy

class MoodKeyframe(bpy.types.PropertyGroup):
    frame: bpy.props.IntProperty()
    emotion: bpy.props.StringProperty()
    intensity: bpy.props.IntProperty()

class MoodTrack(bpy.types.PropertyGroup):
    keyframes: bpy.props.CollectionProperty(type=MoodKeyframe)

class MOODCURVE_OT_SaveKey(bpy.types.Operator):
    bl_idname = "moodcurve.save_key"
    bl_label = "Sauvegarder l'émotion"

    def execute(self, context):
        scene = context.scene
        track = scene.moodcurve_track

        # Ajout de la clé dans la collection
        new_key = track.keyframes.add()
        new_key.frame = scene.frame_current
        new_key.emotion = scene.moodcurve_emotion
        new_key.intensity = scene.moodcurve_intensity

        # Ajout d’un marker visuel sur la timeline
        marker_label = f"{new_key.emotion.capitalize()} ({new_key.intensity})"
        scene.timeline_markers.new(name=marker_label, frame=new_key.frame)

        self.report({'INFO'}, f"Émotion '{marker_label}' enregistrée à la frame {new_key.frame}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MoodKeyframe)
    bpy.utils.register_class(MoodTrack)
    bpy.utils.register_class(MOODCURVE_OT_SaveKey)
    bpy.types.Scene.moodcurve_track = bpy.props.PointerProperty(type=MoodTrack)

def unregister():
    bpy.utils.unregister_class(MoodKeyframe)
    bpy.utils.unregister_class(MoodTrack)
    bpy.utils.unregister_class(MOODCURVE_OT_SaveKey)
    del bpy.types.Scene.moodcurve_track
