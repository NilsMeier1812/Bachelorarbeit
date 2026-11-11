"""Erzeugt Bilder/tikz/kugelmodell-haende.tex aus kugeln.json (export_kugeln.py).
Ansicht: x-z-Ebene des wrist_yaw-Frames (x = vom Flansch weg), linke Hand."""
import json, sys
import numpy as np
S = 32.0  # cm je m
d = json.load(open(sys.argv[1]))

def hull(P):
    P = sorted(set(map(tuple, np.round(P, 5))))
    if len(P) < 3: return P
    def cr(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo, up = [], []
    for p in P:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(P):
        while len(up) >= 2 and cr(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]

titles = {"inspire": "a) Inspire-Hand (Modell auch für die Rubber Hand verwendet)",
          "haken": "b) Gedruckter Box-Haken (Hand-Profil)"}
L = ["% Kugelmodell des Armplaners (Hand und Handgelenk, linke Seite), Ansicht x-z im wrist_yaw-Frame.",
     "% Eigene Darstellung, ERZEUGT von Daten/kugelmodell/tikz_kugeln.py aus kugeln.json",
     "% (export_kugeln.py: ArmGeometry aus G1-Repo, g1pilot/g1pilot/manipulation/arm_geometry.py). Nicht von Hand ändern.",
     r"\begin{tikzpicture}[ba]"]
y0 = 0.0
for n in ("inspire", "haken"):
    e = d[n]
    allp = np.concatenate([np.array(p)[:, [0, 2]] for p in e["polys"]])
    C = np.array(e["c"])[:, [0, 2]]; R = np.array(e["r"])
    zmax = max(allp[:, 1].max(), (C[:, 1] + R).max()); zmin = min(allp[:, 1].min(), (C[:, 1] - R).min())
    off = y0 - zmax * S
    L.append(f"  % {n}: {len(R)} Kugeln")
    for P in e["polys"]:
        h = hull(np.array(P)[:, [0, 2]])
        if len(h) < 3: continue
        pts = " -- ".join(f"({x*S:.2f},{z*S+off:.2f})" for x, z in h)
        L.append(f"  \\fill[baFlaeche, draw=baGruen, ba duenn] {pts} -- cycle;")
    for (x, z), r in zip(C, R):
        L.append(f"  \\draw[ba duenn, baBlau] ({x*S:.2f},{z*S+off:.2f}) circle ({r*S:.2f});")
    t = e["tcp"]
    L.append(f"  \\draw[ba normal, black] ({t[0]*S-0.12:.2f},{t[2]*S+off-0.12:.2f}) -- ++(0.24,0.24) ({t[0]*S-0.12:.2f},{t[2]*S+off+0.12:.2f}) -- ++(0.24,-0.24);")
    L.append(f"  \\node[anchor=south west, font=\\footnotesize] at ({t[0]*S+0.1:.2f},{t[2]*S+off+0.1:.2f}) {{TCP}};")
    L.append(f"  \\node[ba teiltitel, anchor=north west] at ({-0.1*S:.2f},{zmin*S+off-0.25:.2f}) {{{titles[n]}}};")
    y0 = zmin * S + off - 1.6
# Maßstab
L.append(f"  \\draw[ba normal] ({0.24*S:.2f},{y0+0.4:.2f}) -- ++({0.05*S:.2f},0) node[midway, below, font=\\footnotesize] {{5\\,cm}};")
L.append(f"  \\draw[ba normal] ({0.24*S:.2f},{y0+0.3:.2f}) -- ++(0,0.2) ({0.29*S:.2f},{y0+0.3:.2f}) -- ++(0,0.2);")
# Legende
L.append(f"  \\fill[baFlaeche, draw=baGruen, ba duenn] ({-0.1*S:.2f},{y0+0.25:.2f}) rectangle ++(0.4,0.3);")
L.append(f"  \\node[anchor=west] at ({-0.1*S+0.45:.2f},{y0+0.4:.2f}) {{Kollisionsgeometrie (Projektion)}};")
L.append(f"  \\draw[ba duenn, baBlau] ({0.115*S:.2f},{y0+0.4:.2f}) circle (0.17);")
L.append(f"  \\node[anchor=west] at ({0.115*S+0.25:.2f},{y0+0.4:.2f}) {{Kugel des Planers}};")
L.append(r"\end{tikzpicture}")
open(sys.argv[2], "w").write("\n".join(L) + "\n")
print("ok", y0)
