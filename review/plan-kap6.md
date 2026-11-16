# Kapitelplan Kap. 6 – Konzept der Umgebung

Stand 16.11.2026 (Claude, Kapitel-Workflow Schritt 1). **Nur Plan, kein Fließtext.** Wartet auf Nils' Prüfung.
**Arbeitsfassung zum Bearbeiten und Kommentieren (seit 16.11.):** Claude-Dokument https://claude.ai/artifact/WMSov4954nNSCRqM8VPr5Y .
Nils' Änderungen dort werden vor dem Start der Arbeitspakete in diese Datei übertragen; die Subagents lesen diese Datei.
Code-Stand der Befunde: Repo `NilsMeier1812/G1`, `main` @ `25d5c1a` (11.11.2026), derselbe Stand wie in `review/plan-kap7.md`.
Abgrenzung zu Kap. 7 ist mit dem Thread „Kapitel 7 konzipieren und planen“ abgestimmt (Abschnitt 2).

Aufbau dieser Datei: 1 Rolle · 2 Abgrenzung · 3 Belegstrategie · 4 Gliederung · 5 Abschnitte im Detail ·
6 Darstellungen · 7 Quellenlage und Lücken · 8 Fragen an Nils · 9 Arbeitspakete mit Prompts · 10 Abnahme.

---

## 1 Rolle des Kapitels

Kap. 6 ist das Scharnier zwischen den Anforderungen A1–A7 (Kap. 5.2) und der Umsetzung (Kap. 7). Es beantwortet
für jede tragende Entscheidung: **Welche Anforderung liegt zugrunde, welche Alternativen gab es, was wurde gewählt
und warum, und wo wird die Entscheidung in Kap. 8 nachgewiesen?** Das Schema steht schon im Kopf von
`Kapitel/06_Konzept.tex` und ist Nils' Vorgabe vom 29.10. („wissenschaftliche Arbeit, kein Handbuch“).

Was der Leser nach Kap. 6 wissen muss:
1. Auf welcher Basis die Umgebung aufbaut und was daran Eigenleistung ist (6.1).
2. Wie die Umgebung aufgebaut ist und wodurch derselbe Code in Simulation und am Roboter läuft (6.2 → F1, A2).
3. Wie verhindert wird, dass ein Bedienfehler am realen Roboter zu einer Gefährdung führt (6.3 → F3, A5).
4. Wie Personen ohne Vorerfahrung die Umgebung bedienen (6.4 → F3, A6, A1).
5. Wo andere Projekte andocken (6.5 → F4, A7).

Kap. 6 ist das einzige Kapitel des Eigenteils, das **werten und begründen** darf, ohne Messwerte zu nennen.
Messwerte gehören nach Kap. 8, Algorithmen und Parameter nach Kap. 7.

Zielumfang: **11–12 Seiten** als Richtwert (Gerüst: ca. 10). **Nils, 16.11.:** Der Entwurf darf länger werden;
Nils kürzt selbst (Regel in `Richtlinien-BA.md` §3.2). Schreibaufträge streichen also nichts vorsorglich, auch
Kann-Teile werden geschrieben und mit `% Kann` markiert.

## 2 Abgrenzung

**Grundregel 6/7 (abgestimmt):** Kap. 6 = *was und warum* auf der Ebene Komponenten, Zustände, Schnittstellen.
Kap. 7 = *wie*: Algorithmen, Regler, Takte, Datenformate, Parameter. In Kap. 6 stehen **keine** Dateinamen,
Knoten-/Topic-Namen in Code-Schreibweise, Taktraten oder Bedienschritte. Ausnahme: Auslegungswerte der
Schutzmechanismen (Grenzwerte) stehen **nur** in Kap. 6, Tabelle `tab:schutzmechanismen`; Kap. 7 verweist darauf.

| Thema | Kap. 6 | Kap. 7 |
|---|---|---|
| Sim/Real | Prinzip: ein Schalter, getrennte DDS-Domains, was gleich bleibt und was nicht (6.2.2) | Bridge MuJoCo↔DDS, Befehls-Merge, Zeitschritt, Lockstep (7.2.1, 7.2.2) |
| Fortbewegung | Prinzip Ersatzregler hinter gleichen Befehlen, Auswahlbegründung der Lauf-Policies (6.2.3) | Stand-PD, Übergabe Gehen→Stehen, Abfangen, Einbindung der Policies (7.3.1); Anbindung Onboard-Regler (7.3.2) |
| Sicherheit | Betriebszustände, Halt-Stufen, Katalog der Schutzmechanismen mit Grenzwerten, Prinzip der Armübergabe (6.3) | Umsetzung bei der Komponente: Totmann/Bodenkontakt 7.3.2, Reihenfolge der Begrenzer, Gewichtsrampe, Rückgabe 7.4.1, Kollisions-Gate 7.4.2, Hände 7.5, Zeitüberwachungen 7.6 |
| Bedienung | Leitgedanken, Matrix `tab:bedienwege` (wandert aus 7.6 hierher), geteilter Bedienzustand, Rollen und Steuerhoheit (6.4.1, 6.4.2) | je Bedienweg Transport und Anbindung, `tab:bedienwege_umsetzung`, Funkprotokoll des Smartphones (7.6) |
| Posen/Abläufe | Datenmodell Pose – relative Bewegung – Ablauf, Ausführungsarten (6.4.3) | Dateiformat und Ablauf-Zustandsmaschine 7.6.1, geplantes Anfahren 7.4.3 |
| Erweiterung | Ebenenmodell der Andockpunkte (6.5.1), Container-Profile als Prinzip (6.5.2) | Arm-API 7.6.4, Hand-Profile 7.5.2 (`sec:hand_profile`), Szenen 7.2.3, Images/Compose/Startmenü 7.1 |
| Kennwerte | keine Messwerte | nur Auslegungsparameter; Messwerte (Gangbild, Stoßtests, Planungszeit, IK-Restfehler) in Kap. 8 |

**Gegenüber Kap. 3/4:** Grundlagen werden nicht wiederholt, sondern mit `\ref` aufgegriffen (DDS-Domains 3.3.2,
Container 3.3.3, Schutzfunktionen 3.4.2, Zweibeiner 3.4.3, Lauf-Policies 4.1, Teleoperation 4.3, Stacks 4.4).
**Gegenüber Kap. 5:** Kap. 5.1 wertet die Literatur und leitet die Lücke ab, Kap. 5.2 legt A1–A7 fest. Kap. 6
zitiert A1–A7 nur per Kürzel und `Tabelle~\ref{tab:anforderungen}` (Label muss Kap. 5 so vergeben, → Abhängigkeit D1).
6.1.2 wertet **nur die gewählte Basis** gegen A1–A7, nicht noch einmal den ganzen Stand der Technik.
**Gegenüber Kap. 8:** Jeder Unterabschnitt endet mit einem Satz „Nachweis in Abschnitt~\ref{…}“. Kap. 6 behauptet
nicht, dass etwas funktioniert, sondern nur, wie es angelegt ist.

Labels aus dem Gerüst bleiben unverändert (Kap. 7 und 8 verweisen darauf): `sec:ausgangsbasis`, `sec:auswahl_basis`,
`sec:defizite`, `sec:eigenleistung`, `sec:architektur`, `sec:komponenten`, `sec:sim_real_schalter`,
`sec:fortbewegungspfade`, `sec:sicherheitskonzept`, `sec:zustaende`, `sec:schutzmechanismen`, `sec:armuebergabe`,
`sec:bedienkonzept`, `sec:leitgedanken`, `sec:bedienwege_konzept`, `sec:posen_ablaeufe`, `sec:erweiterungskonzept`,
`sec:andockpunkte`, `sec:container_profile`.

## 3 Belegstrategie (für Kap. 6 besonders wichtig)

Kap. 6 beschreibt überwiegend Nils' eigenes System. Deshalb gibt es drei Arten von Aussagen, die im Text
unterschiedlich behandelt werden. Jeder Schreib-Auftrag muss diese Tabelle kennen.

| Art | Beispiel | Behandlung im Text |
|---|---|---|
| **E – Eigenleistung** (Aufbau, Entscheidung, Auslegungswert des eigenen Systems) | „Der Not-Halt lässt die Beine stehen.“ | Kein `\cite`. Datenbasis als LaTeX-Kommentar **vor dem Absatz**: `% Basis: G1@25d5c1a g1pilot/docs/51-T-Notaus.md, Abschnitt „Wer was tut“`. Werte exakt aus Doku/Code übernehmen und am Code gegenprüfen. Unklar oder nicht auffindbar → `\pruefen{…}`. Nie aus dem Gedächtnis ergänzen (CLAUDE.md Regel 5). |
| **F – Fremdes System** (g1pilot-Original, Unitree-Software, Onboard-Regler, Policies) | „Der Onboard-Regler ist nicht quelloffen.“ | `\cite{Key}\ev{Key.NN}` mit vorhandenem Beleg. Fehlt der Beleg → `\qf{…}`. Eigene Analyse des fremden Codes („im übernommenen Stand fehlt X“) ist Art E mit Datenbasis (Commit), als eigene Analyse kenntlich. |
| **G – Grundlage zur Begründung** (Norm, Literatur) | „Das Abschalten der Energie führt beim Zweibeiner zum Sturz.“ | Rückverweis `Abschnitt~\ref{sec:…}` **und**, wenn die Tatsache im Satz wiederholt wird, erneut `\cite{}\ev{}`. Paraphrase darf nicht mehr sagen als der Beleg (Regel 4). |

Zusätzlich:
- **Begründungen sind Nils' Begründungen.** Dieser Plan nennt je Entscheidung die Gründe, die in der G1-Doku
  dokumentiert sind (mit Fundstelle). Wo dort kein Grund steht, ist die Zeile mit **[N?]** markiert: Dann fragt der
  Schreib-Auftrag nicht nach und erfindet nichts, sondern setzt `\pruefen{Begründung für … von Nils}`.
- **Normbezug nur als Orientierung.** Die Schutzmechanismen sind Softwarefunktionen auf einem Standard-PC, keine
  sicherheitsbewerteten Funktionen. Formulierungen wie „erfüllt ISO …“, „normgerecht“, „Performance Level“ sind
  verboten. Erlaubt: „orientiert sich an dem in Abschnitt~\ref{sec:schutzfunktionen} beschriebenen Prinzip …“.
