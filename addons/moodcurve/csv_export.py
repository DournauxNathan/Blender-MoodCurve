import bpy
import csv
import os

class MOODCURVE_OT_ExportCSV(bpy.types.Operator):
    bl_idname = "moodcurve.export_csv"
    bl_label = "Exporter CSV des émotions"

    def execute(self, context):
        track = context.scene.moodcurve_track
        export_path = bpy.path.abspath("//moodcurve_export.csv")

        with open(export_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Frame", "Emotion", "Intensity"])
            for key in track.keyframes:
                writer.writerow([key.frame, key.emotion, key.intensity])

        self.report({'INFO'}, f"Exporté vers : {export_path}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MOODCURVE_OT_ExportCSV)

def unregister():
    bpy.utils.unregister_class(MOODCURVE_OT_ExportCSV)
