# Faktenblatt Testumgebung (AP1, Kap. 5)

Stand: G1 `25d5c1a` (Commit vom 11.11.2026, `git log -1`). Alle Pfade relativ zu `/home/user/G1`.
`G/` = `g1pilot/` (Paketwurzel). Zahlen am Code gezählt (Befehle in Klammern), nicht aus der Doku.
Keine Messwerte, keine Bewertung. Ausführen der Tests war nicht möglich (kein `pytest`, `rclpy`, `pinocchio` in dieser Umgebung);
alle Angaben stammen aus statischer Zählung und Lesen des Codes.

## (a) Testsuite: Umfang und Gruppen

### Umfang

| Größe | Wert | Fundstelle / Zählung |
|---|---|---|
| Testdateien `test/test_*.py` | 46 | `ls G/test/test_*.py \| wc -l` |
| Testfunktionen (`def test_`, auch eingerückt) | 597 | `grep -hE "^\s*(async )?def test_" G/test/test_*.py \| wc -l`; alle auf Modulebene (keine Testklassen, `grep -lE "^class Test"` = 0) |
| davon in den drei langsamen Dateien | 50 (43 + 2 + 5) | `test_arm_controller_real.py` 43, `test_jog_reference_real.py` 2, `test_ik_servo_async.py` 5; Liste `SLOW` in `G/test/run_tests.sh:18` |
| Gruppe `schnell` (46 minus 3 langsame) | 43 Dateien, 547 Testfunktionen | `run_tests.sh:46-50` |
| `@pytest.mark.parametrize` | 39 Vorkommen in 14 Dateien | `grep -c parametrize`; die Zahl der tatsächlich gesammelten Testfälle liegt damit über 597 und ist ohne `pytest --collect-only` nicht ermittelbar |
| Weitere Dateien in `G/test/` (keine Tests) | `run_tests.sh`, `phone_client.py`, `sphere_coverage.py`, `teleop_jitter_probe.py` | `ls G/test` |
| Dateien mit `pytest.importorskip` / `skipif` | 30 Dateien | `grep -c importorskip`; Voraussetzungen: `pinocchio`, `rclpy`, `PyQt6`, `unitree_sdk2py`, `mujoco`, `yaml`, `dbus_next`, `playwright`, `node`, `dbus-daemon` |

### Gruppen (`G/test/run_tests.sh:20-51`; Dateien je Gruppe und Testfunktionen am Code gezählt)

| Gruppe | Dateien | Testfunktionen | Inhalt (laut Dateinamen im Skript; Doku-Kurzbeschreibung `G/docs/60-A-Tests.md:30-42`) |
|---|---|---|---|
| `sicherheit` (Z. 21-27) | 25 | 442 | `arm_controller` real, `loco_client` real, PS4-/Xbox-Controller, Joy-Mux, Bodenkontakt, Statusleiste, Demo-GUI (Bodenvorprüfung, Temperatur, externer Not-Halt, Real beenden, Abläufe), Taille halten/drehen, Armplaner, IK-Prozess, Inspire-Modbus, Handy-Gateway und Handy-GUI |
| `arm` (Z. 28-29) | 8 | 172 | `arm_controller` real, IK-Prozess, Jog-Bezug, Taille, Hüftdrehung, Jog-Halten, PS4-Arm, Spiegeln |
| `planer` (Z. 30) | 3 | 72 | Armplaner, `arm_controller` real, Hand-Profil |
| `loco` (Z. 31-33) | 10 | 138 | `loco_client` real, Controller-Gehen, Bodenkontakt, Joy-Mux, Hüftdrehung, Statusleiste, Demo-GUI-Teile, `walk_diag` |
| `controller` (Z. 34-36) | 12 | 193 | PS4/Xbox, Gehen, gemeinsamer Zustand, Spiegeln, Hüfte, GUI-Sync |
| `gui` (Z. 37-41) | 16 | 147 | Demo-GUI (Vollbild, Sync, Temperaturen, Abläufe, Hüfte, Real beenden), Batterie/Temperatur, Fenster-Icons, Handy-GUI |
| `haende` (Z. 42) | 1 | 4 | Inspire-Modbus-Backend |
| `sim` (Z. 43) | 5 | 55 | Lauf-Policy (`test_walk_policy`), `loco_sim`-Zustand, Schubs, Auto-Start, Hand-Profil |
| `handy` (Z. 44-45) | 5 | 63 | Gateway, BLE gegen nachgebautes BlueZ, `proto.js`, Handy-Seite in Chromium, Handy-GUI |
| `schnell` (Z. 46-50) | 43 | 547 | alles außer den drei langsamen Dateien |
| `voll` (Z. 51) | 46 (ganzes `test/`) | 597 | komplette Suite |