- **Keine Wirksamkeitsaussagen.** „verhindert“, „stellt sicher“ nur für das, was der Mechanismus konstruktiv tut
  (z. B. „begrenzt den Sollwert auf …“), nicht für das Ergebnis („der Roboter kann nicht stürzen“).
- Entwicklungsgeschichte („früher …, seit 15.10. …“) steht in der G1-Doku häufig. Sie gehört **nicht** in den Text
  (Richtlinien §3.4 Methodik). Der dokumentierte Realtest darf als Begründung genannt werden, aber nur, wenn Nils
  ihn als Beobachtung freigibt (→ N6), sonst sachlich begründen.

## 4 Gliederung

„Kern“ = muss hinein; „Kann“ = bei Platzmangel zuerst streichen. Schema je Unterabschnitt:
Anforderung → Alternativen → Entscheidung mit Begründung → Kern der Lösung → Nachweis in Kap. 8.

| Abschnitt | Umfang | Stufe | Anforderung / Frage | Grundlage (Rückverweis) | Nachweis in | Änderung ggü. Gerüst 30.10. |
|---|---|---|---|---|---|---|
| Kapiteleinleitung | 6–8 Sätze | Kern | A1–A7 | 5.2 | – | **neu:** drei Entwurfsgrundsätze + optional `tab:konzept_uebersicht` (→ N2) |
| **6.1 Ausgangsbasis und Abgrenzung** | ~2 S. | | | | | |
| 6.1.1 Auswahl der Ausgangsbasis | 0,3 S. | Kern | A2, A7 | 4.4 (Merkmalstabelle der Stacks), 2.3 | – | Argument über die Tabelle in 4.4, **keine** zweite Vergleichstabelle |
| 6.1.2 Übernommener Funktionsumfang und Defizite | 0,6 S. | Kern | A1–A7 | 5.2 | – | Defizite **je Anforderung** statt als Funktionsliste; leitet 6.2–6.5 her |
| 6.1.3 Abgrenzung der Eigenleistung | 0,8 S. | Kern | – | – | 8.1.1 | `tab:eigenleistung` mit drei Stufen übernommen / erweitert / neu |
| **6.2 Gesamtarchitektur** | ~3 S. | | F1 | | | |
| 6.2.1 Komponenten und Datenflüsse | 1,2 S. | Kern | A2, A7 | 3.3.1, 3.3.2, 2.3 | 8.1.1 | Kernbild `fig:architektur`; drei Architekturregeln |
| 6.2.2 Umschaltung zwischen Simulation und Realbetrieb | 1 S. | Kern | A2, A3, A4 | 3.2.2, 3.2.3, 3.3.2 | 8.1.1, 8.1.2, 8.2.1 | **ergänzt:** Wahl des Simulators (Rückverweis aus 3.2.3 war bisher ohne Ziel); `tab:sim_real` |
| 6.2.3 Fortbewegungspfade in Simulation und Realbetrieb | 0,8 S. | Kern | A2, A4 | 2.3.2, 4.1 (`tab:policies`), 3.1.2 | 8.2.2, 8.5.3 | **ergänzt:** Auswahlbegründung der Lauf-Policies (Wunsch Nils 09.11.) |
| **6.3 Sicherheitskonzept** | ~3 S. | | F3 | | | |
| 6.3.1 Betriebszustände und Übergänge | 1 S. | Kern | A5 | 2.3.2, 3.4.3 | 8.3.1 | `fig:betriebszustaende` + `tab:haltstufen`; Leitgedanke „aktiver sicherer Zustand“ |
| 6.3.2 Schutzmechanismen | 1,3 S. | Kern | A5 | 3.4.1, 3.4.2, 4.2.2 | 8.3.1 | `tab:schutzmechanismen` nach vier Wirkprinzipien, mit Spalte „Umsetzung in“ |
| 6.3.3 Übergabe der Arme an den Onboard-Regler | 0,7 S. | Kern | A5, A2 | 2.3.3 | 8.1.2, 8.3.1 | vier Fälle (Übernehmen, Zurückgeben, Not-Halt, Programmende); `fig:armuebergabe` Kann |
| **6.4 Bedienkonzept** | ~2,5 S. | | F3 | | | |
| 6.4.1 Leitgedanken | 0,8 S. | Kern | A6, A5 | 4.3.1, 4.3.2 | 8.3.2 | fünf Leitgedanken statt zwei |
| 6.4.2 Bedienwege und geteilter Bedienzustand | 1 S. | Kern | A6, A5 | 4.3 | 8.3.2 | `tab:bedienwege` aus 7.6 hierher; Rollen und Steuerhoheit |
| 6.4.3 Posen und Abläufe als aufgabenunabhängige Bausteine | 0,7 S. | Kern | A1 | 4.3.2 | 8.4.2 | Datenmodell; `fig:posen_ablaeufe` Kann |
| **6.5 Erweiterungskonzept** | ~1,5 S. | | F4 | | | |
| 6.5.1 Andockpunkte für externe Projekte | 0,9 S. | Kern | A7, A1 | 3.3.1, 3.3.2 | 8.4.1, 8.4.2 | Ebenenmodell „Aufwand gegen Schutz“; `tab:andockpunkte` |
| 6.5.2 Modularisierung über Container-Profile | 0,6 S. | Kern | A7, A6 | 3.3.3 | 8.3.2 | nur Prinzip; Bild der Container-Topologie liegt in 7.1 |

Richtlinien §5.1: 6.5 hat nur zwei Unterabschnitte. Das ist zulässig („wer A sagt, muss B sagen“ ist erfüllt),
die Empfehlung „mindestens drei“ ist weich (§13.1). Kein dritter Unterabschnitt erfinden.

## 5 Abschnitte im Detail

Lesehilfe: **Kette** = Argumentationsfolge für den Text. **Befunde** = Tatsachen über das eigene System mit
Fundstelle im G1-Repo (Pfade relativ zu `g1pilot/`, Art E). **Leitfragen** = fremde Aussagen, die ein Beleg tragen
muss (Art F/G), mit Status *abgedeckt / teilweise / offen* und passenden Beleg-IDs.

### Kapiteleinleitung

- Kette: Anknüpfung an A1–A7 und die Lücke aus 5.1 → drei Entwurfsgrundsätze, die das ganze Kapitel tragen →
  Vorschau auf 6.1–6.5 (ein Satz je Abschnitt).
- Die drei Grundsätze (Art E, aus den Befunden unten abgeleitet, Wortlaut mit Nils klären → N2):
  1. **Eine Schnittstelle:** Simulation und Roboter werden über dieselbe Herstellerschnittstelle angesprochen.
  2. **Logik an einer Stelle:** Bewegung und Schutz liegen in wenigen Funktionsknoten; Bedienwege und externe
     Projekte senden nur Ziele und können die Schutzmechanismen nicht umgehen.
  3. **Simulation zuerst:** Jede Funktion ist mit derselben Bedienung zuerst in der Simulation ausführbar.
- Kann: `tab:konzept_uebersicht` (Anforderung · Konzeptbaustein · Abschnitt · Nachweis). Sie macht sichtbar, dass
  A3 und A4 kein eigener Abschnitt in Kap. 6 sind, sondern in 6.2.2/6.2.3 und Kap. 7.2 behandelt werden.

### 6.1.1 Auswahl der Ausgangsbasis

- Kette: Neuentwicklung gegen Aufbau auf einem vorhandenen Stack → Kandidaten aus 4.4 → Auswahlkriterien aus
  A2/A7 → Entscheidung für g1pilot → Preis der Entscheidung (kein Simulationspfad, Forschungs-Bedienung).
- Befunde: Herkunft und Abzweigstand in `NOTICE.md` (hucebot/g1pilot, BSD-3-Clause, Upstream `455e287`/`efc5e7c`,
  Okt./Nov. 2025). **Nils, 16.11. (N3):** Das Original-g1pilot war nur für den Realbetrieb gedacht; **alles, was
  Simulation ist, ist Nils' Werk**, auch die Sim-Dateien, die schon im ersten Commit `6c0f331` (12.06.2026) liegen.
- Leitfragen:
  - L1 Was bietet g1pilot laut eigener Beschreibung? – **abgedeckt**: HucebotG1Pilot.01–.04 (ROS-2-Paket,
    Unterkörper beim Unitree-Regler, Oberkörpersteuerung und Teleoperation, Docker, Navigation).
  - L2 Was bieten die Alternativen (Unitree-SDK mit unitree_mujoco, xr_teleoperate, GR00T-WBC, OpenWBT, LeRobot)?
    – **teilweise**: UnitreeMujoco.01/.02, UnitreeSDK2Py.01, UnitreeXRTeleop.01/.02, NvidiaGR00TWBC.01/.02,
    GalbotOpenWBT.01/.02; LeRobot (Cadene2024) ohne Belege. Tiefe nur so weit, wie 4.4 sie schon liefert.
  - L3 Nach welchen Kriterien wurde gewählt? – Art E. **Nils, 16.11. (N4):** Einzige echte Alternative war die
    Neuentwicklung; g1pilot passte zum Vorhaben. Für den Text reichen **zwei bis drei Sätze**: Neuentwicklung gegen
    Aufbau auf g1pilot, Grund = vorhandene Bausteine, die zum Vorhaben passen (ROS 2, kartesische Armsteuerung,
    Unterkörper beim Onboard-Regler, BSD-Lizenz; jeden Punkt mit HucebotG1Pilot.01–.03 bzw. eigener Analyse belegen).
    Keine ausführliche Bewertung der anderen Stacks, die steht in 4.4. 6.1.1 schrumpft auf ca. 0,3 Seiten.
- Darstellung: keine. Verweis auf die Merkmalstabelle in 4.4 (dort noch `\pruefen`, Label abstimmen → D3).
- Stil: Hier ist ein wertender Vergleich erlaubt. Die Fakten über die Alternativen tragen Belege, das Urteil nicht.

### 6.1.2 Übernommener Funktionsumfang und Defizite

- Kette: Was übernommen wurde (ein Absatz) → Soll-Ist-Abgleich gegen A1–A7 → daraus die vier Handlungsfelder,
  die 6.2–6.5 bearbeiten.
