"""Kap. 8, Versuch V1 (Eigenleistung, Claude für Nils, 25.11.2026).
Aufruf: python3 v1_betriebsart.py <Pfad zu G1/g1pilot> [--csv v1_betriebsart.csv]
Bezugsstand: G1 Branch BA-Stable @ 6a40e47.

V1: Stellen im Python-Code, an denen die Betriebsart (Sim/Real) ausgewertet wird.
Zaehlt per AST: Aufrufe is_sim_mode()/_sim_mode(...), Zugriffe auf Attribut/Name 'sim_mode',
Lesen von G1_SIM_MODE ueber os.getenv/env.get. Keine Kommentare, Docstrings, Importe."""
import ast, sys, pathlib, collections
root = pathlib.Path(sys.argv[1])
res = collections.OrderedDict()
for f in sorted(root.rglob("*.py")):
    rel = f.relative_to(root)
    if rel.parts[0] == "test": continue
    try: tree = ast.parse(f.read_text(encoding="utf-8"))
    except Exception: continue
    lines = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            fn = n.func
            name = fn.id if isinstance(fn, ast.Name) else fn.attr if isinstance(fn, ast.Attribute) else None
            if name in ("is_sim_mode", "_sim_mode"):
                lines.add(n.lineno)
            if name in ("getenv", "get") and n.args and isinstance(n.args[0], ast.Constant) and n.args[0].value == "G1_SIM_MODE":
                lines.add(n.lineno)
        elif isinstance(n, ast.Attribute) and n.attr == "sim_mode" and isinstance(n.ctx, ast.Load):
            lines.add(n.lineno)
    if lines: res[str(rel)] = sorted(lines)
# Zweckgruppen je Fundstelle (Datei, Zeile), von Hand nach Lesen des Codes zugeordnet (BA-Stable @ 6a40e47).
G = {
 "Verbindung": [("g1pilot/utils/common.py", l) for l in (28, 38, 53)],
 "Fortbewegung und Onboard-Regler": [("g1pilot/manipulation/arm_controller.py", 2494),
     *[("g1pilot/teleoperation/demo_gui.py", l) for l in (1456, 1641, 1886, 1892)],
     *[("g1pilot/teleoperation/phone/link.py", l) for l in (206, 376)],
     ("g1pilot/teleoperation/ps4_arm_teleop.py", 851)],
 "Taille": [("g1pilot/manipulation/arm_controller.py", l) for l in (1160, 1161, 1893, 2006, 2034, 2098, 2155)],
 "Start, Übergabe und Schutz": [*[("g1pilot/manipulation/arm_controller.py", l) for l in (1029, 1467, 2018, 2446, 2505)],
     *[("g1pilot/teleoperation/demo_gui.py", l) for l in (1074, 1158, 2542, 2545, 2568)],
     *[("g1pilot/teleoperation/phone/link.py", l) for l in (189, 364)],
     ("g1pilot/teleoperation/ps4_arm_teleop.py", 1197)],
 "Hände": [("g1pilot/teleoperation/demo_gui.py", 448), *[("g1pilot/utils/hand_profile.py", l) for l in (28, 37)]],
 "Anzeige und Bedienoberfläche": [("g1pilot/manipulation/arm_controller.py", 2199),
     *[("g1pilot/teleoperation/demo_gui.py", l) for l in (1071, 1080, 1107, 1181, 1185, 1344, 1359, 1371, 1372,
        1373, 1395, 1397, 1403, 1473, 1518, 2511, 2714)],
     *[("g1pilot/teleoperation/phone/link.py", l) for l in (72, 361, 395, 424)]],
 "Diagnosewerkzeuge (nur Simulation)": [(f"g1pilot/tools/{n}.py", l) for n, l in
     (("sim_arm_monitor", 55), ("sim_arm_wiggle", 55), ("sim_dds_check", 44), ("sim_leg_hold", 68))],
}
gefunden = {(k, l) for k, v in res.items() for l in v}
zugeordnet = [x for v in G.values() for x in v]
tot = 0
for k, v in res.items():
    tot += len(v); print(f"{len(v):3d}  {k}  {v}")
print(f"Summe: {tot} Stellen in {len(res)} Dateien")
fehlt = gefunden - set(zugeordnet); zuviel = set(zugeordnet) - gefunden
print("nicht zugeordnet:", sorted(fehlt) or "keine", "| veraltet:", sorted(zuviel) or "keine")
if "--csv" in sys.argv:
    with open(sys.argv[sys.argv.index("--csv") + 1], "w", encoding="utf-8") as f:
        # Semikolon als Trenner (Gruppennamen enthalten Kommas); idx für pgfplots, absteigend sortiert
        f.write("idx;anzahl;gruppe\n")
        for i, (g, v) in enumerate(sorted(G.items(), key=lambda kv: len(kv[1]))):
            f.write(f"{i};{len(v)};{g}\n")
for g, v in G.items():
    print(f"{len(v):3d}  {g}")
