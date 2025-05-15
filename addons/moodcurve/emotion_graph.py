import bpy
import gpu
from gpu_extras.batch import batch_for_shader

def get_emotion_data(context):
    keys = context.scene.moodcurve_track.keyframes
    points = [(k.frame, k.intensity) for k in keys]
    return points

class MOODCURVE_PT_Graph(bpy.types.Panel):
    bl_label = "Courbe Émotionnelle"
    bl_idname = "MOODCURVE_PT_graph"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MoodCurve'

    def draw(self, context):
        layout = self.layout
        layout.template_preview(context.scene, show_buttons=False)

    def draw_header(self, context):
        self.layout.label(icon='FCURVE')

def draw_callback_px(self, context):
    region = context.region
    points = get_emotion_data(context)

    if not points:
        return

    # Normaliser les coordonnées pour l'affichage
    max_frame = max(p[0] for p in points) or 1
    max_intensity = max(p[1] for p in points) or 1

    coords = [
        (
            (p[0] / max_frame) * region.width,
            (p[1] / max_intensity) * region.height
        )
        for p in points
    ]

    shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
    shader.bind()
    shader.uniform_float("color", (1.0, 0.3, 0.3, 1.0))

    batch = batch_for_shader(shader, 'LINE_STRIP', {"pos": coords})
    batch.draw(shader)

# Registration
_draw_handler = None

def register():
    global _draw_handler
    bpy.utils.register_class(MOODCURVE_PT_Graph)
    _draw_handler = bpy.types.SpaceView3D.draw_handler_add(
        draw_callback_px, (None, bpy.context), 'WINDOW', 'POST_PIXEL')

def unregister():
    global _draw_handler
    bpy.utils.unregister_class(MOODCURVE_PT_Graph)
    if _draw_handler:
        bpy.types.SpaceView3D.draw_handler_remove(_draw_handler, 'WINDOW')
        _draw_handler = None