- Befunde (eigene Analyse des übernommenen Stands, Art E mit Datenbasis Commit + `NOTICE.md`):
  übernommen: Armregler-Grundgerüst, IK-Löser, RViz-Marker, Anbindung des Onboard-Reglers, Dijkstra-Navigation,
  Joystick, Roboterzustand. Entfernt: Dex3-Hand, Stream-Deck-Oberfläche, LiDAR-Anbindung, großes Docker-Image.
- Soll-Ist als Fließtext oder dreizeilige Aufzählung, **keine eigene Tabelle** (die Tabelle folgt in 6.1.3):
  A2 kein Fortbewegungspfad in der Simulation (Beine nur über Onboard-Regler) · A5 Schutzmechanismen für den
  Realbetrieb der Arme fehlen (Übergabe, Begrenzungen, gestufter Halt) · A6 Bedienung für Entwickler, alle Funktionen
  gleichzeitig sichtbar · A1/A7 keine Schnittstelle für Projekte ohne ROS, keine Abläufe, keine Inspire-Hände.
  Jede dieser Zeilen muss am Commit des übernommenen Stands geprüft werden; was sich nicht prüfen lässt → `\pruefen`.
  Laut Nils (N3) gab es im Original **keinen** Simulationsbetrieb; das ist das erste und größte Defizit für A2.
- Leitfrage L4 Dokumentiert g1pilot einen Simulationsbetrieb? – **offen** (README-Beleg nennt keinen; ein
  Negativbefund ist kein Zitat, sondern eigene Analyse).

### 6.1.3 Abgrenzung der Eigenleistung

- Kette: Maßstab der Abgrenzung (Funktionsbereiche, nicht Zeilen) → `tab:eigenleistung` → zwei bis drei Sätze je
  Stufe → Hinweis auf Fremdbestandteile (Unitree-Pakete, Policies, Szenen-Editor).
- Befunde: `NOTICE.md` (Tabelle Original-Anteil je Datei; „etwa ein Zehntel der Zeilen“ Stand 30.10.2026),
  `policies/*/ATTRIBUTION.md`, `unitree_mujoco/scene_editor/README.md` (Editor basiert auf `mujoco-scene-editor`).
  Umfang zum Stand `25d5c1a`: ca. 26.400 Zeilen Python im Paket, ca. 13.400 Zeilen Tests, 597 Testfunktionen
  (eigene Zählung 16.11.; vor Verwendung neu zählen, → `\pruefen`).
- `tab:eigenleistung` (Gitter, Spalten Funktionsbereich · Stufe · Bemerkung), Zeilenvorschlag:
  Roboterzustand – übernommen · Navigation (Simulation) – übernommen, eingebunden · Armregelung und IK – erweitert ·
  Onboard-Anbindung – erweitert · Kollisionsmodell und Bahnplaner – neu · Simulationskopplung – neu
  (Basis unitree_mujoco) · Ersatzregler Fortbewegung – neu, Policies übernommen · Sicherheitsfunktionen – neu ·
  Hände (Inspire, eigene Profile) – neu · Bedienoberfläche, Gamepad, Smartphone – neu · Posen und Abläufe – neu ·
  Arm-API – neu · Bereitstellung und Startmenü – neu · Tests und Dokumentation – neu.
- Offene Punkte: Anteil der Betreuerin (Commits zu Greif-Kollision, Szenen, Bedienkonzept) zählt laut Absprache vom
  29.10. als Teil der Arbeit, wird im Text nicht einzeln ausgewiesen. KI-Nutzung wird im Text nicht thematisiert
  (eigene Angabe am Anfang der Arbeit).

### 6.2.1 Komponenten und Datenflüsse

- Kette: Kernbild einführen → vier Ebenen von der Bedienung bis zum Roboter → drei Architekturregeln mit Begründung
  → Rolle der zwei Kommunikationsebenen.
- Befunde (`docs/02-T-Architektur.md`, `docs/05-T-Nodes-und-Topics.md`, `docs/10-T-Demo-GUI.md` „Grundsatz“):
  - Ebenen: Bedienwege (Oberfläche, Gamepad, Smartphone, externe Clients) → Funktionsknoten (Armregler,
    Fortbewegung, Hände, Roboterzustand) → Herstellerschnittstelle (Unitree-DDS) → Roboter **oder** Simulation.
  - Regel 1: Bedienwege rechnen keine Bewegung, sie senden Ziele und lesen Zustände.
  - Regel 2: Zuständigkeit je Gelenkgruppe ist getrennt (Beine/Taille: Fortbewegung; Arme: Armregler; Hände:
    Hand-Knoten). Grund laut Doku: Ein Zustandswechsel der Fortbewegung darf die Arme nicht verstellen.
  - Regel 3: Zwei getrennte Kommunikationsebenen (Herstellerschnittstelle; ROS 2 innerhalb der Umgebung), auf
    verschiedenen DDS-Domains.
  - Regel 4 (nur nennen, Detail 6.3): Es gibt genau eine Stelle, die prüft, ob eine Armbewegung starten darf.
- Leitfragen:
  - L5 Warum verteilte, modulare Knoten? – **abgedeckt**: Macenski2022.04, .05 (Designprinzipien Distribution,
    Modularität), .07/.08 (Topics).
  - L6 Was trennt DDS-Domains? – **abgedeckt**: OMG2015.08, .09 (Isolation), Rückverweis `fig:dds_domains`.
  - L7 Welche Schnittstelle bietet der Roboter (Low-Level, High-Level, arm_sdk)? – **offen**, gehört in Kap. 2.3
    (dort noch kein Text) → D2. Bis dahin Rückverweis + `\qf`.
- Darstellung: `fig:architektur` (Kernbild des Kapitels, Spezifikation in Abschnitt 6).
- Alternative, die genannt werden soll: monolithischer Aufbau bzw. Logik in der Bedienoberfläche (so war die frühere
  Entwickler-Oberfläche nicht aufgebaut, aber als gedankliche Alternative zulässig) **[N?]**.

### 6.2.2 Umschaltung zwischen Simulation und Realbetrieb

- Kette: A2 → drei Wege, denselben Code in beiden Welten zu nutzen → Entscheidung: Simulation spricht die
  Herstellerschnittstelle → Wahl des Simulators → ein Schalter → was trotzdem verschieden ist (`tab:sim_real`) →
  Folge für A3 (Echtzeit) als Vorgriff auf 7.2.2.
- Alternativen (Art E, Formulierung als Entwurfsalternativen): (a) getrennte Programme für Simulation und Roboter,
  (b) eigene Abstraktionsschicht über beiden, (c) Simulation bildet die Herstellerschnittstelle nach. Gewählt (c).
- Befunde (`docs/02-T-Architektur.md` „Sim ↔ Real: Ein Schalter“, `docs/04-T-Umgebungsvariablen.md`,
  `g1pilot/utils/common.py`):
  - Eine Umgebungsvariable entscheidet; ausgewertet an einer Stelle beim Öffnen der Verbindung.
  - Simulation: Domain 1 auf der Loopback-Schnittstelle; Roboter: Domain 0 auf der Netzwerkkarte.
  - Nicht gleich sind: Fortbewegung (6.2.3), Hand-Anbindung (simulierte Finger gegen Modbus), harte Grenzwerte und
    Rampenzeiten (nur real), automatischer Start in die Greifstellung (nur Simulation), Sicherheitsbestätigung vor
    dem Start (nur real), eigene Hand-Profile (nur Simulation), Navigation (nur Simulation).
- `tab:sim_real` (Gitter, Spalten Aspekt · Simulation · Realbetrieb · gleich?): Verbindung · Fortbewegung · Arme ·
  Hände · Grenzwerte · Start · Navigation. Ehrlich ausweisen, **was nicht gleich ist**; das ist die Grundlage für
  8.1.1 (Vergleich von Code und Konfiguration) und 8.5.3.
- Leitfragen:
  - L8 Stellt unitree_mujoco die gleiche Schnittstelle bereit? – **abgedeckt**: UnitreeMujoco.01, .05, .06.
  - L9 Wie trennt Unitree selbst Simulation und Roboter? – **abgedeckt**: UnitreeMujoco.07, .08, .09.
  - L10 Deckt unitree_mujoco auch die High-Level-Funktionen ab? – **abgedeckt**: UnitreeMujoco.02 (nur Low-Level).
  - L11 Warum MuJoCo und nicht ein anderer Simulator? – **teilweise**: Gu2024.03/.04 (MuJoCo als Prüfsimulator,
    Einschränkung „im untersuchten Fall“ erhalten), Rückverweis `tab:simulatoren`; eigentliches Argument ist L8.
    Grund gegen GPU-parallele Simulatoren: kein eigenes Training **[N?]**.
  - L12 Gibt es Arbeiten, die „derselbe Code“ als Übertragungsargument nutzen? – **abgedeckt**: Durrani2026.02, .03
    (gehört eher nach 5.1; hier höchstens ein Halbsatz).

### 6.2.3 Fortbewegungspfade in Simulation und Realbetrieb

- Kette: Problem: Der Regler für Stehen und Gehen läuft nur auf dem Roboter → Alternativen → Entscheidung
  Ersatzregler mit gleicher Befehlsschnittstelle → Auswahl der Lauf-Policies → Grenze: Die Simulation bildet das
  Gangverhalten des realen Reglers nicht ab (Vorgriff auf 8.2.2, 8.5.3).
- Alternativen: (a) Simulation ohne Fortbewegung, Rumpf fixiert, (b) eigenes Training einer Policy, (c) veröffentlichte
  Policies mit ergänzendem Standregler. Gewählt (c). Gegen (b): Eingrenzung der Arbeit in 1.2 (kein eigenes
  RL-Training).
- Befunde (`docs/30-T-Stehen-und-Gehen.md` „Warum zwei völlig verschiedene Implementierungen?“, „Zwei kombinierte
  Regler“, Tabelle der Policies):
  - Beide Pfade bedienen dieselben Befehle (Modus, Geschwindigkeitsvorgabe, Halt); die Bedienwege unterscheiden
    nicht zwischen Simulation und Roboter.
  - Ersatzregler = Lauf-Policy fürs Gehen + modellbasierter Standregler fürs Stehen. Grund: Die Policy macht im
    Stand Ausgleichsschritte, für das Greifen müssen die Füße stehen bleiben (Zahlen dazu nach Kap. 8).
  - Drei wählbare Policies: eine aus unitree_rl_mjlab (Standard), zwei aus NVIDIA WBC-AGILE.
  - Der Ersatzregler nutzt Größen, die nur die Simulation liefert, und ist nicht für den Roboter gedacht.
