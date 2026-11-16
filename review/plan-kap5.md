# Kapitelplan Kap. 5 – Handlungsbedarf, Anforderungen und Bewertungsmethodik

Stand 16.11.2026 (Claude, Kapitel-Workflow Schritt 1). **Nur Plan, kein Fließtext.** Wartet auf Nils' Prüfung.
Code-Stand der Befunde: Repo `NilsMeier1812/G1`, `main` @ `25d5c1a` (11.11.2026), derselbe Stand wie in
`review/plan-kap6.md` und `review/plan-kap7.md`.
Abgestimmt auf die Pläne zu Kap. 6 (auf `main`) und Kap. 7 (Branch `claude/project-thread-jepdj5`): Label
`tab:anforderungen`, Bedeutung und Reihenfolge von A1–A7, Testaufbau in 5.3.3, Grenzwerte in 6.3.2.

Aufbau dieser Datei: 1 Rolle · 2 Abgrenzung · 3 Belegstrategie · 4 Gliederung · 5 Abschnitte im Detail ·
6 Anforderungen A1–A7 (Steckbriefe) · 7 Kennzahlen und Versuchsplan · 8 Darstellungen · 9 Quellenlage, Lücken,
Abhängigkeiten · 10 Fragen an Nils · 11 Arbeitspakete mit Prompts · 12 Abnahme.

---

## 1 Rolle des Kapitels

Kap. 5 ist das Scharnier zwischen dem wertungsfrei dargestellten Stand der Technik (Kap. 2–4) und dem Eigenteil
(Kap. 6–8). Es leistet drei Dinge, und nur diese:

1. **Werten (5.1):** Was können die in Kap. 3 und 4 vorgestellten Arbeiten und Werkzeuge nicht, gemessen am Ziel der
   Arbeit? Ergebnis sind vier Defizite D1–D4, je eines pro Forschungsfrage F1–F4.
2. **Festlegen (5.2):** Was muss die Umgebung können, damit die Defizite geschlossen sind? Ergebnis sind die
   Anforderungen A1–A7, jede mit Prüfkriterium und Zielwert, in `tab:anforderungen`.
3. **Planen (5.3):** Wie wird geprüft, ob die Anforderungen erfüllt sind? Ergebnis sind Kennzahlen K…, Versuche V1–V11
   und die Testumgebung. Der Plan steht fest, **bevor** Kap. 8 Ergebnisse zeigt.

Die Kette, die das Kapitel für die ganze Arbeit festlegt:

**Defizit D → Forschungsfrage F → Anforderung A → Kennzahl K → Versuch V → Abschnitt in Kap. 8 → Abgleich in 8.5.1.**

| Defizit | Frage | Anforderungen | Konzept (Kap. 6) | Nachweis (Kap. 8) |
|---|---|---|---|---|
| D1 Durchgängigkeit Simulation/Realbetrieb nur je Funktion | F1 | A2 | 6.2 | 8.1 |
| D2 Aussagekraft der Simulation für einen Bedien-Stack ungeprüft | F2 | A3, A4 | 6.2.2, 6.2.3 (und 7.2) | 8.2 |
| D3 Bedienung setzt Fachwissen voraus, Schutz für Zweibeiner offen | F3 | A5, A6 | 6.3, 6.4 | 8.3 |
| D4 Werkzeuge sind zweckgebunden | F4 | A1, A7 | 6.4.3, 6.5 | 8.4 |

