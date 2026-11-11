# Kapitelplan Kap. 3 – Simulation und Software-Infrastruktur

Stand 11.11.2026 (Claude, Kapitel-Workflow Schritt 1–4 in einem Lauf, Auftrag Nils vom 11.11.).
Branch `claude/project-thread-hdphmm`. Sammelfreigabe für neue Kap.-3-Quellen von Nils am 11.11. erteilt
(Claude verschiebt geprüfte Quellen mit PDF nach „Bachelorarbeit“, Nils sortiert danach aus).

**Leitgedanke:** Kap. 3 liefert die Grundlagen und den Stand der Technik zu den vier Bausteinen, auf denen die
Umgebung steht: Simulation als Werkzeug, der Physiksimulator, die Kommunikations- und Bereitstellungsschicht und
die Sicherheit. Prüfregel der Betreuerin: Jeder Abschnitt braucht einen Rückverweis aus Kap. 5–8, sonst kürzen.
Darstellung wertungsfrei, die Wertung folgt in 5.1. Zielumfang 9–10 Seiten (Gerüst: ca. 8).

**Abgrenzung:** G1-Hardware, Unitree SDK2 und Onboard-Regler stehen in Kap. 2. RL-Trainingsframeworks und
übernommene Policies stehen in 4.1, Kollisionsmodelle der Bahnplanung in 4.2.2, fertige G1-Software-Stacks und
Simulationsumgebungen anderer Gruppen in 4.4. Kap. 3 erklärt die Werkzeuge, nicht deren Anwendungen.

## Gliederungsvorschlag

„Kern“ = sollte hinein; „Kann“ = möglich, bei Platzmangel zuerst streichen.

| Abschnitt | Umfang | Stufe | Rückverweis aus | Änderung ggü. Gerüst vom 30.10. |
|---|---|---|---|---|
| Kapiteleinleitung | 3–4 Sätze | Kern | – | – |
| **3.1 Simulation in der Robotik** | ~2,5 S. | | | |
| 3.1.1 Einsatzzwecke der Simulation | | Kern | 1.1, 5.1, 6.4.1 (Leitgedanke „Simulation zuerst“) | um digitalen Zwilling, virtuelle Inbetriebnahme und X-in-the-Loop ergänzt (Bezug zur Produktionstechnik) |
| 3.1.2 Sim-to-Real-Lücke | | Kern | 6.2.3, 8.2, 8.5.3 | Ursachen und Gegenmaßnahmen getrennt; Hinweis, dass die Arbeit keinen Policy-Transfer macht |
| 3.1.3 Bewertung der Abbildungsgüte | | Kern (neu) | 5.3, 8.2 | **neu:** Kennzahlen für den Vergleich Simulation/Realität, Sim-to-Sim, Echtzeitfaktor – Grundlage für F2 |
| **3.2 Physiksimulatoren** | ~3 S. | | | |
| 3.2.1 Aufbau einer Physiksimulation | | Kann (neu) | 7.2 | **neu:** Teilmodelle (Mehrkörperdynamik, Kontakt, Aktor, Sensor, Integration); sonst als Einstieg von 3.2.2 |
| 3.2.2 MuJoCo | | Kern | 7.2.1–7.2.3, 8.2.1 | um Modellformat (MJCF), Aktor- und Sensormodelle ergänzt |
| 3.2.3 Vergleich mit weiteren Simulatoren | | Kern | 6.1, 8.5.2 | Merkmalstabelle; GPU-parallele Simulatoren nur kurz (kein eigenes Training) |
| **3.3 Middleware und Bereitstellung** | ~2,5 S. | | | Gerüst hatte keine Unterabschnitte |
| 3.3.1 Robot Operating System 2 | | Kern | 6.2.1, 7.6, 7.7 | neu als Unterabschnitt |
| 3.3.2 Data Distribution Service | | Kern | 2.3.1, 6.2.2, 7.2.1 | neu als Unterabschnitt; Domains als Grundlage der Sim/Real-Umschaltung |
| 3.3.3 Containerisierung | | Kern | 6.5.2, 7.1, 8.3.2 | neu als Unterabschnitt |
| (3.3.4 Test und Modularität von Robotiksoftware) | | Kann | 5.3.3, 6.5, 8.4 | **neu, optional:** simulationsbasiertes Testen, komponentenbasierte Architektur; alternativ je ein Absatz in 3.3.1/3.3.3 |
| **3.4 Sicherheit beim Betrieb von Robotern** | ~2 S. | | | Gerüst hatte keine Unterabschnitte |
| 3.4.1 Rechtsrahmen und Normen | | Kern | 6.3, 8.3.1 | neu als Unterabschnitt; Normentabelle |
| 3.4.2 Schutzfunktionen | | Kern | 6.3.2 | Not-Halt, Stoppkategorien, Zustimmeinrichtung, Betriebsarten, reduzierte Geschwindigkeit |
| 3.4.3 Besonderheiten zweibeiniger Roboter | | Kern | 6.3.1, 6.3.3 | Sturz statt sicherem Stillstand; Herstellerhinweise zum G1 |