- Auswahlkriterien der Policies (Art E, **[N?]** → N5; Nils' Liste gefundener und verworfener Policies steht seit
  09.11. aus): Lizenz, Format (ONNX), Schnittstelle Geschwindigkeitsvorgabe, lauffähig in MuJoCo ohne Nachtraining,
  Arme beim Gehen frei.
- Leitfragen:
  - L13 Ist der Onboard-Regler einsehbar? – **abgedeckt**: Hu2026.02 (nicht quelloffen), Hu2026.01.
  - L14 Woher stammen die Policies, wie wurden sie trainiert? – **teilweise**: UnitreeRLMjlab.01, .04, .05;
    Zakka2026 (mjlab). WBC-AGILE **offen** (Zhao2026 liegt in `_Vorschläge`, vgl. `\pruefen` in `tab:policies`).
  - L15 Warum weicht eine in einem anderen Simulator trainierte Policy in MuJoCo ab? – **teilweise**: Rückverweis
    3.1.2; Gu2024.02. Keine eigene Erklärung erfinden.
- Darstellung: Die beiden Pfade sind in `fig:architektur` als zwei Zweige unter derselben Befehlsebene gezeichnet;
  kein eigenes Bild (Kann: `fig:fortbewegungspfade`, falls das Kernbild zu voll wird).

### 6.3.1 Betriebszustände und Übergänge

- Kette: Besonderheit des Zweibeiners (aktiver sicherer Zustand) → Folgerung: Halt in Stufen statt eines einzigen
  Abschaltens → Betriebszustände der Umgebung → Übergänge und ihre Bedingungen → Quittierung.
- **Leitgedanke (tragendes Argument des ganzen Abschnitts 6.3):** Bei einer fest montierten Maschine ist der
  energielose Zustand sicher. Beim balancierenden Zweibeiner ist das Abschalten selbst eine Gefährdung. Belege:
  Ding2026.01–.03, .08, .09; Prather2025.03, .04; Subburaman2023.01, .07; Rückverweis 3.4.3. Daraus folgt die
  Trennung „Arme entlasten“ gegen „Beine weiter stehen lassen“.
- Befunde (`docs/51-A-Notaus.md`, `docs/51-T-Notaus.md`, `docs/30-T-Stehen-und-Gehen.md` „Zustandsmaschine“ und
  „loco_client“, `docs/20-T-Arm-Manipulation.md` „Zustandsmaschine“, `docs/10-A-Demo-GUI.md` „Modus“):
  - Im Code gibt es **keine einzelne** Zustandsmaschine, sondern vier gekoppelte: Onboard-Regler des Roboters
    (gedämpft, vorbereitet, Gehen), Ersatzregler der Simulation (gehalten, Stehen, Gehen, gedämpft), Armregler
    (inaktiv, aktiv, schlaff, Rückgabe), Bedienmodus (GEHEN, GREIFEN). `fig:betriebszustaende` fasst sie zu einem
    **abstrakten** Diagramm zusammen, das für beide Welten gilt (→ N7, ob Nils diese Abstraktion mitträgt).
  - Vorschlag der abstrakten Zustände: *Gedämpft* → *Bereit* (Gelenke steif, hängend bzw. gehalten) → *Stehen*
    → darin die zwei Bedienmodi *GREIFEN* und *GEHEN* (genau einer aktiv) → von überall *Not-Halt* (verriegelt)
    → *Quittiert* zurück in den vorherigen Bein-Zustand, Arme bleiben schlaff bis zur bewussten Übernahme;
    daneben *Voll-Notaus* (alles gedämpft) und in der Simulation *Sturz erkannt* → gedämpft.
  - Übergangsbedingungen real: Start gibt frei und quittiert; Gehen erst nach Bodenkontakt und zweiter Bestätigung;
    Gehen gesperrt, solange nicht balanciert bzw. die Hüfte nicht in der Mitte steht.
  - Halt-Stufen (`tab:haltstufen`): Stopp (laufende Bewegung endet) · Gehen stoppen (Totmann losgelassen) ·
    Not-Halt (Arme schlaff und gedämpft, Hände halten, Taille gehalten, Beine bleiben stehen) · Voll-Notaus
    (alles gedämpft, Roboter sackt zusammen) · Fernbedienung des Herstellers (unabhängig von PC und Umgebung).
    Spalten: Stufe · Auslöser · Wirkung auf Arme / Hände / Taille / Beine · Quittierung.
  - Unterschied Simulation: Not-Halt dämpft dort auch die Beine. Das gehört in `tab:sim_real` bzw. als Fußnote der
    Tabelle, nicht verschweigen.
- Leitfragen:
  - L16 Welche Zustände hat der Onboard-Regler (gedämpft, vorbereitet, Gehen mit/ohne Taille)? – **teilweise**:
    Benutzerhandbuch G1 (von Nils am 16.11. geliefert, Zotero-Freigabe steht aus, siehe Abschnitt 7 Q1) beschreibt
    Nullmoment-Zustand, Dämpfung, Bereitschaft und Bewegungszustand über die Fernbedienung. Entwicklerdoku fehlt.
  - L17 Welche Stoppkategorien kennt die Maschinensicherheit? – **abgedeckt**: DGUV2015.10; Ding2026.02. Die
    Zuordnung der eigenen Stufen zu Kategorien ist eine **Analogie**, als solche formulieren.
  - L18 Not-Halt als Pflichtfunktion bei Industrierobotern? – **abgedeckt**: DGUV2015.09 (gilt für
    Industrieroboter, Geltungsbereich nicht auf den G1 ausdehnen; DGUV2015.02).
- Darstellung: `fig:betriebszustaende` (Kern), `tab:haltstufen` (Kern).

### 6.3.2 Schutzmechanismen

- Kette: Gefährdungen im Betrieb (Stoß und Quetschen durch den Arm, Kollision mit Umgebung und eigenem Körper,
  Sturz, unbeabsichtigtes Loslaufen, Ausfall von Verbindung oder Bedienperson) → vier Wirkprinzipien →
  `tab:schutzmechanismen` → Einordnung: Softwarefunktionen, nicht sicherheitsbewertet; unabhängige Ebene ist die
  Fernbedienung des Herstellers und die zweite Person.
- Wirkprinzipien und Befunde (Werte aus `docs/50-A-Echter-Roboter.md` Abschnitt E, `docs/20-T-Arm-Manipulation.md`
  „main_loop“, „Laufzeit-Gate“, `docs/04-T-Umgebungsvariablen.md`, `docs/11-T-Controller.md` „Sicherheit“,
  `docs/12-T-Handy.md` „Zeiten“, `docs/51-T-Notaus.md` „Zeitgrenzen“; **jeden Wert vor Übernahme am Code
  gegenprüfen**):
  1. *Begrenzen:* Gelenkgeschwindigkeit der Arme 1,5 rad/s · Geschwindigkeit der Hand 0,25 m/s · Gelenkbeschleunigung
     3,0 rad/s² · Abstand Sollwert–Messwert höchstens 0,3 rad · Obergrenzen der Reglerverstärkungen · Gehen
     0,4 m/s vorwärts, 0,3 m/s seitlich, 0,4 rad/s Drehen. Harte Grenzen gelten nur im Realbetrieb; abweichende
     Vorgaben aus der Konfiguration werden korrigiert.
  2. *Vermeiden:* Kollisionsprüfung zur Laufzeit (Annäherung an Umgebung unter Mindestabstand wird unterbunden,
     Selbstkollision hält an), geplante Bahnen für gespeicherte Posen, Bodenkontaktprüfung vor dem Gehen
     (Knielast mindestens 10 Nm), Verriegelungen (Gehen nur balanciert und mit Hüfte in der Mitte), zweite
     Bestätigung für Dämpfen und Gehen, Sicherheitsbestätigung vor dem Start des Realbetriebs, kein
     selbsttätiger Start einer Bewegung im Realbetrieb.
  3. *Überwachen:* Totmann am Gamepad für das Gehen · Zeitüberwachungen (kein Gamepad-Signal 0,3 s; kein
     Gehbefehl 0,5 s; Gültigkeit eines Gehbefehls am Roboter 1 s; Smartphone sperrt nach 1,5 s ohne Status) ·
     Lebendprüfung der Funkverbindung des Gamepads · Sturzerkennung (Simulation).
  4. *Anhalten:* die Halt-Stufen aus 6.3.1, Not-Halt auf jedem Bedienweg, Quittieren absichtlich nicht am Gamepad.
- `tab:schutzmechanismen` (Gitter, `xltabular` falls mehrseitig; Spalten Wirkprinzip · Mechanismus · Gefährdung ·
  Auslegungswert · Sim/Real · Umsetzung in). Spalte „Umsetzung in“ mit `\ref` auf `sec:onboard_anbindung`,
  `sec:regelkette`, `sec:kollisionsmodell`, `sec:haende`, `sec:bedienwege` (Wunsch des Kap.-7-Threads).
  Ziel 12–16 Zeilen; mehr gehört in den Anhang.
- Leitfragen:
  - L19 Woran orientiert sich die Geschwindigkeitsgrenze der Hand? – **teilweise**: Villani2018.09 nennt 250 mm/s
    als Grundannahme der ISO/TS 15066 für kollaborativen Betrieb; DGUV2015.04 (Betriebsart mit reduzierter
    Geschwindigkeit, Wortlaut des Belegs prüfen). Im Code steht als Kommentar ein Verweis auf ISO 10218-1, die
    Norm selbst liegt **nicht** als Quelle vor → nur sagen, was die Belege sagen; sonst `\qf`.
  - L20 Was ist eine Zustimmeinrichtung, und entspricht der Totmann dem? – **abgedeckt** für die Definition:
    DGUV2015.06 (dreistufig: DGUV2015.07). Der Totmann am Gamepad ist **nicht** dreistufig → als Analogie mit
    genanntem Unterschied formulieren.
  - L21 Gelten Industrieroboternormen für Humanoide? – **abgedeckt**: Prather2025.01, .03, .06; Ding2026.07;
    DGUV2015.02; Rückverweis 3.4.1.
  - L22 Kann Standard-Hardware sicherheitsbewertete Funktionen tragen? – **abgedeckt**: Ding2026.05 (Bordrechner
    des G1 sind Standardhardware). Stützt die Einordnung „nicht sicherheitsbewertet“.
  - L23 Welche Hinweise gibt der Hersteller (Dämpfungsmodus, Fernbedienung)? – **teilweise**, sobald das
    Benutzerhandbuch freigegeben ist: Not-Halt der Fernbedienung = Dämpfung, der Roboter sinkt langsam zu Boden;
    beim Abschalten im Stand fällt er; Befehle der Fernbedienung gelten auch bei eigener High-Level-Entwicklung
    weiter und werden dann parallel ausgeführt, bei Low-Level-Entwicklung nicht; Stehen über längere Zeit nur am
    Schutzgestell. Der vorletzte Punkt stützt die Halt-Stufe „Fernbedienung des Herstellers“ und ihre Grenze.
