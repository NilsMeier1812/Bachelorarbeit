# Recherche Stand der Technik: Bedienung, Frameworks und Sim-to-Real für den Unitree G1

Stand: 05.11.2026 · Betrifft Kap. 4.3 „Bedienung und Teleoperation“, 4.4 „Verwandte Arbeiten“, 3.2/3.3 und 5.1 „Handlungsbedarf“

> **Status dieser Datei:** Recherche-Notiz nach CLAUDE.md, Kapitel-Workflow Schritt 1–2.
> Die Beschreibungen unten stammen aus Webseiten, READMEs und Abstracts und sind **keine Belege**.
> Für den Text zählen nur Belege aus den PDFs in Zotero (Schritt 3). Alle Paper-Vorschläge liegen in
> Zotero unter `_Vorschläge` (Tag `SdT-Recherche 2026-11-05`, ohne Citation Key).

---

## 1. Kurzfassung

- **Viele G1-Projekte, kaum eines für Einsteiger.** Rund um den G1 ist seit 2024 ein großes
  Open-Source-Ökosystem entstanden. Fast alles zielt auf Forschende: RL-Training (mjlab, Isaac Lab),
  Ganzkörper-Teleoperation mit VR-Brillen oder Motion-Capture-Anzügen und das Sammeln von Daten für
  lernende Policies.
- **„Gleicher Code in Sim und Real“ ist verbreitet, aber nur für eine Funktion.** Unitree, NVIDIA,
  LeRobot und mehrere Repos schalten zwischen MuJoCo und echtem Roboter über ein Flag oder ein
  Netzwerk-Interface um. Das gilt jeweils für *eine* Funktion (eine Policy, eine Teleoperation), nicht
  für einen kompletten Bedien-Stack.
- **Einsteigerfreundliche grafische Werkzeuge gibt es nur für kleine Humanoide.** Das Beispiel ist
  Choregraphe für NAO/Pepper. Für den G1 und vergleichbare Humanoide in Menschengröße wurde kein
  Werkzeug gefunden, das GUI, Gamepad, Handy, Not-Halt, Simulation und Realbetrieb für Laien vereint.
  Ebenso fehlt eine Nutzerstudie zur Bedienbarkeit eines G1-Stacks.
- **Mögliche Forschungslücke für Nils:** eine aufgabenunabhängige, containerisierte Umgebung mit
  identischem Code in MuJoCo und am echten G1, mehreren niederschwelligen Bedienwegen, Not-Halt auf allen
  Kanälen und einer offenen Schnittstelle (HTTP/ROS 2) zum Andocken weiterer Projekte. Das deckt sich mit
  F1–F4 und A1–A7.

---

## 2. Leitfragen für den Stand der Technik (Schritt 1)

| # | Frage | Abdeckung durch vorhandene Belege |
|---|---|---|
| Q1 | Welche Wege gibt es, humanoide Roboter zu bedienen (Teleoperation, Gamepad, VR, grafische Programmierung), und für welche Nutzergruppe sind sie gedacht? | teilweise (Saeedvand2019, Tong2024) |
| Q2 | Welche Ansätze gibt es, Nicht-Fachleuten die Roboterprogrammierung zu ermöglichen, und wie wird ihr Erfolg gemessen? | offen |
| Q3 | Welche Software-Frameworks und Stacks gibt es speziell für den G1 oder vergleichbare Humanoide, und was können sie? | offen (nur Yu2026) |
| Q4 | Wie lösen bestehende Arbeiten den Übergang Simulation → Realroboter (gleiche Schnittstelle, Sim2Sim, Policy-Transfer)? | teilweise (Tobin2017, Zhao2020, Tan2018, Radosavovic2024) |
| Q5 | Welche Lern- und Simulationsframeworks werden für Humanoiden-Laufregler genutzt (MuJoCo, Isaac Lab, mjlab)? | teilweise (Todorov2012, Collins2021, Erez2015) |
| Q6 | Welche Rolle spielen Middleware (ROS 2) und Container für reproduzierbare Robotersoftware? | offen |
| Q7 | Wo liegen die Lücken: Was fehlt bestehenden Lösungen für den Einstieg von Laien bzw. Unternehmen? | offen (Schlussfolgerung aus Q1–Q6) |

