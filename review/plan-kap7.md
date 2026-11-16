# Kapitelplan Kap. 7 – Umsetzung

Stand 16.11.2026 (Claude, Kapitel-Workflow Schritt 1 und Schritt 2 für die klaren Lücken). Auftrag Nils vom 16.11.:
nur planen, noch kein Fließtext. Die Ausarbeitung übernehmen danach schwächere Modelle anhand der Arbeitspakete in §9.
**Wartet auf Nils:** Entscheidungen in §8.

- Code-Stand, auf den sich alle Angaben beziehen: Repo `NilsMeier1812/G1`, `main` @ `25d5c1a` (11.11.2026).
  Fundstellen in diesem Plan stammen aus der Technik-Doku `g1pilot/docs/*-T-*.md` und aus Stichproben im Code.
  **Die Doku kann vom Code abweichen** (Beispiel: Doku nennt „rund 550 Testfunktionen in 43 Dateien“, gezählt sind
  597 in 49). Jede Zahl wird in AP 2 am Code nachgelesen, bevor sie in den Text kommt.
- Abgrenzung zu Kap. 6 ist mit dem Thread „Kapitel 6 konzipieren und planen“ abgestimmt (16.11.), siehe §1.2.
- `python3 scripts/check.py` am 16.11.: 0 Fehler, 0 Warnungen, 31 Hinweise (unverändert, dieser Plan ändert keinen Text).

---

## 1 Rolle des Kapitels

### 1.1 Leitgedanke

Kap. 6 begründet, **was** die Umgebung leisten soll und **warum** sie so geschnitten ist. Kap. 7 zeigt, **wie** die
dort getroffenen Entscheidungen technisch gelöst sind, und zwar nur so tief, wie es ein anderer Entwickler braucht, um
die Lösung nachzubauen oder auf einen anderen Roboter zu übertragen (Richtlinien §3.4 „Methodik“: Reproduzierbarkeit,
nur übertragbare Details, keine Entwicklungsgeschichte). Kap. 8 weist nach, dass es funktioniert.

Kap. 7 ist das Kapitel mit dem größten Anteil an Eigenleistung. Der rote Faden ist der Weg eines Befehls durch das
System, von unten nach oben:

1. Bereitstellung (7.1): Wo läuft welcher Prozess?
2. Simulation (7.2): Wie wird MuJoCo so angebunden, dass es sich wie der Roboter verhält?
3. Fortbewegung (7.3): Was ersetzt in der Simulation den Onboard-Regler, und wie wird der echte angesprochen?
4. Arme (7.4): Wie entsteht aus einem Ziel eine sichere Armbewegung?
5. Hände (7.5): Wie werden Hände einheitlich angesteuert und ausgetauscht?
6. Bedienwege (7.6): Wie kommen Eingaben von Mensch und fremder Software in das System?
7. Navigation (7.7): Beispiel für ein übernommenes, eingebundenes Modul.

Jeder Abschnitt folgt demselben Muster (2–4 Sätze Rahmen, dazwischen der Inhalt):
**Rückbezug** auf die Entscheidung in Kap. 6 und die Anforderung (A1–A7) → **Lösung** (Aufbau, Algorithmus,
Schnittstelle, wenige tragende Parameter mit Begründung) → **Vorverweis** auf den Nachweis in Kap. 8.

### 1.2 Abgrenzung

| Gegenüber | Regel |
|---|---|
| Kap. 2–4 (Grundlagen, SdT) | Kap. 7 erklärt keine Grundlagen neu. Aussagen über fremde Werkzeuge und Verfahren (MuJoCo, DDS, ROS 2, Docker, DLS-IK, CHOMP, RRT-Connect, Kugelmodelle, Inspire-Hand) stehen dort und werden per `Abschnitt~\ref{}` aufgerufen. Nur was dort fehlt und für die Umsetzung nötig ist, bekommt in Kap. 7 ein eigenes `\cite{}\ev{}`. |
| Kap. 6 (Konzept) | Kap. 6: Anforderung, Alternativen, Entscheidung, Lösungsprinzip auf Ebene Komponenten, Zustände, Schnittstellen. Keine Takte, Algorithmen, Datenformate. Kap. 7: genau diese. **Alternativen werden in Kap. 7 nicht mehr diskutiert**, außer auf Implementierungsebene (z. B. eigener Prozess statt Thread). |
| Kap. 6.3 (Sicherheit) | Kap. 7 hat **keinen eigenen Sicherheitsabschnitt**. Der Katalog der Schutzmechanismen mit allen Grenzwerten steht einmal in `tab:schutzmechanismen` (6.3.2). Kap. 7 beschreibt die Umsetzung bei der jeweiligen Komponente (7.3.2, 7.4.1, 7.4.2, 7.5.1, 7.6) und verweist für Zahlenwerte auf die Tabelle. Die Tabelle in 6.3.2 bekommt eine Spalte „Umsetzung in Abschnitt“. |
| Kap. 6.4.2 (Bedienwege) | Die Matrix Bedienweg × Funktion × Zielgruppe (`tab:bedienwege`, bisher im Gerüst von 7.6) wandert nach 6.4.2. 7.6 bekommt eine Umsetzungstabelle `tab:bedienwege_umsetzung`. Rollen und Steuerhoheit des Smartphones stehen konzeptionell in 6.4.2, das Protokoll in 7.6.3. |
| Kap. 6.2.3 | Auswahlbegründung der Lauf-Policies steht in 6.2.3 (mit `tab:policies` aus 4.1). 7.3.1 beschreibt nur die Einbindung. |
| Kap. 5.3.3 (Testumgebung) | Testaufbau (Attrappe des Roboters, automatisierte Tests, Referenz-PC) steht in 5.3.3 und 8.3.1, nicht in Kap. 7. |
| Kap. 8 (Evaluation) | **Keine Messergebnisse in Kap. 7.** In Kap. 7 stehen Auslegungswerte (Takt, Schrittweite, Abstände) mit Begründung. Gemessene Kennwerte (Gangbild, Stoßtests, Planungszeiten, IK-Restfehler, Überdeckung des Kugelmodells) gehören nach Kap. 8; Liste der im Repo vorhandenen Messwerte in §6.3. |

### 1.3 Schreibregeln speziell für dieses Kapitel

Zusätzlich zu `CLAUDE.md` und `Richtlinien-BA.md`:

- **R1 Zwei Arten von Aussagen.** (a) Aussage über die eigene Umsetzung = Eigenleistung (CLAUDE.md Regel 5): keine
  Quelle, aber Datenbasis. Am Absatzende steht ein LaTeX-Kommentar
  `% DB: <Pfad im G1-Repo>:<Zeilen> @25d5c1a` (mehrere durch Semikolon). (b) Aussage über etwas Fremdes (Werkzeug,
  Verfahren, Schnittstelle des Herstellers, übernommene Policy): `\ref` auf Kap. 2–4 **oder** `\cite{}\ev{}`, sonst
  `\qf{}`. Im Zweifel ist eine Aussage fremd.
- **R2 Keine Zahl ohne Fundstelle.** Parameterwerte nur aus dem Code am festen Stand, nie aus Doku oder diesem Plan
  abschreiben. Nicht auffindbar → `\pruefen{}`.
- **R3 Keine Entwicklungsgeschichte.** Die Technik-Doku ist voll von „früher …, deshalb jetzt …“. Im Text steht nur
  der Endzustand und sein Grund im Präsens („Die IK läuft in einem eigenen Prozess, weil eine Lösung länger dauert
  als ein Regeltakt.“). Keine Datumsangaben von Fehlern, keine verworfenen Zwischenlösungen.
- **R4 Kein Handbuch** (Nils 29.10.). Keine Bedienschritte, Tastenbelegungen, Befehle, Umgebungsvariablen-Listen,
  Dateinamen im Fließtext. Programmnamen (`loco_sim`, `arm_controller`) erscheinen nicht im Text, sondern die
  deutschen Funktionsbezeichnungen aus §7; die Zuordnung zu Dateien steht einmal im Anhang (Entscheidung E3).
- **R5 Wenige Parameter.** Pro Unterabschnitt höchstens drei bis fünf Zahlenwerte im Text, nämlich die, die das
  Verhalten prägen und eine Begründung haben. Der Rest steht in einer Anhangtabelle (Entscheidung E4). Grenzwerte
  der Schutzmechanismen stehen nur in `tab:schutzmechanismen`.
- **R6 Diagramm vor Code.** Keine Quelltext-Listings (Richtlinien §13.4). Abläufe als Block- oder Zustandsdiagramm,
  Rechenvorschriften als Gleichung mit erklärten Variablen und `\formeleintrag{}`.
- **R7 Sim und Real getrennt kenntlich.** Jeder Unterabschnitt sagt ausdrücklich, was nur in der Simulation, nur am
  realen Roboter oder in beiden gilt.
- **R8 Stil.** Präsens, Sach-Subjekt, kein „ich/wir/man“, keine Autorennamen als Satzsubjekt (Stilregel 11.11.),
  Tabellen und Abbildungen nie ohne Textbezug (vorher einführen, danach erläutern), Absätze mit Topic Sentence.

---

## 2 Gliederung

Zielumfang **15 bis 16 Seiten** (Gerüst: ca. 14; Mehrbedarf durch 7.5.2 und die Abbildungen, siehe Entscheidung E2).
„Kern“ = muss hinein, „Kann“ = zuerst streichen.

| Abschnitt | Label | Umfang | Anf. / Frage | Rückbezug | Nachweis | Änderung ggü. Gerüst vom 30.10. |
|---|---|---|---|---|---|---|
| Kapiteleinleitung | `chap:umsetzung` | 5–6 Sätze | – | Kap. 6 | – | nennt den roten Faden „Weg eines Befehls“ und die Leseregel für Sim/Real |
| **7.1 Containerisierte Bereitstellung** | `sec:bereitstellung` | 1 S. | A6, A7 | 6.5.2, 3.3.3 | 8.3.2, 8.1.1 | – |
| **7.2 Simulationsumgebung** | `sec:simulationsumgebung` | 3 S. | A3, A4, A2 | 6.2.2 | 8.1.1, 8.2.1 | – |
| 7.2.1 Kopplung von MuJoCo und DDS | `sec:bridge` | 1,25 S. | A2 | 6.2.2, 3.2.2, 3.3.2, 2.3 | 8.1.1 | – |
| 7.2.2 Zeitschritt und Echtzeitbetrieb | `sec:zeitschritt` | 0,75 S. | A3 | 3.2.2, 3.1.3 | 8.2.1 | – |
| 7.2.3 Szenen und Arbeitsplatzmodelle | `sec:szenen` | 1 S. | A1, A7 | 6.4.3, 6.5.1 | 8.4.2 | um das gemeinsame Weltmodell ergänzt |
| **7.3 Fortbewegung** | `sec:fortbewegung_umsetzung` | 2,5 S. | A2, A4, A5 | 6.2.3 | 8.2.2 | – |
| 7.3.1 Ersatzregler in der Simulation | `sec:ersatzregler` | 1,75 S. | A4 | 6.2.3, 4.1 | 8.2.2 | – |
| 7.3.2 Anbindung des Onboard-Reglers | `sec:onboard_anbindung` | 0,75 S. | A5 | 6.2.3, 6.3.2, 2.3.2 | 8.1.2, 8.3.1 | – |
| **7.4 Armregelung und Bahnplanung** | `sec:armregelung` | 4 S. | A1, A5 | 6.3, 4.2 | 8.2.3, 8.3.1 | Schwerpunkt des Kapitels |
| 7.4.1 Regelkette und inverse Kinematik | `sec:regelkette` | 1,5 S. | A3, A5 | 6.3.3, 4.2.1, 2.3.3 | 8.2.1, 8.2.3 | nimmt Übergabe an den Onboard-Regler und Halten der Taille auf |
| 7.4.2 Kollisionsmodell und Laufzeitüberwachung | `sec:kollisionsmodell` | 1,25 S. | A5 | 6.3.2, 4.2.2 | 8.3.1 | – |
| 7.4.3 Bahnplaner | `sec:bahnplaner` | 1,25 S. | A1 | 4.2.3 | 8.2.3 | nimmt das geplante Anfahren gespeicherter Posen auf |
| **7.5 Roboterhände** | `sec:haende` | 2 S. | A1, A7 | 4.2.4, 6.5.1 | 8.4 | Titel bisher „Inspire-Hände“; neu zwei Unterabschnitte |
| 7.5.1 Schnittstelle der Inspire-Hände | `sec:hand_schnittstelle` | 1 S. | A2 | 4.2.4 | 8.1.2 | neu als Unterabschnitt |
| 7.5.2 Austauschbare Hand-Profile | `sec:hand_profile` | 1 S. | A7 | 6.5.1 | 8.4 | **neu** (Funktion seit 10.11. im Code, Nils: gehört nach Kap. 7) |
| **7.6 Bedienwege** | `sec:bedienwege` | 3 S. | A6, F3 | 6.4 | 8.3.2 | Matrix nach 6.4.2, dafür Umsetzungstabelle |
| 7.6.1 Demo-Oberfläche | `sec:demo_gui` | 1 S. | A6 | 6.4.1, 6.4.3 | 8.3.2 | nimmt Dateiformat und Ablaufsteuerung der Posen/Abläufe auf |
| 7.6.2 Gamepad | `sec:gamepad` | 0,6 S. | A6, A5 | 6.4.2 | 8.3.1 | – |
| 7.6.3 Smartphone | `sec:smartphone` | 0,6 S. | A6, A5 | 6.4.2 | 8.3.1 | – |
| 7.6.4 Entwickler-Oberfläche und Arm-API | `sec:entwickler_api` | 0,8 S. | A7 | 6.5.1 | 8.4.1 | Streamdeck entfällt (Oberfläche am 30.10. aus dem Code entfernt); Inhalt: Zielmarker in RViz, HTTP-Schnittstelle, direkter DDS-Zugang |
| **7.7 Navigation in der Simulation** | `sec:navigation` | 0,5–0,75 S. | A7 | 6.1.2 | – | kurz, als Beispiel eines eingebundenen Moduls |