- **Nils, 16.11. (N9):** Eine offizielle Gefährdungsbeurteilung gibt es nicht. Der Text erwähnt keine und behauptet
  keine; die Einordnung „nicht sicherheitsbewertet“ in 6.3.2 bleibt, die Lücke wird in 8.5.3 (Limitierungen) genannt.

### 6.3.3 Übergabe der Arme an den Onboard-Regler

- Kette: Ausgangslage: Am Roboter steuert der Onboard-Regler auch die Arme; die Herstellerschnittstelle überblendet
  per Gewicht zwischen ihm und der eigenen Armregelung (Rückverweis 2.3.3) → Gefährdung: Sprung beim Umschalten →
  vier Fälle mit je einer Regel → Folge für die Taille.
- Befunde (`docs/20-T-Arm-Manipulation.md` „Gewichtsrampe“, „Übergabe an den Onboard-Regler“, „E-Stop-Semantik“;
  `docs/50-A-Echter-Roboter.md` Abschnitt E):
  1. *Übernehmen:* gemessene Armpose merken, genau diese kommandieren, Gewicht über 2 s von 0 auf 1.
  2. *Zurückgeben:* erst geplant und langsam in die gemerkte Pose des Onboard-Reglers fahren, dann Gewicht auf 0.
     Währenddessen werden neue Ziele abgelehnt; Zeitgrenze 12 s.
  3. *Not-Halt:* Gewicht bleibt 1, Steifigkeit null, nur Dämpfung. Grund: Bei Gewicht 0 würde der Onboard-Regler
     die Arme aktiv in seine Grundpose fahren.
  4. *Programmende oder Absturz der Bedienung:* kurze Rückfahrt, dann Rampe, statt die Befehle abreißen zu lassen.
  - Das Gewicht schaltet beim G1 auch die Taille vom Onboard-Regler weg; die Umgebung hält die Taille deshalb
    selbst, auch im Not-Halt (dokumentierter Realtest vom 15.10.2026, → N6).
- Leitfrage L24 Wie ist die Überblendung per Gewicht vom Hersteller spezifiziert (Gewichtsslot, Wirkung auf die
  Taille)? – **offen**, gehört in Kap. 2.3.3 → D2. Ohne Beleg nur als eigene Beobachtung mit `\pruefen`.
- Darstellung (Kann): `fig:armuebergabe`, schematischer Zeitverlauf von Gewicht und Armpose für Fall 1 und 2
  nebeneinander (Teilbilder a, b). **Schematisch, ohne Messwerte**; ein gemessener Verlauf wäre Kap. 8.

### 6.4.1 Leitgedanken

- Kette: Zielgruppe aus A6 → warum die Bedienkonzepte aus 4.3.1 dafür nicht passen → fünf Leitgedanken, je mit
  Begründung → Vorschau auf 6.4.2/6.4.3.
- Befunde (`docs/10-A-Demo-GUI.md` „Ziel“, „Modus“; `docs/50-A-Echter-Roboter.md` E; `docs/03-A-Startmenue.md`):
  1. *Eine Entscheidung zur Zeit:* zwei Bedienmodi, genau einer aktiv; angezeigt wird nur, was im Modus sinnvoll ist.
     Dokumentierter Grund: Die frühere Entwickler-Oberfläche zeigte 25 Funktionen gleichzeitig.
  2. *Zustand sichtbar:* jeder Modus hat die Zustände aktiv / wechselt / inaktiv; am Roboter wird der gemeldete
     Zustand des Onboard-Reglers und der Bodenkontakt angezeigt, bevor ein Befehl möglich ist.
  3. *Simulation zuerst:* dieselbe Oberfläche und dieselben Bedienwege in beiden Welten; der Realbetrieb verlangt
     eine ausdrückliche Bestätigung.
  4. *Halt immer erreichbar:* Not-Halt auf jedem Bedienweg, unabhängig von Modus, Rolle und Sperre.
  5. *Nichts bewegt sich von selbst:* Im Realbetrieb sendet die Umgebung ohne Eingabe keinen Bewegungsbefehl.
- Leitfragen:
  - L25 Welche Hürden haben die Teleoperationssysteme aus 4.3.1 für diese Zielgruppe? – **abgedeckt**: Fu2024.01,
    He2024.03 (teure, ortsgebundene Aufbauten), UnitreeXRTeleop.02 (Vorwissen), Zhao2025.01.
  - L26 Was empfiehlt die Literatur für Nutzer ohne Robotikerfahrung? – **abgedeckt**: Ajaykumar2021.01, .03, .05,
    .06, .07, .08; Pot2009.02, .05.
  - L27 Gibt es Belege zu Modusfehlern bzw. zur Wirkung reduzierter Auswahl in Bedienoberflächen? – **offen**
    (Suchhinweis in Abschnitt 7). Ohne Beleg bleibt Leitgedanke 1 eine begründete eigene Entscheidung.
- Darstellung (Kann): schematischer Aufbau der Oberfläche in drei Bereichen. Ein Bildschirmfoto gehört nach 7.6.1.

### 6.4.2 Bedienwege und geteilter Bedienzustand

- Kette: Warum mehrere Bedienwege (verschiedene Nutzer und Situationen) → `tab:bedienwege` → Problem
  widersprüchlicher Anzeigen und gleichzeitiger Befehle → geteilter Bedienzustand → Rollen und Steuerhoheit →
  bewusste Asymmetrie beim Quittieren.
- Befunde (`docs/10-T-Demo-GUI.md`, `g1pilot/teleoperation/shared_state.py`, `docs/11-T-Controller.md`,
  `docs/12-T-Handy.md` „Aktionen und Rechte“, `docs/21-T-Arm-API.md`):
  - Bedienwege zum Stand `25d5c1a`: Bedienoberfläche am PC · Gamepad (PS4/Xbox) · Smartphone (über Bluetooth,
    hängt an der Bedienoberfläche) · Zielmarker in RViz (Entwickler) · Arm-API (externe Programme). Die
    Stream-Deck-Oberfläche ist seit 30.10.2026 entfernt.
  - Geteilter Bedienzustand: Modus, Handauswahl und Tempostufen werden zwischen Oberfläche und Gamepad
    abgeglichen; er enthält keine Fahrbefehle.
  - Smartphone: Rollen „Ansicht“ und „Bedienen“, eine Sitzung gleichzeitig, Steuerhoheit muss übernommen werden,
    Befehle gelten nur mit aktuellem Status; Not-Halt geht auch aus der Rolle „Ansicht“.
  - Quittieren eines Not-Halts ist am Gamepad absichtlich nicht möglich.
  - Ein neues Ziel ersetzt das vorige, gleich von welchem Bedienweg es kommt.
- `tab:bedienwege` (Gitter): Spalten = Bedienwege wie oben, Zeilen = Zielgruppe · Arme · Hände · Gehen · Posen
  und Abläufe · Not-Halt · Quittieren · in Simulation / real. Die Entwurfstabelle in `Kapitel/07_Umsetzung.tex`
  ist die Vorlage, aber veraltet (Spalte „Rviz“ mit „Auto-Nav“, Zeile Not-Halt fehlt); jede Zelle am Code prüfen.
- Leitfragen:
  - L28 Arbeiten zur Roboterbedienung über Gamepad oder Smartphone? – **offen** (offenes `\qf` in 4.3.2, Frage 13
    im Plan zu Kap. 4). Für Kap. 6 nicht zwingend.
  - L29 Schnittstelle als Mittel der Interaktion, Bedienarten? – **abgedeckt**: Darvish2023.04, Tong2024.07.

### 6.4.3 Posen und Abläufe als aufgabenunabhängige Bausteine

- Kette: A1: Eine neue Aufgabe soll ohne Programmierung einrichtbar sein → Alternativen (Skript, grafische
  Programmierung, Lernen aus Demonstration) → Entscheidung: Aufgabe als Daten, nicht als Code → Datenmodell →
  zwei Ausführungsarten → Verbindung zum Schutz (jeder Schritt läuft durch Planung und Kollisionsprüfung).
- Befunde (`docs/23-T-Posen-und-Ablaeufe.md`, `docs/23-A-Posen-und-Ablaeufe.md`, `docs/04-T-Umgebungsvariablen.md`):
  - Drei Bausteine: *Pose* (gespeicherte Stellung von Armen und Händen, einzeln wählbar), *relative Bewegung*
    (Verschiebung der Hände von der aktuellen Stelle, je Achse höchstens 0,30 m), *Ablauf* (Folge von Posen und
    relativen Bewegungen mit optionaler Pause).
  - Einlernen durch Hinfahren und Speichern; dieselbe Pose kann in mehreren Abläufen stehen.
  - Ausführung „am Stück“ oder „Schritt für Schritt“; im Realbetrieb ist Schritt für Schritt voreingestellt.
  - Jeder Schritt wird wie eine einzelne Zielvorgabe geplant; der Ablauf selbst enthält keine Bewegungslogik.
  - Abläufe liegen in einer Datei außerhalb des Containers und sind in Simulation und Realbetrieb dieselben.
- Leitfragen:
  - L30 Vorbilder für Bausteine statt Code bei Humanoiden? – **abgedeckt**: Pot2009.05, .06 (vorgefertigte
    Verhalten, ohne Kompilieren); Ajaykumar2021.05 (vorgegebene Optionen statt offener Eingaben).
  - L31 Nutzen des Einrichtens an der Simulation? – **abgedeckt**: Ajaykumar2021.07, .08.
  - L32 Einlernen von Positionen durch Hinführen als bekannte Betriebsart? – **teilweise**: Villani2018.06,
    DGUV2015.12 (Handführung; hier wird nicht handgeführt, sondern per Bedienweg verfahren → nur als Abgrenzung).
