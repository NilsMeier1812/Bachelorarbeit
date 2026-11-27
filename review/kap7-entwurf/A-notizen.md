# Paket A – Notizen (Entwurf 27.11.2026)

Text: `review/kap7-entwurf/A.tex` (Kapiteleinleitung, `sec:bereitstellung`, `sec:simulationsumgebung` mit
`sec:bridge` inkl. `\paragraph*` + `\label{sec:zeitschritt}`, `sec:szenen`).
Grafiken: `Bilder/tikz/verteilung-container.tex` (B7.1), `Bilder/tikz/bridge-signalfluss.tex` (B7.2),
`Bilder/tikz/lockstep-zeitablauf.tex` (B7.3). Alle drei sind im Testdokument mit der Präambel aus `main.tex`
übersetzt, als PNG gerendert und angesehen: keine Overfull-Boxen, nicht skaliert, höchstens 16 cm breit.
Code-Bezug: G1 `BA-Stable` @6a40e47. Greifobjekt-Kollision nach PR #61 @8eb34f4 (`/home/user/g1-pr61`).

`check.py --file review/kap7-entwurf/A.tex`: 2 Fehler, beide gewollt (`MujocoDoku2026.NEU1`, `.NEU2` fehlen noch
in `evidence/`, siehe b). Sonst 0 Warnungen und 10 offene `\qf`/`\pruefen`.

## (a) Faktenblatt (Eigenleistung, Code @6a40e47, falls nicht anders angegeben)