Prüfung gegen Richtlinien §5.1: höchstens drei Ebenen, kein einzelnes Unterkapitel, sieben Abschnitte. 7.1 und 7.7
haben keine Unterabschnitte (kurz), die übrigen zwei bis vier.

**Streichreihenfolge bei Platzmangel:** (1) 7.7 auf einen Absatz in 7.2.3 kürzen. (2) 7.6.3 Protokolldetails.
(3) Abbildungen der Stufe „Kann“ (§4). (4) Schwerpunkt-Führung in 7.3.1 auf zwei Sätze. Nicht kürzen: 7.2.1, 7.4.

---

## 3 Inhalte je Abschnitt

Aufbau je Abschnitt: **Leitfragen** (offen formuliert), **Kerninhalte** (aus Doku und Code, in AP 2 am Code zu prüfen),
**Belegbedarf** für fremde Aussagen mit Status (abgedeckt / teilweise / offen), **Darstellungen**, **Nicht hinein**.
Kürzel der Darstellungen (B = Abbildung, T = Tabelle, G = Gleichung) siehe §4.

### Kapiteleinleitung

Fünf bis sechs Sätze: Rückblick auf Kap. 6 in einem Satz, roter Faden „Weg eines Befehls“, Reihenfolge der
Abschnitte, Hinweis, dass Grenzwerte in `tab:schutzmechanismen` und Messergebnisse in Kap. 8 stehen, Hinweis auf den
Anhang mit der Zuordnung zu den Quelltextdateien. Kein Inhalt, der nicht in 7.1–7.7 steht.

### 7.1 Containerisierte Bereitstellung

**Leitfragen**
- L7.1 In welche Container-Abbilder ist die Umgebung aufgeteilt, und nach welchem Kriterium?
- L7.2 Wie wird zwischen Simulation und Realbetrieb gewählt, ohne dass sich der Anwendungscode unterscheidet?
- L7.3 Wie gelangt eine Einstellung des Nutzers bis zum Parameter eines Programms?
- L7.4 Was erledigt das Startmenü, damit ein Nutzer ohne Vorerfahrung starten kann?

**Kerninhalte** (Doku `02-T`, `03-A`, `04-T`, `40-T`; Code `g1pilot/docker-compose.yml`, `docker/Dockerfile.*`,
`start.sh`, `g1_gui.py`, `launch/bringup_*.launch.py`, `docker/*_shutdown_watcher.sh`)
- Drei Abbilder: Physiksimulation ohne ROS (Ubuntu 22.04, MuJoCo), Steuerungssoftware für die Simulation
  (ROS 2 Humble, zusätzlich Laufzeit für die Lauf-Policy), Steuerungssoftware für den realen Roboter (ohne
  Policy-Laufzeit). Zwei Profile `sim` und `real` in einer Compose-Datei.
- Simulation = zwei Container, real = ein Container; alle im Netz des Hosts. Der Simulationscontainer nimmt die
  Stelle des Roboters ein.
- Kette Einstellung → Umgebungsvariable → Compose → Launch-Datei → ROS-Parameter. Änderung ohne Neubau des Abbilds.
- Startmenü (grafisch und Text): wählt Modus, Szene, Hände, Lauf-Policy, Bediengeräte; erzeugt die Szene; verlangt im
  Realbetrieb eine ausdrückliche Bestätigung der Sicherheitshinweise.
- Geordnetes Beenden: die Oberfläche fordert das Beenden an, ein Wächter auf dem Host fährt die Container herunter;
  real erst, nachdem die Arme an den Onboard-Regler zurückgegeben sind (Verweis auf 7.4.1).
- Quelltext, Posen und Szenen sind in den Container eingebunden (bleiben über Neustarts erhalten, versionierbar).

**Belegbedarf**
- Container, Abbild, Reproduzierbarkeit → `Abschnitt~\ref{sec:container}` (abgedeckt: Boettiger2015, Cervera2019, Struhar2020).
- Die Ausgangsbasis bringt bereits einen Docker-Ablauf mit → HucebotG1Pilot.03 (abgedeckt), sonst Verweis auf 6.1.
- Warum Host-Netz: als eigene Entwurfsentscheidung formulieren (DDS-Teilnehmer in getrennten Containern müssen sich
  finden). Eine allgemeine Aussage über DDS-Discovery und Container-Netze braucht einen Beleg → **offen**; ggf.
  OMG2015.12 (Discovery) prüfen, sonst ohne Verallgemeinerung schreiben.

**Darstellungen:** B7.1 (Kern), T7.1 (Kern).
**Nicht hinein:** Installationsschritte, Befehle, GPU-Sonderfälle, Fenster-Icons, vollständige Variablenliste.

### 7.2.1 Kopplung von MuJoCo und DDS

**Leitfragen**
- L7.5 Welche Nachrichten des realen Roboters bildet die Kopplungsschicht nach, und woraus gewinnt sie deren Inhalt?
- L7.6 Wie werden die beiden Befehlswege (Beine/Taille und Arme) zu einem Stellmoment je Gelenk zusammengeführt?
- L7.7 Welche Größen liefert die Simulation zusätzlich, die der reale Roboter nicht liefert, und wie bleibt das im
  Code getrennt?
- L7.8 Wie wird der Roboter in der Simulation gehalten, aufgestellt und zurückgesetzt?

**Kerninhalte** (Doku `02-T`, `30-T` „Bridge-Merge“, `40-T`; Code `unitree_mujoco/simulate_python/unitree_sdk2py_bridge.py`
Zeilen ca. 287–490, `unitree_mujoco.py`, `hold_base.py`, `config.py`; `g1pilot/utils/common.py:21-55`)
- Ausgangspunkt ist die Python-Simulation von Unitree; sie spricht dieselben Nachrichtentypen wie der G1.
  Erweitert wurde sie um den zweiten Befehlsweg, das gesteuerte Halten der Basis, das Aufstellen und die Hände.
- Je Gelenk und Physikschritt PD-Gesetz mit Vorsteuermoment (G7.1), Drehmoment-Aktoren in MuJoCo, der PD-Regler
  liegt außerhalb des Simulators.
- Beine und Taille (Index 0–14) kommen unverändert aus dem Befehlsweg der Fortbewegung, Arme (15–28) werden mit einem
  Gewicht zwischen beiden Wegen überblendet (G7.2). Das Gewicht steht im unbenutzten 30. Motoreintrag, wie am realen
  Roboter.
- Einzige Stelle der Unterscheidung Sim/Real: Wahl von DDS-Domain und Netzwerkschnittstelle beim Verbindungsaufbau.
  ROS 2 läuft auf der jeweils anderen Domain.
- Zusatzgrößen der Simulation (Fußkräfte, Basisgeschwindigkeit) in Reservefeldern; nur der Ersatzregler nutzt sie.
- Basis: im Bereitschaftszustand über eine Schweiß-Zwangsbedingung gehalten, beim Aktivieren in die kommandierte
  Standpose gestellt (Beckenhöhe so, dass die Füße aufstehen), danach frei.
- Nebenkanäle ohne ROS (UDP über Loopback) für Störstoß, Testobjekt, Zurücksetzen und Objektposen, weil der
  Simulationscontainer kein ROS enthält.

**Belegbedarf**
- unitree_mujoco als Basis, Nachrichtentypen, Domain 1 und Loopback → UnitreeMujoco.01, .02, .05–.09 (abgedeckt).
- Drehmoment-Aktoren, Schweiß-Zwangsbedingung, Sensoren → `Abschnitt~\ref{sec:mujoco}`; MujocoDoku2026.03, .05, .06,
  MujocoDoku2026a.08 (abgedeckt).
- Getrennte Domains isolieren vollständig → `Abschnitt~\ref{sec:dds}`, OMG2015.09 (abgedeckt).
- „Am realen Roboter mischt die Firmware nach demselben Gewicht“ und PD-Gesetz der Motorbefehle → gehört nach
  Kap. 2.3.3 (`sec:g1_armsdk`, noch nicht geschrieben). **offen**: Herstellerdoku als PDF nötig (E5), sonst `\qf{}`.

**Darstellungen:** B7.2 (Kern), G7.1, G7.2.
**Nicht hinein:** Portnummern, Feldnamen der Nachrichten, Gamepad-Anbindung der Originalsimulation.

### 7.2.2 Zeitschritt und Echtzeitbetrieb

**Leitfragen**
- L7.9 Welcher Zeitschritt ist gewählt, und was begrenzt ihn nach oben?
- L7.10 Wie wird sichergestellt, dass ein mit fester Rate trainierter Regler auf jedem Rechner dieselbe Menge
  simulierter Zeit je Regelschritt sieht?
- L7.11 Was geschieht, wenn der Rechner die Echtzeit nicht hält oder kein Befehl eintrifft?

**Kerninhalte** (Doku `40-T` „Lockstep“, `30-T` „Regelschleife“; Code `config.py:55-100`, `unitree_mujoco.py`,
`loco_sim.py` Regelschleife)
- Physikschritt 1 ms. Begründung: Der Dämpfungsterm des externen PD-Reglers wird explizit integriert; bei größerem
  Schritt schwingen die leichten Armgelenke auf.
- Gleichschritt-Betrieb: je empfangenem Befehl der Fortbewegung genau N = 20 Physikschritte (G7.3), danach ein neuer
  Zustand; der Regler rechnet einen Befehl je Zustand. Nach oben auf Echtzeit begrenzt, Echtzeitfaktor einstellbar.
- Zeitüberwachung: ohne Befehl läuft die Physik nach 0,2 s weiter.
- Armregler läuft unabhängig mit eigener Rate; seine Glättung wird auf die tatsächliche Schrittweite umgerechnet (G7.8).
- Anzeige mit 50 Bildern je Sekunde, von der Physik entkoppelt.

**Belegbedarf**
- Zeitschritt als wichtigster Parameter, Voreinstellung 2 ms, Integrator → `Abschnitt~\ref{sec:mujoco}`;
  MujocoDoku2026.10, MujocoDoku2026b.04, .05, .08 (abgedeckt).
- Echtzeitfaktor als Kenngröße → `Abschnitt~\ref{sec:abbildungsguete}` (abgedeckt).
- Die Messung hinter der Begründung (Schwingweite bei 5, 2 und 1 ms; steht nur als Kommentar in `config.py`) ist ein
  Messwert → nach 8.2.1, in 7.2.2 nur qualitativ plus Vorverweis. `\pruefen{}`, bis Nils die Messung bestätigt (E6).

**Darstellungen:** B7.3 (Kern), G7.3.
**Nicht hinein:** Namen der Schalter, alter Betrieb mit festgehaltenem Oberkörper.

### 7.2.3 Szenen und Arbeitsplatzmodelle

**Leitfragen**
- L7.12 Wie entsteht aus einer vom Nutzer gebauten Umgebung eine lauffähige Simulationsszene, ohne dass der Nutzer
  Robotermodell, Boden oder Licht kennen muss?
- L7.13 Wie unterscheidet das System Hindernisse, greifbare Objekte, Startpunkt und Zielstationen?
- L7.14 Wie erfahren Armregler, Navigation und Anzeige von den Objekten der Szene?
- L7.15 Welche Störungen und Hilfsmittel stellt die Simulation für Versuche bereit?

**Kerninhalte** (Doku `40-T`, `31-T` „scene_bridge“, `unitree_mujoco/scene_editor/README.md`; Code
`scene_editor/build_env_scene.py`, `simulate_python/scene_objects.py`, `scene_state_publisher.py`,
`g1pilot/navigation/scene_bridge.py`, `scene_markers.py`, `push_listener.py`)
- Trennung Basis (Roboter mit gewählter Hand, Boden, Licht, Halte-Zwangsbedingung; wird erzeugt) und Umgebung (nur
  Objekte; vom Nutzer im grafischen Editor gebaut).
- Klassifikation über Namensvorsätze: greifbares Objekt (wird frei beweglich), Startpunkt, Station; alles andere ist
  Hindernis. Keine Codeänderung für eine neue Szene (Bezug A1, Nachweis 8.4.2).
- Kollisionsgeometrie: große Netze werden in konvexe Teile zerlegt; Kollisionsgruppen legen fest, dass Finger nur
  greifbare Objekte berühren.
- Ein gemeinsames Weltmodell: Die Simulation meldet Objektposen, daraus entstehen Marker, die Anzeige, Armregler
  (Kollision) und Navigation (Karte) gemeinsam nutzen.