- Gruppen überlappen (Dateien in mehreren Gruppen). Nur `test_phone_web_offline.py` steht in keiner benannten Gruppe (nur `schnell`/`voll`) (Abgleich Skript gegen `ls`).
- Kommentar im Skript: übersprungene Tests werden mit `-rs` samt Grund angezeigt; „fehlt z. B. pinocchio, skippen ganze Dateien still -- dann ist der Lauf KEIN Nachweis“ (`run_tests.sh:13-14`, `exec ... pytest -q -rs` Z. 70).
- Dauerangaben der Doku (`schnell` 2 min, `sicherheit` 10 min, `voll` 14 min; `run_tests.sh:9-11`, `60-A-Tests.md:30-34`) sind Doku-/Skriptkommentar-Angaben, keine hier gemessenen Werte.
- Gruppen verlangen nur vorhandene Dateien (`run_tests.sh:63`); Exit 5, wenn keine existiert (Z. 65-68).

### Zusätzliche Skripte außerhalb von `test/` (kein pytest, Exit-Code bzw. Ausgabe)

| Skript | Art | Fundstelle |
|---|---|---|
| `G/test_ps4_arm_sim.py`, `G/test_waist_yaw_sim.py`, `G/test_sim_startup_grasp.py`, `G/run_startup_grasp_loop.sh` | Ende-zu-Ende gegen laufende Sim (Container `g1pilot-sim`) | `60-A-Tests.md:63-80` |
| `G/test_agile_walk_sim.py`, `G/test_wholebody_policy.py` | headless MuJoCo ohne ROS/DDS | `60-A-Tests.md:82-87` |
| `unitree_mujoco/simulate_python/test/{gamepad_test.py,test_unitree_sdk2.py}` | gehören zum Simulator-Repo; in `run_tests.sh` und Doku nicht erwähnt | `ls unitree_mujoco/simulate_python/test` |

## (b) Attrappe des Roboters: was nachgebildet wird, was nicht

Zwei getrennte Attrappen, beide ersetzen das Unitree-SDK (`unitree_sdk2py`) per `sys.modules`-Austausch; der Code von `arm_controller` und `loco_client` läuft unverändert (`G1_SIM_MODE=false`).

### Arme: `G/test/test_arm_controller_real.py` (60 916 Byte, 43 Testfunktionen)

Nachgebildet (Klassen `_Motor`, `_LowCmd`, `FakeG1`, `_install_unitree_stubs`, Z. 29-160):
- `rt/lowstate` (Messung, 35 Motoren, `mode_machine=5`) und `rt/arm_sdk` (`LowCmd_`, 35 Motoren); `ChannelSubscriber.Read` liefert den Zustand, `ChannelPublisher.Write` ruft `FakeG1.write` (Z. 140-160).
- Mischgewicht wie beim echten G1: `soll = w*arm_sdk + (1-w)*Onboard-Pose` mit `w = motor_cmd[29].q` (Docstring Z. 6-8; `FakeG1.write`).
- Messung folgt dem Soll als einfaches Nachlaufen (Faktor 0,5 je Write), optional bleibender Regelfehler `sag` und Haftreibung `friction` je Gelenk (`FakeG1.__init__`, `write`).
- E-Stop-Schlaffschaltung: `w>0` und `kp=0` lässt die Arme sacken (Messung bleibt stehen) (`write`).
- Taille (Gelenke 12-14): Mischung nach Gewicht, effektive Steifigkeit `(1-w)*200 + w*kp`; unterhalb `PENDULUM_K = 26.0` Nm/rad kippt der Oberkörper (Pitch +0,01 je Write, Obergrenze 0,52) (Konstanten Z. 34-44, `_waist_write`). Kommentar der Konstante: „grobe Schätzung“.
- `arm_controller` läuft mit manuell getriebenem `main_loop` (`DT = 0.004`); Planer-Prozess und IK sind echt (`_make_node`, `_wait_planner`).