| Aussage im Text | Wert / Beleg | Datenbasis |
|---|---|---|
| Drei Abbilder: Physiksimulation, Steuerung Sim, Steuerung Real | ubuntu:22.04 (MuJoCo, unitree_sdk2_python, kein ROS) bzw. ros:humble | docker/Dockerfile.mujoco, .sim, .real |
| Nur Sim-Steuerung hat ONNX-Laufzeit | onnxruntime nur in Dockerfile.sim | Dockerfile.sim:43-56, Dockerfile.real:15-50 |
| **Real-Abbild ohne OMPL** (Befund, nicht im Plan) | `ompl` fehlt in Dockerfile.real, Bahnplaner fällt auf eingebauten Weg zurück | Dockerfile.real:15-50 → `\pruefen` |
| Profile sim/real, network_mode host, Code eingebunden, colcon build beim Start | | docker-compose.yml:10-17, :14, :130, :145-151 |
| Gespiegelte Domains | Sim: ROS 0 / Unitree 1 auf lo. Real: ROS 1 / Unitree 0 auf Netzwerkkarte | utils/common.py:6-23, compose :85-88, :173-176 |
| ROS-Verkehr nur auf lo | cyclonedds.xml | docker/cyclonedds.xml:1-16 |
| Einstellungskette | Startmenü → Env → start.sh --yes → compose → launch → Parameter | start_gui/core.py:263-316, bringup_sim.launch.py:160-162 |
| Startmenü Sim: Szene, Hände, Policy, Bediengeräte, Vorschaubilder; baut Szene, Handprofil neu, Docker-Prüfung, GPU-Overlay | | start_gui/views.py:131-260, app.py:136-195, start.sh:341-353, :390-398, :440-447 |
| Live-Anzeige alle 3 s: Link, Adresse im Netz, Ping G1, Hände per TCP, Warnung zweite Schnittstelle | POLL_MS = 3000 | start_gui/network.py:26, netsetup.py:241-303 |
| Netzwerk-Assistent: Profil mit fester IP, ohne Gateway/DNS, never-default, modify statt delete, autoconnect, Befehle vorher angezeigt | | start_gui/netsetup.py:1-13, :179-211 |
| Sicherheitsbestätigung Real, nie gespeichert, start.sh verweigert ohne | G1_REAL_CONFIRM | views.py:423-425, core.py:290-295, start.sh:243-253 |
| Beenden über Wächter auf dem Host, Real mit Frist 20 s | stop_grace_period 20s | sim_/real_shutdown_watcher.sh, compose :248-261 |
| PD je Physikschritt | τ = τ_v + kp(q_s − q) + kd(dq_s − dq) | unitree_sdk2py_bridge.py:304-307, :393-456 |
| Gelenke 0–14 über rt/lowcmd, 15–28 überblendet, Gewicht Eintrag 29, auf [0,1] begrenzt | | bridge:280-285, :420-447 |
| Reservefelder 0–3: Fußkräfte, Basis vx/vy, nur Sim | | bridge:184-207 |
| Managed Weld: Zustandscode in lowcmd[29] (0 HOLD, 1 RUN, 2 DAMP), Beckenhöhe aus Standpose, Startup-Hold-PD | | config.py:134-188, bridge:146-180, :309-391, loco_sim.py:655-660 |
| Physikschritt 1 ms, Dezimierung 20 = 0,02/0,001, Watchdog 0,2 s, Echtzeitbegrenzung, Viewer 50 fps | | config.py:61-67, :80, :84-108, unitree_mujoco.py:186-257 |
| Regelschritt Lauf-Policies 20 ms | step_dt 0.02 | policies/*/deploy.yaml |
| Nur lowcmd erhöht cmd_seq (Armregler nicht im Gleichschritt) | | bridge:287-298 |
| Gleichschritt im Betrieb immer an | | start.sh:403-404 |
| Szene = Basis + Umgebung, Boden/Licht der Umgebung verworfen | | build_env_scene.py:96-138, :488-560 |
| Präfixe grasp_ (freejoint), g1_spawn, station_ (entfernt, als Daten abgelegt) | | build_env_scene.py:47-58, :140-172, :609-641 |
| Feste Hindernisse: V-HACD bis 64 Teile, Ablageflächen zusätzlich als exakte Quader | maxConvexHulls 64 | build_env_scene.py:252-303, :437-485 |
| Greifobjekte nicht konvex: achsparallele Quader aus 3-mm-Voxelgitter, konvex: Hülle | GRASP_VOXEL 0.003 | **@8eb34f4** build_env_scene.py:488-526, :659-745 |
| Kollisionsbits: Körper 1, Hände 2, Umgebung 3 | | BA-Stable build_env_scene.py:79, :560-569; g1_29dof_inspire_ftp.xml:227 ff. |
| Weltmodell: UDP 10 Hz → Marker für 3D-Anzeige, Armregler, Navigation, Hindernisse als Quader je Teil, nicht im Realbetrieb | | scene_state_publisher.py, config.py:191-205, scene_bridge.py:1-18, bringup_sim.launch.py:125-133 |

Fremde Aussagen im Text (alle vorhandene Belege): UnitreeMujoco.01, .04, .05, .07, .08; MujocoDoku2026.03, .06, .15;
MujocoDoku2026b.05; Todorov2012.22; Pitonakova2018.01.

## (b) Vorgeschlagene neue Belege (wörtlich aus `sources-text/MujocoDoku2026.txt`, Seite geprüft)

```yaml
  - id: MujocoDoku2026.NEU1        # Text A.tex Abschnitt sec:szenen, Kollision
    seite: "42"
    zitat: "Meshes specified by the user can be non-convex, and are rendered as such. For collision purposes however they are replaced with their convex hulls (visualized with the ‘H’ key in simulate), computed by the qhull library."
    kernaussage: "Nicht konvexe Meshes werden so dargestellt, für die Kollision aber durch ihre konvexe Hülle (qhull) ersetzt."
    quelle: exzerpt
  - id: MujocoDoku2026.NEU2
    seite: "44"
    zitat: "In order to model a non-convex object other than a height field, the user must decompose it into a union of convex geoms (which can be primitive shapes or meshes) and attach them to the same body."
    kernaussage: "Nicht konvexe Objekte (außer Height Fields) muss der Nutzer in eine Vereinigung konvexer Geoms zerlegen, die am selben Körper hängen."
    quelle: exzerpt
```
Optional, im Text nicht verwendet: Rudin2021, S. 11: "For each policy step, which we run at 50 Hz, we need to
perform multiple actuator and simulator steps to obtain a stable simulation." Das würde die Dezimierung im
Gleichschritt-Absatz stützen, falls Nils dort eine Quelle möchte.

## (c) Offene Markierungen in A.tex

| Zeile | Art | Inhalt |
|---|---|---|
| 14 | pruefen | Anhangtabelle `tab:quelltext` anlegen (Label existiert noch nicht) |
| 38 | pruefen | **OMPL fehlt im Real-Abbild**, Bahnplaner nutzt dort Rückfallweg: gewollt? |
| 128 | qf | Herstellerangabe zum Regelgesetz des Motorbefehls am realen G1 (E5) |
| 155 | pruefen | bestätigen, dass außer dem Ersatzregler kein Knoten die Reservefelder liest |
| 171 | pruefen | Beobachtung „Armgelenke schwingen bei größerem Schritt auf“ (Kommentar config.py) bestätigen (E6) |
| 206 | qf | Szenen-Editor (fremdes Projekt mujoco-scene-editor) als Software-Quelle mit Commit-Hash (E5) |
| 222 | qf | Verfahren der konvexen Zerlegung V-HACD (Mamou2009 nicht freigegeben) |
| 227 | pruefen | Stand PR #61, nach Merge BA-Stable-Hash eintragen (DB-Kommentar @8eb34f4) |
| 244 | pruefen | Bild von Nils: `Bilder/kap7/szene-mujoco-rviz.png` (Platzhalter-fbox) |
| 249 | pruefen | Bildbeschreibung an das echte Bild anpassen |

Außerdem verweist der Text auf Labels, die es noch nicht gibt oder die andere Pakete anlegen: `anh:dokumentation`,
`tab:quelltext`, `sec:haende`, `sec:regelkette`, `sec:kollisionsmodell`, `sec:ersatzregler`, `sec:bedienoberflaeche`,
`sec:smartphone`, `sec:entwickler_api`, `sec:navigation`, `sec:bedienwege`, `sec:fortbewegung_umsetzung`.

## (d) Abweichungen vom Plan

1. **Kein `\ac{}`.** In `main.tex` sind nur KI, DSGVO und FAPS als Akronyme angelegt, und Kap. 2, 3 und 6 schreiben
   DDS und ROS~2 im Klartext. Für ein einheitliches Bild bleibt auch Paket A im Klartext. Siehe (e).
2. **Unterabschnitte 7.2.1/7.2.2 statt 7.2.1/7.2.3**, weil der frühere 7.2.2 (Zeitschritt) nun ein `\paragraph*`
   am Ende von `sec:bridge` ist. Das Label `sec:zeitschritt` bleibt über `\phantomsection` erhalten.
3. **B7.3** zeigt nur zwei Regelschritte mit Warten, Rechnen und je 20 Physikschritten. Die Echtzeitbegrenzung und
   den Watchdog nennt nur der Text, damit die Abbildung klein bleibt.
4. **B7.1** zeigt den Controller nicht als eigenen Kasten, damit die Grafik nicht überladen wird. Das Smartphone ist
   eingezeichnet. Falls der Controller hinein soll, passt er als Kasten unter die Bedienoberfläche.
5. **Kein Startmenü-Platzhalter** (Reserve), weil der Umfang ohnehin über dem Ziel liegt.
6. **Kollision:** Feste Hindernisse sind nach BA-Stable beschrieben, Greifobjekte nach PR #61 (Quader aus
   Voxelgitter), wie vorgegeben. Die Kollisionsfilter stützt der vorhandene Beleg MujocoDoku2026.15.
7. **Firmware-PD und Überblendung am realen Roboter:** Das Regelgesetz ist als `\qf` markiert, die lineare
   Überblendung ist ausdrücklich als „Annahme der Simulation“ formuliert, mit Verweis auf `sec:g1_armsdk`.
8. **Programmnamen:** „unitree_mujoco“ ist im Text durch „das MuJoCo-Projekt des Herstellers“ ersetzt (Zitat
   UnitreeMujoco). Dateinamen stehen nur in `% DB:`-Kommentaren und `\pruefen`.

## (e) Fehlende Abkürzungen (für das Abkürzungsverzeichnis, falls `\ac` eingeführt wird)

DDS, ROS, LAN, UDP, HTTP, IMU, PD, MJCF, ONNX, GPU, TCP (in „Modbus TCP“).

## (f) Umfang

Testsatz mit Präambel aus `main.tex` (Kapitelanfang inklusive): 7,4 Seiten, davon etwa 0,6 Seiten Leerraum durch
Kapitelkopf und Gleitumgebungen. Netto also **etwa 6,8 Seiten**, gegenüber dem Ziel von 5,3 Seiten etwa +28 %.
Das liegt über ±15 %, aber im Rahmen von +20–40 % für Entwürfe laut CLAUDE.md.
Kürzungskandidaten (zusammen etwa 1 Seite):
- Absatz „Beenden …“ in `sec:bereitstellung` auf 2 Sätze, ca. 0,15 S.
- Absatz Reservefelder mit dem Absatz zum Rückweg zusammenlegen, ca. 0,15 S.
- Haltezustand (Schweiß-Zwangsbedingung) auf 3 Sätze, ca. 0,15 S.
- Absatz „Tabelle zeigt …“ nach T7.1 kürzen, Profil-Logik steht schon in Kap. 6, ca. 0,15 S.
- B7.4-Platzhalter mit echtem Bild flacher halten (z. B. 5 cm Höhe), Erläuterung nach B7.4 in den Weltmodell-Absatz
  ziehen, ca. 0,25 S.
