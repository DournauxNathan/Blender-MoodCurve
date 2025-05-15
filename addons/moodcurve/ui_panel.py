import bpy

class MOODCURVE_PT_Panel(bpy.types.Panel):
    bl_label = "MoodCurve"
    bl_idname = "MOODCURVE_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MoodCurve'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "moodcurve_emotion")
        layout.prop(scene, "moodcurve_intensity")
        layout.operator("moodcurve.save_key", icon='KEY_HLT')
        layout.operator("moodcurve.export_csv", icon='EXPORT')

def register():
    bpy.types.Scene.moodcurve_emotion = bpy.props.EnumProperty(
        name="Émotion",
        items=[
            ('JOY', "Joie", "Sentiment de joie"),
            ('SADNESS', "Tristesse", "Sentiment de tristesse"),
            ('ANGER', "Colère", "Sentiment de colère"),
            ('FEAR', "Peur", "Sentiment de peur"),
            ('SURPRISE', "Surprise", "Sentiment de surprise")
        ]
    )
    bpy.types.Scene.moodcurve_intensity = bpy.props.IntProperty(
        name="Intensité",
        description="Intensité de l'émotion (0 à 100)",
        default=50,
        min=0,
        max=100
    )
    bpy.utils.register_class(MOODCURVE_PT_Panel)

def unregister():
    bpy.utils.unregister_class(MOODCURVE_PT_Panel)
    del bpy.types.Scene.moodcurve_emotion
    del bpy.types.Scene.moodcurve_intensity