Nicht nachgebildet (aus dem Code ersichtlich):
- DDS-Transport: `ChannelFactoryInitialize` ist leer, `init_dds` auf No-op gesetzt (`ac.init_dds = lambda ...`), `CRC.Crc` liefert 0. Keine Latenz, kein Paketverlust, kein Jitter zwischen Kommando und Zustand.
- Keine Beine/Gleichgewicht, keine Hände (Inspire), keine Temperaturen/Fehlerbits, keine Kollisionen; Armdynamik nur Nachlauffaktor, keine Trägheit/Reibungsmodell (außer den optionalen Feldern).
- Onboard-Regler nur als feste Pose `ONBOARD` bzw. `ONBOARD_WAIST` (Z. 34-41).

### Beine/Gehen: `G/test/test_loco_client_real.py` (46 650 Byte, 73 Testfunktionen)

Nachgebildet (`FakeLoco`, `lc_module`, Z. 28-110; `FakeLoco` Z. 28, `lc_module` Z. 93):
- RPC-Aufzeichnung: `SetFsmId`, `SetVelocity`, `StopMove`, `SetStandHeight`, `BalanceStand`, `Start`, `Damp`; Abfragen `GET_FSM_ID`/`GET_FSM_MODE` liefern JSON `{"data": n}`.
- FSM-Zustand als Zahl (4 Ready/Preparation, 500 Walk, 1 Damp), Wechsel sofort beim Aufruf; Ausfall einzelner RPCs über `fail`-Menge (`RuntimeError("rpc down")`).
- Dienstname `LOCO_SERVICE_NAME = "loco"` wie im Real-Image (SDK-Commit 7c661d2) (Z. 101).
- Bodenkontakt über Knie-Last mit Testuhr (Standard 14 Nm je Knie) (`_make`, `_knees`).
- Joy-/Twist-/Bool-Nachrichten werden direkt in die Callbacks gegeben (`_joy`, `_cmd`, `_bool`).

Nicht nachgebildet: tatsächliche Fortbewegung/Balance (keine Dynamik, Geschwindigkeit wird nur gespeichert), Verzögerung beim Moduswechsel, DDS-Transport (`common.init_dds` ersetzt), Unitree-Fernbedienung/App.

### Messsonde: `G/test/teleop_jitter_probe.py` (13 169 Byte, kein Test, Skript)

- Nutzt `FakeG1`-Stubs aus `test_arm_controller_real.py`, aber echten ROS-Timer des Knotens (`rate_hz` = 250,0 Hz, `G/g1pilot/manipulation/arm_controller.py:268`) in eigenem Executor-Thread.
- Ersetzt `FakeG1.write` durch ein 1-kHz-Gelenkmodell je Armgelenk `I*q'' = kp*(q_cmd-q) - kd*q'` mit `I_ARM = 0.03` kg m² („grobe effektive Trägheit, Annahme“, Z. 27); optionale Störung der Taille und Encoder-Rauschen (`--waist-noise`, `--enc-noise`).
- Aufruf: `python3 test/teleop_jitter_probe.py [--waist-noise] [--enc-noise] [--seconds 3.0] [--speed 0.05] [--jog-rate 30.0] [--param k=v]`.
- Ausgabe je Phase `JOG`, `HALTEN`, `MARKER`, `GEPLANT` (Z. 266, 306 u. a.): `writes_hz`, `dt_p50_ms`, `dt_p95_ms`, `dt_max_ms`, `step_max_mrad`, `stand_ticks_pct`, `cmd_dv_p95`, `acc_hf_rms` (Funktion `metrics`, Z. 93-130); zusätzlich Zeilen zu IK-Aufrufen (ms/Aufruf, Iterationen), Restabstand Hand zu Ziel in mm.
- Docstring: Zahlen „taugen zum Vergleich, nicht als Absolutwerte“ (Z. 20-21). Wandzeit des Python-Prozesses, kein Sim-Echtzeitfaktor.

