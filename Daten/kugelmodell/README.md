# Kugelmodell des Armplaners (Abbildungen Kap. 7)

Eigene Darstellung aus dem G1-Code (`g1pilot/g1pilot/manipulation/arm_geometry.py`), Stand G1 fdb9cba.

1. `python3 -I export_kugeln.py kugeln.json` – braucht pinocchio; `ament_index_python` wird im Skript durch einen Stub ersetzt.
2. (2D-Version am 11.11. verworfen.)
3. 3D: Konvexe Hüllen der Kollisionsteile (scipy ConvexHull) in die JSON schreiben, dann
   `node render.js kugeln3d.json` (three.js r128 von cdnjs neben page.html, Playwright/Chromium) →
   PNGs zuschneiden nach `Bilder/kugelmodell-3d-{inspire,haken}.png`.
