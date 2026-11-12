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
