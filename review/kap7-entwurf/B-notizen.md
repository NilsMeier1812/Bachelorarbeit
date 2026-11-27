# Paket B – Notizen (7.3 Fortbewegung, 7.7 Navigation in der Simulation)

Code-Bezug: BA-Stable @6a40e47 (`/home/user/g1-ba`). Alle Pfade relativ zur Repo-Wurzel G1.

## (a) Faktenblatt

| Aussage | Fundstelle | Werte |
|---|---|---|
| Ersatzregler-Zustände Bereitschaft/Stehen/Gehen/Dämpfen | `g1pilot/g1pilot/navigation/loco_sim.py:89-98`, :355-429, :431-466, :502-517 | Zustandscode in motor_cmd[29] |
| Schreibt Beine 0-11 + Taille 12-14, Arme nicht | loco_sim.py:643-670 | 50 Hz (step_dt 0.02), Lockstep-Option |
| Sturzerkennung | loco_sim.py:144-147, :569-577, :733-775 | Gravitation z > -0,5 (ca. 60 Grad), 0,3 s |
| Standregler Knöchelmoment | `stand_balancer.py:78-92, 348-390`; loco_sim.py:166-186 | kp 150 Nm, kd 40 Nm s/rad, Grenze 50 Nm, ki 80 Nm/s (max 25 Nm, nur |g_x|<0,4); Haltungs-Steifigkeit x10 |
| Schwerpunkt-Führung | `com_model.py:23-51`; stand_balancer.py:99-113, :290-314; loco_sim.py:331-346 | Ziel 3,5 cm vor Knöchel, Zeitkonstante 0,2 s, max 0,2 rad; Lastkorrektur über CoP, 2 s, max 5 cm (im Text gekürzt) |
| Gehen -> Stehen (Beruhigung) | stand_balancer.py:15-29, :124-175, :330-337; loco_sim.py:120-128 | ruhig 0,3 s, Drehrate < 0,3 rad/s, Beingeschw. < 0,5 rad/s, früh. 0,6 s, spät. 3 s; Einblenden 0,4 s (aus Bereitschaft 0,1 s) |
| Abfangen | stand_balancer.py:115-121, :201-234; loco_sim.py:129-139, :417-429 | Sohle > 6 Grad oder horiz. Gravitation > 0,2, jeweils > 0,04 s |
| Policy-Schnittstelle | `walk_policy.py:23-29, 78-120, 183-203, 333-358`; policies/*/deploy.yaml | Format-Kennung wählt Klasse; Längenprüfung beim Laden |
| Drei Policies, Herkunft, Eingriff | policies/*/ATTRIBUTION.md; NOTICE.md:40-41 | Unitree RL Mjlab (98 Werte), AGILE velocity (255), velocity-height (400); AGILE-Netze nur TorchScript -> ONNX |
| Vorwärtsgrenze Policy | deploy.yaml (g1_wholebody:12-15, agile_velocity:66-71, height:67-70,104-108) | 1,0 / 1,0 / 0,5 m/s je Policy (Zuordnung vor Abgabe prüfen) |
| Arm-Gehpose, Freigabe | loco_sim.py:157-163, :444-466, :626-631 | Gehen starten erst bei Arm-Pose und Taille Mitte, Timeout 15 s |
| Onboard-Anbindung | `loco_client.py`; NOTICE.md:21 | FSM 4 Preparation, 500/501 Walk, 1 Damp; Grenzen 0,4/0,3/0,4; Timeout 0,5 s; Dauer 1,0 s @ 20 Hz; Knie-Last >= 10 Nm; Zustandsabgleich 2 Hz; Voll-Notaus Damp zuerst; estop_damp_legs default false |
| Navigation | `create_map.py`, `dijkstra_planner.py`, `nav2point.py`, `sim_localization.py`, `joy_mux.py`, `joy_to_cmdvel.py`, `scene_markers.py` | Raster 100x100, 0,1 m; Inflation 0,30 m; Zielanfahrt 0,60 m, min. 0,10 m; joy_mux Eingang 0,3 s |

## (b) Vorgeschlagene neue Belege

- **UnitreeRLMjlab.NEU1**, Seite 3 (geprüft in `sources-text/UnitreeRLMjlab.txt`, Zeilen 123-125):
  - Zitat: "Before deploying on the real robot, it is recommended to perform simulation deployment using [unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco) to prevent abnormal behaviors on the physical robot."
  - Kernaussage: Das Projekt empfiehlt, Policies vor dem Einsatz am realen Roboter in der Simulation unitree_mujoco zu erproben, um Fehlverhalten am Roboter zu vermeiden.

## (c) Alle \qf / \pruefen

- `\qf` Pinocchio: Laden von MJCF-Modellen und Schwerpunktberechnung (Carpentier2019 stützt das nicht)
- `\qf` WBC-AGILE-Herkunft (Zhao2026, nicht in zotero-map.json)
- `\qf` Trainingsbedingungen der AGILE-Policies (Arme frei)
- `\qf` Wirkung der Befehlsdauer am Onboard-Regler (Unitree-Doku)
- `\pruefen` Beobachtung am Kran (Real-Test 21.10.2026) bestätigen oder in Evaluation belegen
- `\pruefen` Begründung der Geh-Grenzen 0,4 / 0,3 / 0,4
- Entfernt gegenüber früherer Fassung: `\qf` zur Umbenennung des Dienstes (Absatz gekürzt).

## (d) Abweichungen / Auffälligkeiten

- Umfang im Testdokument ca. 4,5 Seiten statt 4 (oberer Rand von +15 %); T7.3 und B7.6 entfallen aus Platzgründen.
- Doku `docs/30-T-Stehen-und-Gehen.md` behauptet, der Ersatzregler nutze `reserve[]`-Werte, der Code @6a40e47 tut das nicht. Text folgt dem Code.
- Verweise auf Labels aus dem Gerüst (`sec:fortbewegungspfade`, `sec:bridge`, `sec:armregelung`, `sec:erweiterungskonzept`, `sec:szenen`, `sec:eval_fortbewegung`, `sec:eval_sicherheit`, `tab:policies`, `tab:eigenleistung`, `tab:andockpunkte`, `tab:schutzmechanismen`, `fig:betriebszustaende`, `chap:evaluation`) sind im Testdokument als ?? sichtbar und beim Einfügen in `07_Umsetzung.tex` zu prüfen. Abschnitt 7.3.2 selbst referenziert A4/A5 nur als Text.
- Die Einleitung in 7.3 verweist auf "Abschnitt A4/A5" als Kürzel, beim Einfügen durch passenden Verweis ersetzen.

## (e) Fehlende Abkürzungen

Als Klartext geschrieben, da kein `\ac{}` in `main.tex`: IMU, ONNX, ROS 2, PD, LiDAR, MOLA (nicht ausgeführt), CoP (nur Notizen).

## (f) Umfang

Ca. 4,5 Seiten im Testdokument (6 Seiten PDF mit Kapitelkopf und Literatur), davon 7.7 etwa 0,7 Seiten.