## (c) Ausdrücklich nicht Abgedecktes

- `G/docs/60-A-Tests.md:89-93` („Was nicht abgedeckt ist“): (1) echter G1 (Hardware), erste Läufe nach `50-A-Echter-Roboter.md`; (2) echtes Bluetooth (BlueZ + Android-Chrome) für das Handy; (3) LED und Vibration echter Controller.
- `60-A-Tests.md:21-23`: Unit-/Integrationstests laufen „ohne Roboter und ohne laufende Sim“; Real-Pfad gegen Fake-G1/Unitree-SDK-Attrappen, GUIs offscreen (`QT_QPA_PLATFORM=offscreen`, Z. 56-57).
- `60-A-Tests.md:59-61`, `run_tests.sh:13-14`: fehlen Pinocchio oder Unitree-SDK, überspringen Dateien still; Lauf dann „kein Nachweis“.
- `60-A-Tests.md:54-56`: Laufzeit-Images enthalten nicht alles (z. B. kein `pytest`); Testimage separat nötig, in Doku nur als „bewährt“ genannt (`ros:humble` oder micromamba/robostack, Python 3.11). Kein Dockerfile für ein Testimage im Repo (`find -name "Dockerfile*"` zeigt nur `docker/Dockerfile.{sim,real,mujoco}` im g1pilot und drei im `unitree_ros2`).
- `60-A-Tests.md:63-66`: Ende-zu-Ende-Skripte brauchen einen laufenden Sim-Stack; sie liegen nicht in `test/`, nicht in `run_tests.sh`.
- Aus dem Code (Abschnitt b): keine Netzwerk-/DDS-Effekte, keine Dynamik der Beine, keine Zeitmessung der Reaktionen (siehe e, V8).
- `jog_axis_probe_sim.py` und `test_agile_walk_sim.py` sind Messskripte bzw. Regressionsszenarien, nicht Teil der pytest-Suite.

## (d) Softwarestände (Docker)

