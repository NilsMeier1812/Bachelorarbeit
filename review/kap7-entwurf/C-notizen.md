# Paket C – Notizen (Entwurf 27.11.2026)

Umfang: Einleitung 7.4 (`sec:armregelung`), 7.4.1 `sec:regelkette`, 7.5 `sec:haende` mit 7.5.1 `sec:hand_schnittstelle`
und 7.5.2 `sec:hand_profile`. Datei `review/kap7-entwurf/C.tex`. Neue Grafiken: `Bilder/tikz/armregler-regelkette.tex` (B7.7),
`Bilder/tikz/handprofil-ablauf.tex` (B7.11). Beide wurden mit der echten Präambel kompiliert (keine Overfull-Boxen) und in zwei
Runden visuell geprüft.

Code-Stand: BA-Stable @6a40e47. Pfade sind relativ zur Repo-Wurzel G1. Kurzform: `ac` = `g1pilot/g1pilot/manipulation/arm_controller.py`.

## (a) Faktenblatt

| Fakt | Wert | Stelle |
|---|---|---|
| Regeltakt Armregler | 250 Hz (Sim und Real) | ac:268 |
| IK in eigenem Prozess, neuestes Ziel ersetzt wartendes | – | manipulation/ik_servo_process.py:1-23, 77-182, ac:288, 3510-3528 |
| Zähler je Anfrage (überholte Ergebnisse verwerfen) | `_ik_gen`, `_plan_gen` | ac:3510-3528, 2745-2775 |
| DLS-Dämpfung adaptiv | λ linear von 1e-6 bis 0,1, wenn σ_min < 0,08 | utils/ik_solver.py:30-53, 604-617 |
| Task-Priorität | Position primär, Orientierung im Nullraum der Position | ik_solver.py:618-634 |
| Nullraum zur Grundstellung | Verstärkung 0,15, Ruhepose = Grundstellung | ik_solver.py:636-646, ac:298, 524-531, 578-580 |
| Schritt / Iterationen / Abbruch | 0,05 rad, max. 60, Schritt < 2e-4 rad | ik_solver.py:30-53, 647-658, ac:292 |
| Reichweite | Ziel auf 97 % der Reichweite geklemmt | ik_solver.py:159-187, 420-441 |
| Divergenzschutz | größerer Fehler → Ausgangskonfiguration | ik_solver.py:660-670 |
| Glättung G7.8 | α = 0,2; f_ref Sim 50 Hz, Real 0 (= je Takt); geplante Bahn Sim α = 1 | ac:214, 270, 279, 3530-3536, 3886-3896; bringup_sim.launch.py:103-122 |
| Schwerkraftvorsteuerung | Pinocchio, ±20 Nm Arme, ±25 Nm Taille | ac:727-744, 1116-1151 |
| Gelenkgeschwindigkeit | 1,5 rad/s Sim und Real, Obergrenze real 1,5 | ac:165, 1116-1151 |
| Hand-/Ellbogengeschw. | Sim 0,5 m/s, Real 0,25 m/s, Obergrenze 0,25 | bringup_sim.launch.py:103-122, ac:171, 1569-1601 |
| Anfahrrampe / Schleppfehler | Sim aus (0), Real 3,0 rad/s² / 0,3 rad | manipulation_launcher.launch.py:74-79, bringup_real.launch.py:103-132, ac:1401-1429 |
| Gains Arm / Handgelenk | Sim 150/12, 40/4; Real 60/1,5, 40/1,5; Obergrenze 80/3, 50/3 | manipulation_launcher.launch.py:53-56, bringup_real.launch.py:103-132, ac:1116-1151 |
| Taille | Real 150/4, Obergrenze 250/6; Sim regelt Ersatzregler | bringup_real.launch.py:119-128, ac:1153-1181, waist_yaw.py:1-20 |
| Gewichtsrampe | Sim 0 s, Real 2,0 s, unter 1,0 s → auf 2,0 s korrigiert | bringup_sim.launch.py, manipulation_launcher.launch.py:74-75, ac:1137-1139, 1772-1798 |
| Rückgabe | Toleranz 0,05 rad, Zeitlimit 12 s, nur real | ac:319-321, 1349-1399 |
| Programmende | ≤ 2,5 s, ≤ 0,8 rad/s, nur real | ac:324, 1461-1532 |
| Not-Halt | Gewicht bleibt 1, kp 0, kd 3,0; ENABLE ignoriert bis Quittierung | ac:221, 1819-1857, 1859-1914, 1930-1942, 2221-2314 |
| Taille halten auch im Not-Halt | estop_waist_hold true; Voll-Notaus gibt Taille frei | ac:227, 242, 1916-1928 |
| Einschalten: gemessene Pose als Ziel | – | ac:2221-2314 |
| Inspire: 6 DOF → 12 Gelenke, 1000 = offen | – | inspire_ftp/joint_map.py:1-61 |
| Hand-Schnittstelle 50 Hz | – | inspire_ftp/bridge.py:45 |
| Anbindungen | Anzeige / MuJoCo-Kontakt / Modbus | inspire_ftp/backends.py:51-108, 111-387, 390-564 |
| Kontaktphysik | 24 Positionsaktuatoren (12 je Hand), 34 Touch-Sensoren (17 je Hand) | g1_29dof_inspire_ftp.xml, unitree_sdk2py_bridge.py:61-90, 403-416 |
| Kraftgrenze Sim | Standard 500 g, proportional öffnen, Position latchen | inspire_ftp/model.py:18-35, backends.py:288-341 |
| Modbus | 20 Hz lesen, Taktil jeder 2. Zyklus, Sollwerte nur bei Änderung, eigener Thread je Hand | backends.py:390-515 |
| Not-Halt Hände | beide Hände aus, real gemessener Winkel als Ziel | bridge.py:80-85, 251-258, backends.py:475 |
| Standard Sim/Real | Sim mujoco, Real modbus | bringup_sim.launch.py:171-183, bringup_real.launch.py:197-210 |
| Profile nur Sim | Real immer Inspire-URDF | utils/hand_profile.py:1-79 |
| Flansch | 41,5 mm vor wrist_yaw_link | unitree_mujoco/unitree_robots/g1/tools/gen_hand_profile.py:53 |
| G7.10 | A = s·H·R·Qᵀ·M, b = f + H·d − A·o, M = I − 2nnᵀ (n = Q[:,2]) | gen_hand_profile.py:159-179 |
| Zerlegung, Trägheit, Prüfsumme | V-HACD, gleichmäßige Dichte, SHA-1 | gen_hand_profile.py:71-83, 193-236 |
| Neuerzeugen beim Start, Rückfall | sonst „rubber“-Hand | g1pilot/start.sh:341-353 |
| Massenschätzung im Dialog | PLA 1240 kg/m³, 50 % Füllung | unitree_mujoco/unitree_robots/g1/tools/hand_new.py:38-39, 66-69 |
| Haken-Profil | 0,15 kg je Hand (geschätzt, „Bitte wiegen“), zwei starre Druckteile | unitree_mujoco/unitree_robots/g1/hands/haken/hand.yaml:1-16 |
| Nutzer der Modelle | Sim, Schwerpunktmodell loco_sim, IK/Anzeige, Kugelmodell | navigation/loco_sim.py:331-345, ik_solver.py:237-238, manipulation/arm_geometry.py:36-46, 370-400 |