- Versuchshilfen: Störstoß mit einstellbarer Kraft, Testobjekt in der Hand, Zurücksetzen von Objekten und Roboter.
- Vier mitgelieferte Szenen (Arbeitsplätze, Stand `scene_editor/scenes/`: A5, AP_1 bis AP_3) → `\pruefen{}`: Nils
  benennt, welche Szene welchen realen Arbeitsplatz abbildet.

**Belegbedarf**
- MJCF → `Abschnitt~\ref{sec:mujoco}`, MujocoDoku2026a.04 (abgedeckt). Kollisionsfilter → MujocoDoku2026.15, .16,
  MujocoDoku2026b.07 (abgedeckt). Freies Gelenk → MujocoDoku2026a.09 (abgedeckt).
- „MuJoCo prüft Netze über ihre konvexe Hülle“ → **teilweise**: in `sources-text/MujocoDoku2026*.txt` suchen (AP 1).
- Konvexe Zerlegung (V-HACD) → Mamou2009 liegt in `_Vorschläge` ohne PDF (IEEE, über FAU) → **offen**.
- Der grafische Editor baut auf einem fremden Projekt auf (`mujoco-scene-editor`, laut README) → Herkunft muss
  genannt werden; Quelle als Software-Eintrag mit README-PDF → **offen** (E5).

**Darstellungen:** B7.4 (Kann; Bildschirmfoto einer Arbeitsplatz-Szene neben dem Weltmodell in RViz).
**Nicht hinein:** Bedienung des Editors, Kraftformel des aufladbaren Stoßes.

### 7.3.1 Ersatzregler in der Simulation

**Leitfragen**
- L7.16 Welche Zustände hat der Ersatzregler, und welche Übergänge laufen selbsttätig ab?
- L7.17 Wie hält der modellbasierte Standregler den Roboter am Platz, auch wenn Arme und Last den Schwerpunkt
  verschieben?
- L7.18 Wie werden vortrainierte Lauf-Policies unterschiedlicher Herkunft hinter einer Schnittstelle eingebunden?
- L7.19 Wie verläuft die Übergabe zwischen Policy und Standregler, und was geschieht, wenn der Standregler den
  Roboter nicht mehr halten kann?
- L7.20 Warum ist dieser Regler nur ein Stellvertreter und nicht für den realen Roboter gedacht?

**Kerninhalte** (Doku `30-T` vollständig; Code `g1pilot/navigation/loco_sim.py`, `walk_policy.py`,
`stand_balancer.py`, `com_model.py`, `policies/*/deploy.yaml`, `policies/*/ATTRIBUTION.md`)
- Vier Zustände: Bereitschaft (Basis gehalten), Stehen (Standregler), Gehen (Policy), Dämpfen (Not-Halt oder Sturz).
  Selbsttätig sind nur Abfangen und Sturz → Dämpfen. Der Regler bedient dieselben Befehle wie die Anbindung des
  Onboard-Reglers (Verweis 6.2.3) und stellt nur Beine und Taille; die Arme gehören allein dem Armregler.
- Arbeitsteilung: Policy fürs Gehen, modellbasierter Regler fürs ortsfeste Stehen (Füße bleiben stehen).
- Standregler: Haltungsregelung auf die Standpose plus Momente an Knöchel und Hüfte aus Neigung und Drehrate der IMU
  (G7.4), Integralanteil gegen statische Neigung. Schwerpunkt-Führung: Schwerpunkt aus allen Gelenkwinkeln über ein
  Starrkörpermodell desselben Robotermodells, Becken wird verschoben, bis der Schwerpunkt über der Fußmitte liegt;
  unbekannte Last wird langsam aus dem Knöchelmoment nachgeführt.
- Standpose = Ausgangspose der Policy, damit der Wechsel ins Gehen ohne Ausgleichsschritt gelingt.
- Einbindung der Policies: je Policy eine Beschreibungsdatei (Beobachtungsaufbau, Skalierung, Verstärkungen,
  Ausgangspose, Befehlsbereiche); eine Formatkennung wählt die Aufbereitung. Aktion → Gelenksollwert (G7.5).
  Drei Policies aus zwei Quellen (T7.2). Ob die Arme beim Gehen eine feste Pose brauchen, wird aus der
  Beschreibungsdatei abgeleitet.
- Übergabe Gehen → Stehen in zwei Schritten: Sollgeschwindigkeit null, dann Übernahme, sobald Drehrate und
  Gelenkgeschwindigkeiten unter Schwellen liegen; der Standregler hält die vorgefundene Beinstellung.
- Abfangen: hebt eine Fußsohle ab oder kippt das Becken, übernimmt vorübergehend eine Policy und gibt nach der
  Beruhigung zurück. Sturz: Neigung über Schwelle → Dämpfen.
- Grenzen (ein Absatz, Vorverweis 8.5.3): nutzt Größen, die nur die Simulation liefert; Schwerpunkt-Führung nur in
  Längsrichtung; kein Anspruch auf Übertragbarkeit.

**Belegbedarf**
- Schwerpunkt, Stützfläche, Gleichgewicht → `Abschnitt~\ref{sec:fortbewegung_sdt}` mit `fig:zmp` (abgedeckt:
  Westervelt2018, Saeedvand2019).
- Herkunft und Eigenschaften der Policies → `Tabelle~\ref{tab:policies}`; UnitreeRLMjlab.01, .04, .05 (abgedeckt);
  AGILE: Zhao2026 liegt mit PDF in `_Vorschläge` → **offen bis Freigabe**.
- Starrkörperbibliothek → Carpentier2019.01, .02 (abgedeckt); dass sie MJCF lädt → **teilweise**, im PDF suchen (AP 1).
- Der Onboard-Regler ist nicht quelloffen → Hu2026.01, .02 und 4.1 (abgedeckt).
- Knöchel- und Hüftstrategie als Begriffe der Literatur → **offen**; entweder ohne die Begriffe schreiben oder Quelle
  suchen (Suchhinweis: Übersichtsarbeiten zur Standbalance zweibeiniger Roboter).

**Darstellungen:** B7.5 (Kern), B7.6 (Kann), T7.2 (Kern), G7.4, G7.5.
**Nicht hinein:** Gangbild-Messwerte, Stoßtests, Wanderung der Füße (alles Kap. 8); Parameterlisten; Geschichte der
Standpose.

### 7.3.2 Anbindung des Onboard-Reglers

**Leitfragen**
- L7.21 Wie werden dieselben Bedienbefehle wie in der Simulation auf die Dienste des Onboard-Reglers abgebildet?
- L7.22 Welche Vorbedingungen prüft die Anbindung, bevor der Roboter gehen darf?
- L7.23 Wie ist sichergestellt, dass ein Halt-Befehl auch dann durchkommt, wenn gerade ein anderer Aufruf läuft?
- L7.24 Wie bleibt der angezeigte Zustand mit dem tatsächlichen Zustand des Roboters abgeglichen?

**Kerninhalte** (Doku `30-T` „loco_client“, `51-T`, `50-A` Abschnitt E; Code `g1pilot/navigation/loco_client.py`,
`ground_contact.py`)
- Dünne Schicht um die Herstellerbibliothek; bildet Bedienbefehle auf Fernaufrufe ab (T7.3, Kann).
- Greift beim Start nicht in den Roboterzustand ein.
- Bodenkontakt vor dem Gehen: aus der Last an den Kniemotoren, weil der vom Roboter gemeldete Modus am Kran nicht
  zwischen hängend und stehend unterscheidet.
- Totmann und Zeitüberwachung: Fahrbefehle nur bei frischem Befehlsstrom, sonst einmaliger Halt.
- Halt-Befehle laufen in einer eigenen Ausführungsgruppe und überholen blockierende Aufrufe.
- Zyklischer Abgleich mit der Zustandsmaschine des Roboters, Ergebnis als Zustandsmeldung für Oberfläche und Smartphone.
- Stufen Stopp / Not-Halt / Voll-Notaus: nur die Wirkung auf die Beine, Definition und Werte in 6.3.

**Belegbedarf**
- Anfrage-Antwort-Schnittstelle des SDK → UnitreeSDK2Py.01 (abgedeckt).
- Zustandsnummern und Dienste des Onboard-Reglers → Kap. 2.3.2 (`sec:g1_onboard`, noch nicht geschrieben); **offen**,
  Herstellerdoku als PDF nötig (E5). Bis dahin im Text ohne Nummern („Vorbereitungs-“, „Geh-Zustand“).
- Abschalten führt beim Zweibeiner zum Sturz → `Abschnitt~\ref{sec:sicherheit_zweibeiner}` (abgedeckt).

**Darstellungen:** T7.3 (Kann). Sonst Verweis auf `tab:schutzmechanismen`.
**Nicht hinein:** der beobachtete Linksdrall beim Gehen (offener Befund → 8.1.2 bzw. 8.5.3), alter Joystick-Modus.

### 7.4.1 Regelkette und inverse Kinematik

**Leitfragen**
- L7.25 Welche Verarbeitungsschritte durchläuft ein Armsollwert in jedem Regeltakt, und in welcher Reihenfolge?
- L7.26 Warum sind Regeltakt, inverse Kinematik und Bahnplanung auf drei Prozesse verteilt?
- L7.27 Wie ist die inverse Kinematik gegenüber dem Grundverfahren aus 4.2.1 ausgeprägt (Dämpfung, Nullraum,
  Abbruch)?
- L7.28 Wie übernimmt der Armregler die Arme vom Onboard-Regler und gibt sie zurück, ohne dass die Arme springen?
- L7.29 Was geschieht mit Armen und Taille bei einem Not-Halt?

**Kerninhalte** (Doku `20-T` bis „Positionsspeicher“, `24-T`, `50-A` Abschnitt E, `51-T`; Code
`g1pilot/manipulation/arm_controller.py` (3954 Zeilen, Einstieg `main_loop`), `ik_servo_process.py`,
`utils/ik_solver.py`, `waist_hold.py`, `waist_yaw.py`)
- Regeltakt 250 Hz. Zwei Wege zu einem Gelenkziel: reaktives Nachführen (Ziel aus Marker, Gamepad, Oberfläche) und
  geplante Bewegung (7.4.3).
- Feste Reihenfolge je Takt (B7.7): Zielkonfiguration nach Betriebsart → Gelenkgeschwindigkeit begrenzen und glätten
  → kartesische Geschwindigkeit begrenzen → Beschleunigung begrenzen (real) → Kollisionsüberwachung (7.4.2) →
  Schleppfehler begrenzen (real) → Schreiben mit Schwerkraft-Vorsteuerung.
- Prozessaufteilung: Eine IK-Lösung dauert länger als ein Regeltakt, und Python führt Threads nicht gleichzeitig aus;
  deshalb IK und Planer in eigenen Prozessen. Der Takt verwendet das zuletzt gelieferte Gelenkziel und fährt es mit
  allen Begrenzern an. Ergebnisse aus überholten Aufträgen werden über Zähler verworfen.
- IK: gedämpfte Pseudoinverse mit an die Nähe zur Singularität angepasster Dämpfung, Nullraum-Term zu einer Ruhehaltung
  (Ellbogen), Begrenzung des Ziels auf die Reichweite, vorzeitiger Abbruch am Fixpunkt. Seiten ohne neues Ziel werden
  ohne IK exakt gehalten.
- Eine einzige Stelle entscheidet, ob eine Bewegung starten darf (Not-Halt, Freigabe, Grundstellung, Gehen, laufende
  Planung); alle Eingänge nutzen sie.
- Übernahme: gemessene Armstellung merken, genau diese kommandieren, Gewicht von 0 auf 1 rampen (real über eine
  Rampenzeit, Simulation sofort). Rückgabe: zuerst geplant in die gemerkte Stellung des Onboard-Reglers fahren, dann
  Gewicht auf 0 rampen. Gilt auch beim Programmende.
- Not-Halt: Gewicht bleibt 1, Arme drehmomentfrei mit Dämpfung, damit der Onboard-Regler die Arme nicht aktiv in
  seine Grundhaltung fährt. Freigabe erst nach Quittieren und erneutem Aktivieren.
- Taille: Das Gewicht schaltet am G1 auch die Taille um; der Armregler hält sie deshalb real mit. Die Hüftdrehung
  setzt nur das Ziel der Hochachse (ein bis zwei Sätze).
- Real gelten Obergrenzen für Verstärkungen, Rampenzeiten und Geschwindigkeiten unabhängig von der Parametrierung.

**Belegbedarf**
- Gedämpfte kleinste Quadrate, Singularität, Nullraum → `Abschnitt~\ref{sec:ik}` (abgedeckt: Aristidou2009,
  DSouza2001, Kucuk2006).
- Starrkörperbibliothek → Carpentier2019 (abgedeckt).
- Schnittstelle `arm_sdk` und Überblendgewicht des Herstellers, Wirkung auf die Taille → `Abschnitt~\ref{sec:g1_armsdk}`
  (Kap. 2 offen) → **offen** (E5).
- Reduzierte Geschwindigkeit als Schutzfunktion → `Abschnitt~\ref{sec:schutzfunktionen}` und 6.3.2 (abgedeckt dort).

**Darstellungen:** B7.7 (Kern), G7.8 (Kann).
**Nicht hinein:** Messwerte zu Rechenzeit und Ruckeln (→ 8.2.1/8.2.3), Filterkonstanten, Zustandsvariablen des Codes,
Rückmeldeformat der Marker.