- Grenze, die genannt werden muss: keine Verzweigungen, keine Sensorbedingungen, keine Objekterkennung. Abläufe sind
  feste Folgen (→ 8.5.3).
- Darstellung (Kann): `fig:posen_ablaeufe`, Datenmodell als Blockbild.

### 6.5.1 Andockpunkte für externe Projekte

- Kette: A7: Die Umgebung soll Grundlage weiterer Projekte sein → externe Projekte unterscheiden sich in Vorwissen
  und Bedarf → Ebenenmodell: Je tiefer ein Projekt andockt, desto mehr Freiheit und desto weniger Schutz →
  `tab:andockpunkte` → Erweiterung über Daten statt Code.
- Befunde (`docs/21-T-Arm-API.md`, `docs/21-A-Arm-API.md`, `docs/25-T-Eigene-Haende.md`,
  `unitree_mujoco/scene_editor/README.md`, `docs/30-T-Stehen-und-Gehen.md`, `docs/31-T-Navigation.md`):
  - *HTTP-Schnittstelle der Arme:* Zielposen und Gelenkwinkel als JSON, kein ROS nötig, nur lokal erreichbar,
    optional mit Zugangsschlüssel. Sie schreibt auf denselben Kanal wie die Bedienwege und kann die
    Schutzmechanismen deshalb nicht umgehen.
  - *ROS-2-Topics:* gleiche Kanäle wie die Bedienwege; Beispiel im eigenen System ist die Navigation, die ihre
    Fahrbefehle über denselben Kanal einspeist wie die manuelle Steuerung (Umschalter zwischen manuell und automatisch).
  - *Herstellerschnittstelle direkt:* Ein Projekt, das den Roboter bereits über das Unitree-SDK anspricht, läuft
    ohne Änderung gegen die Simulation (Domain 1, Loopback). Dabei wirken keine Schutzmechanismen der Umgebung.
  - *Daten:* Szenen (Editor, Hindernis oder greifbares Objekt per Namensregel), Hand-Profile (Konfigurationsdatei
    und Geometrie, nur Simulation), Lauf-Policies (Ordner mit Beschreibung), Posen und Abläufe.
- `tab:andockpunkte` (Gitter): Zeilen = die vier Ebenen + Datenebene; Spalten = Andockpunkt · was ein Projekt
  liefert · nötiges Vorwissen · Schutzmechanismen wirken · Simulation / real · Detail in (`\ref` auf 7.6.4,
  `sec:hand_profile`, `sec:szenen`, `sec:ersatzregler`).
- Leitfragen:
  - L33 Was sagt die Literatur zu Modularität und austauschbaren Komponenten? – **abgedeckt**: Macenski2022.05, .11.
  - L34 Können mit dem SDK entwickelte Programme in der Simulation laufen? – **abgedeckt**: UnitreeMujoco.01.
- **Nils, 16.11. (N10):** Bisher ist kein externes Projekt angebunden. 6.5.1 beschreibt die Andockpunkte deshalb
  rein konzeptionell und behauptet keine erfolgte Anbindung. Wie 8.4.1 nachweist, steht auf `review/todo-nils.md`.

### 6.5.2 Modularisierung über Container-Profile

- Kette: A6/A7: Inbetriebnahme auf einem frischen PC und Austausch von Teilen → Alternativen (native Installation,
  virtuelle Maschine, ein gemeinsames Image) → Entscheidung: getrennte Container je Aufgabe, zwei Profile →
  Konfiguration ohne Neubau → Grenze.
- Befunde (`docker-compose.yml`, `docs/40-T-Simulation.md` „Container“, `docs/03-A-Startmenue.md`,
  `docs/04-T-Umgebungsvariablen.md`):
  - Drei Images: Simulation (ohne ROS), Umgebung für die Simulation, Umgebung für den Realbetrieb.
  - Zwei Profile: „sim“ startet Simulation und Umgebung, „real“ nur die Umgebung. Der Simulationscontainer nimmt im
    Aufbau die Stelle des Roboters ein.
  - Alle Container nutzen das Netzwerk des Hosts (laut Kommentar in `docker-compose.yml` Voraussetzung für die DDS-Kommunikation).
  - Verhalten wird über Umgebungsvariablen eingestellt; eine Änderung braucht einen Neustart, keinen Neubau.
  - Daten, die erhalten bleiben sollen (Posen, Szenen), liegen außerhalb der Container.
- Leitfragen:
  - L35 Warum Container für reproduzierbare Robotiksoftware? – **abgedeckt**: Cervera2019.01, .02, .09;
    Boettiger2015.02, .06; Rückverweis 3.3.3.
  - L36 Container gegenüber virtueller Maschine? – **abgedeckt**: Boettiger2015.05, .07, .08; Cervera2019.11.
  - L37 Beeinträchtigt ein Container das Zeitverhalten? – **abgedeckt**: Struhar2020.03, .06 (Einschränkung
    „laut referierter Literaturübersicht“ erhalten); Grenze Struhar2020.04, .08.
  - L38 Grenzen von Containern für die Reproduzierbarkeit? – **abgedeckt**: Boettiger2015.10, Cervera2019.12.
- Darstellung: keine in Kap. 6. Die Container-Topologie zeichnet Kap. 7.1; in `fig:architektur` deuten gestrichelte
  Rahmen die Container an.

## 6 Darstellungen

Alle nach `ba-grafik.tex` (CLAUDE.md „Grafiken, Diagramme, Tabellen“): TikZ als `Bilder/tikz/<name>.tex` mit
`\begin{tikzpicture}[ba]`, nie skalieren, höchstens 16 cm breit, Bedeutung nie nur über Farbe. Tabellen mit
`\tabstil`, Gitter-Stil, Caption oben. Jede Darstellung wird im Absatz davor mit `\ref` eingeführt und danach
erläutert. Eigene Darstellungen ohne Quellenangabe in der Caption. Muster: `Bilder/tikz/dds-domains.tex`,
`Bilder/tikz/teleoperation-architektur.tex`.

| Label | Abschnitt | Stufe | Inhalt und Spezifikation |
|---|---|---|---|
| `tab:konzept_uebersicht` | Einleitung | Kann | A1–A7 · Konzeptbaustein · Abschnitt in Kap. 6/7 · Nachweis in Kap. 8 |
| `tab:eigenleistung` | 6.1.3 | Kern | Funktionsbereich · übernommen / erweitert / neu · Bemerkung (siehe 5, 6.1.3) |
| `fig:architektur` | 6.2.1 | **Kern, Kernbild** | Datei `Bilder/tikz/architektur-gesamt.tex`. Vier waagrechte Ebenen von oben nach unten: (1) Bedienwege: Bedienoberfläche, Gamepad, Smartphone, externe Programme; (2) Funktionsknoten: Armregelung mit Planung, Fortbewegung, Hände, Roboterzustand – als `ba block hervor`, daran die Marke „Schutzmechanismen“; (3) Herstellerschnittstelle als durchgehender Balken „Unitree-DDS“; (4) links `ba gruppe` „Simulation“ (MuJoCo, Ersatzregler), rechts `ba gruppe` „Realbetrieb“ (Unitree G1, Onboard-Regler, Hände). Zwischen (3) und (4) der Schalter in `baAkzent` mit Beschriftung „Domain 1“ / „Domain 0“. Pfeile: Ziele nach unten, Zustände nach oben (zwei Linienarten). Gestrichelte Rahmen für die Container. Keine Topic-Namen. |
| `tab:sim_real` | 6.2.2 | Kern | Aspekt · Simulation · Realbetrieb · gleich? (7 Zeilen) |
| `fig:fortbewegungspfade` | 6.2.3 | Kann | nur falls `fig:architektur` zu voll: gleiche Befehle oben, darunter Ersatzregler gegen Onboard-Regler |
| `fig:betriebszustaende` | 6.3.1 | Kern | Datei `Bilder/tikz/betriebszustaende.tex`. Zustände als `ba block`, Not-Halt und Voll-Notaus in `baAkzent`; Übergänge beschriftet mit Auslöser und Bedingung; Not-Halt als Sammelübergang „von jedem Zustand“. Abstraktes Diagramm, gilt für Simulation und Realbetrieb; Abweichung der Simulation in der Caption. |
| `tab:haltstufen` | 6.3.1 | Kern | Stufe · Auslöser · Arme · Hände · Taille · Beine · Quittierung (5 Zeilen) |
| `tab:schutzmechanismen` | 6.3.2 | Kern | Wirkprinzip · Mechanismus · Gefährdung · Auslegungswert · Sim/Real · Umsetzung in (12–16 Zeilen) |
| `fig:armuebergabe` | 6.3.3 | Kann | zwei Teilbilder a) Übernehmen, b) Zurückgeben: Gewicht und Abstand zur Onboard-Pose über der Zeit, schematisch, Achsen ohne Zahlenwerte außer den Auslegungswerten (2 s) |
| `tab:bedienwege` | 6.4.2 | Kern | Matrix Bedienweg × Funktion (siehe 5, 6.4.2); Label aus Kap. 7 übernommen, dort löschen |
| `fig:posen_ablaeufe` | 6.4.3 | Kann | Blockbild Pose / relative Bewegung → Ablauf → Ausführung über Planung und Kollisionsprüfung |
| `tab:andockpunkte` | 6.5.1 | Kern | Ebene · liefert · Vorwissen · Schutz wirkt · Sim/Real · Detail in |

Kern: 3 Abbildungen wären zu viel Text ohne Bild, deshalb mindestens `fig:architektur` und `fig:betriebszustaende`
bauen; von den Kann-Abbildungen höchstens zwei (Empfehlung: `fig:armuebergabe`, `fig:posen_ablaeufe`).

## 7 Quellenlage, Lücken und Abhängigkeiten