## (b) Neue Belege (Vorschlag, wörtlich aus `sources-text/`, Zeilenumbrüche entfernt)

| Platzhalter | Seite | Zitat | Kernaussage |
|---|---|---|---|
| `Inspire2024.NEU1` | 6 | "When using Modbus TCP control, the dexterous hands are controlled through IP addresses and port numbers." | Bei Modbus TCP wird die Hand über IP-Adresse und Port angesteuert. |
| `Inspire2024.NEU2` | 23 | "When the angle value for a degree of freedom (DOF) is set to the data within 0-1000, the corresponding finger will take an immediate action." | Ein Winkelwert 0–1000 je Freiheitsgrad bewegt den zugehörigen Finger sofort. |
| `Inspire2024.NEU3` | 25 | "Once it is detected that the actual force (i.e., FORCE_ACT(3);) applied to the index finger during bending reaches 300, the index finger will stop moving; otherwise, the index finger will move to the preset angle." | Im Beispiel stoppt der Zeigefinger, sobald die Ist-Kraft beim Beugen 300 erreicht, sonst fährt er zum Sollwinkel. |
| `Inspire2024.NEU4` | 25 | "set the current actual angle of the index finger \"ANGLE_ACT(3)\" to 1000 (i.e., fully open)." | Der Winkelwert 1000 bedeutet ganz geöffnet. |
| `MujocoDoku2026a.NEU1` | 10 | "While any collection of triangles can be loaded and visualized as a mesh, the collision detector works with the convex hull." | Die Kollisionserkennung arbeitet mit der konvexen Hülle eines Netzes. |

