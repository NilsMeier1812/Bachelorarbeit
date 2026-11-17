# Belegprüfung Kapitel 5 (AP2)

Stand 17.11.2026. Geprüft wurde, ob das **wörtliche Zitat** die Leitfrage trägt (nicht, ob die Aussage „stimmt“). Grundlage: `evidence/<Key>.yaml` gegen `sources-text/<Key>.txt`.
Bewertung: **T** = trägt, **E** = trägt mit Einschränkung, **N** = trägt nicht (für diese Leitfrage). Die Spalte „Einschränkung“ nennt, was im Text stehen muss.
Neu angelegt in AP2: Sekkat2024.12, .13; Durrani2026.05; Ajaykumar2021.13, .14; HucebotG1Pilot.05.
Allgemein: Sekundäraussagen (Quelle zitiert eine andere Arbeit) und Preprints/graue Literatur im Text als solche kennzeichnen.

## 5.1 Handlungsbedarf

| Leitfrage | Beleg-ID | Bew. | Einschränkung, die im Text stehen muss |
|---|---|---|---|
| L1 Potenzial/Hemmnisse | Tong2024.08 | T | „können eingesetzt werden“, Potenzial, keine Aussage zur tatsächlichen Verbreitung. |
| | Tong2024.09 | E | Hohe Kosten „begrenzen die kommerzielle Verbreitung“ gilt allgemein für Humanoide laut Übersichtsarbeit, nicht für den G1. |
| | Tong2024.10 | E | Nur Beispielbereiche (Notfalleinsatz, Gesundheit); Leistung, Sicherheit und Kosten „müssen zum Bedarf passen“, kein Hemmnis im Sinn von Anwendern ohne Robotikerfahrung. |
| | Chi2025.01 | E | „most existing commercially available hardware“: Urteil der Autoren über kommerzielle Humanoid-Hardware (teuer, nicht quelloffen); keine Quantifizierung. |
| | Sekkat2024.02 | E | Nur Pepper; Sekundäraussage (Verweis [13]); nicht auf Humanoide allgemein oder den G1 übertragen. |
| | Sekkat2024.05 | E | Pepper nur als Beispiel („such as“); Sekundäraussage [13]. Simulation „kritisch“ ist Aussage der Autoren. |
| | (Hemmnisse aus Sicht von Unternehmen) | offen | Acatech2020/FAPS2024 ohne PDF → `\qf`. |
| L2 Gleiche Schnittstelle beim Hersteller | UnitreeMujoco.01 | T | Aussage der README („seamless transition“ ist Herstellerwerbung; nur als Angabe des Herstellers wiedergeben). |
| | UnitreeMujoco.02 | T | „Current version“: Stand der README bei Abruf; Zeitangabe nennen. |
| | UnitreeMujoco.03 | E | Nur SportModeState, nur nach Abschalten des eingebauten Bewegungsreglers; nicht auf alle Nachrichten verallgemeinern. |
| | Hu2026.02 | E | Im Zitat steht nur „its implementation“; Bezug auf den Onboard-Regler (D3) ergibt sich aus dem Kontext (Hu2026, S. 7). Beleg sagt „Autoren schreiben keine inneren Mechanismen zu“, nicht „nicht einsehbar“ im weiteren Sinn. |
| L3 Derselbe Code in Sim und am G1 | Durrani2026.01 | T | Eine Funktion (Teleoperation mit IMU-Anzug). |
| | Durrani2026.02 | E | Aussage der Autoren zu ihrer Pipeline; „ohne Änderung“ bezieht sich auf das System, nicht auf den Onboard-Regler. |
| | Durrani2026.03 | E | Nur „Retargeting-Code“ läuft unverändert; bestandene Sim2Sim-Prüfung ist laut Autoren ein Indiz („strong evidence“), kein Nachweis. |
| | Durrani2026.04 | T | Onboard-Regler übernimmt die Stabilität auf niedriger Ebene. |
| | GalbotOpenWBT.01 | E | „supports both real robots and simulation“; daraus folgt nicht „derselbe Code“ oder gleiche Schnittstelle. README-Angabe. |
| L4 Nur Simulation oder nur Roboter | Yu2026.03 | T | MATLAB/Simulink-Modell; Armlänge usw. nicht übernehmen. |
| | Yu2026.04 | T | Limitation laut Autoren: nur Simulation, Versuche am G1 nötig. |
| | Yu2026.11 | E | Künftige Arbeit (Absicht), kein Ergebnis. |
| | HucebotG1Pilot.01 | T | Unterkörper beim Unitree-Regler; README-Angabe. |
| | HucebotG1Pilot.05 | E | Neu. Belegt Visualisierung des realen Roboters. Der Negativbefund „README beschreibt keinen Simulationsbetrieb“ ist Eigenanalyse (Suche in README-Text vom 09.11.2026, Commit 5346e52: keine Treffer für sim/gazebo/mujoco), Art W mit `% Basis:`. |
| | HucebotG1Pilot.02, .03, .04 | N | Für L4 nicht einschlägig (Reglerarchitektur, Docker, Navigation); gehören zu L12/Kap. 4.4. |
| L5 Sicherer Übergang gelöst? | Tong2024.05 | E | Kontext Reinforcement Learning; „gefährlich und ineffizient“ bezieht sich auf Lernen allein in der realen Umgebung. |
| | Tong2024.06 | T | „remains a challenge“; Aussage der Übersichtsarbeit. |
| | Sekkat2024.03 | E | Kontext Training von KI auf Pepper; Aussage „muss getestet werden“, kein Befund zum G1. |
| L6 Sim-to-Real-Lücke | He2025.07 | E | Gilt für den Policy-Transfer der Autoren (ASAP, G1 ist Plattform), Gründe sind Autorenurteil; nicht auf Bedien-Stacks übertragen. |
| | Collins2019.09 | E | Manipulator, Stand 2019; „largely solved“ nur für Kinematik und Regelung, nicht für Kontakt. Kein Humanoid. |
| | Sekkat2024.09 | E | Allgemeine Aussage, Sekundär [1]. |
| L7 Validierung von Simulationen | Choi2021.02 | E | Stützt „physischer Test bleibt nötig“, nicht direkt ein Validierungsverfahren. |
| | Choi2021.18 | T | Bedarf an neuen Validierungswegen laut Autoren, besonders für noch nicht gebaute Roboter. |
| | Kadian2020.01 | E | Domäne Navigation; Maßstab ist Vorhersagekraft, nicht Realismus. |
| | Durrani2026.03 | E | Siehe L3: Indiz, kein Nachweis. |
| | Durrani2026.05 | E | Neu. Zweck der Sim2Sim-Stufe (Korrektheit, Gelenkgrenzen, Stabilität); kein quantitativer Vergleich Simulation/Roboter. |
| | Sekkat2024.12, .13 | E | Neu, siehe L27. |
| L8 Voraussetzungen der Teleoperation | Fu2024.01 | E | Aussage über „prior works“ (Sekundär); Motion Capture, VR, Exoskelett „teuer und örtlich eingeschränkt“. |
| | He2024.03 | E | Bezug: Datensammlung in großem Maßstab; „hindert“ laut Autoren. |
| | UnitreeXRTeleop.01 | T | XR-Geräte (Beispiele genannt); README. |
| | UnitreeXRTeleop.02 | E | Belegt nur die Leseempfehlung für Neueinsteiger, nicht „setzt Fachwissen voraus“ allgemein. |
| | Zhao2025.01 | T | Teleoperation: begrenzte Skalierbarkeit, aufwendige Einrichtung (Aussage der Autoren). |
| | AliPour2026.01 | T | Beispielsystem (XR-Oberkörper plus Pedale), Bauaufgaben; Preprint-Status prüfen. |
| L9 Werkzeuge für Laien | Pot2009.01 | T | Choregraphe für Nao. |
| | Pot2009.02 | E | Absicht der Entwickler („conceived to“), keine Wirksamkeitsaussage. |
| | Pot2009.05 | T | Box Library, Stand 2009. |
| | Pot2009.06 | T | Aussage der Autoren zu Choregraphe. |
| | Ajaykumar2021.01, .03 | E | Survey über Roboter allgemein, nicht humanoid-spezifisch; Stand 2021. |
| | (Aussage „nur kleine Humanoide“) | W | Beleg nennt Nao, nicht die Größe; „klein“ und der Geltungsbereich („unter den betrachteten Arbeiten“) gehören in die Wertung. |
| L10 Evaluation außerhalb des Labors | Ajaykumar2021.12 | E | „may present a limited view“: vorsichtige Formulierung der Autoren, Survey bis 2021. |
| L11 Sicherheitslücke Zweibeiner | Prather2025.01 | E | Graue Literatur (Bericht); „most existing standards“; „nicht ausgelegt“ statt „fehlt“. |
| | Prather2025.03 | E | Graue Literatur; Aussage über spezialisierte Sicherheitsnormen; Energielosigkeit ist laut Bericht „not necessarily“ sicher. |
| | Prather2025.06 | E | Graue Literatur; „nicht direkt anwendbar“. |
| | Ding2026.03 | E | Preprint; Aussage der Autoren zum laufenden Zweibeiner. |
| | Ding2026.05 | E | Preprint; betrifft PROFIsafe/SDA-Controller der Autoren; belegt: Bordrechner des G1 sind COTS, keine sicherheitsbewertete Hardware. |
| | He2024.04 | E | Grenze der OmniH2O-Policy, keine Aussage über Bedien-Stacks. |
| | Tong2024.14 | T | Übersichtsarbeit, allgemein. |
| L12 Wofür sind die Stacks gebaut | Cheng2024.01 | E | Teleoperation für Datensammlung, allgemein. |
| | Zhao2025.01 | T | Datensammlung. |
| | UnitreeRLMjlab.01 | T | RL-Projekt auf MuJoCo, unterstützt u. a. den G1. |
| | UnitreeRLMjlab.06 | E | Zeigt Ablauf Train, Play, Sim2Real; Zweck „Training“ ergibt sich daraus. |
| | NvidiaGR00TWBC.01 | T | Training, Bewertung, Einsatz von Ganzkörperreglern. |
| | Ze2025.01 | E | „most current“ Teleoperationssysteme; nur Teleoperation. |
| | (keine gemeinsame Grundlage zum Andocken) | W | Kein Beleg möglich; Art W mit Geltungsbereich und `% Basis:`. Status bleibt **teilweise**. |
| L13 Modularität/Wiederverwendung | Macenski2022.05 | E | Beschreibt Designprinzip von ROS 2, keine „Forderung der Literatur“ an Bedien-Stacks. |
| | Macenski2022.11 | E | Beispiel (rmw austauschbar ohne Codeänderung); nur ROS 2. |
| | Saeedvand2019.13 | E | ROS als Vereinheitlichung für Humanoide laut Autoren; keine Aussage zu Wiederverwendung eigener Projekte. |

