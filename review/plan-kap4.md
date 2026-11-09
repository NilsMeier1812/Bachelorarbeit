# Kapitelplan Kap. 4 – Fähigkeiten humanoider Roboter und verwandte Arbeiten

Stand 09.11.2026 (Claude, Kapitel-Workflow Schritt 1). Wartet auf Nils' Abstimmung der Gliederung.

**Leitgedanke:** Kap. 4 erklärt nur, was Konzept (Kap. 6), Umsetzung (Kap. 7) und Handlungsbedarf (Kap. 5.1)
später brauchen (Prüfregel der Betreuerin: jeder Abschnitt braucht einen Rückverweis). Darstellung wertungsfrei,
die Wertung folgt in 5.1. Umfang ca. 8 Seiten.

## Gliederungsvorschlag

| Abschnitt | Umfang | Rückverweis aus | Änderung ggü. Gerüst vom 30.10. |
|---|---|---|---|
| Kapiteleinleitung | 3–4 Sätze | – | – |
| **4.1 Fortbewegung** | ~1 S. | 6.2.3, 7.3.1 (Stand-PD, übernommene Policies) | 4.1.1/4.1.2 zu **einem** Abschnitt ohne Unterabschnitte zusammengelegt; RL-Trainingsframeworks (Rudin2021, Mittal2023, Zakka2026) aus 4.4 hierher |
| **4.2 Manipulation** | ~3 S. | 7.4 (IK-Prozess, Kugelmodell, Planer) | – |
| 4.2.1 Inverse Kinematik redundanter Arme | | 7.4.1 | – |
| 4.2.2 Kollisionsmodelle und Abstandsberechnung | | 7.4.2 | vor die Bahnplanung gezogen (der Planer nutzt die Abstände) |
| 4.2.3 Bahnplanung | | 7.4.3 | – |
| *(optional 4.2.4 Greifen mit Mehrfingerhänden)* | | 7.5 | **Frage an Nils** |
| **4.3 Bedienung und Teleoperation** | ~2 S. | 6.4, 7.6 | Entwurf vom 05.11. vorhanden |
| 4.3.1 Teleoperation humanoider Roboter | | | Unterteilung neu |
| 4.3.2 Bedienung durch Nutzer ohne Robotikerfahrung | | | Unterteilung neu |
| **4.4 Verwandte Arbeiten** | ~2 S. | 5.1, 6.1.1 | Fokus nur noch auf Umgebungen/Stacks Sim + Real; Merkmalstabelle |

## Leitfragen je Abschnitt (abgedeckt / teilweise / offen)

### 4.1 Fortbewegung (kurz)
1. Wie halten modellbasierte Regler einen Zweibeiner im Gleichgewicht (Schwerpunkt, Druckpunkt/ZMP), und wo liegen deren Grenzen? – **abgedeckt** (Westervelt2018, Saeedvand2019, Tong2024)
2. Wie entstehen lernbasierte Lauf-Regler (RL in der Simulation, Übertragung auf den Roboter)? – **teilweise** (Tong2024, Rudin2021; Radosavovic2024 freigegeben, aber noch ohne Belege → PDF prüfen)
3. Mit welchen Frameworks werden solche Policies für den G1 trainiert (Isaac Lab/Orbit, mjlab)? – **abgedeckt** (Mittal2023, Zakka2026)
3a. Welche fertigen Lauf-Policies für den G1 sind öffentlich verfügbar (Herkunft, Framework, Simulator, Eingänge, Format, Lizenz)? – **offen**; Wunsch Nils 09.11.: Übersichtstabelle in 4.1, Auswahlbegründung in 6.2.3. Liste der gefundenen/verworfenen Policies kommt von Nils. In `_Vorschläge`: Unitree RL Mjlab, GR00T-WBC, OpenWBT; WBC-AGILE fehlt.

### 4.2 Manipulation
4. Wie löst man die IK eines redundanten 7-DoF-Arms numerisch, wie geht man mit Singularitäten um (DLS, adaptive Dämpfung) und wie nutzt man die Redundanz (Nullraum)? – **abgedeckt** (Aristidou2009, Aristidou2018, Kucuk2006, DSouza2001)
5. Mit welchen Ersatzgeometrien (Kugeln, Kapseln, konvexe Hüllen, Meshes) beschreibt man Roboter und Umgebung für die Kollisionsprüfung, und wie berechnet man Abstände effizient? – **offen**
6. Welche Klassen von Bahnplanern gibt es (sampling-basiert wie RRT-Connect, optimierungsbasiert wie CHOMP/TrajOpt), und was sind ihre Stärken/Schwächen? – **offen**
7. Welche Frameworks bündeln das (MoveIt, OMPL)? – **offen**
8. Wie wird eine geometrische Bahn mit Geschwindigkeits-/Beschleunigungsgrenzen zeitlich parametriert? – **offen** (Yu2026 nur Polynom 5. Grades)
9. *(optional)* Wie werden Mehrfingerhände kraftgeregelt und taktil überwacht? – **offen**

### 4.3 Bedienung und Teleoperation
10. Welche Bedienarten (autonom, teilautonom, Teleoperation) gibt es, und wofür wird Teleoperation eingesetzt? – **abgedeckt**, 3 Sätze laut Verifikation 05.11. zu korrigieren
11. Welche Eingabegeräte und Rückmeldungen nutzen Teleoperationssysteme, und welche Grenzen haben sie (Kosten, Ort, Sicherheit)? – **abgedeckt** (Fu2024, Cheng2024, He2024, Durrani2026); Survey Darvish2023 würde den Überblick stützen (PDF fehlt)
12. Wie machen End-User-Programmierung und grafische Oberflächen Roboter für Nutzer ohne Robotikerfahrung bedienbar? – **abgedeckt** (Ajaykumar2021, Pot2009)
13. Gibt es Arbeiten zur Bedienung über Standard-Eingabegeräte (Gamepad, Smartphone)? – **offen**