---

## 3. Übersicht nach Kategorien

Legende Spalte „Sim/Real“: **gleich** = derselbe Code/Befehl mit Umschalter; **getrennt** = eigene
Einstiegspunkte; **nur Sim** / **nur Real**. „Zielgruppe“ nach Selbstbeschreibung der Projekte.

### 3.1 Offizielle Hersteller-Software von Unitree

| Projekt | Was es ist | Sim/Real | Bedienung | Zielgruppe |
|---|---|---|---|---|
| [unitree_sdk2 / unitree_sdk2_python](https://github.com/unitreerobotics) | Low-Level-SDK über DDS, Grundlage aller Projekte (auch von G1Pilot) | – | Code | Entwickler |
| [unitree_mujoco](https://github.com/unitreerobotics) | MuJoCo-Sim mit derselben DDS-Schnittstelle wie der Roboter | gleich (Netzwerk-Interface) | Gamepad | Entwickler |
| [unitree_rl_mjlab](https://github.com/unitreerobotics/unitree_rl_mjlab) | RL-Training auf mjlab, Deployment per C++ `g1_ctrl` | gleich (`--network=lo` vs. Ethernet) | Gamepad Pflicht | RL-Forschung |
| [xr_teleoperate](https://github.com/unitreerobotics/xr_teleoperate) | Teleoperation mit Vision Pro, PICO, Quest; Datensammlung für Imitation Learning | gleich (`--sim`), Sim aber **Isaac Lab** | XR-Brille, Tastatur | Forschung (Datensammlung) |
| Unitree-App + Handsender | Onboard-Laufregler, Bewegungsmodi | nur Real | App, Handsender | Endkunde, begrenzt |

**Abgrenzung:** Unitree liefert Bausteine pro Funktion. Es gibt keine gemeinsame Oberfläche, die
Arme, Hände, Laufen, Not-Halt und Simulation verbindet. Ein Deployment-Bericht von zwei G1 (Comenius-Univ.
Bratislava, 2026, nicht begutachtet) nennt den G1 ausdrücklich „not a turnkey humanoid worker“. Das ist
ein Suchhinweis, keine zitierfähige Quelle.

### 3.2 Community- und Forschungs-Stacks für den G1

| Projekt | Was es ist | Sim/Real | Bedienung | Zielgruppe |
|---|---|---|---|---|
| [hucebot/g1pilot](https://github.com/hucebot/g1pilot) (Inria) | ROS-2-Stack: Arm-IK, kartesische Steuerung, Joystick, Stream-Deck-UI, RViz-Marker; Laufen über Unitree-Regler | Sim nicht dokumentiert | Joystick, Stream Deck, RViz | Labor/Forschung |
| [LeRobot – Unitree G1](https://huggingface.co/docs/lerobot/unitree_g1) (Hugging Face) | Teleoperation und Datensammlung für lernende Policies | gleich (`is_simulation=true/false`) | Gamepad, Homunculus-Exoskelett | ML-Community |
| [GR00T-WholeBodyControl / SONIC](https://nvlabs.github.io/GR00T-WholeBodyControl/) (NVIDIA) | Ganzkörper-Regler als Foundation Model, Deployment-Stack | gleich (C++-Stack, MuJoCo-Test vor Hardware) | Tastatur, Gamepad, PICO-VR, ZMQ | Forschung, „Get running in minutes“ |
| [OpenWBT](https://github.com/GalaxyGeneralRobotics/OpenWBT) (Galbot/Tsinghua) | Ganzkörper-Teleoperation G1/H1 | getrennt (eigene Skripte, gemeinsame Config) | Vision Pro + 2 Joysticks | Forschung |
| [RoboMimicDeploy_G1](https://github.com/shanpenghui/RoboMimicDeploy_G1) | Deployment von Policies (Tanz, Kung-Fu, Laufen) | getrennt (`deploy_mujoco` / `deploy_real`) | Xbox-Gamepad mit Modi | Bastler; die meisten Bewegungen „nicht für den echten Roboter empfohlen“ |
| [G1-Playground](https://github.com/AlexandreBrown/G1-Playground) | „Lightweight getting started“ für Policies, MuJoCo und Isaac Lab | weitgehend gleich (DDS-Kanal) | Handsender, Not-Halt | **Einsteiger (RL)** |
| [unitree-g1-mujoco-sim](https://github.com/Johannes4044/unitree-g1-mujoco-sim) | MuJoCo-Szenen, Sensoren, Beispiel-Workspace „Start here“ | **nur Sim** | keine („no dashboard, no teleop UI“) | **Einsteiger (Sim)** |
| [MATLAB/Simulink-Sim2Real-Framework](https://doi.org/10.5281/zenodo.23898947) (Univ. de los Andes, Zenodo, Nov. 2026) | Simulink-Workflow: Reglerentwurf, MuJoCo, Visualisierung, Real-Deployment über ROS 2 | gleich (laut Beschreibung) | nicht beschrieben | Regelungstechnik |

**Abgrenzung:** Die beiden einzigen ausdrücklich einsteigerorientierten Repos sind entweder nur Sim
(Johannes4044) oder nur für RL-Policies gedacht (G1-Playground). Keines hat eine grafische Bedienoberfläche
oder einen Handy- bzw. GUI-Not-Halt. g1pilot ist Nils' Ausgangsbasis: Er übernimmt Arm-IK und Navigation
und ergänzt Simulation, Laufen in Sim, Hände, GUI, Handy, Not-Halt, Arm-API und Docker-Startmenü. Das
gehört nach Richtlinien §13 als „Ausgangslage“ klar abgegrenzt in 4.4 und 7.

### 3.3 Teleoperation humanoider Roboter (wissenschaftliche Literatur)

| Quelle (Zotero `_Vorschläge`) | Typ | Kern laut Abstract/Projektseite | Nutzen für Nils |
|---|---|---|---|
| Darvish et al. 2023, *Teleoperation of Humanoid Robots: A Survey*, IEEE T-RO, [10.1109/TRO.2023.3236952](https://doi.org/10.1109/TRO.2023.3236952) | Survey, Journal | Übersichtsarbeit zur Teleoperation humanoider Roboter | **Hauptquelle für 4.3** (Q1) |
| He et al. 2024, *OmniH2O*, CoRL 2024 / PMLR 270, [arXiv:2406.08858](https://arxiv.org/abs/2406.08858) | Konferenz | Ganzkörper-Teleoperation Mensch → Humanoid (laut Titel), RL-basiert | Beispiel Expertenschnittstelle (Q1) |
| Fu et al. 2024, *HumanPlus*, [arXiv:2406.10454](https://arxiv.org/abs/2406.10454) (CoRL 2024 laut Projektseite) | Konferenz | „Shadowing“ und Imitation vom Menschen (laut Titel) | Q1 |
| Cheng et al. 2024, *Open-TeleVision*, [arXiv:2407.01512](https://arxiv.org/abs/2407.01512) (CoRL 2024 laut Projektseite) | Konferenz | Immersive Teleoperation mit aktivem visuellem Feedback (laut Titel) | Q1; Verwandtschaft zu Unitrees `xr_teleoperate` prüfen |
| Ze et al. 2025, *TWIST*, [arXiv:2505.02833](https://arxiv.org/abs/2505.02833) | Preprint | Teleoperiertes Ganzkörper-Imitationssystem (laut Titel); Roboter im PDF prüfen | Q1 |
| Durrani & Khan 2026, *IMU-Based Motion Capture … Sim2Sim and Sim2Real*, [arXiv:2605.12347](https://arxiv.org/abs/2605.12347) | Preprint | IMU-Anzug → G1; erst in MuJoCo validiert, dann „without modification“ real | Sehr nah an A2 (gleicher Code), aber Expertenschnittstelle (Q4) |
| Ali Pour et al. 2026, *Toward Humanoid Robots in Construction*, [arXiv:2610.00718](https://arxiv.org/abs/2610.00718) | Workshop (IROS 2026) | Machbarkeitsstudie G1 im Bau: XR-Oberkörper + Pedal-Laufsteuerung, ein Bediener | Anwendung außerhalb Labor, Bedienergonomie (Q1/Q7) |
| Zhao et al. 2025, *XRoboToolkit*, [arXiv:2508.00097](https://arxiv.org/abs/2508.00097) | Konferenz (SII 2026, angenommen) | Plattformübergreifendes XR-Teleop-Framework | Q1 (Framework-Gedanke) |

**Abgrenzung:** Die Teleoperations-Forschung optimiert Ausdrucksstärke und Datensammlung. Dafür braucht
es teure Spezialhardware (Vision Pro, MoCap-Anzug, Exoskelett) und Fachpersonal. Nils' Bedienwege (GUI,
Gamepad, Handy) liegen am anderen Ende: geringe Einstiegshürde, gröbere Kommandos und Sicherheit vor
Ausdrucksstärke. Das ist ein bewusster Trade-off und gut als Alternative-→-Entscheidung darstellbar.

### 3.4 Bedienung durch Laien / End-User-Programmierung

| Quelle | Typ | Kern | Nutzen |
|---|---|---|---|
| Ajaykumar, Steele & Huang 2021, *A Survey on End-User Robot Programming*, ACM Computing Surveys, [10.1145/3466819](https://doi.org/10.1145/3466819) | Survey, Journal | Ansätze, mit denen Nicht-Programmierer Roboter programmieren; Bewertungsmethoden | **Hauptquelle für Laienbedienung** (Q2, A6, Bewertungsmethodik 5.3) |
| Pot et al. 2009, *Choregraphe: a graphical tool for humanoid robot programming*, IEEE RO-MAN, [10.1109/ROMAN.2009.5326209](https://doi.org/10.1109/ROMAN.2009.5326209) | Konferenz | Grafisches Programmierwerkzeug für NAO | Nächstes Vorbild „einfache Bedienung Humanoid“ (Q2) |
| Sekkat et al. 2024, *Pepper's open-source digital twin*, Heliyon, [10.1016/j.heliyon.2024.e34456](https://doi.org/10.1016/j.heliyon.2024.e34456) | Journal | Offener Digitaler Zwilling für Pepper (Sim + ROS) | Analogie Sim-Umgebung für einen Service-Humanoiden (Q3/Q4) |
| Chi et al. 2025, *Berkeley Humanoid Lite*, RSS 2025, [10.15607/rss.2025.xxi.062](https://doi.org/10.15607/rss.2025.xxi.062) | Konferenz | „Accessible“ Humanoid: Zugänglichkeit über günstige Hardware | Gegenbeispiel: Zugänglichkeit über Hardware statt Software (Q7) |

**Abgrenzung:** Für Laien gibt es etablierte Konzepte (Survey) und Werkzeuge für kleine soziale
Humanoide (NAO/Pepper). Übertragen auf Humanoide in Menschengröße mit Lauf-Policies und realem
Sturz- und Verletzungsrisiko wurde nichts gefunden.

### 3.5 Lern- und Simulationsframeworks für Lauf-Policies (Sim-to-Real)

| Quelle | Typ | Kern | Nutzen |
|---|---|---|---|
| Rudin et al. 2021, *Learning to Walk in Minutes…* (legged_gym), CoRL 2021, [arXiv:2109.11978](https://arxiv.org/abs/2109.11978) | Konferenz | Massiv paralleles RL-Training; Basis vieler Humanoiden-Repos | Q5 |
| Mittal et al. 2023, *Orbit* (heute Isaac Lab), IEEE RA-L, [10.1109/LRA.2023.3270034](https://doi.org/10.1109/LRA.2023.3270034) | Journal | Einheitliches Simulationsframework für Robot Learning | Q5, Vergleich Simulatoren (3.2.2) |
| Gu et al. 2024, *Humanoid-Gym*, [arXiv:2404.05695](https://arxiv.org/abs/2404.05695) | Workshop (ICRA 2024) | RL in Isaac Gym, **Sim2Sim-Prüfung in MuJoCo** vor dem Realtransfer | Q4/Q5: MuJoCo als Prüfstand |
| Zakka et al. 2025, *MuJoCo Playground*, RSS 2025, [10.15607/rss.2025.xxi.020](https://doi.org/10.15607/rss.2025.xxi.020) | Konferenz | GPU-RL auf MuJoCo/MJX inkl. Humanoiden, Sim-to-Real | Q5 |
| Zakka et al. 2026, *mjlab*, [arXiv:2601.22074](https://arxiv.org/abs/2601.22074) | Preprint | Isaac-Lab-API auf MuJoCo Warp; Basis von `unitree_rl_mjlab` | Q5, direkte Herkunft der Policy in G1Pilot |
| He et al. 2025, *ASAP*, RSS 2025, [10.15607/rss.2025.xxi.066](https://doi.org/10.15607/rss.2025.xxi.066) | Konferenz | Abgleich Sim- und Realphysik für agile Ganzkörperfähigkeiten (laut Titel); Roboter im PDF prüfen | Q4 |
| Luo et al. 2026, *SONIC*, Science Robotics, [10.1126/scirobotics.aed4592](https://doi.org/10.1126/scirobotics.aed4592) | Journal | Foundation-Model-Ganzkörperregler (NVIDIA GR00T-WBC), am G1 | Q3/Q4, aktueller Stand Ganzkörperregelung |

Schon in Zotero und hierzu passend: Radosavovic2024, Tobin2017, Zhao2020, Tan2018, Todorov2012, Collins2021.

### 3.6 Middleware und Infrastruktur

| Quelle | Typ | Nutzen |
|---|---|---|
| Macenski et al. 2022, *Robot Operating System 2*, Science Robotics, [10.1126/scirobotics.abm6074](https://doi.org/10.1126/scirobotics.abm6074) | Journal | Kap. 3.3 Middleware (ROS 2, DDS) (Q6) |

Für Docker in der Robotik wurde in dieser Runde kein begutachtetes Paper gesucht. Das wäre ein
Suchauftrag für die nächste Runde, falls 3.3 es braucht.

---

## 4. Einordnung von Nils' Projekt (G1Pilot) und Forschungslücke

Merkmalsvergleich (✓ vorhanden, ◐ teilweise, – nicht vorhanden/nicht dokumentiert). Grundlage: READMEs
und Projektseiten, Stand 05.11.2026. **Vor Verwendung im Text selbst prüfen; als Tabelle in 4.4 oder 5.1
denkbar, Quellen dann als Software-/Webquellen zitieren.**

| Merkmal | Unitree-Beispiele | g1pilot (Inria) | LeRobot G1 | GR00T-WBC | G1-Playground | **G1Pilot (Nils)** |
|---|---|---|---|---|---|---|
| Gleicher Code Sim ↔ Real | ✓ je Funktion | – | ✓ | ✓ | ◐ | ✓ ganzer Stack |
| Simulator | MuJoCo / Isaac Lab | – | MuJoCo | MuJoCo | MuJoCo, Isaac Lab | MuJoCo |
| Arme (IK) + Hände | getrennt | ✓ Arme | ✓ Teleop | Ganzkörper | – | ✓ Arme, Inspire-Hände |
| Laufen | ✓ | Unitree-Regler | ✓ | ✓ | ✓ Policy | ✓ Sim-Policy / Real-Onboard |
| Grafische Bedienoberfläche | – | ◐ Stream Deck/RViz | – | – | – | ✓ Demo-GUI + Startmenü |
| Niederschwellige Eingabe (Gamepad/Handy) | Gamepad | Joystick | Gamepad | Gamepad, Tastatur | Handsender | Gamepad + Handy |
| Not-Halt aus jeder Bedienung | – | – | – | – | ◐ | ✓ |
| Container/Ein-Befehl-Start | – | ✓ Docker | – | – | – | ✓ Docker + Startmenü |
| Andock-Schnittstelle für Fremdprojekte | SDK | ROS 2 | Python | ZMQ | – | ROS 2 + HTTP-Arm-API |
| Zielgruppe Laien/Unternehmen | – | – | – | – | ◐ RL-Einsteiger | ✓ |

**Formulierungsvorschlag für die Lücke (Handlungsbedarf 5.1, noch ohne Belege):**
Für den G1 existieren leistungsfähige Einzelwerkzeuge für Training, Teleoperation und Deployment. Sie
richten sich an Fachleute und decken jeweils eine Funktion ab. Es fehlt eine aufgabenunabhängige
Umgebung, in der Laien den Roboter ohne Programmierkenntnisse zuerst in der Simulation und anschließend
mit identischem Code am realen System bedienen können, mit durchgängigem Not-Halt und einer offenen
Schnittstelle für Folgeprojekte. Außerdem wurde keine Arbeit gefunden, die die Bedienbarkeit eines
G1-Software-Stacks durch Laien evaluiert.

**Ehrliche Grenzen (sollte die Arbeit selbst nennen):**
- Der Policy-Transfer Sim → Real wird in G1Pilot nicht gelöst; real läuft der Unitree-Regler. Die
  Sim-to-Real-Literatur (ASAP, SONIC, Humanoid-Gym) ist deshalb Kontext, nicht Konkurrenz.
- Ohne Nutzerstudie bleibt „einfache Bedienung“ eine Behauptung. Ajaykumar2021 liefert die Begriffe dafür,
  wie man sie bewerten könnte, etwa Aufgabenzeit, Fehler und Fragebogen. Das passt zu 5.3.

---

## 5. Vorschläge in Zotero `_Vorschläge` (21 Einträge, angelegt 05.11.2026)

Alle Einträge haben den Tag `SdT-Recherche 2026-11-05`. DOIs wurden über Crossref geprüft, arXiv-IDs über die
arXiv-API und das Zenodo-Datum über die Record-Seite. OA = PDF frei verfügbar.

| # | Titel (kurz) | DOI / ID | OA | Frage | Priorität |
|---|---|---|---|---|---|
| 1 | Teleoperation of Humanoid Robots: A Survey (Darvish 2023) | 10.1109/TRO.2023.3236952 | ja (arXiv 2301.04317) | Q1 | **hoch** |
| 2 | A Survey on End-User Robot Programming (Ajaykumar 2021) | 10.1145/3466819 | ja (arXiv 2105.01757) | Q2 | **hoch** |
| 3 | Choregraphe (Pot 2009) | 10.1109/ROMAN.2009.5326209 | vermutlich nein → FAU (IEEE Xplore) | Q2 | **hoch** |
| 4 | Pepper's open-source digital twin (Sekkat 2024) | 10.1016/j.heliyon.2024.e34456 | ja (Heliyon OA) | Q3/Q4 | mittel |
| 5 | Robot Operating System 2 (Macenski 2022) | 10.1126/scirobotics.abm6074 | ja (arXiv 2211.07752) | Q6 | **hoch** |
| 6 | Orbit / Isaac Lab (Mittal 2023) | 10.1109/LRA.2023.3270034 | ja (arXiv 2301.04195) | Q5 | mittel |
| 7 | ASAP (He 2025) | 10.15607/rss.2025.xxi.066 | ja (RSS) | Q4 | mittel |
| 8 | SONIC (Luo 2026) | 10.1126/scirobotics.aed4592 | ja (arXiv 2511.07820), Verlag über FAU | Q3/Q4 | mittel |
| 9 | Demonstrating MuJoCo Playground (Zakka 2025) | 10.15607/rss.2025.xxi.020 | ja (RSS) | Q5 | mittel |
| 10 | Berkeley Humanoid Lite (Chi 2025) | 10.15607/rss.2025.xxi.062 | ja (RSS) | Q7 | niedrig |
| 11 | Learning to Walk in Minutes / legged_gym (Rudin 2021) | arXiv:2109.11978 | ja | Q5 | mittel |
| 12 | OmniH2O (He 2024) | arXiv:2406.08858 | ja | Q1 | mittel |
| 13 | Open-TeleVision (Cheng 2024) | arXiv:2407.01512 | ja | Q1 | mittel |
| 14 | HumanPlus (Fu 2024) | arXiv:2406.10454 | ja | Q1 | niedrig |
| 15 | TWIST (Ze 2025) | arXiv:2505.02833 | ja | Q1 | niedrig |
| 16 | Humanoid-Gym (Gu 2024) | arXiv:2404.05695 | ja | Q4/Q5 | mittel |
| 17 | mjlab (Zakka 2026) | arXiv:2601.22074 | ja | Q5 | **hoch** (Herkunft der Policy) |
| 18 | Humanoid Robots in Construction (Ali Pour 2026) | arXiv:2610.00718 | ja | Q1/Q7 | **hoch** (G1, Praxis) |
| 19 | IMU-Based Whole-Body Teleoperation (Durrani 2026) | arXiv:2605.12347 | ja | Q4 | **hoch** (G1, Sim2Sim/Sim2Real) |
| 20 | XRoboToolkit (Zhao 2025) | arXiv:2508.00097 | ja | Q1 | niedrig |
| 21 | MATLAB/Simulink Sim2Real Framework G1 (Trochez 2026, Software) | 10.5281/zenodo.23898947 | ja | Q3 | mittel (direktester „Konkurrent“) |

**Hinweise zu Metadaten:** Bei 11–14 ist die Konferenz (CoRL) nur im Feld *Extra* vermerkt. Die Einträge
sind als Preprint angelegt. Falls du sie als Konferenzbeitrag zitieren willst, bitte den Typ auf zotero.org
ändern; das mache ich nicht ohne Rückfrage. Die arXiv-Kommentare nennen für 11 CoRL 2021, PMLR bestätigt
12 in Bd. 270, für 13 und 14 steht es nur auf der Projektseite.

**Nicht in Zotero angelegt** (nur Webquellen/Software, nach Richtlinien §8 für Softwarefakten
zulässig): unitree_rl_mjlab, xr_teleoperate, unitree_mujoco, hucebot/g1pilot, LeRobot-G1-Doku,
GR00T-WholeBodyControl, OpenWBT, RoboMimicDeploy_G1, G1-Playground, unitree-g1-mujoco-sim. Auf Wunsch
lege ich sie als Typ „Software“ an. Mindestens g1pilot (Ausgangsbasis) und unitree_rl_mjlab (Policy)
wirst du zitieren müssen.

## 6. Nächste Schritte

1. Nils prüft die Liste, lädt die PDFs (OA bzw. über FAU) auf zotero.org hoch und verschiebt die gewünschten
   Einträge in „Bachelorarbeit“.
2. Danach Phase 0/1: Citation Keys, `zot.py text`, Belege entlang Q1–Q7.
3. Offene Suchhinweise: Usability-Bewertung von Robotersoftware (z. B. System Usability Scale), Docker
   in der Robotik (Reproduzierbarkeit), Sicherheitsnormen für (mobile/humanoide) Roboter. Diese wurden noch nicht recherchiert.