| Merkmal | Wert | Fundstelle |
|---|---|---|
| Basis-Image Sim und Real | `ros:humble` (Tag, keine Digest-Pinnung) | `G/docker/Dockerfile.sim:1`, `Dockerfile.real:7` |
| Basis-Image MuJoCo-Container | `ubuntu:22.04` | `G/docker/Dockerfile.mujoco:1` |
| ROS-2-Distribution | Humble (`ENV ROS_DISTRO=humble`) | `Dockerfile.sim:5`, `Dockerfile.real:11` |
| Python im Container | nicht gesetzt; folgt der Basis (Ubuntu 22.04). Kommentar „cp310 fuer Ubuntu 22.04 = ros:humble“ | `Dockerfile.sim:47-50` (Kommentar zu `ompl`) |
| MuJoCo (Python) | `pip3 install mujoco pygame numpy`, **keine Versionsangabe**; installierte Version aus dem Repo nicht ermittelbar | `Dockerfile.mujoco:14` |
| MuJoCo-Simulator | `unitree_mujoco/simulate_python/` (Python-Variante) wird ins Image kopiert; Compose bindet `../unitree_mujoco` zusätzlich read-only ein | `Dockerfile.mujoco:23-24`, `G/docker-compose.yml` (Service `mujoco-sim`, `volumes`) |
| Physikschritt Sim | `SIMULATE_DT = 0.001` s; Regeltakt Lockstep `SIM_CONTROL_DT = 0.02` s (Env überschreibbar), Dezimierung 20 | `unitree_mujoco/simulate_python/config.py:66,103-104` |
| Hersteller-SDK (Python) | `lnotspotl/unitree_sdk2_python`, Commit `7c661d27f4ae064ffd0dd633fd9d5b518ef0b508`, `pip3 install -e .` (in allen drei Dockerfiles gleich) | `Dockerfile.sim:36-39`, `Dockerfile.real:42-45`, `Dockerfile.mujoco:16-19` |
| Hersteller-SDK-Kopie im Repo | `unitree_sdk2_python/` (setup.py: Version 1.0.1, `cyclonedds==0.10.2`); **wird in keinem Dockerfile verwendet** (Docker klont die Fork-URL) | `unitree_sdk2_python/setup.py` |
| DDS-Implementierung (ROS) | `rmw_cyclonedds_cpp` (apt `ros-humble-rmw-cyclonedds-cpp`, Version nicht gepinnt); `CYCLONEDDS_URI=file:///etc/cyclonedds.xml` | `Dockerfile.sim:81-82`, `Dockerfile.real:80-81` |
| DDS-Konfiguration | Interface `lo`, Multicast aus, Peer 127.0.0.1 | `G/docker/cyclonedds.xml` |
| DDS-Domains | Sim: ROS 0, Unitree 1 (Interface `lo`); Real: ROS 1, Unitree 0 auf `ROBOT_INTERFACE` (Default `eth0`) | `Dockerfile.sim:72-75`, `Dockerfile.real:70-72`, `docker-compose.yml` (Service `g1pilot-real`) |
| Pinocchio | Sim `pin>=3.0`, Real `pin>=2.6` (unterschiedliche Untergrenzen, keine Obergrenze) | `Dockerfile.sim:43`, `Dockerfile.real:48` |
| Weitere Pakete (ungepinnt) | `pyqt6`, `meshcat`, `evdev`, `numpy`, `dbus-next`; Sim zusätzlich `ompl` (Fallback RRT-Connect, wenn fehlt), `onnxruntime`, `onnx` | `Dockerfile.sim:43-56` |
| Z. Zt. Sim-Image nicht enthalten | `pytest` | `60-A-Tests.md:54-55` |
| Image-Tags | `g1pilot-sim:v1.1.0`, `g1pilot-real:v1.2.0`, `g1pilot-mujoco:v1.0` | `G/docker-compose.yml:31,75,167` |
| Compose-Dateien | `docker-compose.yml` (Profile `sim`, `real`); Zusätze `docker-compose.gpu.yml` (`/dev/dri`), `docker-compose.nvidia.yml` (`gpus: all`), `docker-compose.ps4.yml` (Eingabegeräte, Sim) | `ls G/docker-compose*` |
| Sim-Takt-Parameter in Compose | `SIM_REALTIME_FACTOR` (Default 1.0), `SIM_LOCKSTEP` (Compose-Default 1; `config.py`-Default False) | `docker-compose.yml` (mujoco-sim `environment`), `config.py:80,102` |
| Roboter-Konfiguration Real (Compose-Defaults) | `G1_WALK_FSM_ID=501`, `G1_LOCO_SERVICE=sport`, `G1_MAX_VX/VY/VYAW=0.4/0.3/0.4`, `G1_KNEE_LOAD_MIN_NM=10.0`, `G1_WAIST_KP/KD=150.0/4.0` | `docker-compose.yml` (Service `g1pilot-real`) |
| Host-OS laut Doku | Ubuntu 22.04 oder 24.04 (Real: nativ, kein WSL2) | `G/docs/01-A-Installation.md:24`, `50-A-Echter-Roboter.md:34` |
| Referenz-PC, Roboter-Firmware, Unitree-Softwarestand am G1 | **nicht im Repo ermittelbar** (Nils liefert) | – |