### 7.4.2 Kollisionsmodell und Laufzeitüberwachung

**Leitfragen**
- L7.30 Wie entsteht das Kugelmodell der Arme und Hände selbsttätig aus den Kollisionsnetzen, und wie fein ist es?
- L7.31 Wie werden Abstände zwischen Roboter und Umgebung so berechnet, dass Planer und Überwachung sie in jedem Takt
  nutzen können?
- L7.32 Wie reagiert die Laufzeitüberwachung auf einen Schritt, der zu nah an ein Objekt führt?
- L7.33 Wie wird die Kollision des Roboters mit sich selbst geprüft?
- L7.34 Wie wird gewolltes Berühren (Greifen, Aufsetzen der Hand) von ungewolltem unterschieden?

**Kerninhalte** (Doku `20-T` „Kugelmodell“, „Laufzeit-Gate“, `25-T` „Kollision“; Code
`g1pilot/manipulation/arm_geometry.py` (618 Zeilen), `arm_controller.py` `_apply_collision_gate`, `utils/ik_solver.py`
Zeilen ca. 247–350; Daten `Bachelorarbeit/Daten/kugelmodell/`)
- Erzeugung beim Start: Oberflächen der Kollisionsnetze abtasten (Eckpunkte und Dreiecksflächen), Punkte clustern,
  je Cluster eine Kugel, deren Radius alle Punkte einschließt.
- Drei Auflösungen: fein für Abstände zur Umgebung, grob für Arm gegen Arm im Planer, Körperkugeln für Rumpf und
  Beine (T7.4, Kann; Werte aus dem Code).
- Umgebung als orientierte Quader aus dem gemeinsamen Weltmodell (7.2.3); vorzeichenbehafteter Abstand jeder Kugel zu
  jedem Quader mit Gradient; Vorauswahl der erreichbaren Objekte.
- Vorwärtskinematik der Armketten für viele Konfigurationen gleichzeitig.
- Laufzeitüberwachung je Takt für beide Wege (reaktiv und geplant): Ein Kugel-Objekt-Paar unter seiner Untergrenze
  darf sich nicht weiter nähern; der verletzende Anteil des Schritts wird herausprojiziert (G7.9), die Hand gleitet
  an der Fläche entlang. Annäherung wird verlangsamt.
- Greifbare Objekte sind für Handkugeln freigegeben, für Armkugeln nicht; die Hand darf aufsetzen.
- Selbstkollision: exakte Prüfung der konvexen Hüllen mit Sicherheitsabstand; harte Verletzung hält an, im Randband
  ist nur Herausfahren erlaubt.
- Das Modell gilt auch für ausgetauschte Hände (Verweis 7.5.2), `fig:kugelmodell` zeigt beide Fälle.

**Belegbedarf**
- Hüllkörper, Kugelnäherung, Abstandsbibliotheken → `Abschnitt~\ref{sec:kollision_sdt}` (abgedeckt: Hubbard1996,
  Pan2012, LaValle2006).
- Clusterverfahren (k-Means) → Lloyd1982, neu in `_Vorschläge` (I: `GS2D6G9F`) → **offen bis Freigabe**; sonst das
  Verfahren ohne Namen beschreiben.
- Bibliothek für die exakte Prüfung (coal, Nachfolger von hpp-fcl) → **offen**; Pan2012 belegt nur FCL. Die
  Verwandtschaft braucht eine Quelle (Suchhinweis: Dokumentation bzw. Veröffentlichung der coal-/hpp-fcl-Bibliothek),
  sonst nur „eine Kollisionsbibliothek für konvexe Körper“.

**Darstellungen:** B7.8 = vorhandene `Bilder/tikz/kugelmodell-haende-3d.tex` (Kern, fertig), T7.4 (Kann), G7.9.
**Nicht hinein:** Überdeckungsfehler in mm (→ 8.2.3), Kugelanzahl als Messergebnis formulieren (ist Auslegung, ok).

### 7.4.3 Bahnplaner

**Leitfragen**
- L7.35 Welche Anforderung an den Abstand unterscheidet den Planer von einem Planer mit konstantem Sicherheitsabstand,
  und wie ist sie formuliert?
- L7.36 Aus welchen Kostenanteilen besteht das Optimierungsproblem, und wie wird es gelöst?
- L7.37 Was geschieht, wenn die Optimierung keine gültige Bahn findet?
- L7.38 Wie wird aus der geometrischen Bahn eine zeitlich abfahrbare Bewegung?
- L7.39 Wie wird die Planung in den Regelbetrieb eingebunden, ohne ihn zu stören, und wie werden Abbrüche behandelt?

**Kerninhalte** (Doku `20-T` „arm_planner.py“, „Planer-Prozess“, „Positionsspeicher“; Code
`g1pilot/manipulation/arm_planner.py` (805 Zeilen; Voreinstellungen ab Zeile ca. 80, Abstandsbedarf ab ca. 250),
`arm_planner_process.py`, `arm_controller.py` `_start_planned_motion`, `_poll_plan_result`)
- Leitidee: in der Bahnmitte Abstand, an Start und Ziel darf es eng werden. Abstandsbedarf je Kugel, Objekt und
  Bahnpunkt als stetige Funktion (G7.6): „Trichter“ um Start und Ziel.
- Optimierung im Gelenkraum über Stützpunkte: Kosten aus Glattheit, Weglänge der Hand, Strafe für unterschrittenen
  Bedarf (Umgebung, Körper, Arm gegen Arm) und Anfahrrichtung (G7.7). Schritte mit der inversen Glattheitsmatrix
  vorkonditioniert, Schrittweitensteuerung, Strafgewicht wird stufenweise erhöht.
- Anfahrrichtung: nahe an einem Hindernis kommt die Hand entlang ihrer Achse an, ersatzweise von oben.
- Rückfallkette (B7.10): Gerade im Gelenkraum → Optimierung aus mehreren Startbahnen → stichprobenbasierter Planer
  als Startbahn mit anschließender Glättung → verringerter Abstand. Ziel in Kollision wird abgelehnt.
- Abschlussprüfung: dichte Nachabtastung mit dem Kugelmodell und exakte Selbstkollisionsprüfung.
- Zeitparametrierung: Grenzen für Geschwindigkeit und Beschleunigung im Gelenkraum und kartesisch, langsamer nahe an
  Objekten.
- Beide Arme werden gemeinsam geplant (7 oder 14 Freiheitsgrade) und über eine gemeinsame Bahnuhr abgefahren, die
  nur läuft, solange der Sollwert der Bahn folgt.
- Einbindung: eigener Prozess mit Rechenzeitbudget; Ergebnisse überholter Anfragen werden verworfen (Abbruch durch
  Not-Halt, neue Eingabe, Deaktivieren).
- Nutzer der geplanten Bewegung: gespeicherte Posen, Abläufe, Arm-API, Rückgabe an den Onboard-Regler, Weg in die
  Lauf-Pose (je ein Halbsatz mit Verweis).

**Belegbedarf**
- Optimierungsbasierte Planung, Glattheit gegen Hindernisse, lokale Minima → `Abschnitt~\ref{sec:bahnplanung_sdt}`;
  Zucker2013.01–.05 (abgedeckt). Vorkonditionierung mit der Glattheitsmetrik → **teilweise**: Beleg aus
  `sources-text/Zucker2013.txt` ergänzen (AP 1).
- Zwei aufeinander zu wachsende Bäume → Kuffner2000.01, .04 (abgedeckt).
- Zeitparametrierung → Kunz2012.01, Pham2018 (abgedeckt); der eigene Ansatz ist einfacher, das klar sagen.
- Schrittweitensteuerung (Vertrauensbereich, Rückschritt) → Nocedal2006, neu in `_Vorschläge` (`E7RGUNWK`), nur falls
  die Begriffe im Text fallen; sonst weglassen.
- Abgrenzung zu MoveIt/OMPL gehört nach 6 bzw. 8.5.2, nicht hierher.

**Darstellungen:** B7.9 (Kern), B7.10 (Kern), G7.6, G7.7.
**Nicht hinein:** Planungszeiten und Erfolgsquoten (→ 8.2.3), alle Voreinstellungen (→ Anhangtabelle).

### 7.5.1 Schnittstelle der Inspire-Hände

**Leitfragen**
- L7.40 Wie spricht die übrige Software die Hand an, unabhängig davon, ob sie simuliert oder real ist?
- L7.41 Wie werden die sechs Antriebe der Hand auf die Gelenke des Modells abgebildet?
- L7.42 Wie sind Kraftmessung, Kraftbegrenzung und Tastzonen in der Simulation nachgebildet?
- L7.43 Wie wird die reale Hand angebunden, und was geschieht bei einem Not-Halt?

**Kerninhalte** (Doku `22-T`; Code `g1pilot/manipulation/inspire_ftp/` mit `bridge.py`, `backends.py`,
`joint_map.py`, `tactile.py`, `model.py`, `modbus_client.py`; MuJoCo-Seite in `unitree_sdk2py_bridge.py`
`HandCmdHandler`)
- Eine Schnittstelle (Befehle, Zustandsmeldung, Gelenkzustände für die Anzeige), drei Anbindungen (T7.5): nur
  Anzeige, Kontaktphysik in MuJoCo, reale Hand über Modbus TCP.
- Abbildung sechs Antriebe → zwölf Gelenke je Hand an einer Stelle; Wertebereich wie im Register der realen Hand.
- Simulation: Finger als Positions-Aktoren; Tastzonen aus Berührungssensoren an den Sensorflächen des Modells;
  Kraft je Finger als Summe seiner Zonen.
- Kraftbegrenzung in der Simulation: Über der Grenze öffnet der Finger proportional zur Überschreitung, die erreichte
  Stellung wird gehalten, bis ein neuer Griff oder das Öffnen kommt (verhindert Dauerschwingung).
- Real: zyklisches Lesen von Winkel, Kraft und Tastzonen in eigenem Thread.
- Not-Halt: keine neuen Sollwerte, Stellung halten, Wiederaktivierung nur bewusst.
- Fingerstellungen werden mit Armposen gespeichert (Verweis 7.6.1).

**Belegbedarf**
- Aufbau, Antriebe, Sensoren, Schnittstellen der Hand → `Abschnitt~\ref{sec:haende_sdt}`; Inspire2024.01–.05
  (abgedeckt). Register, Wertebereich 0–1000, Krafteinheit → **teilweise**: im Handbuch suchen (AP 1).
- Kraftbegrenzung und Schlupf → Romeo2020 über 4.2.4 (abgedeckt).
- Positions-Aktoren, Berührungssensoren → MujocoDoku2026b.02, MujocoDoku2026a.08 (abgedeckt).
- Modbus TCP als Protokoll → **offen**; nur nennen (das Handbuch nennt die Schnittstelle), nicht erklären.

**Darstellungen:** T7.5 (Kern).
**Nicht hinein:** Registeradressen, entfernte Browser-Oberflächen.

### 7.5.2 Austauschbare Hand-Profile

**Leitfragen**
- L7.44 Was muss ein Nutzer liefern, um eine eigene, gedruckte Hand in der Simulation zu verwenden?
- L7.45 Wie entstehen daraus übereinstimmende Modelle für Physik, Kinematik und Kollisionsprüfung?
- L7.46 Wie ist die Montage am Handgelenk festgelegt, damit linke und rechte Hand spiegelgleich sind?
- L7.47 Welche Teile der Umgebung müssen von der Wahl der Hand erfahren?

**Kerninhalte** (Doku `25-T`, `25-A`; Code `unitree_mujoco/unitree_robots/g1/tools/gen_hand_profile.py`,
`hand_adjust.py`, `g1pilot/utils/hand_profile.py`; Beispielprofil `unitree_robots/g1/hands/haken/`)
- Hand-Profil = Beschreibungsdatei plus Netzgeometrie. Ein Generator erzeugt Robotermodell für die Physik, Modell
  für Kinematik und Anzeige, Kollisionsteile und Szene.
- Bezugssysteme: Flansch am letzten Handgelenkglied, Hand-Koordinatensystem, Werkzeugpunkt; Abbildung der
  Netzkoordinaten ins Handgelenk (G7.10, Kann).
- Kollision: Zerlegung in konvexe Teile, weil ein Netz sonst nur als eine konvexe Hülle kollidiert; dieselben Teile
  speisen Physik, Selbstkollisionsprüfung und Kugelmodell des Planers.
- Masse aus dem Profil, Trägheit aus dem Netz; der Standregler lädt das passende Modell für den Schwerpunkt.
- Prüfsumme über die Eingaben entscheidet, ob neu erzeugt wird.
- Nur Simulation; real bleibt die Wahl wirkungslos.
- Beispiel: gedruckter Haken für Kisten (`fig:kugelmodell` b).

**Belegbedarf**
- Selbst gedruckte, quelloffene Hände als Stand der Technik → 4.2.4; Ma2017 freigegeben, aber ohne PDF → **offen**.
- Konvexe Zerlegung → Mamou2009 (**offen**, wie 7.2.3).
- Masse des Hakens (0,15 kg) ist nur geschätzt → `\pruefen{}` (Nils wiegt).

**Darstellungen:** B7.11 (Kann).
**Nicht hinein:** Bedienung des Justierwerkzeugs, Dateilisten.

### 7.6 Bedienwege (Einleitung vor 7.6.1)