**Vorhandene Belege reichen für die Begründungen weitgehend aus.** Kap. 6 braucht wenig neue Literatur, weil es
Eigenleistung beschreibt. Zitierbar (alle in `zotero-map.json`, Belege in `evidence/`):
HucebotG1Pilot, UnitreeMujoco, UnitreeSDK2Py, UnitreeXRTeleop, UnitreeRLMjlab, NvidiaGR00TWBC, GalbotOpenWBT,
Hu2026, Gu2024, Durrani2026, Zakka2026, Macenski2022, OMG2015, Boettiger2015, Cervera2019, Struhar2020, Ding2026,
Prather2025, Subburaman2023, DGUV2015, Villani2018, Ajaykumar2021, Pot2009, Fu2024, He2024, Zhao2025,
Darvish2023, Tong2024.
Hinweise: Ding2026 ist ein Preprint, Prather2025 graue Literatur (beide über die Sammelfreigabe Kap. 3 in der
Sammlung). Für das tragende Argument in 6.3.1 stehen damit zwei nicht begutachtete Quellen; Subburaman2023 und
Westervelt2018.15 stützen den Sturz als Gefährdung zusätzlich.

**Lücken (Suchhinweise, keine Quellenangaben):**

| Nr. | Lücke | betrifft | Dringlichkeit | Suchhinweis |
|---|---|---|---|---|
| Q1 | Herstellerdoku G1: Zustände des Onboard-Reglers, Überblendung der Arme per Gewicht und Wirkung auf die Taille, Dämpfungsmodus, Fernbedienung | 6.2.3, 6.3.1, 6.3.3 (L7, L16, L23, L24), Kap. 2.3 | **hoch** | **Teilweise geschlossen 16.11.:** Benutzerhandbuch G1 V1.0 (2024) von Nils geliefert; Kopie von manualslib.com, besser die Originaldatei von Unitree. Deckt Fernbedienung, Dämpfung, Not-Halt, Start und Sicherheitshinweise, **nicht** arm_sdk, FSM-IDs, LocoClient. Entwicklerdoku: Nils druckt die Seiten als PDF (`review/todo-nils.md`) |
| Q2 | WBC-AGILE: Herkunft und Training der beiden Policies | 6.2.3 (L14) | mittel | Zhao2026 liegt in `_Vorschläge` (Q4ACNEZH), Freigabe fehlt |
| Q3 | ISO 10218-1 (Grenze der Geschwindigkeit, Betriebsarten) als Primärquelle | 6.3.2 (L19) | mittel | Normen liegen ohne PDF in `_Vorschläge`; über die UB (Normendatenbank) |
| Q4 | Modusbasierte Bedienoberflächen, Modusfehler, reduzierte Auswahl | 6.4.1 (L27) | niedrig | Stichworte „mode error“, „mode awareness“, Mensch-Maschine-Schnittstelle, Robotik oder Automatisierung |
| Q5 | Bedienung über Gamepad oder Smartphone | 6.4.2 (L28) | niedrig | bereits Frage 13 im Plan zu Kap. 4 |
| Q6 | Softwarearchitektur für Robotik (Schichten, Komponenten, Trennung der Zuständigkeiten) | 6.2.1 | niedrig | im Plan zu Kap. 3 als L17 („Kann“) geführt; Macenski2022 trägt das Nötigste |
| Q7 | Programmierung durch Posen und Abläufe (Teach-in) als Verfahren | 6.4.3 (L32) | niedrig | Lehrbuch Industrierobotik, Kapitel Programmierverfahren |

Empfehlung: Vor dem Schreiben nur Q1 und Q2 schließen. Q3–Q7 als `\qf` stehen lassen oder nach Nils' Entscheidung
in einer Rechercherunde (Arbeitspaket AP0) bearbeiten.

**Abhängigkeiten von anderen Kapiteln:**
- **D1 Kap. 5 (Stand 16.11., `review/plan-kap5.md`):** Label `tab:anforderungen` und Reihenfolge A1–A7 bestätigt. A2 lautet dort „gleicher Programmstand, Wechsel nur über Konfiguration, Unterschiede gezählt und begründet“ (passt zu `tab:sim_real`). Einzige Zahl in `tab:anforderungen` ist die Geschwindigkeit der Hand (250 mm/s); alle übrigen Grenzwerte bleiben in `tab:schutzmechanismen`. Ursprünglicher Stand: A1–A7 müssen mit endgültigem Wortlaut und Kennzahlen feststehen, Label `tab:anforderungen`. Kap. 5
  ist noch Gerüst. Kap. 6 kann mit den Kürzeln aus dem Gerüst geschrieben werden, die Kapiteleinleitung und 6.1.2
  erst danach endgültig.
- **D2 Kap. 2.3:** `sec:g1_sdk`, `sec:g1_onboard`, `sec:g1_armsdk` sind Rückverweis-Ziele für 6.2.1, 6.2.3, 6.3.1,
  6.3.3 und noch leer. Hängt an Q1.
- **D3 Kap. 4.4:** Merkmalstabelle der Stacks ist noch `\pruefen`; 6.1.1 verweist darauf. Label laut Plan zu Kap. 5: `tab:stacks`.
- **D4 Kap. 7:** `tab:bedienwege` in `Kapitel/07_Umsetzung.tex` löschen, wenn sie in 6.4.2 steht. Labels
  `sec:hand_profile`, `sec:hand_schnittstelle` vergibt Kap. 7.
- **D5 Kap. 8:** Jeder Nachweis-Verweis setzt voraus, dass der Versuch existiert. Stand heute liegen im G1-Repo
  automatisierte Tests und Simulationsmessungen, aber keine Messdaten vom realen Roboter. Die Verweise auf 8.1.2
  und 8.3.2 sind erst belastbar, wenn Nils die Realtests dokumentiert hat.

## 8 Fragen an Nils

Antworten von Nils vom 16.11.2026 sind eingearbeitet. Was noch fehlt, steht in `review/todo-nils.md`.

| Nr. | Frage | Stand |
|---|---|---|
| N1 | Umfang | **beantwortet:** 60–80 Seiten gesamt, Entwurf darf länger sein, Nils kürzt (Abschnitt 1, Richtlinien §3.2) |
| N2 | Drei Entwurfsgrundsätze in der Kapiteleinleitung, Übersichtstabelle | **offen**, Nils hat nachgefragt, Erklärung im Thread am 16.11. Bis zur Antwort: Grundsätze ja, Tabelle als `% Kann` |
| N3 | Ausgangsstand des Simulations-Containers | **beantwortet:** alles, was Simulation ist, ist Nils' Werk (6.1.1, 6.1.2, `tab:eigenleistung`) |
| N4 | Auswahlgründe für g1pilot | **beantwortet:** einzige Alternative war Neuentwicklung, g1pilot passte; 6.1.1 kurz halten |
| N5 | Liste der Lauf-Policies | **offen**, steht auf `review/todo-nils.md`; bis dahin `\pruefen` in 6.2.3 |
| N6 | Realtests als Begründung | **beantwortet: ja.** Doku der Realtests steht auf `review/todo-nils.md`; ohne Doku `\pruefen` statt Datum |
| N7 | Abstraktes Zustandsdiagramm `fig:betriebszustaende` | **beantwortet: vermutlich ja** (Nils, nach Erklärung im Thread final bestätigen) |
| N8 | Herstellerdoku | **teilweise:** Benutzerhandbuch G1 geliefert (Abschnitt 7, Q1); Entwicklerdoku als PDF steht auf `review/todo-nils.md` |
| N9 | Gefährdungsbeurteilung | **beantwortet:** keine offizielle (6.3.2) |
| N10 | Externes Projekt für 8.4.1 | **beantwortet:** bisher keins angebunden; 6.5.1 nur konzeptionell, Entscheidung auf `review/todo-nils.md` |
| N11 | Verweis auf das eigene Repo | **beantwortet:** kein eigener Name nötig. Umsetzung: Anhang „Inhalt des Datenträgers“ mit Commit-Stand, Text spricht von „der Umgebung“ und verweist auf den Anhang; nicht im Literaturverzeichnis |

## 9 Arbeitspakete

Reihenfolge: AP0 (optional) → AP1 und AP2 parallel → AP3–AP7 parallel → AP8 → AP9. Jedes Paket schreibt in eine
eigene Datei, damit sich parallele Aufträge nicht überschreiben; erst AP8 fasst zusammen.
Empfohlene Modelle: Sonnet für AP1, AP2; Opus für AP3–AP7 und AP9; Prüfung des Ergebnisses von AP8 durch Opus oder Nils.

### Rahmenprompt (jedem Auftrag voranstellen)

> Du arbeitest an Nils' Bachelorarbeit (Repo `Bachelorarbeit`, LaTeX). Lies zuerst vollständig: `CLAUDE.md`,
> `Richtlinien-BA.md` (§0.3, §4, §6, §12, §13.1) und `review/plan-kap6.md`. Der Plan ist verbindlich: Gliederung,
> Labels, Argumentationsketten, Abgrenzung zu Kap. 7 und die Belegstrategie in Abschnitt 3.
> Klone `NilsMeier1812/G1` und wechsle auf den Stand `25d5c1a`; alle Befunde im Plan beziehen sich darauf.
> Regeln:
> 1. Aussagen über das eigene System (Art E): kein `\cite`, dafür vor dem Absatz ein Kommentar
>    `% Basis: G1@25d5c1a <Pfad>, <Abschnitt>`. Jeden Zahlenwert in der genannten Datei und im Code nachschlagen.
>    Findest du ihn nicht oder weicht er ab: `\pruefen{…}` und im Bericht nennen. Nichts aus dem Gedächtnis.
> 2. Aussagen über fremde Systeme oder Literatur (Art F, G): nur `\cite{Key}\ev{Key.NN}` mit den im Plan genannten
>    Beleg-IDs. Lies den Beleg in `evidence/<Key>.yaml` und schreibe nicht mehr, als das Zitat sagt. Kein
>    passender Beleg: `\qf{…}`, Aussage nicht ausformulieren. Keine neuen Quellen, keine Websuche.
> 3. Wo der Plan **[N?]** oder eine Frage N… nennt und keine Antwort von Nils vorliegt: `\pruefen{…}`.
> 4. Kap. 6 enthält keine Dateinamen, keine Knoten- oder Topic-Namen, keine Taktraten, keine Bedienschritte, keine
>    Messwerte und keine Entwicklungsgeschichte. Grenzwerte stehen nur in `tab:schutzmechanismen`.
> 5. Stil: Präsens, kein ich/wir/man, kein Konjunktiv, Sach-Subjekte, keine Autorennamen als Satzsubjekt
>    (Stilregel vom 11.11.), ein Argument je Absatz mit Kernsatz zuerst, mindestens zwei Sätze je Absatz. Keine
>    Aussagen wie „normgerecht“ oder „stellt sicher, dass“ über das Ergebnis. Deutsche Fachbegriffe, einheitlich:
>    Bedienoberfläche, Gamepad, Smartphone, Not-Halt, Voll-Notaus, Onboard-Regler, Ersatzregler, Lauf-Policy,
>    Realbetrieb, Herstellerschnittstelle.
> 6. Jeder Unterabschnitt folgt der Kette aus dem Plan (Anforderung → Alternativen → Entscheidung → Lösung) und
>    endet mit einem Satz, der auf den Nachweis in Kap. 8 verweist (`Abschnitt~\ref{…}`).
> 7. Jede Abbildung und Tabelle wird im Absatz davor mit `\ref` eingeführt und danach erläutert; Umgebung mit
>    `[htbp]` direkt nach diesem Absatz.
> 8. Lieber zu viel als zu wenig schreiben (Richtlinien §3.2); Kürzungskandidaten mit `% Kann` markieren.
> 9. Schreibe nur in die Datei, die dein Auftrag nennt. Ändere keine generierten Dateien und nichts in Zotero.
> 10. Bericht am Ende: was geschrieben ist, Liste aller `\qf` und `\pruefen` mit Grund, jede Abweichung vom Plan.