## 5.2 Anforderungen

| Leitfrage | Beleg-ID | Bew. | Einschränkung |
|---|---|---|---|
| L14 Grenze Handgeschwindigkeit | Villani2018.09 | E | 250 mm/s als Grundannahme der ISO/TS 15066 (Sekundärquelle), für kollaborative Operationen von Industrierobotern; nur Orientierung. |
| | DGUV2015.04 | E | Betriebsart T1 mit Zustimmungsschalter und Tippschaltung, Industrieroboter; Wert gilt nur zusammen mit diesen Schutzmaßnahmen. |
| | DGUV2015.01 | T | Geltungsbereich EN ISO 10218-1: Industrieroboter. |
| | DGUV2015.02 | E | Für nichtindustrielle Anwendungen „dürfen“ die Anforderungen angewendet werden (solange keine eigenen Normen existieren); keine Pflicht, keine „Normerfüllung“. |
| | Prather2025.05 | E | Graue Literatur; Anwendungsbereich der ISO/TS 15066 fixiert oder statisch stabil. |
| L15 Rechtsrahmen Not-Halt | MRL2006.08 | T | Maschinenrichtlinie; ob der G1 unter „Maschine“ fällt, ist nicht belegt; nur Orientierung. |
| | MRL2006.09 | T | wie oben. |
| | MRL2006.04 | T | wie oben. |
| | DINENISO13850.01 | E | Norm für Maschinen; Orientierung, keine Normerfüllung. |
| | DINENISO13850.02 | E | wie oben; „ohne zusätzliche Gefährdungen“ stützt L16. |
| | DINENISO13850.03 | E | Definition Stopp-Kategorie 1; nur Begriff. |
| L16 Abschalten genügt nicht | Ding2026.03 | E | Preprint. |
| | Ding2026.08 | E | Preprint; Konzept der Autoren (kontrollierter Halt im Stand), nicht allgemeine Praxis. |
| | Ding2026.09 | E | Preprint; „aggressiver Halt kann Sturz auslösen“ ist Autorenaussage. |
| | Prather2025.03 | E | Graue Literatur, siehe L11. |
| | Subburaman2023.02 | E | Autorenurteil (Stand 2023), Sturz „unavoidable“. |
| | Subburaman2023.10 | E | Aussage über Literaturlücke (Stand 2023). |
| | DINENISO13850.02 | E | Halt „ohne zusätzliche Gefährdungen“ (Norm für Maschinen allgemein). |
| L17 Zeitbezug des Halts | DGUV2015.17 | E | Neu geprüft. EN ISO 10218-1 Anhang B fordert vom Hersteller Angaben zu Anhaltezeit und Anhalteweg; Sekundärquelle (DGUV), Industrieroboter. |
| | DGUV2015.18 | T | Definition Anhaltezeit (Einleiten bis Stillstand). |
| | DGUV2015.19 | E | Anhaltezeit = Reaktionszeit + Bremszeit; Reaktionszeit hängt von Übertragung, Verarbeitung, Schaltzeiten ab. Keine Zahlenwerte. |
| | DINENISO13850.01–.03 | N | Enthalten keinen Zeitwert und keine Zeitdefinition (Volltext durchsucht). |
| | Valori2021.01 | E | Nur „fehlende Nachweisverfahren“ bei Cobots; keine Zeitwerte. |
| | (keine feste Höchstzeit in den Normen) | W | Negativbefund der Nachrecherche, nicht zitierbar; Formulierung: „in den ausgewerteten Quellen (Geltungsbereich nennen) ist eine gemessene und angegebene Anhaltezeit gefordert, kein fester Grenzwert“. ISO 13855 ohne PDF → `\qf`. Status **teilweise**; K5.3/K5.4 bleiben Setzung [V]. |
| L18 Echtzeitfaktor | Pitonakova2018.01 | E | Definition R = simulierte/reale Zeit für V-REP, Gazebo, ARGoS; „R > 1: schneller als Echtzeit“. Keine Definition von „Echtzeit“ allgemein, keine Grenze für „Echtzeit erreicht“. |
| | Pitonakova2018.02 | E | Nur Beschreibung des Headless-Benchmarks (5 min, ohne Oberfläche); Messmethode der Autoren, keine Norm. |
| | Ayala2020.08 | E | Sekundärzitat zu Pitonakova (Preprint-Seiten), Kennzahlen Echtzeitfaktor, CPU, Speicher; im Zitat steht „simt/realt“ nur als Textextraktion. |
| | Choi2021.10 | E | Nur Größenordnung für Starrkörpermodelle (Stand 2020); nicht als Anforderung verwenden. |
| | (Takttreue, Zielwert 0,95, „handelsüblicher PC“) | S | Setzung ohne Quelle. Hinweis: In Pitonakova kann R > 1 sein; bei begrenzter Simulation (Lockstep) ist R ≤ 1. Status **abgedeckt für Definition**, Bestimmung nur als Beispiel. |
| L19 Gebrauchstauglichkeit messen | Ajaykumar2021.09 | E | SUS „häufigstes Werkzeug“ in Nutzerstudien zu Endnutzer-Programmiersystemen; Survey, Stand 2021. SUS selbst nicht belegt (Q3). |
| | Ajaykumar2021.10 | E | NASA-TLX misst Arbeitsbelastung, nicht Usability. |
| | Ajaykumar2021.11 | T | Fehler zählen. |
| | Ajaykumar2021.13 | T | Neu. Aufgabenerfolg als übliches Maß (Ausführung erfolgreich oder vorab festgelegte Korrektheit). |
| | Ajaykumar2021.14 | E | Neu. Grenzen subjektiver Maße, siehe L28. |
| L20 Zugänglichkeit | Pot2009.03 | E | Begründung der Autoren („we believe“, Haushaltsroboter). |
| | Pot2009.04 | E | Anforderung nur für Choregraphe; Plattformunabhängigkeit. |
| | Pot2009.06 | T | Bedienung ohne C++. Alle drei: Beispiel eines Werkzeugs, nicht „vergleichbare Werkzeuge“ verallgemeinern. |
| L21 Größen für Armbewegungen | Collins2019.03 | E | Manipulator (Arm), Motion-Capture als Referenz. |
| | Collins2019.06 | E | Maß ist der euklidische Abstand der Handgelenkposition zur Zielposition, **nicht Gelenkwinkel**; für K4.1 nur analog, für K4.2 (Handposition) direkt anschlussfähig. |
| | He2025.09 | E | MPJPE (Positionsfehler je Gelenk), für Policy-Tracking; nicht Gelenkwinkel. |
| L22 Anforderungsmethodik | Bender2021.01 | E | Neu. Unterscheidung Forderung (Muss) und Wunsch (Soll); Quelle: Methodikbuch, kein Robotikbezug. Passt nur, falls die Einteilung im Text vorkommt. |
| | Bender2021.02 | T | Messbarkeit als Voraussetzung für Beurteilung der Umsetzung. |
| | Bender2021.03 | T | Verifizierbarkeit durch messbare Ausprägung als Qualitätskriterium. |
| | Bender2021.04 | E | Zielkonflikt operational vs. lösungsneutral; belegt nicht die Forderung „lösungsneutral“ selbst. |
| | Bender2021.05 | T | Wertebereich oder Grenzwert statt Punktwert, wenn Spielraum zulässig; stützt „höchstens“-Zielwerte. Status **abgedeckt**. |