Ein Absatz plus T7.6: gemeinsames Prinzip aller Bedienwege. Jeder Bedienweg erzeugt nur Befehle auf den vorhandenen
Themen; Bewegungslogik und Schutzmechanismen liegen in den Zielprogrammen (Armregler, Fortbewegung, Hände) und
lassen sich von keinem Bedienweg umgehen. Verweis auf `tab:bedienwege` (6.4.2) für den Funktionsumfang.

### 7.6.1 Demo-Oberfläche

**Leitfragen**
- L7.48 Wie ist die Oberfläche von der Bewegungslogik getrennt?
- L7.49 Wie bleiben Oberfläche, Gamepad und Smartphone über Betriebsart, Handauswahl und Geschwindigkeit einig?
- L7.50 Wie sind Posen, relative Bewegungen und Abläufe gespeichert, und wie wird ein Ablauf abgearbeitet?
- L7.51 Worin unterscheidet sich das Verhalten der Oberfläche in Simulation und Realbetrieb?

**Kerninhalte** (Doku `10-T`, `23-T`, `40-T` „Auto-Start“; Code `g1pilot/teleoperation/demo_gui.py`, `gui_base.py`,
`shared_state.py`, `sequence_runner.py`, `sim_autostart.py`, `manipulation/pose_store.py`)
- Oberfläche rechnet keine Bewegung; sie sendet Befehle und zeigt Zustände.
- Gemeinsamer Bedienzustand als gehaltene Zustandsmeldung mit Zeitstempel je Feld; der neueste Stand gilt.
- Posenspeicher: versionierte Datei mit Posen (Arme, Finger), relativen Bewegungen und Abläufen als Folge von
  Verweisen; Schreiben atomar. Gespeichert wird der kommandierte, nicht der gemessene Stand.
- Ablaufsteuerung als Zustandsautomat ohne Abhängigkeit von Oberfläche oder ROS: am Stück oder Schritt für Schritt;
  jeder Schritt ist eine geplante Bewegung (7.4.3) mit Rückmeldung.
- Simulation: selbsttätiges Aktivieren nach dem Start mit Quittung; real: keine Bewegung ohne Eingabe.
- Anzeige des Roboterzustands (Onboard-Modus, Bodenkontakt, Temperaturen, Akku) in einem Satz.

**Belegbedarf**
- Bedienung durch Nutzer ohne Robotikerfahrung, grafische Abläufe → `Abschnitt~\ref{sec:laienbedienung_sdt}`
  (abgedeckt: Ajaykumar2021, Pot2009).
- Gehaltene Zustandsmeldungen (QoS „transient local“) → `Abschnitt~\ref{sec:ros2}`; Macenski2022 (abgedeckt).

**Darstellungen:** B7.12 (Kern, Bildschirmfoto von Nils, E7).
**Nicht hinein:** Beschreibung der Knöpfe, offene Punkte der Doku.

### 7.6.2 Gamepad

**Leitfragen**
- L7.52 Wie wird aus Knüppelausschlägen ein Ziel für die Hand?
- L7.53 Wie erkennt die Software eine abgerissene oder eingefrorene Funkverbindung?
- L7.54 Wie ist verhindert, dass der Roboter beim Bewegen der Hände losläuft?

**Kerninhalte** (Doku `11-T`; Code `g1pilot/teleoperation/ps4_joystick.py`, `ps4_layout.py`, `ps4_arm_teleop.py`,
`ps4_walk.py`, `hand_jog.py`)
- Schichten: Geräteschicht bildet zwei Gerätefamilien auf eine feste Belegung ab; reine Bedienlogik ohne ROS
  (testbar); Programme, die Ziele senden.
- Tippbetrieb: Ziel = aktuelle Hand + Geschwindigkeit × Vorlauf, im Bezug des Oberkörpers; beim Loslassen Halteziel.
- Totzone und progressive Kennlinie; Gehen nur bei gehaltenem Zustimmtaster auf eigenem Befehlsweg.
- Zeitüberwachungen: fehlende Eingaben und eingefrorene Funkstrecke führen zum Halt (Werte in `tab:schutzmechanismen`).
- Not-Halt und Voll-Notaus am Gerät, wirken auch im gesperrten Zustand.

**Belegbedarf:** Zustimmeinrichtung als Begriff → `Abschnitt~\ref{sec:schutzfunktionen}` (abgedeckt). Teleoperation
mit Standardgeräten → `Abschnitt~\ref{sec:teleoperation_teil}` (Leitfrage 13 in Kap. 4 war offen; nur verweisen, wenn
dort belegt).
**Darstellungen:** keine eigene; B7.13 zeigt den Signalweg.
**Nicht hinein:** Tastenbelegung (höchstens Anhang), Treibervarianten, LED und Vibration.

### 7.6.3 Smartphone

**Leitfragen**
- L7.55 Über welchen Weg erreicht das Smartphone die Umgebung, ohne dass eine App oder ein Netzwerkzugang nötig ist?
- L7.56 Wie ist sichergestellt, dass nur ein gekoppeltes Gerät Befehle absetzen kann und Befehle nicht wiederholt
  werden können?
- L7.57 Wie werden Rechte und Steuerhoheit durchgesetzt, und was geschieht bei Funkabriss?

**Kerninhalte** (Doku `12-T`; Code `g1pilot/teleoperation/phone/` mit `ble_server.py`, `gateway.py`, `protocol.py`,
`link.py`, `web/`)
- Webseite im Browser des Smartphones, Verbindung über Bluetooth Low Energy direkt zum Bedienrechner.
- Kopplung über einen angezeigten Code, daraus Geräteschlüssel; je Sitzung ein Sitzungsschlüssel; jede Zeile mit
  Zähler und Prüfcode (Inhalte lesbar, aber nicht fälschbar und nicht wiederholbar).
- Vermittlungsschicht prüft je Aktion Rolle, Steuerhoheit und Aktualität des Zustands und ruft dann dieselben
  Funktionen wie die Oberfläche auf. Not-Halt ist immer erlaubt.
- Herzschlag und Zeitgrenzen (Werte in `tab:schutzmechanismen`).

**Belegbedarf**
- Schlüsselabhängiger Prüfcode (HMAC) → Krawczyk1997 (RFC 2104), neu in `_Vorschläge` (`I3N3R8MP`) → **offen bis Freigabe**.
- Bluetooth Low Energy, GATT → **offen** (Suchhinweis: Bluetooth Core Specification); nur nennen, nicht erklären.

**Darstellungen:** keine eigene (Kann: Bildschirmfoto der Handy-Seite neben B7.12).
**Nicht hinein:** Paketformat, Seitenaufteilung der Übertragung, Versionierung der Webseite.

### 7.6.4 Entwickler-Oberfläche und Arm-API

**Leitfragen**
- L7.58 Über welche Schnittstellen kann fremde Software die Arme bewegen, und welche Schutzmechanismen gelten dabei?
- L7.59 Wie ist das Befehlsformat aufgebaut, und welche Zustände durchläuft ein Auftrag?
- L7.60 Wie kann ein Projekt, das den G1 bereits direkt anspricht, die Simulation nutzen?

**Kerninhalte** (Doku `21-T`, `21-A`, `20-T` „Reaktives Servoing“; Code `g1pilot/manipulation/arm_api.py`,
`arm_command.py`, `interactive_marker.py`, `examples/arm_api/`)
- Drei Ebenen (Verweis auf das Ebenenmodell in 6.5.1): Zielmarker in der 3D-Anzeige; HTTP-Schnittstelle mit JSON;
  direkter DDS-Zugang zur Simulation.
- HTTP-Brücke als eigenes Programm ohne Regellogik; Format wird an einer Stelle geprüft, die auch der Armregler nutzt.
  Auftragsarten: Gelenkwinkel, kartesische Pose, Spiegeln; Zustandsfolge angenommen → ausgeführt → erreicht /
  abgelehnt / fehlgeschlagen / abgebrochen.
- Schutz: alle Prüfungen liegen im Armregler; Bindung an den lokalen Rechner, Zugriff von außen nur mit Kennwort.
- Direkter DDS-Zugang umgeht Armregler und Schutzmechanismen (ausdrücklich so benennen).

**Belegbedarf:** Zielmarker stammen aus der Ausgangsbasis → HucebotG1Pilot.01 und 6.1 (abgedeckt). Sonst Eigenleistung.
**Darstellungen:** B7.13 (Kern, gemeinsam für 7.6).
**Nicht hinein:** Endpunktliste, HTTP-Codes, Beispielaufrufe (höchstens Anhang).

### 7.7 Navigation in der Simulation

**Leitfragen**
- L7.61 Welche Teile der Navigation sind übernommen, und was wurde für die Einbindung ergänzt?
- L7.62 Woher kommen Karte und Position, wenn keine Umgebungserfassung vorhanden ist?
- L7.63 Wie wird der selbsttätige Fahrbefehl mit der manuellen Bedienung zusammengeführt?

**Kerninhalte** (Doku `31-T`; Code `g1pilot/navigation/dijkstra_planner.py`, `nav2point.py`, `create_map.py`,
`sim_localization.py`, `teleoperation/joy_mux.py`; Anteil übernommenen Codes laut `g1pilot/NOTICE.md`)
- Planer und Pfadfolger stammen aus der Ausgangsbasis; ergänzt: Karte aus dem gemeinsamen Weltmodell, Position aus
  dem Simulationszustand, Stationen als Ziele, Zielanfahrt nahe an Tischen.
- Der Pfadfolger erzeugt Befehle wie ein Bediengerät; ein Umschalter wählt zwischen manuell und selbsttätig.
- Nur Simulation; real fehlt die Umgebungserfassung (Verweis 8.5.3).

**Belegbedarf:** HucebotG1Pilot.04 (abgedeckt). Kürzeste-Wege-Suche → Dijkstra1959, neu in `_Vorschläge`
(`QDDK4KV2`), nur falls der Name fällt.
**Darstellungen:** keine.

---

## 4 Abbildungen, Tabellen, Gleichungen

Alle Grafiken mit `ba-grafik.tex` (TikZ `[ba]`, nie skalieren), Ablage `Bilder/tikz/<name>.tex`, eigene Darstellung
ohne Quellenangabe. Jede wird im Absatz davor mit `\ref` eingeführt und danach erläutert.

| Nr. | Label | Abschnitt | Stufe | Art und Inhalt | Datei |
|---|---|---|---|---|---|
| B7.1 | `fig:verteilung` | 7.1 | Kern | Blockbild: Host, Container, Prozesse; links Simulation, rechts Realbetrieb (`ba trenner`, Teilbilder a/b); Kanäle DDS (mit Domain), ROS 2, UDP, HTTP, Bluetooth, Modbus als unterschiedliche Linienarten | `verteilung-container.tex` |
| B7.2 | `fig:bridge` | 7.2.1 | Kern | Signalfluss: zwei Befehlswege → Überblendung → PD-Gesetz → Aktoren MuJoCo; Rückweg Sensoren → Zustandsnachrichten; Zusatzgrößen gestrichelt | `bridge-signalfluss.tex` |
| B7.3 | `fig:lockstep` | 7.2.2 | Kern | Zeitablauf über zwei Regelschritte: Zustand → Regler rechnet → Befehl → 20 Physikschritte; Echtzeitgrenze und Zeitüberwachung eingezeichnet | `lockstep-zeitablauf.tex` |
| B7.4 | `fig:szene` | 7.2.3 | Kann | Bildschirmfotos: Arbeitsplatz-Szene in MuJoCo und dasselbe Weltmodell in der 3D-Anzeige (von Nils) | `Bilder/` |
| B7.5 | `fig:ersatzregler_zustaende` | 7.3.1 | Kern | Zustandsdiagramm: Bereitschaft, Stehen, Gehen, Dämpfen; Abfangen als Schleife; Übergänge beschriftet mit Auslöser; selbsttätige Übergänge in `baAkzent` plus gestrichelt | `ersatzregler-zustaende.tex` |
| B7.6 | `fig:standregler` | 7.3.1 | Kann | Regelstruktur: IMU-Neigung → Momente Knöchel/Hüfte; Schwerpunktmodell → Beckenverschiebung; Nachführung aus Knöchelmoment | `standregler-struktur.tex` |
| B7.7 | `fig:regelkette` | 7.4.1 | Kern | Verarbeitungskette je Takt als Blockfolge; darüber die drei Prozesse (Regeltakt, IK, Planer) als `ba gruppe`; Blöcke „nur real“ markiert | `armregler-regelkette.tex` |
| B7.8 | `fig:kugelmodell` | 7.4.2 | Kern | **fertig:** Kugelmodell Inspire-Hand und Haken | `kugelmodell-haende-3d.tex` |
| B7.9 | `fig:trichter` | 7.4.3 | Kern | a) Skizze: Bahn der Hand von Tisch zu Tisch mit Trichtern um Start und Ziel; b) pgfplots: Abstandsbedarf über dem Abstand zum näheren Endpunkt für zwei Fälle (Endpunkt frei, Endpunkt in Berührung), aus G7.6 berechnet, CSV in `Daten/` | `planer-trichter.tex` |
| B7.10 | `fig:rueckfallkette` | 7.4.3 | Kern | Ablaufdiagramm der Rückfallstufen bis Abschlussprüfung und Zeitparametrierung | `planer-rueckfallkette.tex` |
| B7.11 | `fig:handprofil` | 7.5.2 | Kann | Ablauf: Profil (Beschreibung + Netz) → Generator → vier Ergebnisse → Nutzer (Physik, Kinematik, Planer, Standregler) | `handprofil-ablauf.tex` |
| B7.12 | `fig:demo_gui` | 7.6.1 | Kern | Bildschirmfoto der Demo-Oberfläche mit beschrifteten Bereichen (von Nils) | `Bilder/` |
| B7.13 | `fig:bedienwege_signal` | 7.6 | Kern | Blockbild: Eingabegeräte → Bedienprogramme → gemeinsame Befehlsthemen → Zielprogramme mit Schutzmechanismen → Roboter; fremde Software über HTTP und DDS | `bedienwege-signalfluss.tex` |

