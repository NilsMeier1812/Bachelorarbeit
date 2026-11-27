# Paket E: Notizen (7.4.2 Kollisionsmodell, 7.4.3 Bahnplaner, 7.4.4 Laufzeitüberwachung)

Stand 27.11.2026. Code-Bezug: G1 **PR #62 @e452513** (Worktree `/home/user/g1-pr62`), das ist BA-Stable `6a40e47` + 2 Commits,
geändert nur `arm_planner.py`, `arm_planner_process.py`, `arm_geometry.py` (+ Doku/Tests). Alle `% DB:`-Kommentare in `E.tex`
nennen `@e452513`, auch für unveränderte Dateien, damit die Zeilennummern zusammenpassen. Nach dem Merge: Hash ersetzen, Zeilennummern
in `arm_planner.py` und `arm_geometry.py` prüfen (in den anderen Dateien gleich wie 6a40e47).

## (a) Faktenblatt

Pfade relativ zur Repo-Wurzel G1. `AP` = `g1pilot/g1pilot/manipulation/arm_planner.py`, `AG` = `.../arm_geometry.py`,
`AC` = `.../arm_controller.py`, `IK` = `g1pilot/g1pilot/utils/ik_solver.py`.

| Aussage im Text | Wert | Fundstelle @e452513 | Sim/Real |
|---|---|---|---|
| Kugeln beim Start aus Kollisionsnetzen, Oberfläche (Ecken + Dreiecke) abgetastet | Punktabstand 5 mm | AG:58-62, 195-250 | beide |
| Clusterverfahren (k-means mit FPS-Start), Radius = entferntester Punkt, k steigt bis r ≤ r_max oder k_max | k_max 40 Hand / 12 Arm / 10 grob / 24 Körper | AG:114-149, 396-405, 435 | beide |
| Feiner Satz gegen Umgebung | Hand 2,2 cm, Arm 4 cm | AG:335, 387-402 | beide |
| Grober Satz gegen Körper/anderen Arm ab Ellbogen (SELF_LINK_MIN = 3) | 5 cm | AG:43-46, 403-408 | beide |
| Körperkugeln (Rumpf, Kopf, Becken, Hüften, Knie) | 9 cm | AG:47-53, 424-436 | beide |
| „Hand“ = ab Glied 5 (wrist_pitch, wrist_yaw, Finger) | HAND_LINK_MIN = 5 | AG:39-42 | |
| Weltmodell als orientierte Quader, Vorauswahl erreichbarer Objekte | REACH_RADIUS 1,5 m, Reichweite je Arm | AG:54-57, 279-322, 486-498 | |
| Vorzeichenbehafteter Abstand Kugel–Quader + Gradient, eigene vektorisierte FK | | AG:506-618 | |
| Quader = je konvexer Teilkörper eines zerlegten Hindernisses bzw. Ablagefläche; Greifobjekte live | | `unitree_mujoco/simulate_python/scene_objects.py:277-309`, `scene_state_publisher.py:15-21` | nur Sim |
| Weltmodell nur in der Simulation (einziger Sender `scene_bridge`, nur in `bringup_sim` gestartet) | | `g1pilot/launch/bringup_sim.launch.py:125-132`, `g1pilot/g1pilot/navigation/scene_bridge.py:56`; `bringup_real.launch.py` ohne Szene | **nur Sim** |
| Handkugeln dürfen Greifobjekte berühren | | AP:155-158; AC:1633 (`-inf`) | |
| Abstandsbedarf (G7.6), smoothstep, Endwert min(0, d_end) | C 5 cm, R 15 cm, Körper/Arm 1,5 cm | AP:72-85, 112-114, 160-180, 251-272, 297-316 | beide |
| **PR #62:** nahe an beiden Enden gilt der tiefere Endwert | | AP:264-271 | beide |
| 24 innere Stützpunkte, Kosten Glattheit + Handweg + Strafe + Anfahrrichtung | W_VEL 1, W_ACC 4, W_CART 10, W_COLL 4000, W_APP 400; approach_len 10 cm | AP:86-88, 102-109, 194-245, 356-404 | |
| Vorkonditionierung mit H⁻¹, Schrittweite (Vertrauensbereich), Kosten müssen sinken, W_COLL ×5 bis 4-mal | | AP:231-245, 407-464 | |
| Zielprüfung: Selbstkollision (Mesh, hart); **PR #62:** exakte Geometrie, Ablehnung ab 2 cm Eindringtiefe (vorher Kugelmodell) | goal_max_depth 0,02 | AP:78-80, 730-744; AG:621-696; `arm_planner_process.py:53-58,115-125` | beide |
| Rückfallkette: Gerade → Optimierung aus Startbahnen (Gerade, 15 cm anheben, 15 cm zurückziehen, **PR #62:** 30 cm anheben) → RRT-Connect bei C_min, Glättung mit steigendem Abstand → reduzierter Abstand mit 2 besten Bahnen + über Lauf-Pose | Abstandsstufen 5 / 3 / 1,8 / 1,5 cm | AP:516-615, 746-833 | |
| Budget | 2,5 s CPU-Zeit, Wandzeit-Obergrenze 3× | AP:65-70, 89, 706-711 | |
| Abschlussprüfung dicht (0,03 rad / 12 mm), Toleranz 4 mm, Gelenkgrenzen, exakte Selbstkollision | | AP:91, 467-501 | |
| Zeitparametrierung (Vor-/Rückwärtsdurchlauf), 1,2 rad/s, 2 rad/s², 0,22 m/s, 0,6 m/s², unter 5 cm bis 35 % | effektiv min(Planerwert, 0,95 × Reglergrenze): real 1,5 rad/s / 0,25 m/s, Sim 1,5 rad/s / 0,5 m/s → in beiden 1,2 und 0,22 | AP:93-99, 621-663; AC:2969-2980; `bringup_sim.launch.py:112`, `bringup_real.launch.py:106-107` | gleich |
| Eigener Prozess (nice +2), gemeinsame Planung beider Arme, Ergebnisse überholter Anfragen verworfen (Generationszähler) | | `arm_planner_process.py:1-41`; AC:2745-2779, 2982-3131, 3148-3171 | |
| Nutzer: Pose-Store, arm_command (API/Abläufe), Grundstellung, Lauf-Pose, Rückgabe | | AC:2966, 2837/2862, 2363, 2483, 1382 | |
| Laufzeitüberwachung in jedem Takt, nach Geschwindigkeits-/Beschleunigungsbegrenzern, vor Schleppfehlerbegrenzung | | AC:3895-3908 | beide |
| Untergrenzen: Hand 0 cm, Arm 1 cm, Hand↔Greifobjekt keine | | AC:200-206, 1623-1645 | beide |
| Projektion (G7.9), 2 Durchläufe, sonst halten | | AC:1663-1710 | |
| Verlangsamung nur reaktiv: < 5 cm über Untergrenze, Faktor ≥ 25 % | | AC:1712-1727, 1740-1744 | |
| Selbstkollision: konvexe Hüllen (coal), Paare Ellbogen/Handgelenk/Handbasis/Werkzeug gegen Körper + Arm gegen Arm, keine Finger, Marge 3 cm; hart → halten; Band: reaktiv nur wenn vorher schon im Band, geplant erlaubt | | IK:53, 89, 232-300, 327-345; AC:1603-1607, 1750-1758 | beide (real explizit `self_collision_gate: true`) |
| Geplante Bewegung: Untergrenze = min(Grenze, Endwert − 3 mm) | | AC:1634-1644, 3115-3124 | |
| Bahnuhr läuft nur bei Schleppabstand < 0,05 rad; nach 3 s Stillstand Abbruch | | AC:3735-3795 | |

Hintergrund (nicht im Text, nur für die Evaluation): Planer-Studie 26.11. Die Zahl zum Kugelüberstand (bis ca. 2,4 cm) steht im
Kommentar AG:629-632, ist aber ein Messwert und deshalb nur als Vorverweis auf `sec:eval_manipulation` erwähnt.

## (b) Vorgeschlagene neue Belege

1. **Zucker2013.NEU1**, Seite 11 (Seitenmarker `=== PDF-Seite 11 | Seite 11 ===`)
   - zitat: "In the typical Euclidean case we would have M = I; instead, we choose M to be the matrix A defined in the previous subsection. Again, this means we prefer perturbations which add only small amounts of additional acceleration to the overall trajectory."
   - kernaussage: CHOMP misst die Schrittweite der Bahnänderung mit der Glattheitsmatrix A statt euklidisch und bevorzugt so Änderungen, die der Bahn nur wenig zusätzliche Beschleunigung hinzufügen.
   - Achtung: im Text-Extrakt läuft der Satz über einen Zeilenumbruch (Z. 734-736), wörtlich prüfen.
2. **Carpentier2019.NEU1**, Seite 3
   - zitat: "Aside the kinematic model, Pinocchio defines a geometric model, i.e. the volumes attached to the kinematic tree. This model can be used for displaying the robot and computing quantities associated to collisions."
   - kernaussage: Pinocchio hat neben dem kinematischen ein geometrisches Modell (an den kinematischen Baum gehängte Volumen), das u. a. für Kollisionsgrößen dient.
3. **Carpentier2019.NEU2**, Seite 3
   - zitat: "Collision and distance algorithms for the kinematic trees are implemented, based on FCL methods."
   - kernaussage: Pinocchio implementiert Kollisions- und Abstandsalgorithmen für kinematische Bäume auf Basis von FCL.

Verwendet ohne neue IDs: Schulman2014.03 (vorkonditionierter Gradientenabstieg bei CHOMP), Kuffner2000.01 (RRT-Connect).

## (c) Offene Markierungen

- `\pruefen{Realbetrieb ohne Weltmodell so gewollt? ...}` (7.4.2): im Realbetrieb gibt es keinen Sender für das Weltmodell, also keine Umgebungsprüfung.
- `\pruefen{Stand PR \#62 ...}` dreimal: tieferer Endwert (G7.6), Zielprüfung an exakter Geometrie + Startbahn 30 cm (7.4.3), aufliegende Hand am Ende geplanter Bewegungen (7.4.4). Auch in den Kommentaren von `Bilder/tikz/planer-rueckfallkette.tex`.
- `\qf{Kollisionsbibliothek coal ...}` (7.4.4): Pinocchio 2019 belegt FCL, der Code nutzt coal (bzw. hppfcl als Rückfall). Vorschlag: GitHub-Eintrag coal mit Commit-Hash und README-PDF.
- Zitat-IDs `Zucker2013.NEU1`, `Carpentier2019.NEU1`, `Carpentier2019.NEU2` brauchen echte Nummern, bevor der Text nach `Kapitel/` geht (sonst Fehler in `check.py`).

## (d) Abweichungen vom Plan

- **Umfang:** etwa 4,1 Seiten statt 3,3 (im Testsatz gemessen). Haupttreiber ist die vorhandene B7.8 (`kugelmodell-haende-3d.tex`, zwei Bilder mit 14 cm Breite, ca. 0,75 S.). Der Fließtext ist schon auf etwa 800 Wörter gekürzt. Kürzungsvorschlag: in B7.8 nur Teilbild a) zeigen (spart ca. 0,3 S.) oder den Absatz zur Anfahrrichtung/Gewichten in 7.4.3 streichen.
- **T7.4 (`tab:kugelmodell`) weggelassen**, kein Platz. Die Radien der Kugelsätze stehen im Text. Die Kugelzahlen in `Daten/kugelmodell/kugeln.json` (68 Handkugeln) stammen von fdb9cba und müssten für die Tabelle neu erzeugt werden.
- **Selbstkollision, Randband:** Laut Plan ist dort „nur Herausfahren erlaubt“. Im Code hält das reaktive Nachführen nur an, wenn ein Schritt das Band **neu betritt**. Ist die Stellung schon im Band, ist auch eine Bewegung weiter hinein erlaubt, bis eine echte Durchdringung vorliegt (AC:1755-1758). Der Text folgt dem Code.
- **Weltmodell im Realbetrieb:** Im Plan nicht erwähnt. Laut Code gibt es real keine Umgebungsprüfung, deshalb steht das im Text als Sim/Real-Unterschied und hat ein `\pruefen` bekommen.
- **Stufe 3 der Rückfallkette:** Auch der stichprobenbasierte Planer kann ein Ergebnis mit verringertem Abstand liefern (`rrt_optimized_reduced`, notfalls die ungeglättete Bahn). Der Plan ordnet „verringerten Abstand“ nur der letzten Stufe zu.
- **Clusterverfahren ohne Namen** (Lloyd1982 nicht freigegeben). Die Kollisionsbibliothek ist über Carpentier2019 mit FCL belegt, coal als `\qf`.
- G7.7 ist vereinfacht: Die Skalierung mit der Stützpunktzahl ((T−1), (T−1)³) steckt in H und λ, die Gewichtswerte stehen nur hier im Faktenblatt.
- Label-Annahmen: `sec:hand_profile` (7.5.2 nach Festlegung 26.11., im Gerüst noch nicht vorhanden), `sec:posen_ablaeufe`, `sec:armuebergabe` (Kap. 6), `sec:entwickler_api`, `sec:regelkette`, `sec:eval_manipulation`, `sec:eval_sicherheit`.
- Gerüst-Titel „Kollisionsmodell und Laufzeitüberwachung“ → „Kollisionsmodell“ (Laufzeitüberwachung ist eigener Unterabschnitt, wie in den Festlegungen).

## (e) Abkürzungen

Keine `\ac{}` benutzt (`main.tex` hat nur KI, DSGVO, FAPS). FCL und CHOMP stehen als Eigennamen wie in Kap. 4. „RRT-Connect“ ist ebenfalls ein Eigenname aus Kap. 4.

## (f) Umfang

7.4.2 ca. 1,3 S. (mit B7.8 0,75), 7.4.3 ca. 2,0 S. (mit B7.9 0,4 und B7.10 0,35, zwei Gleichungen), 7.4.4 ca. 0,8 S. (eine Gleichung). Zusammen ca. 4,1 S.

## Dateien

- `review/kap7-entwurf/E.tex`
- `Bilder/tikz/planer-trichter.tex` (B7.9, `fig:trichter`), `Bilder/tikz/planer-rueckfallkette.tex` (B7.10, `fig:rueckfallkette`)
- `Daten/planer-trichter.py` → `Daten/planer-trichter.csv` (Rechnung aus den Voreinstellungen von AP @e452513, kein Messwert)
- Kompiliert mit der echten Präambel: keine Fehler, keine Overfull-Boxen, PNG-Sichtprüfung gemacht. `check.py`: 0 Fehler, 0 Warnungen (E.tex liegt noch nicht in `Kapitel/`).