### Mögliche Darstellungen (Vorschläge, noch nicht gebaut außer Tabellen im Entwurf)
- T1 Tabelle Simulatorvergleich (3.2.3): Simulator · Physik-Engine/Kontaktmodell · Parallelisierung · Lizenz · Bezug zum G1.
- T2 Tabelle Normen und Vorschriften (3.4.1): Regelwerk · Gegenstand · Geltung für Humanoide.
- T3 Tabelle Stoppkategorien bzw. Schutzfunktionen (3.4.2).
- B1 Ursachen der Sim-to-Real-Lücke und Gegenmaßnahmen als Blockbild (3.1.2).
- B2 Ablauf eines Simulationsschritts (3.2.1/3.2.2): Zustand → Kontakterkennung → Zwangskräfte → Integration.
- B3 DDS: Teilnehmer, Topics und getrennte Domains für Simulation und Realroboter (3.3.2) – Kernbild für die Umschaltung.
- B4 Container gegenüber virtueller Maschine (3.3.3).

## Leitfragen je Abschnitt

Status: **abgedeckt** (Belege vorhanden) / **teilweise** / **offen**. Stand vor der Recherche vom 11.11.

### 3.1 Simulation in der Robotik
- **L1** Wofür wird Simulation in der Robotik und Produktionsautomatisierung eingesetzt (Regler- und Softwaretest,
  Offline-Programmierung, virtuelle Inbetriebnahme, Schulung, Datenerzeugung/Lernen), und welchen Nutzen nennt die
  Literatur (Kosten, Sicherheit, Zeit)? – **teilweise** (Choi2021 noch ohne Belege; Tong2024, Ajaykumar2021, Sekkat2024)
- **L2** Was ist ein digitaler Zwilling (Abgrenzung zu digitalem Modell und digitalem Schatten), und was bedeuten
  Model-, Software- und Hardware-in-the-Loop? – **offen**
- **L4** Was ist die Sim-to-Real-Lücke, und welche Ursachen nennt die Literatur (Dynamikparameter, Aktordynamik,
  Kontakte, Latenz, Sensorrauschen)? – **teilweise** (Zhao2020, Tan2018, Tobin2017 noch ohne Belege; Tong2024, Yu2026)
- **L5** Welche Ansätze verringern die Lücke (Systemidentifikation, Domain Randomization, Aktormodelle,
  Real-to-Sim), und was setzen sie voraus? – **teilweise** (wie L4; He2025)
- **L6** Wie wird die Abbildungsgüte einer Robotersimulation bewertet (Kennzahlen im Vergleich Simulation/realer
  Roboter, Sim-to-Sim als Zwischenstufe, Echtzeitfaktor)? – **teilweise** (Gu2024, Durrani2026, Erez2015)

### 3.2 Physiksimulatoren
- **L3** Aus welchen Teilmodellen besteht eine Robotersimulation (Mehrkörperdynamik, Kontakt und Reibung, Aktoren,
  Sensoren, Zeitintegration)? – **teilweise** (Todorov2012, Erez2015 noch ohne Belege)
- **L7** Wie modelliert MuJoCo Mehrkörperdynamik und Kontakte (generalisierte Koordinaten, weiche, konvex
  formulierte Kontakte), und was folgt daraus? – **teilweise** (Todorov2012; Todorov2014 ohne PDF)
- **L8** Welche Einstellungen bestimmen in MuJoCo Genauigkeit und Rechenzeit (Zeitschritt, Integrator, Löser,
  Kontaktparameter)? – **offen** (Todorov2012, Erez2015; MuJoCo-Dokumentation)
- **L9** Wie werden Roboter, Aktoren und Sensoren beschrieben (MJCF, URDF), und welche Modelle und Schnittstellen
  sind verfügbar (Python-Bindings, Modellsammlungen)? – **teilweise** (Tunyasuvunakool2020 ohne Belege; UnitreeMujoco)
- **L10** Welche weiteren Simulatoren werden für Humanoide und Laufroboter genutzt (Gazebo, Bullet/PyBullet,
  Isaac Gym/Sim/Lab, Webots, Drake, RaiSim), und worin unterscheiden sie sich? – **teilweise** (Erez2015, Collins2021
  ohne PDF, Mittal2023, Zakka2025, Zakka2026, Saeedvand2019, Sekkat2024, Yu2026)
- **L11** Welche Vergleichsstudien bewerten Genauigkeit, Stabilität und Geschwindigkeit der Simulatoren? –
  **teilweise** (Erez2015; Gu2024 für Einzelfall)

### 3.3 Middleware und Bereitstellung
- **L12** Was leistet eine Robotik-Middleware, und wie ist ROS 2 aufgebaut (Knoten, Topics, Services, Actions,
  Quality of Service)? – **teilweise** (Macenski2022 noch ohne Belege)
- **L13** Wie funktioniert DDS (datenzentriertes Publish/Subscribe, Discovery, Domains, QoS), und wie nutzt ROS 2
  es? – **offen** (Macenski2022 für den ROS-2-Bezug)