Hinweis: In der Zusammenfassung vor dem Kontextwechsel stand für NEU3 die Seite 24. Laut Seitenmarker ist es Seite 25.

## (c) Offene Marker in C.tex

- `\qf` GIL: Beleg, dass rechenintensiver Python-Code andere Threads im selben Prozess blockiert (Begründung für den eigenen IK-Prozess).
- `\qf` E5: Herstellerdoku zur Wirkung des Überblendgewichts auf die Taille (gleiche Lücke wie Kap. 6, L24).
- `\qf` V-HACD: Quelle für die näherungsweise konvexe Zerlegung (Suchhinweis: Mamou et al., V-HACD).
- `\pruefen` Foto `Bilder/kap7/hand-inspire.jpg`.
- `\pruefen` Foto `Bilder/kap7/hand-haken.jpg`.
- `\pruefen` Masse Haken: Nils schätzt rund 110 g (todo-nils, 24.11.), das Profil trägt 0,15 kg je Hand. Bitte wiegen und klären, ob je Hand oder für beide.
- Nicht als Marker gesetzt, aber offen: `anh:dokumentation` existiert noch nicht (der Verweis ist trotzdem gesetzt).

## (d) Abweichungen vom Plan

- Neue Tabelle `tab:arm_auslegung` (booktabs, schlicht) mit den Auslegungswerten Sim/Real/Obergrenze (Zeilen 1–4 und 11 aus dem
  Kommentar unter `tab:schutzmechanismen`, am Code geprüft). Kostet etwa 0,5 Seiten. Wird es zu lang, kann sie entfallen; dann
  stehen die Werte nur noch als Fließtext.
- Neue Labels: `eq:glaettung` (G7.8), `eq:handabbildung` (G7.10), `fig:haende` (Fotos mit Teilbildern), `tab:arm_auslegung`.
- Zum Code: Der Versatz heißt in G7.10 `d` statt δ, weil amsmath bzw. `\boldsymbol` in main.tex fehlt.
- Die Gewichtsrampe wird im Realbetrieb nicht auf „≥ 1,0 s“ geklemmt, sondern unter 1,0 s auf 2,0 s gesetzt. So steht es in der Tabelle.
- Die Taillengains im Realbetrieb sind im Code als „ungeprüft“ kommentiert (bringup_real.launch.py:119-128). Der Text nennt nur die
  eingestellten Werte. Vielleicht sollte Nils das vor der Abgabe bestätigen.
- Der Rückfall bei einem nicht baubaren Profil geht laut Code auf die „rubber“-Hand. Der Text sagt neutral „mitgeliefertes
  Standardprofil“. Ob es im Text Gummihand heißen soll, entscheidet Nils.
- Das Kinematikmodell wird bei den Profilen mit seinem Werkzeugpunkt erwähnt. Pfadplanung für den Zielmarker wird wie gefordert nicht erwähnt.

## (e) Fehlende Abkürzungen (nur Notiz, nicht in main.tex eingetragen)

IK (Inverse Kinematik), TCP (Transmission Control Protocol, in „Modbus TCP“), DOF wird nicht verwendet (der Text sagt
„Freiheitsgrad“), API (in Abb. B7.7 „Arm-API“). In C.tex ist kein `\ac{}` gesetzt, weil die Kürzel noch nicht definiert sind.
Andere Kapitel schreiben IK ebenfalls im Klartext.

## (f) Umfang

Etwa 2100 Wörter Quelltext inklusive Kommentaren, davon etwa 1350 Wörter Fließtext. Im Testdokument kommen hinzu: Abbildung B7.7
(ca. 0,5 S.), Tabelle `tab:arm_auslegung` (ca. 0,5 S.), Fotoabbildung (ca. 0,4 S.), Tabelle T7.5 (ca. 0,4 S.), Abbildung B7.11
(ca. 0,25 S.) und zwei Gleichungen. Geschätzt sind es zusammen **etwa 5,2 Seiten**: 7.4 plus 7.4.1 etwa 2,5 S. und 7.5 etwa 2,7 S.
Das liegt an der Obergrenze von +15 %. Wenn gekürzt werden soll, lässt sich am einfachsten `tab:arm_auslegung` streichen
(−0,5 S.), dann liegt der Teil bei etwa 4,7 S.