## (e) Versuche V1 bis V11: vorhandene Skripte, Ausgabe, Lücken

Mittel-Spalte des Plans (Abschn. 7.2) am Code geprüft. Pfade relativ zu `/home/user/G1`.

| Versuch | Vorhandenes | Ausgabe | Fehlt |
|---|---|---|---|
| V1 Code/Konfiguration Sim vs. Real | Kein Skript. Betriebsart-Abfragen: 46 Treffer (`is_sim_mode()`, `self.sim_mode`, `G1_SIM_MODE`) in 6 Dateien unter `G/g1pilot/` ohne `tools/`: `demo_gui.py` 22, `arm_controller.py` 14, `utils/common.py` 6, `utils/hand_profile.py` 2, `sim_autostart.py` 1, `ps4_arm_teleop.py` 1 (`grep -rcE "is_sim_mode\(\)\|self\.sim_mode\|G1_SIM_MODE" --include=*.py G/g1pilot`). Zusätzlich getrennte Startdateien `G/launch/bringup_sim.launch.py` (236 Z.), `bringup_real.launch.py` (212 Z.), getrennte Knoten `loco_sim` vs. `loco_client`, Dockerfiles/Compose-Profile `sim`/`real` | – | Auswerteskript; Zählung ist hier nur eine Stichprobe mit einem Suchmuster |
| V2 Funktionsprüfung am G1 | Ablauf `G/docs/50-A-Echter-Roboter.md` Abschnitt F (Z. 290-400): Demo-GUI-Ablauf (7 Schritte, Z. 292-314) und Einzeltests ab Z. 316; DDS-Check `G/g1pilot/tools/sim_dds_check.py` (Alias `dds_check`, Docstring: „rt/lowstate mit ~500 Hz“ als Erwartung) | `dds_check`: sekündliche Meldung zu `rt/lowstate`-Eingang, `mode_machine`, Armwinkel | Protokoll mit Prüfkriterien, Daten |
| V3 Werbevideo | – | – | alles (Angaben von Nils) |
| V4 Echtzeitfaktor, Takttreue | `G/test/teleop_jitter_probe.py` (Befehlsstrom der Arme, Wandzeit, Fake-G1; siehe b). In `loco_sim`: Regeltakt-Überwachung alle 100 Takte, nur Warnung bei Regeltakt < `LOOP_HZ_WARN_FRAC` = 0,9 des Solls oder Neigung (`G/g1pilot/navigation/loco_sim.py:104-106, 579-606`); bei `lockstep` wird `eff` auf Soll gesetzt, also keine Messung; Voll-Statuszeile nur mit `G1_LOCO_DEBUG=1`. Sim: `SIM_REALTIME_FACTOR` nur Soll-Deckel, kein Messwert (`unitree_mujoco/simulate_python/unitree_mujoco.py:166-178, 186-250`) | Probe: `writes_hz`, `dt_*_ms` usw.; `loco_sim`: Logzeilen | Ausgabe des Echtzeitfaktors (Simulationszeit je Wandzeit) und des Taktes der Sim-Schleife; keine Ausgabe der Takttreue des Sim-Kanals `rt/lowstate`/`rt/lowcmd` |
| V5 Fortbewegung Simulation | `G/test_agile_walk_sim.py` (560 Z., headless MuJoCo, `--policy`, `--rescue-policy`, `--inspire`, `--quick`): Szenarien 1) Laufen+Anhalten, 2) Arme frei beim Laufen, 3) Policy im Stand 20 s, 4) PD-Stand mit Arm und Last, 5) Übergänge PD-Stand/Policy, 6) Zufallsübergänge, 7) Anlauf mit cmd=0, 8) Stöße auf den Torso (Z. 382-543); `G/test_wholebody_policy.py` (Policy `g1_wholebody`: Stillstand, Laufen, Anhalten) | Zeilen `[OK ]/[FAIL]/[info]` mit Detailwerten, Schlusszeile `ERGEBNIS: BESTANDEN/DURCHGEFALLEN`, Exit-Code (Z. 345-356, 555) | Lauf gegen die ROS-/DDS-Sim-Kette (die Skripte nutzen die Regler-Module, nicht `loco_sim`/Bridge); Roboter: `G/g1pilot/tools/walk_diag.py` (588 Z.) `record` (CSV, 50 Hz, nur lesend) und `analyze`; Daten und Auswertung gegen Befehl liegen nicht im Repo |
| V6 Manipulation Simulation | Tippbetrieb: `G/jog_axis_probe_sim.py` (376 Z.; Abweichung der Nebenachsen, Weg/quer/ori, `--mirror`, `--reference`, `--json`, `--quick`; braucht Sim mit `G1_PS4_ARMS=1`). Planer: 11 Testfunktionen in `G/test/test_arm_planner.py` (FK, Kollisionsabstand, Grenzen, Abbruch, Zielablehnung); `G/g1pilot/tools/sim_goal_probe.py` (Sinusziel auf Achse, loggt 1x/s Soll/Ist); der Planer liefert `plan_time_s` im Ergebnis (`G/g1pilot/manipulation/arm_planner.py:702`) | Probe: Tabellenzeilen je Startpose/Richtung (Maße s. Docstring); Tests: pass/fail; `plan_time_s` im Planerergebnis | Messreihe: feste Testfälle mit Erfolg und Rechenzeit; Restfehler der inversen Kinematik als Ausgabe |
| V7 Sim gegen Roboter, Gelenkwinkel | `G/g1pilot/tools/sim_arm_monitor.py` (liest `rt/arm_sdk`, `rt/lowstate`, loggt Fenster `cmd/meas/d/osc`, `--window`, `--seconds`), `G/demo_sequence.py` (fährt gespeicherte Posen aus `G/data/arm_poses.json` über die Arm-API ab, `--loop`, `--dry-run`), Posen in `G/data/arm_poses.json` | Monitor: Textzeilen je Fenster, keine Datei | Aufzeichnung mit Zeitstempel als Datei, gleiche Auswertung für Sim und Roboter; Daten |
| V8 Schutzmechanismen | `test/run_tests.sh sicherheit` (25 Dateien, 442 Testfunktionen); Testfunktionen mit `estop`/`stop`/`emergency`/`notaus` im Namen: 96 (`grep -hE "^def test_.*(estop\|e_stop\|emergency\|notaus\|stop)"`); Not-Halt-Stufen `G/docs/51-A-Notaus.md` | pytest: Punkte/Fehler, `-rs`-Skips | Zeitmessung (Auslösen bis Befehl), größte Handgeschwindigkeit bei Zielsprüngen; keine Reaktionszeit in `test/` (`grep -rniE "latenz\|reaktionszeit\|latency" G/test` ohne Treffer) |
| V9 Bedienaufwand | Schrittfolgen: `G/docs/01-A-Installation.md` (Schritt für Schritt Z. 36-141, „Starten im Alltag“ Z. 280), `G/docs/50-A-Echter-Roboter.md` Kurzfassung (Tabelle mit 8 Schritten, Z. 13-26); `G/start.sh`, `G/Makefile` (`make sim`, `make build-sim`, `make build-real`) | – | Zeiten (Doku nennt Bauzeiten „ca. 8 / 10 Minuten“ in `Makefile`-Kopf und `01-A`:85; das sind Doku-Angaben, keine Messung) |
| V10 Externes Projekt | `G/examples/arm_api/` (`arm_cli.py`, nur Standardbibliothek, Befehle `state/joints/pose/cancel/status/save`; Anleitung `G/docs/21-A-Arm-API.md`); Schnittstelle: `arm_api` (Knoten in `G/launch/manipulation_launcher.launch.py:155`), `127.0.0.1:8770` (`demo_sequence.py`-Kopf) | – | Projekt offen (Nils); der Beispiel-Client ist Teil des Repos |
| V11 Neue Aufgabe | Szenen-Editor `unitree_mujoco/scene_editor/` (`run_editor.py`, `build_env_scene.py`, `setup.sh`, Szenen `scenes/*.json/xml`), Ablaufwerkzeuge `G/pose_tool.py`, `G/demo_sequence.py`, `G/g1pilot/tools/install_example_sequences.py`, Tests `test_sequences.py`, `test_demo_gui_sequences.py` | – | Durchführung und Zeitaufwand |