### 4.4 Verwandte Arbeiten
14. Welche Arbeiten nutzen eine Simulation als Prüfstand vor dem Realroboter (Sim-to-Sim, gleicher Code)? – **abgedeckt** (Gu2024, Durrani2026)
15. Welche Simulationsumgebungen/Plattformen gibt es für G1 und vergleichbare Humanoide? – **teilweise** (Sekkat2024, Yu2026; Zakka2025, He2025, Chi2025 freigegeben, aber Bild-PDFs ohne Text)
16. Welche quelloffenen Software-Stacks gibt es für den G1 (g1pilot, unitree_mujoco, xr_teleoperate, LeRobot, GR00T-WBC, OpenWBT), und was decken sie ab? – **offen** (Einträge liegen in `_Vorschläge` als Software, ohne PDF)

## Offene Entscheidungen für Nils
- A: Gliederung wie oben (4.1 zusammenlegen, RL-Frameworks nach 4.1, Kollision vor Bahnplanung)?
- B: Greifen/Hände als 4.2.4 aufnehmen oder weglassen?
- C: Software-Repos als Quellen: Belege brauchen ein PDF in Zotero. Vorschlag: README/Doku-Seite des Repos als PDF speichern und an den Software-Eintrag hängen.
- D: OCR-Fassungen von Zakka2025/He2025/Chi2025 liegen im Projektordner – an die Zotero-Einträge hängen (darf Claude das per API)?
- E: Die 11 „teilweise“-Korrekturen aus `verifikation-kap4-2026-11-05.md` nach Vorschlag des Prüfers einarbeiten?

## Recherche (Schritt 2) – 09.11.2026, Fragen 5–8

12 Einträge in Zotero `_Vorschläge`, Tag `Kap4-Recherche 2026-11-09`, ohne Citation Key. Metadaten je per Crossref/doi.org
abgeglichen (Titel, Autoren, Jahr), Duplikatsuche in der Bibliothek ohne Treffer. Fragen 9 und 13 erst nach Nils' Entscheidung B.

| Vorschlag | DOI/ISBN | frei verfügbar | Frage | warum geeignet |
|---|---|---|---|---|
| Kuffner, LaValle 2000: RRT-Connect | 10.1109/ROBOT.2000.844730 | nein → FAU (IEEE) | 6 | Originalarbeit des sampling-basierten Planers, den der eigene Planer als Rückfallebene nutzt |
| Zucker et al. 2013: CHOMP (IJRR) | 10.1177/0278364913488805 | nein → FAU (SAGE) | 6 | Journalfassung des Optimierungsplaners, an dem sich der eigene Planer orientiert (Glattheit + Hindernisterm, vorkonditionierter Gradient) |
| Schulman et al. 2014: TrajOpt | 10.1177/0278364914528132 | nein → FAU (SAGE) | 5, 6 | zweiter optimierungsbasierter Ansatz, vergleicht mit CHOMP; konvexe Kollisionsprüfung |
| Kalakrishnan et al. 2011: STOMP | 10.1109/ICRA.2011.5980280 | nein → FAU (IEEE) | 6 | gradientenfreie Alternative zu CHOMP (optional, nur wenn Platz) |
| Sucan, Moll, Kavraki 2012: OMPL | 10.1109/MRA.2012.2205651 | nein → FAU (IEEE) | 7 | Standardbibliothek sampling-basierter Planer |
| Coleman et al. 2014: MoveIt! | 10.6092/JOSER_2014_05_01_P3 | ja (aisberg.unibg.it) | 7 | Framework, das Planer, Kollisionsprüfung und Zeitparametrierung bündelt; Gegenstück zum eigenen Planer |
| Pan, Chitta, Manocha 2012: FCL | 10.1109/ICRA.2012.6225337 | nein → FAU (IEEE) | 5 | Kollisions- und Abstandsbibliothek; coal (im Projekt genutzt) ist deren Weiterentwicklung – das muss aber eine Quelle belegen |
| Hubbard 1996: Polyeder durch Kugeln annähern | 10.1145/231731.231732 | nein → FAU (ACM) | 5 | Grundlage der Kugel-Approximation (eigenes Kugelmodell der Arme) |
| Kunz, Stilman 2012: Zeitoptimale Bahnparametrierung | 10.15607/RSS.2012.VIII.027 | ja (RSS-Proceedings) | 8 | Zeitparametrierung mit Beschleunigungsgrenzen, in MoveIt verbreitet |
| Pham, Pham 2018: TOPP-RA | 10.1109/TRO.2018.2819195 | Preprint auf arXiv, sonst FAU (IEEE) | 8 | aktueller Ansatz zur zeitoptimalen Parametrierung |
| LaValle 2006: Planning Algorithms (Buch) | ISBN 978-0-521-86205-9 | Autorenfassung frei online | 5, 6 | Lehrbuch: Konfigurationsraum, Kollisionsprüfung, sampling-basierte Planung |
| Carpentier et al. 2019: Pinocchio | 10.1109/SII.2019.8700380 | vermutlich HAL | 4 (Werkzeug) | Kinematikbibliothek, auf der die IK im Projekt aufbaut; eher für Kap. 7 |