### AP0 – Recherche zu den Lücken (optional, nur nach Nils' Freigabe)

> Rahmenprompt, aber Regel 2 ersetzt durch den Recherche-Modus aus `CLAUDE.md` (Kapitel-Workflow Schritt 2).
> Bearbeite die Lücken Q3, Q4, Q6, Q7 aus Abschnitt 7 des Plans. Je Lücke höchstens zwei Quellen, bevorzugt
> Fachbuch, Norm oder begutachteter Artikel. Jede Quelle über Crossref oder Verlagsseite verifizieren, auf
> Duplikate in Zotero prüfen, in `_Vorschläge` anlegen (Tag `Kap6-Recherche`), ohne Citation Key. Keine Belege aus
> Abstracts. Ergebnis als Abschnitt „Recherche (Schritt 2)“ an `review/plan-kap6.md` anhängen: Titel · DOI/ISBN ·
> frei verfügbar ja/nein · welche Leitfrage. Danach stoppen.

### AP1 – Abbildungen

> Rahmenprompt. Baue nach Abschnitt 6 des Plans `Bilder/tikz/architektur-gesamt.tex` und
> `Bilder/tikz/betriebszustaende.tex`, danach die Kann-Abbildungen `armuebergabe.tex` und `posen-ablaeufe.tex`.
> Muster und Stile: `Bilder/tikz/dds-domains.tex`, `ba-grafik.tex`. Für das Zustandsdiagramm die Zustände und
> Übergänge aus Abschnitt 5, 6.3.1 des Plans nehmen und jeden Übergang in `docs/51-T-Notaus.md`,
> `docs/30-T-Stehen-und-Gehen.md` und `docs/20-T-Arm-Manipulation.md` nachprüfen; was nicht belegt ist, weglassen
> und melden. Lege `review/kap6-entwurf/abbildungen.tex` an, das jede Grafik in einer `figure`-Umgebung mit
> Caption-Vorschlag (Titel im Nominalstil + ein erläuternder Satz) und Label einbindet. Kompiliere `main.tex` mit
> eingebundener Testdatei, sieh dir jede Grafik im PDF an (Überlappungen, Breite höchstens 16 cm) und nimm die
> Testeinbindung wieder heraus.

### AP2 – Tabellen

> Rahmenprompt. Erstelle `review/kap6-entwurf/tabellen.tex` mit `tab:eigenleistung`, `tab:sim_real`,
> `tab:haltstufen`, `tab:schutzmechanismen`, `tab:bedienwege`, `tab:andockpunkte` nach den Spaltenvorgaben in
> Abschnitt 5 und 6 des Plans (Gitter-Stil, `\tabstil`, `tabularx`, Caption oben). Jede Zelle am Code-Stand
> prüfen; hinter jede Tabelle als Kommentar die Fundstellen je Zeile. In `tab:schutzmechanismen` die Werte aus
> der Doku **und** die zugehörige Stelle im Code angeben; bei Abweichung gilt der Code und die Abweichung kommt in
> den Bericht. In `tab:bedienwege` nur Bedienwege aufnehmen, die es zum Code-Stand gibt. Leere oder unsichere
> Zellen als `\pruefen{}`.

### AP3 – Abschnitt 6.1

> Rahmenprompt. Schreibe 6.1 mit 6.1.1–6.1.3 nach Abschnitt 5 des Plans nach `review/kap6-entwurf/6-1.tex`
> (ca. 2 Seiten). Kurze Einleitung des Abschnitts vor 6.1.1. Für 6.1.2 den übernommenen Stand im G1-Repo
> selbst ansehen (erster Commit `6c0f331`, `NOTICE.md`) und nur Defizite nennen, die du dort nachweisen kannst.
> `tab:eigenleistung` aus AP2 mit `\input` bzw. per Label einbinden und im Text zeilenweise aufgreifen.

### AP4 – Abschnitt 6.2

> Rahmenprompt. Schreibe 6.2 mit 6.2.1–6.2.3 nach `review/kap6-entwurf/6-2.tex` (ca. 3 Seiten). `fig:architektur`
> ist das Kernbild: Der Text von 6.2.1 führt von oben nach unten durch das Bild. In 6.2.2 ausdrücklich benennen,
> was zwischen Simulation und Realbetrieb **nicht** gleich ist (`tab:sim_real`). In 6.2.3 keine Kennwerte der
> Policies; die Grenze der Übertragbarkeit als Vorgriff auf `sec:eval_fortbewegung` und `sec:limitierungen`.

### AP5 – Abschnitt 6.3

> Rahmenprompt. Schreibe 6.3 mit 6.3.1–6.3.3 nach `review/kap6-entwurf/6-3.tex` (ca. 3 Seiten). Beginne 6.3.1 mit
> dem Leitgedanken „aktiver sicherer Zustand“ und belege ihn mit den im Plan genannten IDs aus Ding2026,
> Prather2025 und Subburaman2023. Normen nur als Orientierung und nur über vorhandene Belege; jede Zuordnung
> eigener Mechanismen zu Normbegriffen als Analogie mit genanntem Unterschied. Schließe 6.3.2 mit der Einordnung,
> dass es Softwarefunktionen ohne Sicherheitsbewertung sind und welche unabhängige Ebene bleibt.

### AP6 – Abschnitt 6.4

> Rahmenprompt. Schreibe 6.4 mit 6.4.1–6.4.3 nach `review/kap6-entwurf/6-4.tex` (ca. 2,5 Seiten). Die fünf
> Leitgedanken als Fließtext, nicht als Aufzählung von Schlagworten. Keine Tastenbelegungen, keine Namen von
> Schaltflächen außer den zwei Bedienmodi. In 6.4.3 die Grenze (feste Folgen ohne Bedingungen) nennen.

### AP7 – Abschnitt 6.5

> Rahmenprompt. Schreibe 6.5 mit 6.5.1–6.5.2 nach `review/kap6-entwurf/6-5.tex` (ca. 1,5 Seiten). Kernaussage von
> 6.5.1 ist der Zielkonflikt zwischen Freiheit und Schutz entlang der Ebenen. In 6.5.2 nur das Prinzip; Images,
> Startmenü und Befehle gehören nach Kap. 7.1.

### AP8 – Zusammenführen und mechanisch prüfen

> Rahmenprompt. Füge `review/kap6-entwurf/6-1.tex` … `6-5.tex`, Tabellen und Abbildungen in
> `Kapitel/06_Konzept.tex` zusammen; Labels und Überschriften aus dem Gerüst unverändert. Schreibe die
> Kapiteleinleitung (Plan Abschnitt 5) und je Abschnitt einen Überleitungssatz. Entferne `tab:bedienwege` aus
> `Kapitel/07_Umsetzung.tex`, falls sie dort noch steht. Prüfe: einheitliche Begriffe, keine Wiederholung zwischen
> den Abschnitten, jede Darstellung vor ihrem Float eingeführt, Umfang 11–12 Seiten. Führe
> `python3 scripts/zot.py text` und `python3 scripts/check.py` aus (0 Fehler Pflicht), kompiliere mit `latexmk`
> und sieh das PDF durch. Bericht: Seitenzahl, Liste aller `\qf` und `\pruefen`, offene Verweise („??“).
> Arbeite auf einem eigenen Branch und öffne einen Pull Request; nicht direkt auf `main`.

### AP9 – Inhaltlich verifizieren

> Nach `CLAUDE.md` Phase 4: `python3 scripts/check.py --pairs review/pairs.jsonl --file Kapitel/06_Konzept.tex`,
> dann ein **neuer** Auftrag mit dem Verifier-Prompt aus `CLAUDE.md` (wörtlich), Ergebnis nach
> `review/verifikation-kap6-<datum>.md`. Zusätzlich, weil Kap. 6 vor allem Eigenleistung enthält, ein zweiter
> Prüfauftrag: „Prüfe jeden Absatz mit einem Kommentar `% Basis: …` gegen die genannte Datei im G1-Repo
> (Stand `25d5c1a`). Liste jede Aussage, die dort nicht steht, anders steht oder einen abweichenden Wert nennt.
> Ändere nichts.“ Korrekturen erst nach Rücksprache mit Nils.

## 10 Abnahmekriterien für den Entwurf

- Jeder Unterabschnitt nennt Anforderung, mindestens eine Alternative, die Entscheidung mit Grund und den Nachweis.
- Kein Absatz über das eigene System ohne `% Basis:`-Kommentar; kein Zahlenwert ohne Fundstelle.
- `check.py` 0 Fehler; alle `\qf` und `\pruefen` sind im Bericht einzeln begründet.
- Keine Doppelung mit Kap. 7: Stichprobe an den sieben Themen der Tabelle in Abschnitt 2.
- Die Storyline ist allein über die Kernsätze und allein über die Darstellungen lesbar (Richtlinien §3.3).
- 6.2.2 und 6.3.2 benennen ihre Grenzen selbst (nicht gleiche Teile; nicht sicherheitsbewertet).