Prüfen, ob `Bilder/tikz/teleoperation-architektur.tex` (für 4.3.1 gebaut, bisher nicht eingebunden) als Vorlage für
B7.13 taugt.

| Nr. | Label | Abschnitt | Stufe | Inhalt | Stil |
|---|---|---|---|---|---|
| T7.1 | `tab:container` | 7.1 | Kern | Abbild · Basis · Inhalt · Profil · läuft in Sim/Real | Gitter |
| T7.2 | `tab:policies_einbindung` | 7.3.1 | Kern | Policy · Herkunft (Verweis `tab:policies`) · Beobachtungen · Aktionen · Arme beim Gehen · Abfang-Policy | Gitter |
| T7.3 | `tab:loco_abbildung` | 7.3.2 | Kann | Bedienbefehl · Wirkung Simulation · Wirkung Realbetrieb | Gitter |
| T7.4 | `tab:kugelmodell` | 7.4.2 | Kann | Modellstufe · Zweck · Anzahl Kugeln · größter Radius | schlicht |
| T7.5 | `tab:hand_anbindungen` | 7.5.1 | Kern | Anbindung · Fingerbewegung · Kraft/Tastsinn · Einsatz | Gitter |
| T7.6 | `tab:bedienwege_umsetzung` | 7.6 | Kern | Bedienweg · Eingabegerät/Transport · Schnittstelle zum System · Zeitüberwachung (Verweis) | Gitter |
| TA.1 | `tab:quelltext` | Anhang | Kern | Abschnitt · Funktionsbezeichnung im Text · Programm/Datei im Repository | Gitter, `xltabular` |
| TA.2 | `tab:parameter` | Anhang | Kann | Parameter · Wert · Bedeutung · Fundstelle | schlicht, `xltabular` |

| Nr. | Abschnitt | Inhalt (in AP 2 gegen den Code prüfen, Vorzeichen und Bezeichner!) |
|---|---|---|
| G7.1 | 7.2.1 | Stellmoment je Gelenk: Vorsteuermoment + Steifigkeit × Lagefehler + Dämpfung × Geschwindigkeitsfehler |
| G7.2 | 7.2.1 | Überblendung der Armmomente mit Gewicht w zwischen beiden Befehlswegen (Code: `bridge.py:444`) |
| G7.3 | 7.2.2 | Physikschritte je Regelschritt N = Regelperiode / Physikschritt |
| G7.4 | 7.3.1 | Momente des Standreglers an Knöchel und Hüfte aus Neigung und Drehrate |
| G7.5 | 7.3.1 | Gelenksollwert = Ausgangsstellung + Skalierung × Aktion |
| G7.6 | 7.4.3 | Abstandsbedarf mit Trichter (Gewicht über Glättungsfunktion, Boden, Bedarf) |
| G7.7 | 7.4.3 | Kostenfunktion des Planers als Summe der Anteile |
| G7.8 | 7.4.1 | Umrechnung der Glättungskonstante auf die tatsächliche Schrittweite (Kann) |
| G7.9 | 7.4.2 | Projektion des Schritts bei unterschrittener Untergrenze |
| G7.10 | 7.5.2 | Abbildung der Netzkoordinaten ins Handgelenk (Kann) |

Erwartet werden 7–8 Gleichungen im Text. Variablen direkt darunter erklären, Verweis als `Gleichung~\ref{}`.

---

## 5 Quellen

### 5.1 Vorhandene, freigegebene Quellen mit Belegen (Stand `evidence/` 16.11.)

| Key | Belege | Verwendung in Kap. 7 |
|---|---|---|
| UnitreeMujoco | 9 | 7.2.1 (Basis der Simulation, Nachrichten, Domain/Loopback) |
| UnitreeSDK2Py | 5 | 7.3.2 (Anfrage-Antwort) |
| UnitreeRLMjlab | 7 | 7.3.1 (Herkunft Standard-Policy, ONNX) |
| HucebotG1Pilot | 4 | 7.1, 7.6.4, 7.7 (Ausgangsbasis) |
| Hu2026 | 2 | 7.3 (Onboard-Regler nicht quelloffen) |
| MujocoDoku2026 / a / b | 16 / 9 / 10 | 7.2.1–7.2.3, 7.5.1 (Aktoren, Zwangsbedingung, Zeitschritt, Kollisionsfilter, Sensoren) |
| Todorov2012 | 31 | 7.2.2 (über 3.2.2) |
| OMG2015, Macenski2022 | 12 / 16 | 7.1, 7.2.1, 7.6.1 (Domains, QoS; über 3.3) |
| Boettiger2015, Cervera2019, Struhar2020 | 11 / 12 / 8 | 7.1 (über 3.3.3) |
| Carpentier2019 | 2 | 7.3.1, 7.4.1 |
| Aristidou2009, DSouza2001, Kucuk2006 | 12 / 9 / 9 | 7.4.1 (über 4.2.1) |
| Hubbard1996, Pan2012, LaValle2006 | 2 / 2 / 7 | 7.4.2 (über 4.2.2) |
| Zucker2013, Kuffner2000, Schulman2014 | 5 / 4 / 3 | 7.4.3 |
| Kunz2012, Pham2018 | 3 / 2 | 7.4.3 (Zeitparametrierung) |
| Inspire2024, Romeo2020 | 5 / 4 | 7.5.1 |
| Westervelt2018 | 21 | 7.3.1 (über 4.1) |
| Ajaykumar2021, Pot2009 | 12 / 6 | 7.6.1 (über 4.3.2) |

Grundsatz: lieber `Abschnitt~\ref{}` auf Kap. 2–4 als dieselbe Quelle erneut zitieren. Ein eigenes Zitat in Kap. 7 nur
für die konkrete Eigenschaft, auf der eine Umsetzungsentscheidung beruht.

### 5.2 Belege, die aus vorhandenen PDFs noch zu ziehen sind (AP 1)

| Frage | Quelle | Abschnitt |
|---|---|---|
| Prüft MuJoCo Netze über ihre konvexe Hülle? | MujocoDoku2026 / a / b | 7.2.3, 7.5.2 |
| Wie beschreibt die Dokumentation Berührungssensoren (was wird gemessen)? | MujocoDoku2026a | 7.5.1 |
| Mit welcher Metrik bzw. Vorkonditionierung arbeitet CHOMP? | Zucker2013 | 7.4.3 |
| Lädt Pinocchio Modelle aus URDF und MJCF? Bietet es Kollisionsprüfung über eine Bibliothek an? | Carpentier2019 | 7.3.1, 7.4.2 |
| Welche Register, Wertebereiche und Einheiten (Winkel, Kraft, Kraftschwelle) nennt das Handbuch? Welches Protokoll über Ethernet? | Inspire2024 | 7.5.1 |
| Was sagt das README zum Python-Simulator (Aktoren, PD-Gesetz, Hilfsmittel wie elastisches Band)? | UnitreeMujoco | 7.2.1 |
| Welche Aussagen zu Discovery und Erreichbarkeit von Teilnehmern? | OMG2015 | 7.1 |

### 5.3 Lücken

| Lücke | Abschnitt | Stand |
|---|---|---|
| Herstellerdoku G1: `arm_sdk` mit Überblendgewicht (auch Taille), PD-Gesetz der Motorbefehle, Dienste und Zustandsnummern des Onboard-Reglers | 7.2.1, 7.3.2, 7.4.1 (und Kap. 2.3) | Seiten von support.unitree.com sperren automatische Abrufe → Nils druckt sie als PDF (E5). Wichtigste Lücke. |
| AGILE (Zhao 2026) | 7.3.1 | in `_Vorschläge` (`Q4ACNEZH`) mit PDF, wartet auf Freigabe |
| V-HACD (Mamou, Ghorbel 2009) | 7.2.3, 7.5.2 | in `_Vorschläge` (`95ZWHP4V`), PDF nur über FAU (IEEE) |
| Ma, Dollar 2017 (OpenHand) | 7.5.2 | freigegeben, PDF fehlt (IEEE, FAU) |
| Kollisionsbibliothek coal / hpp-fcl | 7.4.2 | keine Quelle; GitHub ist aus der Cloud nicht prüfbar. Suchhinweis, kein Vorschlag |
| Grafischer Szenen-Editor (fremdes Projekt, auf dem der eigene aufbaut) | 7.2.3 | keine Quelle; als Software-Eintrag mit README-PDF wie bei den anderen Repos (E5) |
| Bluetooth Low Energy / GATT, Modbus TCP | 7.6.3, 7.5.1 | keine Quelle; Empfehlung: nur nennen, nicht erklären, dann genügt je ein `\qf{}` oder ein Normdokument |
| Begriffe Knöchel-/Hüftstrategie | 7.3.1 | keine Quelle; Empfehlung: ohne die Begriffe schreiben |

### 5.4 Neue Vorschläge in Zotero `_Vorschläge` (16.11., Tag `Kap7-Recherche 2026-11-16`)

Metadaten je über Crossref geprüft, keine Duplikate, ohne Citation Key, ohne PDF. Alle vier sind **optional**: Sie
werden nur gebraucht, wenn der Name des Verfahrens im Text fällt.

| Vorschlag | DOI | frei verfügbar | Frage | warum |
|---|---|---|---|---|
| Lloyd 1982: Least squares quantization in PCM (IEEE Trans. Inf. Theory 28(2), 129–137) | 10.1109/TIT.1982.1056489 | nein → FAU (IEEE) | L7.30 | Ursprung des Clusterverfahrens, mit dem das Kugelmodell angepasst wird |
| Krawczyk, Bellare, Canetti 1997: HMAC, RFC 2104 | 10.17487/RFC2104 | ja (rfc-editor.org) | L7.56 | Prüfcode des Smartphone-Protokolls |
| Dijkstra 1959: A note on two problems in connexion with graphs (Numer. Math. 1, 269–271) | 10.1007/BF01386390 | über FAU (Springer) | L7.61 | Verfahren des übernommenen Pfadplaners |
| Nocedal, Wright 2006: Numerical Optimization (Springer) | 10.1007/978-0-387-40065-5 | nein → FAU (Springer) | L7.36 | Schrittweitensteuerung der Bahnoptimierung |

---

## 6 Daten und Experimente aus dem Repo G1

### 6.1 Datenbasis der Eigenleistung

| Abschnitt | Technik-Doku (`g1pilot/docs/`) | Code (Einstieg) |
|---|---|---|
| 7.1 | `02-T`, `03-A`, `04-T` | `g1pilot/docker-compose.yml`, `docker/`, `start.sh`, `g1_gui.py`, `launch/bringup_*.launch.py` |
| 7.2.1 | `02-T`, `30-T` (Bridge-Merge) | `unitree_mujoco/simulate_python/unitree_sdk2py_bridge.py`, `hold_base.py`, `g1pilot/utils/common.py` |
| 7.2.2 | `40-T` | `simulate_python/config.py`, `unitree_mujoco.py`, `g1pilot/navigation/loco_sim.py` |
| 7.2.3 | `40-T`, `31-T`, `scene_editor/README.md` | `scene_editor/build_env_scene.py`, `simulate_python/scene_*.py`, `navigation/scene_bridge.py` |
| 7.3.1 | `30-T` | `navigation/loco_sim.py`, `walk_policy.py`, `stand_balancer.py`, `com_model.py`, `policies/` |
| 7.3.2 | `30-T`, `51-T`, `50-A` (E) | `navigation/loco_client.py`, `ground_contact.py` |
| 7.4.1 | `20-T`, `24-T`, `51-T` | `manipulation/arm_controller.py`, `ik_servo_process.py`, `utils/ik_solver.py`, `waist_*.py` |
| 7.4.2 | `20-T`, `25-T` | `manipulation/arm_geometry.py`, `arm_controller.py` (`_apply_collision_gate`) |
| 7.4.3 | `20-T` | `manipulation/arm_planner.py`, `arm_planner_process.py` |
| 7.5.1 | `22-T` | `manipulation/inspire_ftp/` |
| 7.5.2 | `25-T` | `unitree_robots/g1/tools/gen_hand_profile.py`, `g1pilot/utils/hand_profile.py` |
| 7.6.1 | `10-T`, `23-T` | `teleoperation/demo_gui.py`, `shared_state.py`, `sequence_runner.py`, `manipulation/pose_store.py` |
| 7.6.2 | `11-T` | `teleoperation/ps4_*.py`, `hand_jog.py` |
| 7.6.3 | `12-T` | `teleoperation/phone/` |
| 7.6.4 | `21-T` | `manipulation/arm_api.py`, `arm_command.py`, `interactive_marker.py` |
| 7.7 | `31-T`, `NOTICE.md` | `navigation/dijkstra_planner.py`, `nav2point.py`, `create_map.py`, `sim_localization.py` |

