bl_info = {
    "name": "MoodCurve",
    "author": "DOOURNAUX Nathan",
    "version": (0, 2),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > MoodCurve",
    "description": "Éditeur de courbes émotionnelles pour l'animation de personnages",
    "category": "Animation",
}

from . import ui_panel
from . import emotion_data
from . import csv_export
from . import emotion_graph
modules = [ui_panel, emotion_data, csv_export, emotion_graph]

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in reversed(modules):
        mod.unregister()

if __name__ == "__main__":
    register()