## 5.3 Bewertungsmethodik

| Leitfrage | Beleg-ID | Bew. | Einschränkung |
|---|---|---|---|
| L23 Externe Referenz und Abstandsmaß | Collins2019.03 | E | Siehe L21. |
| | Collins2019.04 | T | Motion Capture, 1 mm Genauigkeit, als Näherung der Ground Truth: begründet, warum dieser Weg ohne Motion Capture nicht anwendbar ist. |
| | Collins2019.06 | E | Siehe L21. |
| L24 Gleiche Trajektorie in zwei Umgebungen | He2025.09 | E | Siehe L21; Vergleich Trainings- und Testumgebung. |
| | Erez2015.13 | T | Ursachen der Abweichung: numerische Integration und Modellfehler. |
| | Erez2015.14 | E | Konsistenz gegen Referenzintegration mit kleinem Zeitschritt, Simulator gegen sich selbst; kein Vergleich mit dem Roboter. |
| L25 Vorhersagekraft | Kadian2020.01 | E | Navigation; Maßstab Vorhersagekraft. |
| | Kadian2020.02 | E | SRCC braucht mehrere Methoden mit Genauigkeit in Simulation und Realität (Navigation); als nicht anwendbar begründen. |
| | Kadian2020.03 | T | Bedeutung der SRCC-Werte. |
| L26 Zeitfenster | Acosta2022.08 | E | Cassie-Sprung, 50 ms um den Stoß (2000 Hz); Kann, nur als Beispiel. |
| L27 Digitaler Zwilling | Sekkat2024.07 | T | Pepper, Vergleich mit Choregraphe und realem Roboter. |
| | Sekkat2024.12 | E | Neu. Referenz: HD-Video (1080p, 60 fps) plus IMU-Sensoren an den Gelenken; Pepper/Gazebo, nicht G1. |
| | Sekkat2024.13 | E | Neu. Ergebnis der Autoren (0,01 bis 0,02 rad); nur Pepper-Arme/Kopf; nicht als Zielwert für A4 verwenden. |
| L28 Grenzen Laborstudien | Ajaykumar2021.12 | E | Siehe L10. |
| | Ajaykumar2021.14 | E | Neu. Subjektive Maße (z. B. Usability) werden durch Hardware-Unzuverlässigkeit und Wahrnehmung des Roboters beeinflusst; Survey. |
| L29 Nutzen der Simulation | Choi2021.03 | T | Chancen laut Autoren (sicher, kontrolliert, günstig). |
| | Choi2021.05 | E | „can make simulation instrumental“: Möglichkeit, keine Garantie. |
| | Sekkat2024.03 | E | Siehe L5. |
| L30 Physischer Test nötig | Choi2021.02 | T | „mandatory“ laut Autoren (Übersichtsarbeit). |
| L31 SIL/HIL-Analogie | Mihalic2022.04 | E | Automotive (ECU); SIL-Zertifizierung ohne Hardware. |
| | Mihalic2022.07 | E | HIL; Aussage der Autoren zu Regelsystemen allgemein. |
| | Mihalic2022.08 | E | HIL-Test: Embedded-Code ohne Systemhardware, auch Fehlerfälle. Passt zur Attrappe nur als **Analogie**. |
| | Afzal2021.03 | E | Neu. SITL (Steuerungssoftware auf demselben Rechner wie Simulator) und HIL (langsamer, teurer); Robotikbezug. Die Attrappe ist weder SITL noch HIL im Sinn der Quellen. |
| L32 Simulationsbasiertes Testen | Afzal2021.01 | E | Neu. Feldtest laut Autoren zeitaufwendig, teuer, nicht skalierbar, potenziell gefährlich. |
| | Afzal2021.02 | E | Neu. „promising“; Autorenurteil, Konferenzbeitrag. Status **abgedeckt**. |
| L33 Container | Boettiger2015.02 | T | Rechenumgebung nachbilden als Voraussetzung. |
| | Boettiger2015.06 | E | Docker löst Abhängigkeitsproblem ähnlich einem VM-Image; Forschungsreproduzierbarkeit. |
| | Cervera2019.01 | T | Docker für ausführbare Images in isolierter Umgebung. |
| | Cervera2019.02 | E | Frameworks haben die Reproduktion nicht vereinfacht; stützt Container indirekt. Container fixieren Software, nicht Hardware und Zeitverhalten (siehe L34). |
| L34 Hardware und Zeitmessung | Kronauer2021.12 | E | Latenz von Middleware; Messgröße ist nicht der Echtzeitfaktor einer Physiksimulation. |
| | Kronauer2021.13 | E | wie oben; Energiesparfunktionen als Einfluss. |
| | Kronauer2021.05 | T | Muster für Angabe der Messrechner (Prozessor, RAM). |