Übernommen oder eigen? `g1pilot/NOTICE.md` nennt je Datei den Anteil aus der Ausgangsbasis. Wo ein Abschnitt
überwiegend Übernommenes beschreibt (7.7, Teile von 7.6.4, Grundgerüst von 7.3.2 und 7.4.1), muss der Text das sagen
und auf `tab:eigenleistung` in 6.1.3 verweisen.

### 6.2 Für Abbildungen zu erzeugen

- B7.9 b): kleines Skript, das G7.6 für zwei Fälle auswertet → `Daten/planer-trichter.csv` (reine Rechnung aus der
  Formel und den Voreinstellungen des Codes, kein Messwert).
- B7.8: vorhanden (`Daten/kugelmodell/`).
- T7.4: Kugelanzahlen und Radien aus `arm_geometry.py` bzw. `Daten/kugelmodell/kugeln.json`.
- Bildschirmfotos B7.4, B7.12: von Nils (E7).

### 6.3 Messwerte im Repo, die nach Kap. 8 gehören (für den Plan von Kap. 8 vormerken, **nicht** in Kap. 7)

Alle stehen nur in der Doku oder in Kommentaren; vor Verwendung muss Nils bestätigen, dass sie am festen Code-Stand
reproduzierbar sind (CLAUDE.md Regel 5).

- Gangbild je Policy (Soll-/Ist-Tempo, Schrittfrequenz, Schwankung), `30-T` „Gangbild“, Skript `test_agile_walk_sim.py`.
- Stand-, Übergabe- und Stoßversuche (80/150/250 N), `30-T` „Testergebnisse“, Stand 08.10.2026.
- Stabilität über dem Zeitschritt (5/2/1 ms), Kommentar `config.py:60-65`, Skript `sim_hold_test.py`.
- Rechenzeit der IK und Wirkung auf den Regeltakt, `20-T`; Messsonde `test/teleop_jitter_probe.py`.
- Planungszeiten (typisch und schwierige Fälle), IK-Restfehler, `20-T`.
- Überdeckung des Kugelmodells (größter Überstand), `20-T`, `test/sphere_coverage.py`.
- Umfang der automatisierten Tests (gezählt am 16.11.: 597 Testfunktionen in 49 Dateien unter `test/` und Paketwurzel).
- Realbefund Linksdrall beim Gehen (offen), `30-T` „Bekannte Einschränkungen“.

---

## 7 Begriffe im Text

Programm- und Dateinamen erscheinen nicht im Fließtext (R4). Vorschlag für einheitliche Bezeichnungen, mit Kap. 6
abzustimmen (AP 0):

| Im Code / in der Doku | Im Text |
|---|---|
| Bridge (`unitree_sdk2py_bridge`) | Kopplungsschicht |
| `rt/lowcmd`, `rt/arm_sdk` | Befehlsweg der Fortbewegung, Befehlsweg der Arme |
| Blend-Gewicht, `motor_cmd[29].q` | Überblendgewicht |
| Lockstep | Gleichschritt-Betrieb |
| `loco_sim` | Ersatzregler |
| `loco_client` | Anbindung des Onboard-Reglers |
| HOLD / STAND / WALK / DAMP | Bereitschaft / Stehen / Gehen / Dämpfen |
| PD-Balancer | Standregler |
| Rescue | Abfangen |
| SettleGate | Beruhigungsbedingung |
| `arm_controller` | Armregler |
| Servoing | reaktives Nachführen |
| Gate | Laufzeitüberwachung (Kollisionsüberwachung) |
| Slack | drehmomentfrei mit Dämpfung |
| Release | Rückgabe an den Onboard-Regler |
| Funnel, `relax_radius`, `clearance` | Trichter, Trichterradius, Sicherheitsabstand |
| Pose-Store, Sequence | Posenspeicher, Ablauf |
| Backend | Anbindung |
| Hand-Profil | Hand-Profil |
| Jog | Tippbetrieb |
| Deadman | Zustimmtaster (Gerät), Totmann-Überwachung (Zeit) |
| Gateway | Vermittlungsschicht |
| `/scene_markers` | gemeinsames Weltmodell |
| NOT-HALT, Voll-Notaus, Stopp | wie in 6.3.1 definiert |
| Policy | Lauf-Policy (wie in 4.1) |

Abkürzungen über `\ac{}`: prüfen, welche in `main.tex` schon angelegt sind (IK, DDS, ROS, IMU, PD, TCP, API, BLE, HMAC).

---

## 8 Offene Entscheidungen für Nils

Jede mit Empfehlung; „wie empfohlen“ genügt als Antwort.

- **E1 Gliederung.** Änderungen gegenüber dem Gerüst: 7.5 heißt „Roboterhände“ mit 7.5.1 und 7.5.2 (eigene Hände neu);
  `tab:bedienwege` nach 6.4.2; kein eigener Sicherheitsabschnitt; Posen/Abläufe in 7.6.1; Streamdeck entfällt in 7.6.4.
  *Empfehlung: so übernehmen.*
- **E2 Umfang.** 15–16 statt 14 Seiten. *Empfehlung: zulassen; sonst Streichreihenfolge aus §2.*
- **E3 Bezug zum Quelltext.** *Empfehlung:* keine Programm- und Dateinamen im Fließtext, dafür Anhangtabelle TA.1
  (Abschnitt → Programm/Datei) und im LaTeX-Quelltext die `% DB:`-Kommentare. Alternative: Programmnamen in
  Schreibmaschinenschrift im Text.
- **E4 Fester Code-Stand.** Alle Zahlen beziehen sich auf einen Stand. *Empfehlung:* im Repo G1 einen Tag setzen
  (z. B. `ba-kap7`), sobald keine größeren Änderungen mehr kommen; bis dahin `25d5c1a`. Frage: Ändert sich bis zur
  Abgabe noch etwas an Planer, Händen oder Bedienwegen?
- **E5 Herstellerdoku und Software-Quellen.** Für `arm_sdk`, Motorbefehle und Onboard-Dienste fehlt jede Quelle.
  *Empfehlung:* Nils druckt die Seiten der Unitree-Entwicklerdoku (G1: Basic Services, Arm-Schnittstelle,
  Sport/Loco-Dienste) als PDF und lädt sie ins Quellen-Repo; ebenso die README des fremden Szenen-Editors. Ohne diese
  bleiben in 7.2.1, 7.3.2, 7.4.1 mehrere `\qf{}`.
- **E6 Messwerte.** Die Zahlen aus §6.3 stehen nur in der Doku. *Empfehlung:* nicht in Kap. 7 verwenden; für Kap. 8
  am festen Stand neu messen.
- **E7 Bildschirmfotos.** B7.12 (Demo-Oberfläche) und B7.4 (Szene) braucht Nils' Rechner. *Empfehlung:* je ein
  Bildschirmfoto in hoher Auflösung ins Thesis-Repo unter `Bilder/`; Beschriftung der Bereiche baut ein Arbeitspaket.
- **E8 Freigaben.** Vier neue optionale Vorschläge (§5.4), dazu wartend: Zhao2026 (AGILE), Mamou2009 (V-HACD), PDF
  für Ma2017. *Empfehlung:* Zhao2026 und Mamou2009 freigeben; die vier neuen nur, wenn die Verfahrensnamen im Text
  stehen sollen (dann RFC 2104 und Lloyd).
- **E9 Tiefe beim Smartphone.** *Empfehlung:* 0,6 Seiten, nur Prinzip (Kopplung, Prüfcode mit Zähler, Rollen,
  Zeitgrenzen). Maschinenbau-Leser brauchen kein Protokolldetail.

---

## 9 Arbeitspakete

Arbeit auf einem Branch im Thesis-Repo (nicht `main`), wie bei Kap. 3. Entwürfe der Abschnitte entstehen als einzelne
Dateien unter `review/kap7-entwurf/` und werden erst in AP 6 in `Kapitel/07_Umsetzung.tex` zusammengeführt, damit
`main` kompilierbar bleibt und parallele Pakete sich nicht überschreiben.

| AP | Inhalt | Modell | parallel | hängt ab von |
|---|---|---|---|---|
| 0 | Vorbereitung und Abgleich | Opus | – | Nils' Antworten zu §8, `review/plan-kap6.md` |
| 1 | Belege ergänzen | Sonnet | ja, je Quelle | AP 0 |
| 2 | Faktenblätter aus dem Code | Sonnet (7.4: Opus) | ja, 7 Pakete | AP 0 |
| 3 | Abbildungen und Tabellen | Sonnet (B7.7, B7.9: Opus) | ja, je Darstellung | AP 2 |
| 4 | Abschnitte schreiben | Sonnet (7.4, 7.3.1: Opus) | ja, 7 Pakete | AP 1, AP 2, AP 3 |
| 5 | Anhangtabellen TA.1, TA.2 | Sonnet | – | AP 2 |
| 6 | Zusammenführen, Kapiteleinleitung, Übergänge | Opus | – | AP 4, AP 5 |
| 7 | Prüfung: Belege (Verifier) und Code-Abgleich | Sonnet, je ein neuer Agent | ja | AP 6 |
| 8 | Abnahme | Fable | – | AP 7 |

Stopp für Nils nach AP 0 (nur falls Abweichungen), nach AP 6 (Entwurf lesen) und nach AP 7 (Korrekturen freigeben).

### 9.1 Gemeinsamer Vorspann (jedem Auftrag voranstellen)

> Du arbeitest an Kapitel 7 „Umsetzung“ einer Bachelorarbeit (Maschinenbau, FAU, Lehrstuhl FAPS) über eine
> Simulations- und Ausführungsumgebung für den humanoiden Roboter Unitree G1. Antworte auf Deutsch.
> Lies zuerst vollständig: `CLAUDE.md`, `Richtlinien-BA.md` (mindestens §0, §4, §6, §7, §11, §12) und
> `review/plan-kap7.md` (§1.2, §1.3, §7 und den Abschnitt deines Pakets in §3).
> Thesis-Repo: `/home/user/Bachelorarbeit`, Branch `<BRANCH>`. Code-Repo: `/home/user/G1`, ausgecheckt auf
> `<COMMIT>`; Pfade im Code-Repo immer relativ zu dessen Wurzel angeben.
> Regeln, die über allem stehen: (1) Nichts erfinden. Jede Aussage über den eigenen Code braucht eine Fundstelle
> `Pfad:Zeile`, die du selbst im Code gelesen hast; die Doku unter `g1pilot/docs/` ist nur Wegweiser und kann
> veraltet sein. (2) Jede Aussage über fremde Software, Verfahren oder den Roboter braucht `\cite{Key}\ev{Key.NN}`
> mit einem Beleg aus `evidence/`, einen Verweis `Abschnitt~\ref{…}` auf Kap. 2–4 oder `\qf{…}`. Dein eigenes Wissen
> ist keine Quelle. (3) Unklares mit `\pruefen{…}` markieren statt raten. (4) Ändere nur die Dateien, die dein Auftrag
> nennt. `zotero.bib`, `zotero-map.json`, `sources-text/`, `main.tex` nicht anfassen. (5) Am Ende: kurze Liste, was
> erledigt ist, was offen blieb, welche `\qf{}` und `\pruefen{}` du gesetzt hast.

### 9.2 AP 0 – Vorbereitung und Abgleich

> Auftrag: (a) `git pull` in beiden Repos; G1 auf den von Nils genannten Stand setzen, Kurz-Hash notieren und
> `<COMMIT>` in allen folgenden Aufträgen ersetzen. (b) `pip install -r requirements.txt`, `python3 scripts/zot.py bib`,
> `python3 scripts/zot.py text`, `python3 scripts/check.py`; Ausgangswerte notieren. (c) `review/plan-kap6.md` lesen
> und mit `review/plan-kap7.md` §1.2, §2, §7 abgleichen: Stimmen Labels, Begriffe und die Zuständigkeit je Thema
> überein? Abweichungen als Liste melden, nicht selbst entscheiden. (d) Prüfen, welche der in §3 genannten
> Sprungziele (`sec:…`, `tab:…`, `fig:…`) in `Kapitel/*.tex` schon existieren; fehlende auflisten. (e) Nils'
> Antworten zu §8 in den Plan eintragen (Abschnitt „Entscheidungen“ mit Datum). (f) Branch `<BRANCH>` anlegen,
> Ordner `review/kap7-fakten/` und `review/kap7-entwurf/` anlegen.
> Ergebnis: aktualisierter Plan, Liste der Abweichungen. Kein Fließtext.

### 9.3 AP 1 – Belege ergänzen

> Auftrag: Für jede Zeile der Tabelle in `review/plan-kap7.md` §5.2 und für jede in §3 als „teilweise“ markierte
> Stelle: in `sources-text/<Key>.txt` nach der Antwort suchen und passende Belege in `evidence/<Key>.yaml` ergänzen
> (CLAUDE.md Phase 1: wörtlich kopiert, 1–3 Sätze, gedruckte Seitenzahl, `quelle: exzerpt`, neue laufende Nummer,
> `kommentar: "Kap. 7.x, Leitfrage L7.nn"`). Steht in der Quelle etwas anderes als erwartet, gilt die Quelle. Findest
> du nichts, lege keinen Beleg an. Für neu freigegebene Quellen (Liste von Nils) zuvor Phase 0 nach CLAUDE.md.
> Danach `python3 scripts/check.py` (0 Fehler).
> Ergebnis: `review/kap7-fakten/belege.md` mit Tabelle Leitfrage · Key · neue Beleg-ID · Kernaussage bzw. „nicht
> gefunden“. Keine Änderung an Kapiteltext.

