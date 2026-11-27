#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abstandsbedarf des Armplaners über dem Abstand zum näheren Endpunkt (Abb. fig:trichter b).

Reine Rechnung aus der Formel des Planers (Gleichung eq:abstandsbedarf in Kap. Umsetzung)
mit den Voreinstellungen aus dem Code, KEIN Messwert:

    b(a) = f + w(a) * (C - f),   w(a) = smoothstep(a / R),   smoothstep(u) = 3u^2 - 2u^3 (u in [0, 1])

C = clearance, R = relax_radius aus DEFAULTS in g1pilot/g1pilot/manipulation/arm_planner.py
(Repo NilsMeier1812/G1, Stand PR #62 @e452513: Zeilen 72-100, Formel Zeilen 112-114 und 251-272).
f = Endwert (Abstand der Kugel am Start bzw. Ziel, höchstens 0). Zwei Fälle:
    f = 0      Kugel am Endpunkt frei oder in Berührung
    f = -2 cm  Kugel steckt am Endpunkt 2 cm im Objekt (gewählter Beispielwert, kein Messwert)

Aufruf:  python3 -I Daten/planer-trichter.py [Pfad/zu/arm_planner.py] > Daten/planer-trichter.csv
Ohne Pfad gelten die Werte unten (abgelesen an e452513). Einheiten in der CSV: cm.
"""
import ast
import sys

CLEARANCE = 0.05      # m, DEFAULTS["clearance"]
RELAX_RADIUS = 0.15   # m, DEFAULTS["relax_radius"]
FLOORS = (0.0, -0.02)  # m, Endwerte der beiden Fälle


def defaults_from_code(path):
    """DEFAULTS-Wörterbuch aus arm_planner.py lesen, ohne das Modul zu importieren."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "DEFAULTS" for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("DEFAULTS nicht gefunden")


def smoothstep(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3.0 - 2.0 * u)


def main():
    c, r = CLEARANCE, RELAX_RADIUS
    if len(sys.argv) > 1:
        d = defaults_from_code(sys.argv[1])
        c, r = float(d["clearance"]), float(d["relax_radius"])
    print("a_cm,b_f0_cm,b_fm2_cm")
    n = 100
    a_max = 0.20
    for i in range(n + 1):
        a = a_max * i / n
        w = smoothstep(a / r)
        vals = [f + w * (c - f) for f in FLOORS]
        print(f"{100 * a:.2f}," + ",".join(f"{100 * v:.4f}" for v in vals))


if __name__ == "__main__":
    main()