## Zusammenfassung

- Geprüft: 136 Tabellenzeilen zu Beleg-IDs (einzelne Zeilen fassen 2–3 IDs zusammen; manche IDs stehen unter mehreren Leitfragen). Bewertung nach Zeilen: 40 trägt, 94 trägt mit Einschränkung, 2 trägt nicht (HucebotG1Pilot.02–.04 für L4; DINENISO13850.01–.03 für L17). Dazu 5 Zeilen für Wertung/Setzung/offen ohne Beleg.
- Leitfragen weiter offen oder nur teilweise: **L1** (Hemmnisse aus Sicht von Unternehmen: offen), **L12** (keine gemeinsame Grundlage: Art W, kein Beleg), **L17** (feste Höchstzeit nicht belegbar, nur Negativbefund; ISO 13855 ohne PDF), **L18** (Definition vorhanden; Takttreue und „handelsüblicher PC“ Setzung), **L31** (Attrappe nur Analogie), **L9** („klein“ im Geltungsbereich Art W).
- Nicht belegt, daher Setzung oder Wertung: Zielwerte K3.1, K3.2, K4.2, K5.3, K5.4, K6.1, K6.2; Aussage „keine gemeinsame Grundlage“.
- Offene Quellenlücken: Q3 (SUS/NASA-TLX Primärquellen, nur bei Nutzerstudie), Q4 (Softwarequalitätsmerkmale), Q7 (Hemmnisse Unternehmen), ISO 13855 (kein PDF).