### 9.4 AP 2 – Faktenblätter aus dem Code (je Paket ein Agent)

Pakete: **2a** 7.1 · **2b** 7.2 · **2c** 7.3 · **2d** 7.4 · **2e** 7.5 · **2f** 7.6 · **2g** 7.7.

> Auftrag: Erstelle `review/kap7-fakten/<abschnitt>.md` für Abschnitt `<7.x>`. Arbeite die Leitfragen und jeden
> Punkt unter „Kerninhalte“ deines Abschnitts in `review/plan-kap7.md` §3 ab. Lies dazu die genannte Technik-Doku
> als Wegweiser und dann den genannten Code. Je Punkt: (1) Aussage in einem Satz, sachlich, Präsens, mit den
> Begriffen aus §7; (2) Fundstelle `Pfad:Zeilen`; (3) Zahlenwerte mit Einheit, Name des Parameters und Fundstelle der
> Voreinstellung (auch Überschreibungen in `launch/` und `docker-compose.yml` prüfen, getrennt für Simulation und
> Realbetrieb); (4) Status: bestätigt / weicht vom Plan ab (wie?) / im Code nicht gefunden. Zusätzlich: die
> Gleichungen deines Abschnitts aus §4 mit den Bezeichnern und Vorzeichen des Codes aufschreiben; Fakten, die im
> Plan fehlen, aber zum Verständnis nötig sind, unter „Ergänzungen“; Aussagen über Fremdes (Bibliotheken, Roboter)
> unter „Braucht Quelle“ sammeln, nicht als Fakt führen. Laut `g1pilot/NOTICE.md` übernommene Teile kennzeichnen.
> Keine Bewertung, keine Messergebnisse, keine Entwicklungsgeschichte, kein Fließtext für die Arbeit.
> Abnahme: Jeder Punkt hat eine selbst gelesene Fundstelle; kein Wert stammt nur aus der Doku.

### 9.5 AP 3 – Abbildungen und Tabellen (je Darstellung ein Agent)

> Auftrag: Baue `<Nr., Label>` aus `review/plan-kap7.md` §4 als `Bilder/tikz/<datei>.tex` (Tabellen als
> `review/kap7-entwurf/<label>.tex`). Inhalt ausschließlich aus `review/kap7-fakten/<abschnitt>.md`. Vorgaben aus
> CLAUDE.md „Grafiken, Diagramme, Tabellen“: `\begin{tikzpicture}[ba]`, nur `ba`-Stile und -Farben, nie skalieren,
> Breite höchstens 16 cm, Bedeutung nie allein über Farbe, Teilbilder mit a)/b). Muster:
> `Bilder/tikz/ik-vorwaerts-invers.tex`, `Bilder/tikz/dds-domains.tex`. Beschriftungen deutsch, Begriffe aus §7,
> keine Programm- oder Dateinamen. Schreibe dazu einen Vorschlag für Bildunterschrift (Titel im Nominalstil plus ein
> erläuternder Satz) und zwei Sätze Textbezug (Einführung davor, Erläuterung danach) in
> `review/kap7-entwurf/<label>-text.md`. Kompiliere in einem Testdokument, das `ba-grafik.tex` lädt, und sieh dir
> das PDF an (keine Überlappungen, keine Overfull-Boxen).
> Für B7.9 b): Skript `scripts/`-frei im Ordner `Daten/` ablegen, das G7.6 mit den Voreinstellungen aus dem
> Faktenblatt auswertet und `Daten/planer-trichter.csv` schreibt; Diagramm mit pgfplots `[ba plot]`.
> Abnahme: kompiliert, lesbar bei 100 %, jede Beschriftung im Faktenblatt belegt.

### 9.6 AP 4 – Abschnitte schreiben (je Paket ein Agent)

Pakete: **4a** 7.1 · **4b** 7.2 · **4c** 7.3 · **4d** 7.4 · **4e** 7.5 · **4f** 7.6 · **4g** 7.7.

> Auftrag: Schreibe Abschnitt `<7.x>` als LaTeX nach `review/kap7-entwurf/<abschnitt>.tex` (mit `\section`,
> `\subsection`, Labels und Zielumfang aus `review/plan-kap7.md` §2). Eingaben: Planabschnitt in §3,
> `review/kap7-fakten/<abschnitt>.md`, `review/kap7-fakten/belege.md`, die fertigen Darstellungen aus AP 3.
> Aufbau jedes Unterabschnitts: Rückbezug auf Kap. 6 und die Anforderung (1–2 Sätze, per `\ref`) → Lösung →
> Vorverweis auf Kap. 8 (1 Satz, per `\ref`). Beantworte die Leitfragen in ihrer Reihenfolge; eine Leitfrage ohne
> bestätigten Fakt wird zu `\pruefen{}`, nicht zu Text.
> Regeln R1–R8 aus §1.3 strikt: Absatz über die eigene Umsetzung endet mit `% DB: Pfad:Zeilen @<COMMIT>` aus dem
> Faktenblatt; Aussage über Fremdes mit `\cite{}\ev{}` oder `\ref` oder `\qf{}`; höchstens fünf Zahlenwerte je
> Unterabschnitt; Grenzwerte der Schutzmechanismen nicht nennen, sondern auf `Tabelle~\ref{tab:schutzmechanismen}`
> verweisen; keine Messergebnisse; keine Programm- und Dateinamen; keine Bedienschritte; keine
> Entwicklungsgeschichte; ausdrücklich sagen, was nur in der Simulation oder nur real gilt.
> Sprache nach Richtlinien §4: Präsens, Sach-Subjekt, kein ich/wir/man, kein Konjunktiv, Topic Sentence, mindestens
> zwei Sätze je Absatz, Zahlen mit `\,` vor der Einheit, Abkürzungen mit `\ac{}`. Jede Abbildung und Tabelle vor
> ihrer Umgebung im Text einführen und danach erläutern; Gleichungen in den Satz einbinden, Variablen erklären,
> `\formeleintrag{}`.
> Abschluss: Liste aller `\qf{}`/`\pruefen{}` und aller Stellen, an denen du vom Plan abgewichen bist, mit Grund.
> Abnahme: Umfang ±15 %, jede Leitfrage beantwortet oder markiert, kein Absatz ohne `% DB:` oder Beleg.

Zusätze je Paket:
- **4b (7.2):** G7.1–G7.3 ausformulieren; B7.2 und B7.3 tragen den Abschnitt. Das PD-Gesetz als das der
  Kopplungsschicht beschreiben; die Aussage über die Firmware des Roboters nur mit Quelle.
- **4c (7.3):** Trennung Ersatzregler (eigene Entwicklung um übernommene Policies) und Onboard-Regler (fremd,
  geschlossen) in jedem Absatz erkennbar halten. Keine Aussage zum Training der Policies ohne Beleg.
- **4d (7.4):** Schwerpunkt des Kapitels, deshalb stärkeres Modell. 7.4.3 erklärt G7.6 an B7.9 Zeile für Zeile.
  Verhältnis zum Stand der Technik nur als Verweis auf 4.2.3, kein Vergleich (der steht in 8.5.2).
- **4e (7.5):** 7.5.2 klar als reine Simulationsfunktion kennzeichnen.
- **4f (7.6):** Einleitung mit T7.6 und B7.13 zuerst; in 7.6.1–7.6.4 nichts wiederholen, was dort steht.
- **4g (7.7):** höchstens drei Absätze; zuerst sagen, was übernommen ist.

### 9.7 AP 5 – Anhangtabellen

> Auftrag: Erstelle aus allen Faktenblättern TA.1 (`tab:quelltext`: Abschnitt · Funktionsbezeichnung im Text ·
> Programm/Datei) und, falls Nils E3/E4 so entschieden hat, TA.2 (`tab:parameter`: Parameter · Wert Simulation/Real ·
> Bedeutung · Fundstelle) als `review/kap7-entwurf/anhang-*.tex` mit `xltabular` und `\tabstil`. Nur Werte mit
> Fundstelle aus den Faktenblättern.

### 9.8 AP 6 – Zusammenführen

> Auftrag: Füge die Dateien aus `review/kap7-entwurf/` in der Reihenfolge der Gliederung in
> `Kapitel/07_Umsetzung.tex` zusammen (Gerüstkommentare ersetzen), die Anhangtabellen in eine neue
> `Kapitel/Anhang_B.tex` (Einbindung in `main.tex` nur vorschlagen, nicht ändern). Schreibe die Kapiteleinleitung
> nach §3 und je einen Überleitungssatz zwischen den Abschnitten. Vereinheitliche Begriffe nach §7, entferne
> Doppelungen zwischen Abschnitten und gegenüber Kap. 6 (dort nachsehen), prüfe alle `\ref` gegen vorhandene Labels
> (fehlende Ziele in Kap. 2, 6, 8 als `\pruefen{Verweisziel … fehlt noch}`), prüfe Abkürzungen gegen `main.tex`.
> Füge keine neuen Sachaussagen hinzu. Dann `python3 scripts/check.py` (0 Fehler) und `latexmk` (Build muss
> durchlaufen; Seitenzahl des Kapitels und Overfull-Boxen melden).
> Ergebnis: Kapitel auf dem Branch, PDF nach `/mnt/project-files/bachelorarbeit/entwurf-kap7-<datum>.pdf`,
> Bericht mit Umfang je Abschnitt und allen offenen Markierungen.

### 9.9 AP 7 – Prüfung (zwei getrennte, neue Agenten)

**7a Belegprüfung:** `python3 scripts/check.py --pairs review/pairs.jsonl --file Kapitel/07_Umsetzung.tex`, dann der
Verifier-Prompt aus `CLAUDE.md` wörtlich. Ergebnis nach `review/verifikation-kap7-<datum>.md`.

**7b Code-Abgleich** (neuer Agent, der weder Faktenblätter noch Text geschrieben hat):

> Du prüfst Absätze einer Bachelorarbeit gegen den Quelltext, den sie beschreiben. Du hast keinen Anteil am Text.
> Lies `Kapitel/07_Umsetzung.tex`. Jeder Absatz über die eigene Umsetzung endet mit `% DB: Pfad:Zeilen @Commit`.
> Öffne die Fundstelle in `/home/user/G1` (Stand `<COMMIT>`) und bewerte **nur anhand des Codes**: **gedeckt** (jede
> Aussage und jede Zahl steht so im Code), **teilweise** (Kern stimmt, aber eine Zahl, Einheit, Reihenfolge oder
> Bedingung weicht ab, oder ein Teil ist an der Fundstelle nicht zu finden), **nicht gedeckt**. Melde außerdem
> Absätze ohne `% DB:` und ohne Beleg, Messergebnisse, Grenzwerte, die nicht aus `tab:schutzmechanismen` stammen,
> und Sätze, die Vergangenes erzählen. Ausgabe als Markdown-Tabelle Datei:Zeile | Bewertung | Begründung (1 Satz) |
> Vorschlag; „gedeckt“ nur als Anzahl. Ändere keine Dateien.

Ergebnis nach `review/code-abgleich-kap7-<datum>.md`. Korrekturen erst nach Rücksprache mit Nils.

### 9.10 AP 8 – Abnahme

Prüfpunkte: roter Faden über Topic Sentences und über die Abbildungen allein erfassbar; jeder Abschnitt mit
Rückbezug und Vorverweis; keine Überschneidung mit Kap. 6 und 8; Rückverweis-Regel der Betreuerin umgekehrt geprüft
(jede Grundlage, die Kap. 7 braucht, steht in Kap. 2–4); Umfang; `\qf{}`/`\pruefen{}` als Liste an Nils.

---

## 10 Abhängigkeiten und Risiken

- **Kap. 2 ist noch nicht geschrieben.** Kap. 7 verweist auf `sec:g1_sdk`, `sec:g1_onboard`, `sec:g1_armsdk`. Die
  Herstellerschnittstellen müssen dort belegt sein; ohne die PDFs aus E5 bleibt die Lücke in beiden Kapiteln.
- **Kap. 6 entsteht parallel.** Labels und `tab:schutzmechanismen` müssen vor AP 4 feststehen (AP 0 gleicht ab).
- **Kap. 8 ist noch nicht geplant.** Vorverweise aus Kap. 7 zeigen auf die Labels des Gerüsts (`sec:eval_*`).
- **Der Code ändert sich noch.** Ohne festen Stand (E4) veralten Faktenblätter; nach jeder Änderung des Stands AP 2
  für die betroffenen Abschnitte wiederholen.
- **Overleaf:** Nach Freigabe neuer Quellen `zotero.bib` in Overleaf aktualisieren, sonst kompiliert der Text nicht.
- **Doku ist kein Beleg.** Die Technik-Doku ist ausführlich, erzählt aber Geschichte und enthält Messwerte ohne
  festen Stand. Sie darf Wegweiser sein, nie Datenbasis.
