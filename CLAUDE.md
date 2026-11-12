# Regeln für dieses Projekt
- Antworte immer auf Deutsch, kurz und einfach, für einen 13-Jährigen.
- Wir bauen ein 3D-Spiel im Browser mit Three.js.
- Immer WebGPU nutzen: `WebGPURenderer` aus `three/webgpu` (Import-Map auf `build/three.webgpu.js`), nie `WebGLRenderer`.
- Alles in einer Datei index.html. Three.js über eine Import-Map von cdn.jsdelivr.net laden, ohne Build-Schritt.
- Arbeite in kleinen Schritten. Nach jedem Schritt: sag, was ich im Browser ausprobieren soll.
- Erkläre bei jeder Änderung in einem Satz, was der Code macht.
- Nach jedem funktionierenden Schritt einen Git-Commit mit einer kurzen deutschen Nachricht.
- Zum Ansehen: einen lokalen Webserver mit `npx serve .` starten.
- Online stellen: mit `gh repo create` ein öffentliches Repo anlegen und GitHub Pages auf den Branch main einschalten.

## Modelle aus Blender
- Die 3D-Modelle liegen in `blender/spiel-objekte.blend` (Szene "Spiel-Objekte"). Beim Speichern exportiert das Blender-Add-on `blender/spiel_export.py` ("Ins Spiel exportieren", Seitenleiste N → Reiter "Spiel") nach `modelle/spiel.glb`.
- Das Spiel lädt `modelle/spiel.glb` beim Start und lädt sich neu, sobald sich die Datei ändert. Fehlt ein Modell, baut das Spiel das Teil selbst im Code.
- Die Namen der obersten Objekte (Affe, Cabrio, Sportwagen, Monstertruck, Motorrad, Go-Kart, Auto, Kleinbus, Bus, Laster, Muenze, Ampel, Laterne, Tanne, Laubbaum, Busch, Pilz, Haus) und der beweglichen Teile (z. B. `Affe_Arm_links`, `Cabrio_Rad_vorne_1`, `Ampel_Licht_rot`) nie umbenennen. Material `Fell` = Fell des Affen, `Lack` = Autofarbe im Verkehr.
- Neue Objekte für das Spiel: in Blender in der Szene "Spiel-Objekte" bauen, eindeutig benennen und im Code mit `modell('Name')` oder `modellAlsInstanz('Name', …)` einsetzen.
- Blender-Export nie mit `temp_override` auf eine andere Szene machen (Blender stürzt ab).