Was der Leser nach Kap. 5 wissen muss: welche Lücke die Arbeit schließt, woran ihr Erfolg gemessen wird und dass
dieser Maßstab vor den Ergebnissen feststand. Das ist der Teil, der die Entwicklungsarbeit zu einer wissenschaftlichen
Arbeit macht (Nils' Vorgabe vom 29.10.: „kein Handbuch“).

Zielumfang: **6 Seiten** (Gerüst: ca. 5). Begründung: vier Tabellen, auf die Kap. 6, 8 und 9 verweisen, brauchen
zusammen etwa 2 Seiten. Obergrenze 6,5 Seiten; die Gesamtarbeit liegt mit den Plänen zu Kap. 6 (11–12 S.) und Kap. 7
(15–16 S.) schon am oberen Rand von 80 Seiten. → Frage N6.

## 2 Abgrenzung

| Gegenüber | Regel |
|---|---|
| Kap. 1.1/1.2 | Motivation und Wortlaut von F1–F4 stehen in Kap. 1. Kap. 5.1 **leitet her**, warum genau diese Fragen offen sind, und verweist auf `Abschnitt~\ref{sec:zielsetzung}`. F1–F4 werden nicht umformuliert. Die Eingrenzung (kein eigenes RL-Training, kein Policy-Transfer, keine Real-Navigation) steht in 1.2 und wird in 5.1 in einem Satz aufgegriffen und begründet. |
| Kap. 2–4 | Dort steht, **was es gibt** (wertungsfrei). Kap. 5.1 stellt nichts Neues vor. Jede Tatsache in 5.1 ist dort schon eingeführt und wird mit `\ref` **und** erneutem `\cite{}\ev{}` aufgegriffen. Braucht 5.1 eine Tatsache, die in Kap. 2–4 fehlt, wird sie dort ergänzt, nicht hier. |
| Kap. 4.4 | Der neutrale Merkmalsvergleich der Software-Stacks (`tab:stacks`, in 4.4 noch `\pruefen`) bleibt in 4.4. Kap. 5.1 wertet ihn aus und baut **keine zweite Vergleichstabelle** (Empfehlung, → N7). |
| Kap. 3.1.3 | Dort stehen die Kennzahlen der Literatur für die Abbildungsgüte. 5.3.1 wählt daraus aus und begründet, was nicht anwendbar ist. Der letzte Satz von 3.1.3 verweist bereits auf `sec:bewertungsmethodik`. |
| Kap. 6 | Kap. 5 ist **lösungsneutral**: keine Komponenten, keine Auslegungswerte, keine Namen von Bedienwegen. Kap. 6 zitiert A1–A7 per Kürzel und `Tabelle~\ref{tab:anforderungen}`. 6.1.2 wertet nur die gewählte Ausgangsbasis gegen A1–A7; 5.1 wertet den Stand der Technik insgesamt. g1pilot erscheint in 5.1 als eine von mehreren Arbeiten, nicht als „Ausgangsbasis“. |
| Kap. 6.3.2 | **Anforderungswert gegen Auslegungswert:** In `tab:anforderungen` stehen nur Zielwerte, die aus der Literatur oder aus der Aufgabe hergeleitet sind (z. B. Geschwindigkeit der Hand). Alle Auslegungswerte der Schutzmechanismen (Gelenkgeschwindigkeit, Zeitüberwachungen, Rampen) stehen nur in `tab:schutzmechanismen`. Kap. 5 nennt sie nicht. |
| Kap. 7 | Der Testaufbau (Attrappe des Roboters, automatisierte Tests, Referenz-PC) steht in 5.3.3 und wird in 8.3.1 benutzt, nicht in Kap. 7 (so im Plan zu Kap. 7 festgelegt). |
| Kap. 8 | Kap. 5.3 legt fest: Kennzahl, Messmittel, Umgebung, Umfang, Auswertung. Kap. 8 nennt unter „Versuchsaufbau“ nur noch die Parameter des einzelnen Versuchs und verweist auf `Tabelle~\ref{tab:versuchsplan}`. **In Kap. 5 steht kein Messergebnis**, auch keines aus der G1-Doku. |
| Kap. 9 | 9.1 prüft gegen A1–A7 und beantwortet F1–F4; die Tabelle dazu ist `tab:abgleich` in 8.5.1. |

Labels: aus dem Gerüst unverändert `chap:handlungsbedarf`, `sec:handlungsbedarf`, `sec:anforderungen`,
`sec:bewertungsmethodik`, `sec:kennzahlen`, `sec:versuchsplan`, `sec:testumgebung`. Neu: `tab:defizite`,
`tab:anforderungen`, `fig:bewertungslogik`, `tab:kennzahlen`, `tab:versuchsplan`, `tab:testumgebung`.

Kürzel im Text: D1–D4, A1–A7, K-Nummern (K2.1 = erste Kennzahl zu A2), V1–V11. Alle werden in Kap. 8 wieder benutzt.
Sie werden beim ersten Auftreten eingeführt und stehen nicht im Abkürzungsverzeichnis.

## 3 Belegstrategie

Kap. 5 enthält vier Arten von Aussagen. Jeder Schreib-Auftrag muss sie unterscheiden.

| Art | Beispiel | Behandlung im Text |
|---|---|---|
| **T – Tatsache aus der Literatur** | „Der Simulator des Herstellers unterstützt nur die Entwicklung auf niedriger Ebene.“ | `\cite{Key}\ev{Key.NN}` mit vorhandenem Beleg, zusätzlich Rückverweis auf den Abschnitt in Kap. 2–4. Fehlt der Beleg: `\qf{…}`. |
| **W – Wertung** | „Keine der betrachteten Arbeiten verbindet …“ | Eigene Schlussfolgerung, kein `\cite` am Urteil. **Immer mit Geltungsbereich** („unter den in Abschnitt~\ref{sec:verwandte_arbeiten} betrachteten Arbeiten“), nie als Aussage über den gesamten Stand der Technik („es gibt kein …“). Vor dem Absatz: `% Basis: Kap. 4.4 tab:stacks; review/plan-sdt-verwandte-arbeiten.md`. Jede Tatsache, auf der das Urteil ruht, trägt im selben Absatz ihren Beleg (Art T). |
| **S – Setzung** (Anforderung, Zielwert, Wahl einer Kennzahl oder Methode) | „Die Hand bewegt sich im Realbetrieb mit höchstens 250 mm/s.“ | Braucht eine **Begründung**, keine Quelle: entweder aus einem Defizit, aus der Literatur (dann `\cite{}\ev{}` an der Herleitung) oder aus der Aufgabe. Zielwerte sind Nils' Entscheidung. Wo dieser Plan **[N?]** schreibt, setzt der Auftrag `\pruefen{Zielwert … von Nils}` und erfindet keinen Wert. |
| **E – Eigenleistung** (Testumgebung, Skripte, Attrappe) | „Die automatisierten Tests laufen ohne Roboter und ohne Simulation.“ | Kein `\cite`. Vor dem Absatz `% Basis: G1@25d5c1a <Pfad>`. Hardware- und Versionsangaben des Referenz-PCs liefert Nils, bis dahin `\pruefen{}`. Zahlen (Anzahl Tests) am Code-Stand neu zählen. |

Zusätzlich:
- **Negativbefunde sind eigene Analyse.** „Das README von g1pilot nennt keinen Simulationsbetrieb“ ist kein Zitat,
  sondern eine Auswertung. Formulierung mit Geltungsbereich und `% Basis:`-Kommentar.
- **Normbezug nur als Orientierung** (wie im Plan zu Kap. 6): kein „normgerecht“, kein „erfüllt ISO …“. Der Zielwert
  von A5 „orientiert sich an“ dem in `sec:schutzfunktionen` beschriebenen Wert.
- **Kein Ergebnis vorwegnehmen.** Die G1-Doku enthält Messwerte (Geschwindigkeitsfolge, Stoßversuche, Planungszeiten).
  Sie sind nicht am festen Code-Stand gemessen und gehören auch dann nach Kap. 8. In Kap. 5 erscheinen sie nicht,
  auch nicht als Begründung für einen Zielwert.
- **Stilregel vom 11.11.:** keine Autorennamen als Satzsubjekt. Sprache: Präsens; Anforderungen im Indikativ
  („Die Umgebung führt … aus“, „muss“ ist erlaubt), kein Konjunktiv.

## 4 Gliederung

„Kern“ = muss hinein; „Kann“ = bei Platzmangel zuerst streichen.

| Abschnitt | Umfang | Stufe | Leistet | Grundlage (Rückverweis) | Wird benutzt in | Änderung ggü. Gerüst 30.10. |
|---|---|---|---|---|---|---|
| Kapiteleinleitung | 4–5 Sätze | Kern | Anknüpfung an Kap. 2–4, Vorschau, Kette D→F→A→K→V | – | – | – |
| **5.1 Handlungsbedarf** | 1,5 S. | Kern | Defizite D1–D4, Lücke, präzisiertes Ziel, Eingrenzung | 2.1.2, 3.1, 3.4, 4.3, 4.4 | 6.1.2, 8.5.2 | gegliedert nach F1–F4 statt als Fließtext; `tab:defizite` (Kann) |
| **5.2 Anforderungen** | 2 S. | Kern | A1–A7 mit Prüfkriterium, Zielwert, Herleitung | 5.1, 3.4.2, 3.1.3 | 6 (alle Abschnitte), 7, 8.5.1, 9.1 | Kennzahlen aus dem Gerüst **lösungsneutral** umformuliert (siehe 5.2 unten); Randbedingungen ergänzt |
| **5.3 Bewertungsmethodik** | 2,5 S. | | | | | |
| 5.3.1 Zuordnung von Kennzahlen zu Anforderungen und Forschungsfragen | 0,9 S. | Kern | Nachweisarten, Kennzahlen K…, Auswahl gegenüber 3.1.3, Gütekriterien | 3.1.3, 4.3.2 | 8.1–8.4 | `fig:bewertungslogik`, `tab:kennzahlen` |
| 5.3.2 Versuchsplan | 0,9 S. | Kern | V1–V11, drei Prüfebenen, Umfang, Auswertung | 3.1.1 | 8.1–8.4 | `tab:versuchsplan`; Prüfebene „Attrappe“ ergänzt |
| 5.3.3 Testumgebung | 0,7 S. | Kern | Referenz-PC, Roboter, Code-Stand, Testsuite, Attrappe, Messmittel | 3.3.3 | 8 (alle), 7 (Verweis) | `tab:testumgebung` |

Richtlinien §5.1: 5.1 und 5.2 haben keine Unterabschnitte, 5.3 hat drei. Das ist zulässig. Innerhalb von 5.1 und 5.2
gliedern Absätze nach F1–F4, keine `\paragraph`-Überschriften.

## 5 Abschnitte im Detail

Lesehilfe: **Kernaussage** = der Satz, der hängen bleiben muss. **Kette** = Argumentationsfolge für den Text.
**Leitfragen** = Aussagen, die ein Beleg tragen muss (Art T), mit Status *abgedeckt / teilweise / offen* und
Beleg-IDs. **Befunde** = Tatsachen über das eigene System mit Fundstelle im G1-Repo (Art E, Pfade relativ zu `g1pilot/`).

### Kapiteleinleitung

- Kette: Kap. 2–4 haben den Roboter, die Werkzeuge und die verwandten Arbeiten beschrieben → Kap. 5 wertet sie,
  legt den Maßstab fest und plant die Prüfung → ein Satz je Abschnitt → Verweis auf `fig:bewertungslogik`, falls die
  Abbildung in die Einleitung wandert (→ N7).
- Keine Belege nötig.

### 5.1 Handlungsbedarf

- **Kernaussage:** Unter den betrachteten Arbeiten gibt es für den G1 leistungsfähige Werkzeuge für einzelne
  Funktionen und für Fachleute. Keine davon verbindet den durchgängigen Weg von der Simulation zum Roboter mit einer
  Bedienung für Personen ohne Robotikerfahrung, Schutzmechanismen für den Realbetrieb und offenen Schnittstellen.
- Kette (sechs Absätze):
  1. *Maßstab der Wertung:* Zielgruppe und Ziel aus 1.1/1.2 in zwei Sätzen (Anwender ohne Robotikerfahrung, die den
     Nutzen eines Humanoiden vor dem Einsatz prüfen wollen; erst Simulation, dann Roboter). Daraus vier
     Bewertungsgesichtspunkte, einer je Forschungsfrage.
  2. *D1 Durchgängigkeit (→ F1):* Gleiche Schnittstelle in Simulation und am Roboter ist verbreitet, deckt aber
     jeweils nur einen Teil ab: der Simulator des Herstellers nur die niedrige Ebene, einzelne Arbeiten nur eine
     Funktion mit Spezialhardware; andere Arbeiten bleiben ganz in der Simulation.
  3. *D2 Aussagekraft der Simulation (→ F2):* Die Übertragbarkeit ist nicht allgemein gegeben und hängt von der
     Anwendung ab. Die Literatur bewertet sie für gelernte Policies; für einen Bedien-Stack, bei dem in Simulation
     und am Roboter verschiedene Regler für die Fortbewegung arbeiten, liegt unter den betrachteten Arbeiten keine
     Bewertung vor.
  4. *D3 Bedienung und Sicherheit (→ F3):* Bedienkonzepte für Humanoide in Menschengröße setzen Spezialhardware und
     Fachwissen voraus; Werkzeuge für Personen ohne Programmiererfahrung gibt es für kleine Humanoide. Für
     zweibeinige Roboter fehlt ein passender Normenrahmen, und der energielose Zustand ist kein sicherer Zustand.
  5. *D4 Zweckbindung (→ F4):* Die Werkzeuge sind auf einen Zweck zugeschnitten (Training, Datensammlung,
     Teleoperation). Ein Anwender, der eine vorab nicht bekannte Aufgabe erproben will, findet keine gemeinsame
     Grundlage, an die sich eigene Aufgaben und Projekte andocken lassen.
  6. *Lücke, Ziel, Eingrenzung:* Zusammenführung von D1–D4 zur Lücke (mit Geltungsbereich) → präzisiertes Ziel der
     Arbeit → für wen relevant (Anwender, Folgeprojekte am Lehrstuhl) → was die Arbeit **nicht** schließt (kein
     Policy-Transfer, keine Nutzerstudie nach Stand N3, keine sicherheitstechnische Bewertung) → Überleitung zu 5.2.
- Leitfragen:
  - L1 Welches Anwendungspotenzial und welche Hemmnisse nennt die Literatur für Humanoide? – **abgedeckt**:
    Tong2024.08, .09, .10; Chi2025.01; Sekkat2024.02, .05. (Hemmnisse aus Sicht von Unternehmen: **offen**, Acatech2020
    und FAPS2024 sind freigegeben, aber ohne PDF → Q7; gehört vorrangig nach Kap. 1.1.)
  - L2 Was deckt die gleiche Schnittstelle in Simulation und am Roboter beim Hersteller ab? – **abgedeckt**:
    UnitreeMujoco.01, .02, .03; Hu2026.02 (Onboard-Regler nicht quelloffen).
  - L3 Welche Arbeiten führen denselben Code in Simulation und am G1 aus, und für welche Funktion? – **abgedeckt**:
    Durrani2026.01, .02, .03, .04 (eine Funktion, Motion-Capture-Anzug); GalbotOpenWBT.01 (real und Simulation).
    Vorsicht: Aus GalbotOpenWBT.01 folgt nicht „derselbe Code“.
  - L4 Welche Arbeiten bleiben in der Simulation oder am Roboter? – **abgedeckt**: Yu2026.03, .04, .11;
    HucebotG1Pilot.01–.04 (Simulationsbetrieb dort nicht beschrieben = Negativbefund, Art W).
  - L5 Ist der sichere Übergang von der Simulation zum Roboter gelöst? – **abgedeckt**: Tong2024.05, .06;
    Sekkat2024.03.
  - L6 Wie ausgeprägt ist die Sim-to-Real-Lücke, speziell am G1? – **abgedeckt**: He2025.07; Collins2019.09;
    Sekkat2024.09; Rückverweis `sec:sim2real`.
  - L7 Was sagt die Literatur zur Validierung von Simulationen? – **abgedeckt**: Choi2021.02, .18; Kadian2020.01;
    Durrani2026.03 (bestandene Prüfung als Indiz, nicht als Nachweis).
  - L8 Welche Voraussetzungen haben die Teleoperationssysteme? – **abgedeckt**: Fu2024.01; He2024.03;
    UnitreeXRTeleop.01, .02; Zhao2025.01; AliPour2026.01; Rückverweis `sec:teleoperation_teil`.
  - L9 Welche Werkzeuge gibt es für Nutzer ohne Robotikerfahrung, und für welche Roboter? – **abgedeckt**:
    Pot2009.01, .02, .05, .06; Ajaykumar2021.01, .03; Rückverweis `sec:laienbedienung_sdt`. Die Aussage „nur für
    kleine Humanoide“ ist Art W mit Geltungsbereich.
  - L10 Wie weit ist die Evaluation solcher Werkzeuge außerhalb des Labors? – **abgedeckt**: Ajaykumar2021.12.
  - L11 Welche Sicherheitslücke besteht für zweibeinige Roboter? – **abgedeckt**: Prather2025.01, .03, .06;
    Ding2026.03, .05; He2024.04; Tong2024.14; Rückverweis `sec:normen`, `sec:sicherheit_zweibeiner`.
    Hinweis: Ding2026 ist ein Preprint, Prather2025 graue Literatur (im Text so kennzeichnen, wie in 3.4.3).
  - L12 Wofür sind die vorhandenen Stacks gebaut? – **teilweise**: Cheng2024.01; Zhao2025.01 (Datensammlung);
    UnitreeRLMjlab.01, .06; NvidiaGR00TWBC.01 (Training und Einsatz von Reglern); Ze2025.01 (meist nur Fortbewegung
    oder Manipulation). Für „keine gemeinsame Grundlage zum Andocken“ gibt es keinen Beleg → Art W.
  - L13 Was fordert die Literatur an Modularität und Wiederverwendung? – **abgedeckt**: Macenski2022.05, .11;
    Saeedvand2019.13.
- Darstellung: `tab:defizite` (Kann), siehe Abschnitt 8. Pflicht ist der Verweis auf `tab:stacks` in 4.4.
- Stil: Hier ist Wertung erlaubt und gefordert (Richtlinien §3.4). Trotzdem keine Abwertung der Arbeiten: Sie
  verfolgen andere Ziele. Formulierung „ist nicht Gegenstand“, „richtet sich an“, nicht „versäumt“.
- Offene Punkte: Die Lücke ist nur so tragfähig wie die Recherche vom 05.11. Der Text nennt deshalb ausdrücklich den
  Betrachtungsumfang (die in Kap. 4 behandelten Arbeiten, Stand der Recherche November 2026).

### 5.2 Anforderungen

- **Kernaussage:** Sieben Anforderungen machen das Ziel prüfbar. Jede hat ein Kriterium, das sich messen oder
  eindeutig feststellen lässt, und einen Zielwert, der vor der Evaluation feststeht.
- Kette:
  1. *Herleitung:* Aus jedem Defizit folgt, was die Umgebung leisten muss. Drei Nutzergruppen bestimmen die Sicht:
     die Bedienperson ohne Robotikerfahrung, die Person, die ein eigenes Projekt andockt, und die Person in der Nähe
     des Roboters. Maßstab für eine Anforderung: lösungsneutral und prüfbar.
  2. *Tabelle* `tab:anforderungen` einführen.
  3. *Je Forschungsfrage ein Absatz*, der die Zeilen der Tabelle anspricht und Kriterium und Zielwert herleitet:
     F1 → A2; F2 → A3, A4; F3 → A5, A6; F4 → A1, A7. Die Steckbriefe in Abschnitt 6 dieses Plans sind die Vorlage.
  4. *Randbedingungen* (ein Absatz, Kann): Roboter und Hände sind gegeben, der Onboard-Regler ist nicht einsehbar,
     es steht ein handelsüblicher PC ohne Rechenbeschleuniger zur Verfügung, quelloffene Werkzeuge.
  5. *Zielkonflikte* (zwei bis drei Sätze, Kern): Schutz gegen Freiheit der Bewegung (A5 gegen A1), einfache Bedienung
     gegen Funktionsumfang (A6 gegen A1), offene Schnittstellen gegen Schutz (A7 gegen A5). Kap. 6 löst sie auf;
     hier nur benennen, mit Vorverweis.
- **Wichtigste Änderung gegenüber dem Gerüst:** Die Kennzahlen aus dem Gliederungsdokument vom 29.10. waren
  „Startwerte“ und enthalten teils schon die Lösung. Eine Anforderung, die die Lösung vorwegnimmt, lässt sich nicht
  mehr verfehlen und prüft nichts. Deshalb:

  | ID | Kennzahl im Gerüst | Problem | Im Plan |
  |---|---|---|---|
  | A2 | „Umschaltung nur per Umgebungsvariable“ | nennt den Mechanismus (Kap. 6.2.2) | „Wechsel ohne Änderung am Programmcode, nur über Konfiguration“ |
  | A3 | „Physik 1 kHz, Lauf-Regler 50 Hz, Armregler 250 Hz“ | Auslegungswerte aus Kap. 7 | Echtzeitfaktor und Takttreue auf dem Referenz-PC; die Solltakte nennt Kap. 7 |
  | A4 | „Abweichung für ausgewählte Größen“ | offen, welche Größen, kein Zielwert | zwei benannte Größen für die Arme mit Zielwert aus der Aufgabe; Fortbewegung nur als Charakterisierung |
  | A5 | „Gelenk ≤ 1,5 rad/s, Notaus < x ms“ | 1,5 rad/s ist Auslegungswert (6.3.2) | nur hergeleitete Werte; fünf Teilkriterien |
- Leitfragen (für die Herleitung der Zielwerte):
  - L14 Woran orientiert sich eine Grenze für die Geschwindigkeit der Hand? – **abgedeckt**: Villani2018.09
    (250 mm/s als Grundannahme der ISO/TS 15066); DGUV2015.04 (Betriebsart mit reduzierter Geschwindigkeit, höchstens
    250 mm/s mit Zustimmungsschalter und Tippschaltung). Beide gelten für Industrieroboter bzw. kollaborativen
    Betrieb → nur Orientierung; Geltungsbereich DGUV2015.01, .02; Prather2025.05 (ISO/TS 15066 nur für fixierte oder
    statisch stabile Roboter).
  - L15 Was verlangt der Rechtsrahmen vom Not-Halt? – **abgedeckt**: MRL2006.08, .09 (jederzeit verfügbar, unabhängig
    von der Betriebsart); MRL2006.04 (vorhersehbare Bedienungsfehler); Rückverweis `sec:schutzfunktionen`.
  - L16 Warum genügt beim Zweibeiner kein Abschalten? – **abgedeckt**: Ding2026.03, .08, .09; Prather2025.03;
    Subburaman2023.02, .10.
  - L17 Welche Zeit gilt als Bezug für die Reaktion eines Halts? – **offen** (Normen zum Not-Halt liegen ohne PDF in
    `_Vorschläge`) → Q6. Ohne Beleg ist der Zielwert eine reine Setzung von Nils.
  - L18 Was heißt „Echtzeit“ bei einer Physiksimulation, und wie wird der Echtzeitfaktor bestimmt? – **offen**
    (offenes `\qf` in 3.1.3) → Q2. Choi2021.10 nennt nur eine Größenordnung für Starrkörpermodelle (Stand 2020).
  - L19 Wie misst die Literatur Gebrauchstauglichkeit bei Nutzern ohne Robotikerfahrung? – **abgedeckt**:
    Ajaykumar2021.09 (SUS), .10 (NASA-TLX), .11 (Fehler).
  - L20 Welche Anforderungen an Zugänglichkeit nennen vergleichbare Werkzeuge? – **abgedeckt**: Pot2009.03, .04, .06.
  - L21 Welche Größen nutzt die Literatur für den Vergleich Simulation/Roboter bei Armbewegungen? – **abgedeckt**:
    Collins2019.03, .06; He2025.09; Rückverweis `sec:abbildungsguete`.
  - L22 Methodik der Anforderungsermittlung (prüfbare Anforderungen, Fest- und Wunschforderungen) – **offen** → Q1.
    Ohne Quelle entfällt die Einteilung in Fest- und Wunschforderungen; die Tabelle kommt auch ohne sie aus.
- Darstellung: `tab:anforderungen` (Kern, zentrale Tabelle der Arbeit).

### 5.3.1 Zuordnung von Kennzahlen zu Anforderungen und Forschungsfragen

- **Kernaussage:** Jede Forschungsfrage wird über ihre Anforderungen und deren Kennzahlen beantwortet; für jede
  Kennzahl steht fest, wie sie bestimmt wird.
- Kette:
  1. `fig:bewertungslogik` einführen: die Kette D → F → A → K → V → Abschnitt in Kap. 8.
  2. *Vier Nachweisarten:* Analyse (des Programmcodes und der Konfiguration), Test (automatisiert, mit festem
     Soll-Ergebnis), Messung (Kennzahl mit Einheit), Demonstration (Funktion wird am Roboter gezeigt und
     protokolliert). Begründen, warum nicht alles gemessen wird: A2, A1, A7 sind Eigenschaften des Aufbaus und lassen
     sich nur durch Analyse und Demonstration zeigen.
  3. `tab:kennzahlen` einführen und nach Forschungsfragen durchgehen (Inhalt: Abschnitt 7.1 dieses Plans).
  4. *Auswahl gegenüber 3.1.3:* übernommen wird der Vergleich derselben Bewegung in Simulation und am Roboter über
     der Zeit mit einem Abstandsmaß. Nicht anwendbar sind: der Korrelationskoeffizient über mehrere Verfahren (es wird
     nur ein System bewertet), die Referenz über ein Motion-Capture-System (nicht vorhanden, Bezug sind die
     Gelenkwinkelgeber des Roboters), der Vergleich zweier Simulatoren (nur ein Simulator) und der Return (keine
     gelernte Policy als Untersuchungsgegenstand).
  5. *Gütekriterien* (Richtlinien §3.4): Objektivität durch Skripte statt Handmessung, Reliabilität durch
     Wiederholungen und festen Code-Stand, Validität mit ihren Grenzen (Gelenkwinkel statt absoluter Lage;
     Bedienaufwand statt Gebrauchstauglichkeit; Attrappe statt Roboter). Die Grenzen hier nennen, nicht erst in 8.5.3.
- Leitfragen:
  - L23 Vergleich gegen eine externe Referenz und Abstandsmaß – **abgedeckt**: Collins2019.03, .04, .06.
  - L24 Vergleich derselben Trajektorie in zwei Umgebungen – **abgedeckt**: He2025.09; Erez2015.13, .14.
  - L25 Vorhersagekraft statt Realismus – **abgedeckt**: Kadian2020.01, .02, .03 (als nicht anwendbar begründen).
  - L26 Auswertung nur eines Zeitfensters zur Begrenzung von Modellunsicherheit – **abgedeckt**: Acosta2022.08 (Kann).
  - L27 Vergleich eines digitalen Zwillings mit dem realen Roboter als Bewertungsweg – **abgedeckt**: Sekkat2024.07.
  - L28 Grenzen von Laborstudien bei der Bewertung der Bedienung – **abgedeckt**: Ajaykumar2021.12.
- Darstellung: `fig:bewertungslogik` (Kern, einzige Abbildung des Kapitels), `tab:kennzahlen` (Kern).

### 5.3.2 Versuchsplan

- **Kernaussage:** Geprüft wird auf drei Ebenen mit wachsendem Aufwand und wachsender Aussagekraft: gegen eine
  Attrappe des Roboters, in der Simulation, am realen Roboter. Wo möglich, werden in Simulation und am Roboter
  dieselben Kennzahlen mit denselben Skripten bestimmt.
- Kette:
  1. *Drei Prüfebenen* und was jede zeigen kann:
     - *Attrappe:* Die Programme für den Realbetrieb laufen unverändert gegen nachgebildete Antworten des Roboters.
       Zeigt die Logik der Schutzmechanismen ohne Gefährdung, auch für Fehlerfälle, die am Roboter nicht gefahrlos
       auslösbar sind. Zeigt nicht das Verhalten der Mechanik.
     - *Simulation:* Verhalten mit Physik, wiederholbar und ohne Risiko.
     - *Roboter:* Übertragbarkeit. Aufwendig, wenige Wiederholungen, nur unter Sicherung.
  2. *Grundsätze:* erst Simulation, dann Roboter; gleiche Kennzahlen; fester Code-Stand; jede Messung mit Skript und
     Rohdaten ablegbar; Wiederholungen und Angabe von Mittelwert und Spannweite; bei wenigen Wiederholungen keine
     statistischen Tests.
  3. `tab:versuchsplan` einführen und nach Kap.-8-Abschnitten durchgehen (Inhalt: Abschnitt 7.2 dieses Plans).
  4. *Sicherung der Versuche am Roboter* (zwei Sätze, Art E): Roboter am Kran gesichert, zweite Person mit der
     Fernbedienung des Herstellers. Basis `docs/50-A-Echter-Roboter.md` Abschnitt F.
  5. *Was der Plan nicht enthält:* keine Nutzerstudie (nach Stand N3), keine Messung des Gangverhaltens des
     Onboard-Reglers gegen die Simulation als Gütemaß (verschiedene Regler, siehe A4), keine Dauerläufe.
- Leitfragen:
  - L29 Nutzen der Simulation als Testumgebung (wiederholbar, kontrolliert, ohne Risiko) – **abgedeckt**:
    Choi2021.03, .05; Sekkat2024.03; Rückverweis `sec:sim_zwecke`.
  - L30 Physischer Test bleibt nötig – **abgedeckt**: Choi2021.02.
  - L31 Test von Steuerungssoftware gegen ein nachgebildetes Gegenstück (Software- bzw. Hardware-in-the-Loop) –
    **teilweise**: Mihalic2022.04, .07, .08 (dort für Steuergeräte; in 3.1.1 steht dazu ein offenes `\qf`). Die
    Attrappe nur als **Analogie** einordnen oder ohne Literaturbezug als Eigenleistung beschreiben → Q5.
  - L32 Simulationsbasiertes Testen von Robotiksoftware in der Praxis – **offen** (Afzal 2021 liegt in `_Vorschläge`,
    DF5GV737) → Q5.
- Befunde (Art E, Basis für die Spalte „Mittel“ in `tab:versuchsplan`): siehe Abschnitt 7.3.
- Darstellung: `tab:versuchsplan` (Kern).

### 5.3.3 Testumgebung

- **Kernaussage:** Alle Messungen beziehen sich auf einen festen Code-Stand, einen beschriebenen Referenz-PC und
  einen beschriebenen Roboter; damit sind sie wiederholbar.
- Kette: Referenz-PC und Softwarestände (`tab:testumgebung`) → Roboter und Hände → Code-Stand → automatisierte Tests
  (Umfang, Gruppen, was sie nicht abdecken) → Attrappe (was sie nachbildet, Grenzen) → Messmittel.
- Befunde (Art E; **jede Zahl am Code-Stand neu ermitteln**):
  - Automatisierte Tests: laufen ohne Roboter und ohne laufende Simulation; die Programme des Realbetriebs
    (Armregler, Anbindung des Onboard-Reglers) laufen gegen eine Attrappe mit nachgebildeter Herstellerschnittstelle;
    Bedienoberflächen laufen ohne Bildschirm. `docs/60-A-Tests.md` „Unit- und Integrationstests“.
  - Umfang: 597 Testfunktionen in 49 Dateien unter `test/` (eigene Zählung 16.11. mit `grep -c "def test_"`; die
    Doku nennt noch „rund 550 in 43 Dateien“ → es gilt die Zählung am festen Stand).
  - Gruppen der Testsuite, darunter eine Gruppe „sicherheit“ (Not-Halt, Totmann, Moduswechsel, Bodenkontakt,
    Armregler im Realbetrieb, Planer, Smartphone-Anbindung). `test/run_tests.sh`, `docs/60-A-Tests.md`.
  - Was die Tests nicht abdecken: den realen Roboter, die echte Funkverbindung des Smartphones, Anzeige und
    Vibration echter Gamepads. `docs/60-A-Tests.md` „Was nicht abgedeckt ist“. **Im Text nennen.**
  - Fehlen Abhängigkeiten, werden ganze sicherheitsrelevante Testdateien übersprungen; ein solcher Lauf ist kein
    Nachweis. Folge für die Methodik: Ein Testlauf zählt nur, wenn kein Test übersprungen wurde.
  - Attrappe: `test/test_arm_controller_real.py` (Klasse `FakeG1`), `test/test_loco_client_real.py` (`FakeLoco`);
    für Messungen des Befehlsstroms eine Variante mit einfachem Gelenkmodell (`test/teleop_jitter_probe.py`; dort
    steht ausdrücklich, dass die Zahlen nur zum Vergleich taugen, nicht als Absolutwerte).
  - Ende-zu-Ende-Prüfungen gegen die laufende Simulation und Versuche ohne Middleware direkt im Simulator:
    `docs/60-A-Tests.md` „Ende-zu-Ende“ und „Headless-MuJoCo“.
  - Voraussetzungen laut Installationsanleitung: Linux (getestet Ubuntu 22.04/24.04) oder Windows mit WSL2,
    mindestens 8 GB Arbeitsspeicher, keine Grafikkarte für die Physik nötig. `docs/01-A-Installation.md`
    „Voraussetzungen“. Das ist die Angabe der Doku, nicht die Beschreibung des Referenz-PCs.
- `tab:testumgebung` (schlichter Stil, zwei Spalten Merkmal · Wert): Prozessor, Arbeitsspeicher, Grafik,
  Betriebssystem, Container-Laufzeit, ROS-2-Version, MuJoCo-Version, Version des Hersteller-SDK, Code-Stand der
  Umgebung, Roboter (Modell, Ausführung, Softwarestand), Hände. Alle Werte `\pruefen{}`, bis Nils sie liefert (→ N4);
  Softwareversionen aus den Dockerfiles am Code-Stand (Arbeitspaket AP1).
- Leitfragen:
  - L33 Warum Container die Wiederholbarkeit stützen – **abgedeckt**: Boettiger2015.02, .06; Cervera2019.01, .02;
    Rückverweis `sec:container` (nur ein Satz).
  - L34 Einfluss von Hardware und Energiesparfunktionen auf Zeitmessungen – **abgedeckt**: Kronauer2021.12, .13
    (begründet, warum der Referenz-PC beschrieben wird); Kronauer2021.05 als Muster für die Angabe der Messrechner.
- Darstellung: `tab:testumgebung` (Kern).

## 6 Anforderungen A1–A7 (Steckbriefe)

Die Steckbriefe sind die Vorlage für `tab:anforderungen` und die Absätze in 5.2. **Wortlaut und Zielwerte sind
Vorschläge**; alles mit [N?] entscheidet Nils (→ N2). Bedeutung und Reihenfolge von A1–A7 entsprechen dem Gerüst und
den Plänen zu Kap. 6 und 7 und dürfen sich nicht verschieben.

Nachweisarten: An = Analyse, T = Test, M = Messung, D = Demonstration.

### A1 Aufgabenunabhängigkeit (F4, aus D4)

- Wortlaut: Die Umgebung stellt die Grundfähigkeiten Gehen, Armbewegung und Greifen einzeln und kombiniert bereit.
  Eine neue Aufgabe lässt sich einrichten, ohne den Programmcode zu ändern.
- Herleitung: D4 (Werkzeuge sind zweckgebunden); Vorbild vorgefertigter Bausteine Pot2009.05, .06.
- Kriterien: **K1.1** Abdeckung der Grundfähigkeiten (drei Fähigkeiten, je in Simulation und Realbetrieb, einzeln
  und kombiniert), Zielwert: vollständig. **K1.2** geänderte Zeilen Programmcode für eine neue Beispielaufgabe (neue
  Szene und neuer Ablauf), Zielwert: 0. **K1.3** Zeit für das Einrichten der Beispielaufgabe (nur berichtet, kein
  Zielwert).
- Nachweis: D, An → V11 (8.4.2); K1.1 auch aus V2. Konzept: 6.4.3, 6.5.1.
- Grenze, die 5.2 nennen muss: „Aufgabe“ heißt hier eine feste Folge von Bewegungen ohne Wahrnehmung der Umgebung.

### A2 Einheitliche Ausführung in Simulation und Realbetrieb (F1, aus D1)

- Wortlaut: Derselbe Programmstand steuert die Simulation und den realen G1. Der Wechsel erfordert keine Änderung am
  Programmcode, nur eine Änderung der Konfiguration.
- Herleitung: D1; Übertragungsargument Durrani2026.03.
- Kriterien: **K2.1** geänderte Zeilen Programmcode beim Wechsel, Zielwert: 0. **K2.2** Stellen im Programmcode, an
  denen sich das Verhalten zwischen Simulation und Realbetrieb unterscheidet: Anzahl und Art, Zielwert: vollständig
  erfasst und jede begründet (kein Zahlenziel). **K2.3** Funktionen, die in Simulation und Realbetrieb mit derselben
  Bedienung ausführbar sind, Zielwert: alle außer den in 6.2.2 ausgewiesenen.
- Nachweis: An → V1 (8.1.1); D → V2 (8.1.2), V3 (8.1.3). Konzept: 6.2.
- Befund für die Planung (Art E, nicht in Kap. 5): Am Stand `25d5c1a` fragen 13 Dateien unter `g1pilot/` und
  `launch/` die Betriebsart ab (grobe Suche nach `sim_mode`, `SIM_MODE`, `is_sim`); der Schalter selbst steht in
  `g1pilot/utils/common.py`. Außerdem gibt es getrennte Container-Images für Simulation und Realbetrieb. A2 darf
  deshalb **nicht** „identischer Code ohne Unterschiede“ versprechen. Ehrlich ist: gleicher Programmstand, Unterschiede
  gezählt und begründet. → N2.

### A3 Echtzeitfähigkeit auf einem Standard-PC (F2, aus D2)

- Wortlaut: Die Simulation und die Regelkreise der Umgebung laufen auf einem handelsüblichen PC ohne
  Rechenbeschleuniger in Echtzeit.
- Herleitung: Die Bedienung in der Simulation soll sich zeitlich wie am Roboter verhalten (sonst ist D2 nicht
  prüfbar); niedrige Einstiegshürde (D3). Für „handelsüblich“ und den Zielwert gibt es keinen Literaturbeleg (L18).
- Kriterien: **K3.1** Echtzeitfaktor (simulierte Zeit je verstrichener Zeit), Zielwert [N?] (Vorschlag: im Mittel
  mindestens 0,95). **K3.2** Takttreue je Regelkreis (erreichte Rate je Sollrate, dazu Streuung der Zykluszeit),
  Zielwert [N?] (Vorschlag: mindestens 95 % der Sollrate). Die Sollraten sind Auslegungswerte aus Kap. 7.
- Nachweis: M → V4 (8.2.1). Konzept: 6.2.2; Umsetzung 7.2.2, 7.4.1.
- Hinweis: Die G1-Doku beschreibt, dass die Simulation ihren Takt an die Regelung koppelt und nach oben auf
  Echtzeit begrenzt (`docs/40-T-Simulation.md` „Lockstep“). Der Echtzeitfaktor kann deshalb 1 nicht überschreiten;
  gemessen wird, wie weit er darunter liegt. Ein Messwert liegt im Repo nicht vor.

### A4 Realitätsnahe Simulation (F2, aus D2)

- Wortlaut: Eine in der Simulation eingerichtete Armbewegung verläuft am realen Roboter so, dass die Abweichung
  innerhalb einer für die Aufgabe festgelegten Toleranz bleibt. Für die Fortbewegung sind die Abweichungen zwischen
  Simulation und Realbetrieb bestimmt und benannt.
- Herleitung: D2; Vergleichsweg der Literatur Collins2019.03, .06; He2025.09. „Realitätsnah“ wird damit auf zwei
  benannte Größen eingegrenzt.
- Kriterien: **K4.1** Abweichung der Gelenkwinkel der Arme zwischen Simulation und Realbetrieb bei gleicher
  Bewegungsfolge (Verlauf über der Zeit, mittlere und größte Abweichung). **K4.2** daraus berechnete Abweichung der
  Handposition am Ende jeder Bewegung, Zielwert [N?] (aus der Toleranz der Greifaufgabe ableiten). **K4.3**
  Fortbewegung: Verhältnis von erreichter zu vorgegebener Geschwindigkeit in Simulation und Realbetrieb
  nebeneinander, **ohne Zielwert** (Charakterisierung).
- Nachweis: M → V7 (8.2.3), V5 (8.2.2). Konzept: 6.2.2, 6.2.3.
- Grenze, die 5.2 nennen muss: Für die Fortbewegung arbeiten in Simulation und Realbetrieb verschiedene Regler
  (6.2.3). Die Simulation soll das Gangbild des realen Reglers nicht abbilden; gefordert ist nur, dass dieselben
  Befehle in beiden Fällen wirken (A2). Bezug der Messung sind die Gelenkwinkelgeber des Roboters, keine externe
  Referenz.
- **Risiko:** Für K4.1–K4.3 liegen im G1-Repo keine Daten vom realen Roboter. Ohne Versuch V7 bleibt A4 für den
  Realbetrieb unbelegt und F2 nur für die Simulation beantwortet. → N1.

### A5 Sicherheit im Realbetrieb (F3, aus D3)

- Wortlaut: Ein Bedienfehler oder der Ausfall eines Bedienwegs führt am realen Roboter nicht zu einer unbegrenzten
  Bewegung. Bewegungen der Arme sind begrenzt, ein Halt ist jederzeit auslösbar, und der Halt bringt den stehenden
  Roboter nicht zum Sturz.
- Herleitung: D3; MRL2006.04, .08, .09 (Orientierung); Ding2026.03, .08; Prather2025.03.
- Kriterien: **K5.1** größte Geschwindigkeit der Hand im Realbetrieb, Zielwert: höchstens 250 mm/s (Orientierung an
  Villani2018.09, DGUV2015.04). **K5.2** Verfügbarkeit des Not-Halts: Anteil der Kombinationen aus Bedienweg und
  Betriebszustand, in denen er auslösbar ist, Zielwert: alle. **K5.3** Reaktionszeit vom Auslösen des Not-Halts bis
  zum geänderten Befehl an der Herstellerschnittstelle, Zielwert [N?]. **K5.4** Zeit vom Ausfall eines Bedienwegs
  oder der Verbindung bis zum Halt der Bewegung, Zielwert [N?]. **K5.5** Anteil bestandener sicherheitsrelevanter
  Tests, Zielwert: alle, kein Test übersprungen. **K5.6** Der Roboter bleibt nach einem Not-Halt der Arme stehen
  (Demonstration).
- Nachweis: T, M → V8 (8.3.1); D → V2 (8.1.2). Konzept: 6.3.
- Abgrenzung: Auslegungswerte (Gelenkgeschwindigkeit, Beschleunigung, Zeitüberwachungen) stehen nur in
  `tab:schutzmechanismen`. Die Schutzmechanismen sind Softwarefunktionen ohne sicherheitstechnische Bewertung;
  A5 fordert keine Normerfüllung. Dieser Satz gehört wörtlich sinngemäß in 5.2.

### A6 Bedienbarkeit ohne Vorerfahrung (F3, aus D3)

- Wortlaut: Eine Person ohne Robotik- und Programmiererfahrung nimmt die Umgebung in Betrieb und führt die
  Grundfähigkeiten aus, ohne Programmcode zu schreiben.
- Herleitung: D3; Ajaykumar2021.01, .03; Pot2009.03, .04.
- Kriterien: **K6.1** Inbetriebnahme: Anzahl der Schritte und Zeit von einem frisch eingerichteten PC bis zur ersten
  Bewegung in der Simulation, Zielwert [N?]. **K6.2** Bedienung: Anzahl der Bedienhandlungen von der gestarteten
  Umgebung bis zur ersten Arm- und zur ersten Gehbewegung, Zielwert [N?]. **K6.3** Grundfähigkeiten ohne
  Programmierung und ohne Befehlszeile nach dem Start ausführbar (ja/nein je Fähigkeit). **K6.4** (nur mit
  Nutzerstudie, → N3) Bewertung durch Probanden, etwa mit der System Usability Scale, und Anzahl der Bedienfehler
  (Ajaykumar2021.09, .11).
- Nachweis: M, D → V9 (8.3.2). Konzept: 6.4; Umsetzung 7.1, 7.6.
- Grenze, die 5.2 und 5.3.1 nennen müssen: Schritte und Zeit messen den Aufwand, nicht die Gebrauchstauglichkeit.
  Ohne Probanden ist A6 nur über den Aufwand belegt. Die Inbetriebnahme selbst braucht laut
  `docs/01-A-Installation.md` einige Befehle an der Befehlszeile; „ohne Befehlszeile“ gilt deshalb erst nach dem
  Start (K6.3).

### A7 Erweiterbarkeit (F4, aus D4)

- Wortlaut: Ein externes Projekt lässt sich über dokumentierte Schnittstellen anbinden, ohne den Kern der Umgebung
  zu ändern.
- Herleitung: D4; Macenski2022.05, .11.
- Kriterien: **K7.1** geänderte Zeilen im Kern der Umgebung für die Anbindung, Zielwert: 0. **K7.2** Aufwand der
  Anbindung (Zeilen Programmcode auf der Seite des Projekts, Arbeitszeit; nur berichtet). **K7.3** Anzahl der
  gezeigten Schnittstellen (von den in 6.5.1 beschriebenen), Zielwert: mindestens eine am Beispielprojekt.
- Nachweis: D, An → V10 (8.4.1). Konzept: 6.5.
- **Risiko:** Ohne ein tatsächlich angebundenes Projekt bleibt A7 konzeptionell (gleiche Frage wie N10 im Plan zu
  Kap. 6). → N5.

## 7 Kennzahlen und Versuchsplan

### 7.1 Inhalt von `tab:kennzahlen`

Spalten: Kennzahl · Bestimmung (Größe und Einheit) · Nachweisart · Anforderung · Frage. Zeilen: K1.1 bis K7.3 aus
Abschnitt 6, zusammengefasst auf höchstens 14 Zeilen (K1.3, K6.4, K7.2 als Fußnote oder im Text, wenn die Tabelle
sonst über eine Seite geht). Reihenfolge nach Forschungsfragen F1–F4, nicht nach A-Nummer (also A2, A3, A4, A5, A6,
A1, A7), damit die Tabelle zur Gliederung von Kap. 8 passt.

### 7.2 Inhalt von `tab:versuchsplan`

Spalten: Versuch · Gegenstand · Prüfebene (Attrappe / Simulation / Roboter) · Kennzahlen · Umfang · Auswertung in.
„Umfang“ (Anzahl Wiederholungen, Dauer) ist überall [N?] und hängt an N1.

| Versuch | Gegenstand | Ebene | Kennzahlen | Auswertung in | Mittel am Stand `25d5c1a` |
|---|---|---|---|---|---|
| V1 | Vergleich von Programmcode und Konfiguration zwischen Simulation und Realbetrieb | Analyse | K2.1, K2.2 | 8.1.1 `sec:eval_code` | machbar am Repo; Auswerteskript fehlt (einfach) |
| V2 | Funktionsprüfung am realen G1 nach festem Protokoll: Verbinden, Arme übernehmen und zurückgeben, Greifen, Gehen, Not-Halt | Roboter | K2.3, K1.1, K5.6 | 8.1.2 `sec:eval_realtests` | Ablauf in `docs/50-A-Echter-Roboter.md` F; **Protokoll und Daten fehlen** |
| V3 | Anwendungsfall Werbevideo: genutzte Funktionen, nötige Anpassungen | Roboter | K2.3 (qualitativ) | 8.1.3 `sec:eval_video` | **Angaben von Nils** (→ N10) |
| V4 | Echtzeitfaktor und Takttreue auf dem Referenz-PC, Kann: zusätzlich auf einem schwächeren PC | Simulation, Attrappe | K3.1, K3.2 | 8.2.1 `sec:eval_echtzeit` | Sonde für den Befehlsstrom der Arme vorhanden (`test/teleop_jitter_probe.py`); **Messung des Echtzeitfaktors fehlt** |
| V5 | Fortbewegung in der Simulation je Lauf-Policy: Geschwindigkeitsfolge, Wechsel zwischen Gehen und Stehen, Stöße; dazu Geschwindigkeitsfolge am Roboter | Simulation, Kann: Roboter | K4.3 | 8.2.2 `sec:eval_fortbewegung` | Skript vorhanden (`test_agile_walk_sim.py`), Werte in der Doku vom 08.10. → am festen Stand neu messen; für den Roboter Aufzeichnung mit `g1pilot/tools/walk_diag.py` möglich, Daten fehlen |
| V6 | Manipulation in der Simulation: Planungserfolg und Planungszeit über feste Testfälle, Restfehler der inversen Kinematik, Genauigkeit im Tippbetrieb | Simulation | (stützt A4, A1) | 8.2.3 `sec:eval_manipulation` | Tippbetrieb: `jog_axis_probe_sim.py` vorhanden; **Messreihe für den Planer fehlt** |
| V7 | Vergleich Simulation gegen Roboter: dieselbe Folge gespeicherter Posen in beiden, Aufzeichnung der Gelenkwinkel | Simulation und Roboter | K4.1, K4.2 | 8.2.3 `sec:eval_manipulation` | **Aufzeichnungsskript und Daten fehlen**; Schlüsselversuch für F2 |
| V8 | Schutzmechanismen: automatisierte Tests der Gruppe „sicherheit“; größte Geschwindigkeit der Hand bei provozierten Zielsprüngen; Reaktionszeit des Not-Halts; Ausfall eines Bedienwegs | Attrappe, Kann: Roboter | K5.1–K5.5 | 8.3.1 `sec:eval_sicherheit` | Tests vorhanden (`test/run_tests.sh sicherheit`); **Zeitmessung fehlt** |
| V9 | Bedienaufwand: frisch eingerichteter PC bis erste Bewegung; gestartete Umgebung bis erste Arm- und Gehbewegung | Simulation, Kann: Roboter | K6.1–K6.3 (K6.4) | 8.3.2 `sec:eval_bedienaufwand` | Schrittfolgen in `docs/01-A-Installation.md`, `docs/50-A-Echter-Roboter.md` „Kurzfassung“; **Zeiten fehlen** |
| V10 | Anbindung eines externen Projekts | Simulation, Kann: Roboter | K7.1–K7.3 | 8.4.1 `sec:eval_extern` | **Projekt offen** (→ N5); Beispiel-Client in `examples/arm_api/` ist kein externes Projekt |
| V11 | Neue Aufgabe: neue Szene und neuer Ablauf, in der Simulation eingerichtet, am Roboter ausgeführt | Simulation, Roboter | K1.1–K1.3 | 8.4.2 `sec:eval_aufgaben` | Werkzeuge vorhanden (Szenen-Editor, Abläufe); **Durchführung fehlt** |

Der Abgleich aller Anforderungen steht in 8.5.1 (`tab:abgleich`: Anforderung · Kriterium · Zielwert · Ergebnis ·
erfüllt / teilweise / nicht erfüllt). Eine verfehlte Anforderung ist zulässig und wird benannt (Richtlinien §13.2).

### 7.3 Folgen für das G1-Repo (keine Textarbeit, nur nach Nils' Freigabe)

Damit der Versuchsplan ausführbar ist, fehlen fünf Messmittel. Sie sind klein, müssen aber vor den Realversuchen
fertig sein, weil am Roboter nicht nachgemessen werden kann:

1. Auswertung der Betriebsart-Abfragen im Programmcode (V1).
2. Messung des Echtzeitfaktors und der Takte über eine feste Dauer (V4).
3. Aufzeichnung der Gelenkwinkel der Arme mit Zeitstempel, gleich in Simulation und am Roboter, nur lesend (V7).
4. Zeitmessung vom Auslösen des Not-Halts bis zum Befehl an der Herstellerschnittstelle, gegen die Attrappe (V8).
5. Feste Testfälle für den Planer mit Erfolg und Rechenzeit (V6).

## 8 Darstellungen

Alle nach `ba-grafik.tex` und CLAUDE.md („Grafiken, Diagramme, Tabellen“). Tabellen mit `\tabstil`, Gitter-Stil,
`tabularx`, Caption oben, `[htbp]`. Jede Darstellung wird im Absatz davor mit `\ref` eingeführt und danach erläutert.
Eigene Darstellungen ohne Quellenangabe in der Caption; Belege in Tabellenzellen wie im Fließtext.

| Label | Abschnitt | Stufe | Inhalt und Spezifikation |
|---|---|---|---|
| `tab:defizite` | 5.1 | Kann | Vier Zeilen D1–D4. Spalten: Defizit · Befund in den betrachteten Arbeiten (mit `\cite{}\ev{}` und Abschnittsverweis) · Forschungsfrage. Entfällt, wenn 5.1 sonst über 1,5 Seiten geht; dann trägt `tab:stacks` aus 4.4 allein. |
| `tab:anforderungen` | 5.2 | **Kern** | Sieben Zeilen A1–A7 in Nummernfolge. Spalten: Nr. · Anforderung (ein Satz) · Prüfkriterium · Zielwert · Frage · Nachweis in (`\ref` auf `sec:eval_*`). Höchstens eine Seite. Kap. 6, 7, 8 und 9 verweisen darauf. |
| `fig:bewertungslogik` | 5.3.1 | **Kern, Kernbild** | Datei `Bilder/tikz/bewertungslogik.tex`. Fünf Spalten von links nach rechts: Defizite D1–D4 → Forschungsfragen F1–F4 → Anforderungen A1–A7 → Versuche V1–V11 → Abschnitte 8.1–8.4, rechts außen ein Block „Abgleich 8.5.1“. Blöcke als `ba block`, Verbindungen als `ba pfeil`; die Zuordnung F→A als Linien (F1–A2, F2–A3/A4, F3–A5/A6, F4–A1/A7). Anforderungen in der Reihenfolge der Fragen anordnen, damit sich keine Linien kreuzen. Kennzahlen nicht einzeln zeichnen. Keine Farbe als einziger Bedeutungsträger, Breite höchstens 16 cm, nicht skalieren. |
| `tab:kennzahlen` | 5.3.1 | **Kern** | siehe 7.1. |
| `tab:versuchsplan` | 5.3.2 | **Kern** | siehe 7.2, ohne die Spalte „Mittel am Stand“ (die ist nur Planungshilfe). |
| `tab:testumgebung` | 5.3.3 | **Kern** | siehe Abschnitt 5, 5.3.3. Schlichter Stil (booktabs), zwei Spalten. |

Fünf Tabellen auf sechs Seiten sind viel. Reihenfolge beim Streichen: `tab:defizite`, dann `tab:kennzahlen` in
`tab:anforderungen` aufgehen lassen (Spalte „Prüfkriterium“ trägt dann die K-Nummern). `tab:anforderungen`,
`tab:versuchsplan` und die Abbildung bleiben.

## 9 Quellenlage, Lücken und Abhängigkeiten

**Vorhandene Belege reichen für 5.1 fast vollständig.** Kap. 5 führt keine neuen Quellen ein; es wertet aus, was
Kap. 2–4 schon zitieren. Zitierbar (alle in `zotero-map.json`, Belege in `evidence/`): Tong2024, Yu2026, Sekkat2024,
Chi2025, He2025, Collins2019, Choi2021, Kadian2020, Erez2015, Acosta2022, Durrani2026, UnitreeMujoco, UnitreeXRTeleop,
UnitreeRLMjlab, NvidiaGR00TWBC, GalbotOpenWBT, HucebotG1Pilot, Hu2026, Fu2024, He2024, Cheng2024, Zhao2025, Ze2025,
AliPour2026, Pot2009, Ajaykumar2021, Prather2025, Ding2026, Subburaman2023, MRL2006, DGUV2015, Villani2018,
Macenski2022, Saeedvand2019, Mihalic2022, Kronauer2021, Boettiger2015, Cervera2019.

**Lücken (Suchhinweise, keine Quellenangaben):**

| Nr. | Lücke | betrifft | Dringlichkeit | Suchhinweis |
|---|---|---|---|---|
| Q1 | Methodik der Anforderungsermittlung: prüfbare Anforderungen, Anforderungsliste, Fest- und Wunschforderungen | 5.2 (L22) | mittel | Lehrbuch Konstruktionsmethodik (Anforderungsliste), VDI 2221, Norm zum Requirements Engineering; UB-Katalog |
| Q2 | Definition und Bestimmung des Echtzeitfaktors einer Physiksimulation | 5.2 A3 (L18), 3.1.3 | **hoch** | Dokumentation oder Grundlagenartikel eines Simulators (Stichwort „real time factor“); in `_Vorschläge` liegt ein Beitrag zu Gazebo (BCRGB9Q7), PDF prüfen |
| Q3 | Primärquellen zur Messung der Gebrauchstauglichkeit (System Usability Scale, NASA-TLX), Begriff Gebrauchstauglichkeit | 5.2 A6, 5.3.1 | niedrig; **hoch**, falls Nutzerstudie (N3) | Originalarbeiten zu beiden Verfahren, Norm zur Gebrauchstauglichkeit |
| Q4 | Qualitätsmerkmale von Software (Modularität, Änderbarkeit, Erweiterbarkeit) als Begriffsrahmen | 5.2 A1, A7 | niedrig | Norm zum Qualitätsmodell für Softwareprodukte; Lehrbuch Softwaretechnik |
| Q5 | Testen von Robotiksoftware gegen Simulation und nachgebildete Gegenstücke; allgemeine Definition Software-in-the-Loop | 5.3.2 (L31, L32), 3.1.1 | mittel | in `_Vorschläge`: Afzal 2021 (DF5GV737); sonst Lehrbuch zu X-in-the-Loop |
| Q6 | Bezugswerte für Reaktions- und Stoppzeiten, Prüfung von Schutzfunktionen | 5.2 A5 (L17), 5.3.2 | mittel | in `_Vorschläge` ohne PDF: Norm zum Not-Halt (3RN96K4E), Valori 2021 (FUG3BW6N); über die UB |
| Q7 | Hemmnisse aus Sicht von Unternehmen beim Einstieg in humanoide Robotik | 5.1 (L1), Kap. 1.1 | mittel | Acatech2020 und FAPS2024 sind freigegeben, aber ohne PDF; Studien von Verbänden oder Forschungsinstituten |
| Q8 | Herstellerangaben zur Schnittstelle des G1 (Raten der Zustandsmeldungen) als Bezug für Solltakte | 5.2 A3 | niedrig für Kap. 5 | identisch mit Q1 im Plan zu Kap. 6 (Herstellerdoku als PDF) |

Empfehlung: Vor dem Schreiben nur Q2 schließen. Q1 und Q6 nach Nils' Entscheidung (Arbeitspaket AP0); der Rest bleibt
`\qf` oder entfällt, weil die Aussage gestrichen wird.

**Abhängigkeiten:**
- **D1 Kap. 1:** `sec:zielsetzung` muss F1–F4 und die Eingrenzung enthalten (Gerüst vorhanden, Text fehlt). Kap. 5
  kann mit den Kürzeln geschrieben werden.
- **D2 Kap. 4.4:** `tab:stacks` (Merkmalsvergleich) ist noch `\pruefen`. 5.1 verweist darauf. Die Spalten sollten zu
  D1–D4 passen: gleiche Schnittstelle in Simulation und am Roboter, Simulator, Bedienung und Zielgruppe, Halt aus
  jeder Bedienung, Schnittstelle für fremde Projekte. Jede Zelle braucht einen Beleg aus den README-PDFs. Ohne die
  Tabelle trägt 5.1 die Belege im Fließtext.
- **D3 Kap. 6 und 7:** benutzen `tab:anforderungen` und die Bedeutung von A1–A7 wie hier. Änderung für beide: A3
  nennt keine Taktraten mehr; A5 nennt nur die Geschwindigkeit der Hand als Zahl.
- **D4 Kap. 8:** ist noch nicht geplant. Dieser Plan legt die Zuordnung V1–V11 zu den Labels `sec:eval_*` fest; der
  Plan zu Kap. 8 muss sie übernehmen. Empfehlung: Kap. 8 erst planen, wenn N1 beantwortet ist.
- **D5 Daten:** Im G1-Repo liegen keine Messdaten vom realen Roboter. V2, V3, V7 und Teile von V5, V8, V9, V11
  hängen an Nils' Zugang zum Roboter (→ N1).
- **D6 Fester Code-Stand:** wie E4 im Plan zu Kap. 7. Alle Versuche laufen an einem markierten Stand; 5.3.3 nennt ihn.

**Folgen für andere Kapiteldateien** (erledigt Arbeitspaket AP7 bzw. der jeweilige Kapitel-Auftrag):
- `Kapitel/04_…tex`, 4.4: Merkmalstabelle dort einfügen, Label `tab:stacks`; das `\pruefen` verweist bisher auf
  „hier oder in Kap. 5.1“.
- `Kapitel/08_Evaluation.tex`: Kommentare im Gerüst um die Versuchsnummern V1–V11 ergänzen; `tab:abgleich` in 8.5.1.
- `Kapitel/03_…tex`, 3.1.3: Der Schlusssatz verweist schon auf `sec:bewertungsmethodik`; nach Q2 das `\qf` zum
  Echtzeitfaktor schließen.

## 10 Fragen an Nils

Reihenfolge nach Gewicht. Zu jeder Frage steht, wie der Plan ohne Antwort weiterläuft.

- **N1 Realversuche:** Bis wann ist Abgabe, und wie oft kommst du bis dahin noch an den G1? Davon hängt ab, ob V2, V7
  und V11 stattfinden. Ohne Antwort: Die Versuche stehen im Plan; fällt einer aus, wird die Anforderung in 8.5.1 als
  „nicht nachgewiesen“ geführt und in 8.5.3 als Grenze genannt.
- **N2 Zielwerte:** Passen Wortlaut und Zielwerte in Abschnitt 6? Offen sind A3 (Echtzeitfaktor, Takttreue), A4
  (Toleranz an der Hand), A5 (Reaktionszeit, Ausfallzeit) und A6 (Schritte, Zeit). Außerdem: Bist du einverstanden,
  dass A2 „gleicher Programmstand, Unterschiede gezählt und begründet“ heißt statt „identischer Code“? Ohne Antwort:
  `\pruefen` an jedem offenen Zielwert.
- **N3 Nutzerstudie:** Sollen drei bis fünf Personen ohne Robotikerfahrung die Simulation bedienen (Fragebogen,
  Fehler zählen)? Das würde A6 deutlich stärken, kostet aber etwa einen Tag und zwei weitere Quellen. Ohne Antwort:
  keine Studie; A6 wird über den Aufwand belegt, die Studie steht im Ausblick.
- **N4 Referenz-PC:** Auf welchem Rechner wird gemessen (Prozessor, Arbeitsspeicher, Grafik, Betriebssystem)? Gibt es
  einen zweiten, schwächeren PC für A3? Ohne Antwort: `\pruefen` in `tab:testumgebung`.
- **N5 Externes Projekt:** Welches Projekt wird für V10 angebunden (gleiche Frage wie N10 im Plan zu Kap. 6)? Ohne
  Antwort: A7 bleibt konzeptionell.
- **N6 Umfang:** 6 Seiten statt ca. 5? Ohne Antwort: 6 Seiten, `tab:defizite` entfällt.
- **N7 Tabellen und Kernbild:** Merkmalstabelle der Stacks in 4.4 und in 5.1 nur die Auswertung (Empfehlung), oder
  eine Bewertungstabelle in 5.1? Soll `fig:bewertungslogik` in 5.3.1 stehen (Empfehlung) oder schon in der
  Kapiteleinleitung?
- **N8 Aufgabenstellung:** Gibt es eine schriftliche Aufgabenstellung des Lehrstuhls für die Arbeit? Vorgaben daraus
  wären die stärkste Begründung für einzelne Anforderungen. Ohne Antwort: Herleitung nur aus den Defiziten.
- **N9 Bisherige Realtests:** Zu den Tests vom Oktober (in der G1-Doku erwähnt): Gibt es Aufzeichnungen, Videos oder
  Notizen, und dürfen sie als Datenbasis für V2 dienen? Ohne Antwort: zählen nicht, V2 wird neu protokolliert.
- **N10 Werbevideo:** Wann, mit welchen Funktionen, was musste angepasst werden? Wird für V3 gebraucht.
- **N11 Messmittel:** Sollen die fünf fehlenden Messmittel aus Abschnitt 7.3 im G1-Repo gebaut werden? Ohne Antwort:
  nicht; die betroffenen Versuche bleiben offen.
- **N12 Recherche:** Sollen die Lücken Q1, Q2, Q5, Q6 recherchiert werden (Arbeitspaket AP0)? Ohne Antwort: nur Q2.

## 11 Arbeitspakete

Reihenfolge: AP0 (optional) → AP1 und AP2 parallel → AP3 → AP4, AP5, AP6 parallel → AP7 → AP8. Jedes Paket schreibt
in eine eigene Datei unter `review/kap5-entwurf/`; erst AP7 fasst in `Kapitel/05_Handlungsbedarf_Methodik.tex`
zusammen. Empfohlene Modelle: Sonnet für AP1, AP2, AP3; Opus für AP4, AP5, AP6, AP7; Prüfung des Ergebnisses von AP7
durch Fable oder Nils. Kap. 5 ist kurz, aber jede Formulierung bindet Kap. 6–9; deshalb die Textpakete nicht an das
kleinste Modell geben.

### Rahmenprompt (jedem Auftrag voranstellen)

> Du arbeitest an Nils' Bachelorarbeit (Repo `Bachelorarbeit`, LaTeX). Lies zuerst vollständig: `CLAUDE.md`,
> `Richtlinien-BA.md` (§0.3, §3.4, §4, §6, §12, §13.2, §13.3) und `review/plan-kap5.md`. Der Plan ist verbindlich:
> Gliederung, Labels, Argumentationsketten, Abgrenzung (Abschnitt 2) und Belegstrategie (Abschnitt 3). Lies außerdem
> die Abschnitte 3.1, 3.4, 4.3 und 4.4 der Arbeit, weil Kap. 5 sie auswertet.
> Führe `python3 scripts/zot.py text` aus, bevor du Belege liest oder `check.py` startest.
> Regeln:
> 1. Tatsachen aus der Literatur (Art T): nur `\cite{Key}\ev{Key.NN}` mit den im Plan genannten Beleg-IDs. Lies den
>    Beleg in `evidence/<Key>.yaml` und schreibe nicht mehr, als das Zitat sagt; Einschränkungen und Geltungsbereich
>    bleiben erhalten. Kein passender Beleg: `\qf{…}`, Aussage nicht ausformulieren. Keine neuen Quellen, keine
>    Websuche, nichts aus dem Gedächtnis.
> 2. Wertungen (Art W): immer mit Geltungsbereich („unter den in Abschnitt~\ref{…} betrachteten Arbeiten“), nie
>    „es gibt kein …“. Vor dem Absatz ein Kommentar `% Basis: …`. Arbeiten nicht abwerten; sie verfolgen andere Ziele.
> 3. Setzungen (Art S): Jede Anforderung und jeder Zielwert braucht im Text eine Begründung. Zielwerte, die der Plan
>    mit [N?] markiert und zu denen keine Antwort von Nils vorliegt: `\pruefen{Zielwert für … festlegen}`. Keinen
>    Wert erfinden, auch keinen „typischen“.
> 4. Eigenleistung (Art E): kein `\cite`, vor dem Absatz `% Basis: G1@25d5c1a <Pfad>, <Abschnitt>`. Jede Zahl am
>    Code-Stand nachzählen. Angaben zum Referenz-PC und zum Roboter liefert Nils: `\pruefen{…}`.
> 5. Kap. 5 enthält **kein Messergebnis** und **keine Lösung**: keine Komponenten, Bedienwege, Dateinamen,
>    Taktraten oder Auslegungswerte der Schutzmechanismen, keine Zahlen aus der G1-Doku.
> 6. Normen nur als Orientierung: nie „normgerecht“ oder „erfüllt …“. Preprints und graue Literatur wie in
>    Abschnitt 3.4.3 der Arbeit kennzeichnen.
> 7. Stil: Präsens, kein ich/wir/man, kein Konjunktiv, Sach-Subjekte, keine Autorennamen als Satzsubjekt, ein
>    Argument je Absatz mit Kernsatz zuerst, mindestens zwei Sätze je Absatz. Einheitliche Begriffe: Realbetrieb,
>    Onboard-Regler, Lauf-Policy, Not-Halt, Herstellerschnittstelle, Attrappe des Roboters, Referenz-PC,
>    Echtzeitfaktor, Takttreue, Prüfkriterium, Zielwert.
> 8. Jede Tabelle und Abbildung wird im Absatz davor mit `\ref` eingeführt und danach erläutert; Umgebung mit
>    `[htbp]` direkt nach diesem Absatz.
> 9. Schreibe nur in die Datei, die dein Auftrag nennt. Ändere keine generierten Dateien und nichts in Zotero.
> 10. Bericht am Ende: was geschrieben ist, Liste aller `\qf` und `\pruefen` mit Grund, jede Abweichung vom Plan.

### AP0 – Recherche zu den Lücken (optional, nur nach Nils' Freigabe)

> Rahmenprompt, aber Regel 1 ersetzt durch den Recherche-Modus aus `CLAUDE.md` (Kapitel-Workflow Schritt 2).
> Bearbeite die Lücken Q2, danach Q1, Q5, Q6 aus Abschnitt 9 des Plans. Prüfe zuerst, ob ein Eintrag in `_Vorschläge`
> die Lücke schon schließt (dort genannte Item-Keys) und ob sein PDF frei verfügbar ist. Je Lücke höchstens zwei
> neue Quellen, bevorzugt Fachbuch, Norm oder begutachteter Artikel. Jede Quelle über Crossref oder Verlagsseite
> verifizieren, auf Duplikate prüfen, in `_Vorschläge` anlegen (Tag `Kap5-Recherche`), ohne Citation Key. Keine
> Belege aus Abstracts. Ergebnis als Abschnitt „Recherche (Schritt 2)“ an `review/plan-kap5.md` anhängen:
> Titel · DOI/ISBN · frei verfügbar ja/nein · welche Leitfrage. Danach stoppen.

### AP1 – Faktenblatt Testumgebung

> Rahmenprompt. Klone `NilsMeier1812/G1`, Stand `25d5c1a`. Erstelle `review/kap5-entwurf/fakten-testumgebung.md`
> (kein LaTeX) mit Fundstelle zu jeder Angabe: (a) Anzahl der Testfunktionen und Testdateien, Gruppen der Testsuite
> und ihr Inhalt (`test/run_tests.sh`, `docs/60-A-Tests.md`); (b) was die Attrappe des Roboters nachbildet und was
> nicht (`test/test_arm_controller_real.py`, `test/test_loco_client_real.py`, `test/teleop_jitter_probe.py`);
> (c) was die Tests ausdrücklich nicht abdecken; (d) Softwarestände aus den Dockerfiles und `docker-compose.yml`
> (Basis-Images, ROS-2-Distribution, MuJoCo, Python, Hersteller-SDK, DDS-Implementierung); (e) je Versuch V1–V11
> aus Abschnitt 7.2 des Plans: welches Skript es gibt, was es ausgibt, was fehlt. Wo Doku und Code voneinander
> abweichen, gilt der Code; die Abweichung kommt in den Bericht. Keine Messwerte übernehmen.

### AP2 – Belege prüfen und ergänzen

> Rahmenprompt. Gehe die Leitfragen L1–L34 aus Abschnitt 5 des Plans durch. Prüfe für jede genannte Beleg-ID in
> `evidence/`, ob das Zitat die Leitfrage wirklich trägt, und notiere das Ergebnis in
> `review/kap5-entwurf/belegpruefung.md` (Leitfrage · Beleg-ID · trägt / trägt mit Einschränkung / trägt nicht ·
> Einschränkung, die im Text stehen muss). Für Leitfragen mit Status „teilweise“ suche in `sources-text/<Key>.txt`
> der **schon freigegebenen** Quellen nach weiteren Stellen und lege neue Belege nach CLAUDE.md Phase 1 an
> (fortlaufende IDs, wörtlich, gedruckte Seite). Besonders: Bewertungsmethoden in Ajaykumar2021, Validierungsweg in
> Sekkat2024 und Durrani2026, Angaben zur Messumgebung in Kronauer2021 und Collins2019. Keine neuen Quellen.
> `python3 scripts/check.py` muss danach 0 Fehler melden.

### AP3 – Tabellen und Abbildung

> Rahmenprompt. Erstelle `review/kap5-entwurf/tabellen.tex` mit `tab:anforderungen`, `tab:kennzahlen`,
> `tab:versuchsplan`, `tab:testumgebung` und (Kann) `tab:defizite` nach Abschnitt 6, 7 und 8 des Plans. Zielwerte
> mit [N?] als `\pruefen{}`. In `tab:anforderungen` die Spalte „Nachweis in“ mit `\ref` auf die Labels `sec:eval_*`
> aus `Kapitel/08_Evaluation.tex`. Keine Tabelle länger als eine Seite. Baue außerdem
> `Bilder/tikz/bewertungslogik.tex` nach der Spezifikation in Abschnitt 8 (Muster: `Bilder/tikz/dds-domains.tex`,
> Stile aus `ba-grafik.tex`). Lege `review/kap5-entwurf/abbildungen.tex` mit `figure`-Umgebung, Caption-Vorschlag
> (Titel im Nominalstil und ein erläuternder Satz) und Label an. Kompiliere `main.tex` mit eingebundenen Testdateien,
> sieh dir jede Darstellung im PDF an (Überlappungen, Breite, Overfull-Boxen) und nimm die Testeinbindung wieder
> heraus.

### AP4 – Abschnitt 5.1

> Rahmenprompt. Schreibe 5.1 nach Abschnitt 5 des Plans nach `review/kap5-entwurf/5-1.tex` (höchstens 1,5 Seiten,
> sechs Absätze in der Reihenfolge der Kette). Jeder Defizit-Absatz beginnt mit dem Defizit als Kernsatz, belegt
> die Tatsachen mit den IDs aus L1–L13 und der Belegprüfung aus AP2, verweist auf den Abschnitt in Kap. 2–4 und
> endet mit der Forschungsfrage, die daraus folgt (`Abschnitt~\ref{sec:zielsetzung}`). Die Lücke im letzten Absatz
> trägt ihren Geltungsbereich. Nenne ausdrücklich, was die Arbeit nicht schließt. g1pilot ist hier eine von mehreren
> Arbeiten; die Auswahl als Ausgangsbasis gehört nach 6.1.

### AP5 – Abschnitt 5.2

> Rahmenprompt. Schreibe 5.2 nach `review/kap5-entwurf/5-2.tex` (höchstens 2 Seiten einschließlich
> `tab:anforderungen` aus AP3). Aufbau: Herleitung, Tabelle, je Forschungsfrage ein Absatz, Randbedingungen,
> Zielkonflikte. Halte dich an die Steckbriefe in Abschnitt 6 des Plans, auch an die dort genannten Grenzen
> (A1: feste Bewegungsfolgen; A2: Unterschiede werden gezählt, nicht geleugnet; A4: Fortbewegung nur
> Charakterisierung; A5: keine sicherheitstechnische Bewertung; A6: Aufwand ist nicht Gebrauchstauglichkeit).
> Formuliere jede Anforderung lösungsneutral: Wer den Satz liest, darf nicht erkennen, wie die Umgebung gebaut ist.
> Prüfe am Ende jede Anforderung mit der Frage: Kann sie verfehlt werden? Wenn nein, ist sie falsch formuliert.

### AP6 – Abschnitt 5.3

> Rahmenprompt. Schreibe 5.3 mit 5.3.1–5.3.3 nach `review/kap5-entwurf/5-3.tex` (höchstens 2,5 Seiten
> einschließlich der Darstellungen aus AP3). Kurze Einleitung des Abschnitts vor 5.3.1. In 5.3.1 die Auswahl der
> Kennzahlen gegenüber Abschnitt 3.1.3 der Arbeit begründen, auch was nicht anwendbar ist, und die Grenzen der
> Aussagekraft nennen. In 5.3.2 die drei Prüfebenen und die Grundsätze, dann die Tabelle; „Umfang“ je Versuch als
> `\pruefen{}`, solange Nils ihn nicht festgelegt hat. In 5.3.3 nur Angaben aus dem Faktenblatt (AP1); Versuche am
> Roboter mit ihrer Sicherung beschreiben, ohne Bedienschritte. Keine Ergebnisse, keine Formulierung im Perfekt
> („wurde gemessen“): Der Abschnitt beschreibt, was geprüft wird.

### AP7 – Zusammenführen und mechanisch prüfen

> Rahmenprompt. Füge `5-1.tex`, `5-2.tex`, `5-3.tex`, Tabellen und Abbildung in
> `Kapitel/05_Handlungsbedarf_Methodik.tex` zusammen; Labels und Überschriften aus dem Gerüst unverändert. Schreibe
> die Kapiteleinleitung und den Überleitungssatz zu Kap. 6. Prüfe: (a) Jedes Defizit führt zu einer Frage, jede
> Frage zu mindestens einer Anforderung, jede Anforderung zu mindestens einer Kennzahl, jede Kennzahl zu einem
> Versuch, jeder Versuch zu einem Label in Kap. 8; (b) Kürzel und Zielwerte sind in Text, Tabellen und Abbildung
> identisch; (c) kein Auslegungswert, kein Messergebnis, kein Komponentenname; (d) Umfang höchstens 6,5 Seiten.
> Erledige die „Folgen für andere Kapiteldateien“ aus Abschnitt 9 des Plans, soweit sie nur Kommentare und Labels
> betreffen. Führe `python3 scripts/zot.py text` und `python3 scripts/check.py` aus (0 Fehler Pflicht), kompiliere
> mit `latexmk` und sieh das PDF durch. Bericht: Seitenzahl, Liste aller `\qf` und `\pruefen`, offene Verweise („??“).
> Arbeite auf einem eigenen Branch und öffne einen Pull Request; nicht direkt auf `main`.

### AP8 – Inhaltlich verifizieren

> Nach `CLAUDE.md` Phase 4: `python3 scripts/check.py --pairs review/pairs.jsonl --file
> Kapitel/05_Handlungsbedarf_Methodik.tex`, dann ein **neuer** Auftrag mit dem Verifier-Prompt aus `CLAUDE.md`
> (wörtlich), Ergebnis nach `review/verifikation-kap5-<datum>.md`. Zusätzlich ein zweiter Prüfauftrag, weil Kap. 5
> vor allem wertet und setzt: „Lies nur `Kapitel/05_Handlungsbedarf_Methodik.tex`. Liste (1) jede wertende Aussage
> ohne Geltungsbereich, (2) jede Anforderung, die eine Lösung vorwegnimmt oder nicht verfehlt werden kann, (3) jeden
> Zielwert ohne Begründung im Text, (4) jede Kennzahl ohne Versuch und jeden Versuch ohne Kennzahl. Ändere nichts.“
> Korrekturen erst nach Rücksprache mit Nils.

## 12 Abnahmekriterien für den Entwurf

- Die Kette D → F → A → K → V → Abschnitt in Kap. 8 ist lückenlos und in Text, Tabellen und Abbildung gleich.
- Jede Anforderung ist lösungsneutral, prüfbar und kann verfehlt werden; jeder Zielwert ist begründet oder als
  `\pruefen` markiert.
- Jede Wertung in 5.1 nennt ihren Geltungsbereich; jede Tatsache trägt `\cite{}\ev{}`.
- Kap. 5 enthält kein Messergebnis, keinen Auslegungswert und keinen Namen einer Komponente.
- 5.3 nennt die Grenzen der eigenen Methode (Bezug Gelenkwinkelgeber, Aufwand statt Gebrauchstauglichkeit, Attrappe
  statt Roboter, wenige Wiederholungen am Roboter).
- `check.py` 0 Fehler; alle `\qf` und `\pruefen` sind im Bericht einzeln begründet.
- Die Storyline ist allein über die Kernsätze und allein über die Darstellungen lesbar (Richtlinien §3.3).
- Umfang höchstens 6,5 Seiten.