## Abweichungen Doku gegen Code (Code gilt)

1. Anzahl Testfunktionen/-dateien: `G/docs/60-A-Tests.md:21` „Rund 550 Testfunktionen in 43 Dateien“; Code: 597 Testfunktionen in 46 Dateien. Die Doku-Zahlen entsprechen der Gruppe `schnell` (547 in 43 Dateien) bzw. wirken veraltet.
2. Gruppeninhalt `sicherheit`: Doku `60-A-Tests.md:33` „Notaus, Totmann, Walk/Modus, Bodenkontakt, Arm-Controller real, Planer, Handy-Gateway“; Skript nennt 25 Dateien, darunter auch Inspire-Modbus, Demo-GUI-Dateien, Xbox-Layout, Handy-GUI, Taille, Abläufe (`run_tests.sh:21-27`). Doku-Kurzfassung unvollständig.
3. Gruppen `planer` und `sim`: Doku `60-A-Tests.md:36,41` nennt `test_hand_profile` nicht; Skript enthält es in beiden (`run_tests.sh:30,43`). Gruppe `loco`: Doku ohne `test_walk_diag`, Demo-GUI-Dateien, Hüftdrehung (`run_tests.sh:31-33`).
4. `test_phone_web_offline.py` steht in keiner benannten Gruppe; Doku nennt sie nicht.
5. Python-Version: Doku `60-A-Tests.md:56` nennt Python 3.11 (micromamba) für Tests, `01-A-Installation.md:107` Host-Python 3.10/3.12; Container-Python folgt `ros:humble` (Ubuntu 22.04, 3.10 laut Kommentar `Dockerfile.sim`). Mehrere unterschiedliche Stände je Zweck, nirgends eine feste Versionsangabe im Code.
6. Pinocchio-Untergrenze: Sim-Image `>=3.0`, Real-Image `>=2.6`; Doku `60-A-Tests.md:49` nennt „Pinocchio (für `com_model` Version 3)“ ohne Hinweis auf das Real-Image.
7. `G/Makefile` (Kopf) „es gibt bewusst keine separaten docker-compose.*.yaml-Dateien mehr“ (Ausnahme gpu/nvidia genannt); vorhanden ist zusätzlich `docker-compose.ps4.yml` (wird von `start.sh` automatisch dazugenommen, Kopfkommentar der Datei).
8. Bauzeiten (Makefile „~8 min“/„~10 min“, `01-A`:85 „ca. 8 Minuten“) und Testdauern sind Doku-Angaben; nicht nachgemessen.
9. Hersteller-SDK: Repo enthält `unitree_sdk2_python/` (Unitree, `cyclonedds==0.10.2`), die Images installieren aber einen Fork (`lnotspotl`, Commit 7c661d2). Für die Testumgebung maßgeblich ist der Fork-Stand.

## Nicht ermittelbar am Repo

- Gesammelte Testfallzahl inklusive Parametrisierung (kein `pytest`/`rclpy` hier); tatsächlich installierte Versionen von MuJoCo, CycloneDDS, ROS-Paketen und Pinocchio (ungepinnt); Python-Minorversion im Container (nur über Basis-Image-Kommentar belegt).
- Referenz-PC (CPU, RAM, GPU, Betriebssystem), Roboter-Firmware/Unitree-Softwarestand, Netzwerkaufbau real: Angaben von Nils.
- Ausgabeformat der Probe `teleop_jitter_probe.py` mit Zahlenwerten (nicht ausgeführt; keine Messwerte übernommen).