- **L14** Welche Latenzen und Echtzeiteigenschaften haben ROS 2 und DDS? – **offen**
- **L15** Was ist Containerisierung (Image, Container, Abgrenzung zur virtuellen Maschine), welchen Overhead hat
  sie, und warum wird sie für Reproduzierbarkeit und in der Robotik eingesetzt? – **offen**
- **L16** (Kann) Wie wird Robotiksoftware getestet (simulationsbasiertes Testen, kontinuierliche Integration)? – **offen**
- **L17** (Kann) Was sagt die Literatur zu Modularität und Erweiterbarkeit von Robotiksoftware? – **offen**

### 3.4 Sicherheit beim Betrieb von Robotern
- **L18** Welche Rechtsvorschriften und Normen regeln den sicheren Betrieb von Robotern (Maschinenrichtlinie und
  -verordnung, ISO 12100, ISO 10218, ISO/TS 15066, ISO 13482), für welche Roboter gelten sie, und gibt es Normen
  für Humanoide? – **offen**
- **L19** Welche Schutzfunktionen definieren sie (Not-Halt, Stoppkategorien, Zustimmeinrichtung, Betriebsarten,
  reduzierte Geschwindigkeit, Leistungs- und Kraftbegrenzung)? – **offen**
- **L20** Welche Besonderheiten haben zweibeinige Roboter (Sturz beim Abschalten, Sturzerkennung, Fallstrategien)? –
  **teilweise** (Westervelt2018, Tong2024)
- **L21** (Kann) Wie setzen Forschungssysteme Sicherheit softwareseitig um (Grenzwertüberwachung, Watchdog,
  Totmannschalter)? – **offen**
- **L22** Welche Sicherheitshinweise gibt der Hersteller für den G1? – **offen** (Handbuch als PDF nötig)

## Befunde aus dem Code (Repo G1, Stand bae3420, Sichtung 11.11.2026)

Bestimmt, was Kap. 3 erklären muss (Rückverweis-Regel) und was nicht.

**Wird benutzt, braucht also Grundlagen:**
- MuJoCo über das Python-Binding, Zeitschritt 1 ms (`unitree_mujoco/simulate_python/config.py:61-66`, begründet mit
  der Stabilität der PD-Regelung), Integrator, Löser und Kontaktparameter des G1 auf den Voreinstellungen.
- Drehmoment-Aktuatoren (`motor`) mit PD-Regler außerhalb des Simulators (`unitree_sdk2py_bridge.py:305-307`),
  Positions-Aktuatoren für die Finger; Gelenkparameter Dämpfung, Rotorträgheit (armature), Reibung.
- Kollisionsgeometrie mit Kollisionsgruppen (contype/conaffinity), konvexe Zerlegung großer Netze, Weld-Zwangsbedingung
  zum Halten der Basis; Sensoren IMU, Gelenkgrößen, Berührung.
- Echtzeitkopplung: freilaufend mit Echtzeitfaktor oder Lockstep (20 Physikschritte je 50-Hz-Regelschritt).
- ROS 2 Humble mit `rmw_cyclonedds_cpp`, nur Topics (keine Services/Actions), QoS „transient local“ für Zustände.
- DDS direkt über das Unitree SDK: Domain 1 + Loopback in der Simulation, Domain 0 + Netzwerkkarte real
  (`g1pilot/utils/common.py:21-55`), Anfrage/Antwort (RPC) über DDS für den Onboard-Regler.
- Docker: drei Images, eine Compose-Datei mit Profilen `sim`/`real`, Host-Netzwerk, Startmenü.
- Sicherheit: Stufen Stopp/Not-Halt/Voll-Notaus, Dämpfungsmodus, Totmann am Gamepad, Zeitüberwachungen,
  Grenzen für Geschwindigkeit (TCP 0,25 m/s mit Verweis auf ISO 10218-1 im Kommentar), Beschleunigung, Schleppfehler,
  Verstärkungen, Kollisionsprüfung, Bodenkontaktprüfung.
- Tests: 589 Testfunktionen mit Attrappe des Roboters („Fake-G1“), keine CI.

**Kommt im Code nicht vor, in Kap. 3 daher nur knapp oder gar nicht:**
- Domain Randomization, Systemidentifikation, Rausch- und Latenzmodelle → in 3.1.2 als Stand der Technik nennen,
  aber kurz; die Arbeit überträgt keine Policy.
- Abstimmung von Integrator, Löser, Reibkegel, Kontaktparametern → in 3.2.2 nur benennen, nicht vertiefen.
- RL-Training → nur als Herkunft der Policies (steht in 4.1).
- ROS-2-Services/-Actions, Nav2, MoveIt, ros2_control, Fast DDS → höchstens ein Halbsatz.
- Lidar-/Kamerasimulation → weglassen.
- Zustimmeinrichtung und Not-Halt-Kette als Hardware, ISO 13850/13482/60204 → in 3.4 als Normenlage darstellen;
  die Lücke zur eigenen Umsetzung gehört in 6.3 und 8.5.3.
- Messskripte Simulation gegen Realroboter liegen nicht im Repo → für 3.1.3/5.3/8.2 klären, welche Kennzahlen Nils
  tatsächlich messen kann.
