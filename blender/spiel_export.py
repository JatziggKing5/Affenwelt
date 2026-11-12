bl_info = {
    "name": "Ins Spiel exportieren",
    "author": "Mein erstes Spiel",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "3D-Fenster > Seitenleiste (N) > Spiel",
    "description": "Speichert die Modelle der Szene 'Spiel-Objekte' als modelle/spiel.glb ins Spiel – automatisch bei jedem Speichern",
    "category": "Import-Export",
}

import os

import bpy
from bpy.app.handlers import persistent

SZENE = "Spiel-Objekte"
NICHT_EXPORTIEREN = {"Boden"}  # Hilfs-Objekte, die nicht ins Spiel gehören


def ziel_datei():
    """modelle/spiel.glb im Spielordner (die .blend-Datei liegt in mein-spiel/blender/)."""
    if not bpy.data.filepath:
        return None
    spiel_ordner = os.path.dirname(os.path.dirname(bpy.data.filepath))
    return os.path.join(spiel_ordner, "modelle", "spiel.glb")


def exportieren():
    szene = bpy.data.scenes.get(SZENE)
    ziel = ziel_datei()
    if szene is None or ziel is None:
        return None
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    # Nur exportieren, wenn gerade die Szene "Spiel-Objekte" offen ist
    # (eine andere Szene "umzubiegen" bringt Blender zum Absturz).
    if bpy.context.scene != szene:
        print(f"[Spiel] Bitte die Szene '{SZENE}' öffnen, dann wird exportiert.")
        return None
    objekte = [o for o in szene.objects
               if o.type not in {"LIGHT", "CAMERA"} and o.name not in NICHT_EXPORTIEREN]
    # Auswahl merken, exportieren, Auswahl wiederherstellen
    vorher = {o.name: o.select_get() for o in szene.objects}
    for o in szene.objects:
        o.select_set(o in objekte)
    try:
        bpy.ops.export_scene.gltf(
            filepath=ziel,
            export_format="GLB",
            use_selection=True,
            export_yup=True,
            export_apply=False,
            export_cameras=False,
            export_lights=False,
            export_animations=False,
        )
    finally:
        for o in szene.objects:
            if o.name in vorher:
                o.select_set(vorher[o.name])
    return ziel


def _spaeter_exportieren():
    try:
        ziel = exportieren()
        if ziel:
            print(f"[Spiel] Modelle exportiert nach {ziel}")
    except Exception as fehler:  # Speichern soll nie wegen des Exports scheitern
        print(f"[Spiel] Export fehlgeschlagen: {fehler}")
    return None  # Timer nur einmal ausführen


@persistent
def nach_dem_speichern(_datei):
    # Nicht direkt beim Speichern exportieren (das mag Blender nicht),
    # sondern einen kurzen Moment danach.
    if not bpy.app.timers.is_registered(_spaeter_exportieren):
        bpy.app.timers.register(_spaeter_exportieren, first_interval=0.3)


class SPIEL_OT_exportieren(bpy.types.Operator):
    bl_idname = "spiel.exportieren"
    bl_label = "Ins Spiel exportieren"
    bl_description = "Modelle jetzt ins Spiel schicken (passiert auch automatisch beim Speichern)"

    def execute(self, context):
        ziel = exportieren()
        if ziel is None:
            self.report({"ERROR"}, "Erst die Datei speichern (und die Szene 'Spiel-Objekte' muss da sein)")
            return {"CANCELLED"}
        self.report({"INFO"}, "Ins Spiel geschickt! Das Spiel lädt die Modelle gleich neu.")
        return {"FINISHED"}


class SPIEL_PT_panel(bpy.types.Panel):
    bl_label = "🎮 Mein Spiel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Spiel"

    def draw(self, context):
        spalte = self.layout.column()
        spalte.operator("spiel.exportieren", icon="EXPORT")
        spalte.label(text="Speichern (Cmd+S) schickt")
        spalte.label(text="die Modelle auch automatisch.")


KLASSEN = (SPIEL_OT_exportieren, SPIEL_PT_panel)


def register():
    for k in KLASSEN:
        bpy.utils.register_class(k)
    if nach_dem_speichern not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(nach_dem_speichern)


def unregister():
    if nach_dem_speichern in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(nach_dem_speichern)
    for k in reversed(KLASSEN):
        bpy.utils.unregister_class(k)
