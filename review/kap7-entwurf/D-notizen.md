# Paket D: 7.6 Bedienwege (Entwurf 27.11.2026, Code @6a40e47)

## (a) Faktenblatt (Pfade relativ zu g1pilot/g1pilot/, Zeilen aus Stand @6a40e47)
- Gemeinsamer Zustand: teleoperation/shared_state.py:3-28,43,47-53,60-107 (latched JSON, Feld-Zeitstempel, neuester gewinnt, Stempel > gesehen, Startwerte DEFAULT_STAMP 1.0, keine Fahrbefehle, jeder Teilnehmer kappt auf eigenes Maximum).
- Posenspeicher JSON v3: manipulation/pose_store.py:13-17,59-77,105-109,274-287 (7 Gelenke/Arm, 6 Finger, Bewegungen je Achse <= 0,30 m, wait_s <= 600 s, 16 Schnellwahlplätze, atomar tmp + os.replace); arm_controller.py:2649-2660 (Speichern = zuletzt kommandiertes Ziel).
- Ablaufsteuerung: teleoperation/sequence_runner.py:4-58,123-243 (ACK_TIMEOUT_S 4,0, MIN_GAP_S 0,3); demo_gui.py:176-198 (Standard Sim am Stück, real Schritt), 2136-2190.
- Auto-Start nur Sim: teleoperation/sim_autostart.py:43-47 (1,5 s, 120 s), demo_gui.py:1146-1162; real Modusauswahl bis Start gesperrt: demo_gui.py:1832-1875.
- Not-Halt/Voll-Notaus: demo_gui.py:150 (QUIT_CONFIRM_MS 4000 = zweiter Tipp 4 s), 153 (FULL_ESTOP_HOLD_S 1,5), 1301-1316, 2462-2549; Quittierung real Startknopf, Sim nächste Modusauswahl.
- Controller: ps4_joystick.py:1-48,68 (stall 0,3 s),381-398; ps4_layout.py:1-20; ps4_walk.py:30-47 (Totmann 0,5), 230 (joy_timeout 0,3); ps4_arm_teleop.py:826-880 (joy_timeout 0,5, Totzone 0,12, axis_snap 20 Grad, Voll-Notaus 2,0 s, quick_timeout 1,5 s), 537-560,1134-1215 (Schnellwahl, Antwort <= 3 s); hand_jog.py:122-135,181-229,263-267 (5/15/30 cm/s, Vorlauf max(4 cm, v*0,5 s), Halteziel 1 s); loco_client.py:714-735 und loco_sim.py:550-556 (Vorrang walk_cmd); Tempostufen 0,35/0,65/1,0 ps4_walk.py:222-230; real Start Langsam/max Normal: launch/bringup_real.launch.py:49-57.
- Smartphone: teleoperation/phone/protocol.py:3-23,41-45,78-113; gateway.py:42-78 (CONTROL 2,0 s, SESSION 4,0 s, STATUS_MAX_LAG 15 = 3 s bei 5 Hz), 163-171,296-410; link.py:36-48,65-71,125-143 (Vermittlungsschicht im Prozess der Bedienoberfläche, demo_gui.py:1143); web/app.js:2-12 (HB_MS 200, FRESH_MS 1500).
- Zielmarker: manipulation/interactive_marker.py:21-70 (goal_timeout_s 30), 249-277, 377-410; NOTICE.md (Herkunft HucebotG1Pilot, etwa 50 % Eigenanteil laut NOTICE).
- Arm-API: manipulation/arm_api.py:3-30,51-53 (ACCEPT 2,0 s, MAX_WAIT 300 s),82-106,222,285-310; arm_command.py:3-31; Bind 127.0.0.1:8770, extern nur mit bind_host und auth_token.
- Direkter DDS-Zugang: utils/common.py:15-47; Belege UnitreeMujoco.01/.07/.08.
- Zeitüberwachungen gegen Kommentar unter tab:schutzmechanismen (Kap. 6) geprüft: alle Werte bestätigt. Fahrbefehl-Timeouts der Onboard-Anbindung (loco_client cmd_vel_timeout 0,5 s, move_duration 1,0 s) stehen nur in 7.3.2, hier nur per \ref.

## (b) Vorgeschlagene neue Belege
Keine. Verwendet nur vorhandene IDs: Macenski2022.15, UnitreeMujoco.01, .07, .08.

## (c) Offene \qf / \pruefen
1. \qf Web Bluetooth / Bluetooth Low Energy (GATT) (7.6.3)
2. \qf HMAC (RFC 2104; Krawczyk nur in _Vorschläge) (7.6.3)
3. \qf RViz und interaktive Marker (7.6.4)
4. \pruefen Bild von Nils: Bilder/kap7/demo-gui-gesamt.png, Bereiche beschriften (7.6.1)
Hinweis: Der Quellenbezug Macenski2022.15 (transient-local / flüchtig) sollte vom Hauptagenten gegen den Wortlaut gegengelesen werden. HucebotG1Pilot wird nur per \ref{sec:ausgangsbasis} zitiert.

## (d) Abweichungen vom Plan
- Smartphone: Vermittlungsschicht läuft im Prozess der Bedienoberfläche (kein eigener Dienst), Abb. B7.13 gruppiert beide.
- Arm-API per HTTP bietet nur Gelenke, Pose, Speichern, Abbrechen. Mirror-Typ nur über Controller.
- T7.6 um Zeile "Direkter DDS-Zugang" ergänzt (Zeitüberwachung: keine).
- Zeitwerte der Fahrbefehle der Onboard-Anbindung nur per \ref auf 7.3.2, nicht dupliziert.
- Kein Streamdeck. Anhang-Verweis nur ein Satz. Controller-Typen werden in der Einleitung erklärt.
- Abbildung nutzt \acs{...}, damit in der Grafik nur Kürzel stehen.

## (e) Fehlende Abkürzungen in main.tex
DDS, BLE, HMAC, HTTP, JSON (im Test mit Definitionen: Data Distribution Service, Bluetooth Low Energy, Hash-based Message Authentication Code, Hypertext Transfer Protocol, JavaScript Object Notation). ROS 2 und Arm-API im Text ausgeschrieben bzw. mit \ref.

## (f) Umfang
Gemessen im Testdokument (12pt, Präambel von main.tex): ca. 4,3 Seiten inkl. Abb. B7.13 (ca. 0,35 S.), Tabelle (ca. 0,5 S.), Platzhalter (ca. 0,3 S.); Sollwert 3,8 (+-15 % = 4,4 max). Kürzungskandidaten: Absatz Pose-Schnellwahl, Hand-Jog-Parameter in 7.6.2. Offen: Querverweise (sec:bedienwege_konzept, tab:bedienwege u. a.) im Testdokument ungeprüft, da Kap. 6 fehlte.
