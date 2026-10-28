# Richtlinien-BA — Regelwerk für das Schreiben der Bachelorarbeit (FAPS, FAU)

> Zweck: Maschinenlesbare Referenz für Claude-Agents, die an dieser Thesis arbeiten. Vor jeder Text-, Struktur- oder Formatierungsänderung lesen. Dicht, nicht hübsch.

## 0. Meta

### 0.1 Quellen (Kürzel in [eckigen Klammern] hinter jeder Regel)
- **[LF]** Leitfaden für die Erstellung von wissenschaftlichen Arbeiten, FAPS, Stand 2026-02-27 (46 S.). Offizielles Hauptdokument, neuester Stand.
- **[CS]** Cheat Sheet „Erstellung studentischer Arbeiten“, v1.2.0, 2025-01-13, Autoren LG, JW (vermutlich Betreuer-Gruppe). Kompakte Regeln mit Nummern (CS x.y.z).
- **[GS]** Handbuch „GetStarted“ Studentische Arbeiten FAPS, v1.1.1, 2024-04. Organisation, Abgabe, Umfang.
- **[REPO]** Ist-Zustand der LaTeX-Vorlage in diesem Repo (main.tex).
- **[ANNAHME]** Eigene Interpretation/Ergänzung, nicht aus den Dokumenten. Bei Zweifel mit Nils klären.

### 0.2 Prioritätsregel bei Konflikten
1. Explizite Anweisung von Nils / Betreuer (in Chat oder in dieser Datei unter §12 nachgetragen) > alles.
2. [LF] (neuestes offizielles Dokument) > [CS] > [GS], **außer** in §1 ist ein anderer Default festgelegt.
3. Offene Konflikte stehen in §1. Dort gilt der markierte DEFAULT, bis Nils ihn überschreibt.

### 0.3 Harte Regeln für Agents (nicht verhandelbar)
- **H1 Niemals Quellen erfinden.** Bereits die erste fiktive Quelle = Täuschungsversuch = Note 5,0 [LF 2.2]. Nur Einträge zitieren, die in `references.bib` stehen UND von Nils stammen/verifiziert sind. Fehlt ein Beleg: Kommentar `% TODO Quelle fehlt: <Aussage>` setzen (kein `\todo`, Paket nicht geladen) und Nils Bescheid geben, keinen Bib-Eintrag ausdenken, keine DOI/Seitenzahl raten.
- **H2 Keine Aussage ohne Beleg.** Jede fremde Aussage zitieren [CS 1.7.1, LF 5]; jede eigene Behauptung durch eigene Analyse oder Quelle belegen [LF 2.3].
- **H3 Kein „ich“, „wir“, „man“** im Text [CS 1.4.3, LF 2.3].
- **H4 Vorlage nur im Textteil ändern.** Kopf-/Fußzeilen, Verzeichnisse, Titelseite-Layout nicht manuell anfassen [GS 5.1, LF 4.1]. Persönliche Daten nur über die `\newcommand`s oben in main.tex.
- **H5 Sprache: Deutsch.** Zitierstil DIN ISO 690 (bei englischer Arbeit wäre es IEEE) [GS 5.3.1].
- **H6 Eigene Worte.** Wörtliche Übernahme oder fast wörtliche Übersetzung englischer Quellen gilt als „nicht ausreichend“ [LF 3.3].
- **H7 Main muss kompilieren** (pdfLaTeX + biber), da Overleaf-Sync auf main [REPO].

---

## 1. Konflikte zwischen den Dokumenten + DEFAULT

| ID | Thema | [LF] sagt | [CS] sagt | DEFAULT (bis Klärung) |
|---|---|---|---|---|
| K1 | Tempus | Durchgängig Präsens, ergebnisorientiert. Kein Erlebnisaufsatz in Vergangenheit („Im Rahmen der Arbeit wurde untersucht…“ = schlecht) [LF 2.3] | Zeitlose Erkenntnisse/wiederholbare Ergebnisse: Präsens. Zu bestimmtem Zeitpunkt durchgeführte Tätigkeiten (Experimente): Vergangenheit [CS 1.3] | Präsens als Grundform überall. Vergangenheit (Präteritum Passiv, „Die Proben wurden … geprüft“) NUR für konkret durchgeführte, einmalige Versuchsdurchführungen in Methodik/Ergebnisse. Nie für Ergebnisse/Erkenntnisse. |
| K2 | Aktiv/Passiv | „Passivsätze sparsam verwenden! Formuliere aktiv!“ [LF 2.3] | „Bevorzugt Passiv“; Aktiv für eigenen Beitrag (Kurzfassung, Schlussfolgerungen) [CS 1.4] | Aktivsätze mit Sach-Subjekt („Abbildung 4 zeigt…“, „Das Verfahren reduziert…“, „Die Ergebnisse belegen…“). Passiv, wo der Handelnde irrelevant ist (v. a. Methodik). Nie Personen als Subjekt (H3). Erfüllt beide Dokumente. |
| K3 | Gliederung Hauptteil | Einleitung+Zielstellung, Grundlagen/SdT, **Handlungsbedarf**, Methodik, Ergebnisse, Diskussion, Zusammenfassung+Ausblick [LF 3.1] | **Kurzfassung**, Einleitung, Grundlagen, Stand der Forschung (endet mit Forschungsbedarf), Methoden, Ergebnisse, Diskussion, Schlussfolgerungen (Beiträge + Ausblick) [CS 1.1] | Repo-Struktur (§3.1) beibehalten. Handlungsbedarf als letztes Unterkapitel von Kap. 3 (Stand der Technik). Kurzfassung: mit Betreuer klären, bis dahin nicht anlegen. |
| K4 | Mehrfachzitate | Getrennte Klammern `[xy] [yz]`, NICHT `[xy; yz]` [LF 5.1] | Beispiel `[27, 28]` [CS 1.7.3] | [LF]: getrennte Klammern → LaTeX `\cite{a} \cite{b}`. Sammelzitate generell vermeiden [CS 1.7.2]. |
| K5 | Achsbeschriftung Diagramme | DIN 461: Achse mit Pfeil in Anstiegsrichtung, Einheit ersetzt die Zahl am vorletzten Achsenstrich, Rahmen um Diagramm [LF 4.4.2] | „Zeit in s“ [CS 2.4.2] | [LF] DIN 461 (Einheit am vorletzten Tick). Mit Betreuer klären, falls Plot-Tool das schwer macht. |
| K6 | Formel-Nummerierung | Kapitelweise `(X.Y)` [LF 4.4.4] | `(n)` oder `(X.Y)` [CS 2.5.3] | `(X.Y)` — macht scrreprt automatisch. Kein Konflikt in der Praxis. |
| K7 | Verweis auf Formel | – | „Gleichung 1“, Identifier ohne Klammer [CS 2.5.4] | `Gleichung~\ref{eq:x}` (nicht `\eqref`). |
| K8 | „ergibt sich“ | Vermeiden (Reflexivpronomen), stattdessen „resultieren“; keine Sätze „Aus der Betrachtung von xy folgt/ergibt sich…“ [LF 2.4] | Nutzt selbst „ergibt sich zu“ im Formelbeispiel [CS 2.5] | Vermeiden. |
| K9 | Literaturverwaltung | Citavi empfohlen [LF 5.1] | – | Nils nutzt biblatex/biber + `references.bib`. Abgabe verlangt Citavi-Projekt [GS 3.4] → stattdessen .bib abgeben; mit Betreuer abklären. |

---

## 2. Organisation & Zeitplan [GS 3, LF 7, CS 0]

- Max. Bearbeitungszeit BA (Maschinenbau): **5 Monate**; Abgabe am Lehrstuhl [GS 3.1 Tab. 1]. Studienordnung prüfen.
- Ablauf [GS 3.1]: Kickoff → 2–3 Wochen Einführung/Admin → Anmeldung (einvernehmlich, auch rückwirkend) → **finale Gliederung 4 Wochen nach Anmeldung** → praktische Arbeit + Schreiben → **Vorabgabe Stand der Technik (ggf. weitere Kapitel) bis 8 Wochen vor Abgabe** → Abgabe → Vortrag ±1 Woche um Abgabe → Feedbackgespräch.
- [LF 7]: Spätestens **2 Wochen** nach Start ausführliche Gliederung + relevante Literatur an Betreuer.
- Phasen [CS 0]: Orientierung ~2 Wo (Aufgabenstellung) → Planung ~2 Wo (Arbeitsplan, Methodenwahl, Statistik-Konzept) → Ausführung ~10/14 Wo (iterativ) → Dokumentation ~4 Wo (Bilder, Tabellen, Rohfassung) → Abschluss ~2 Wo (Überarbeitung, Korrektur, Anhang).
- Regeltermine [GS 3.2]: 1–2-wöchentlich, 30 min, 2–3 Folien (Stand + nächste Schritte, Gestaltung egal), in Teams/FAUbox ablegen.
- Arbeitsweise bewertet [GS 2.2]: Selbstständigkeit, Dokumentation (alles nachvollziehbar, Code kommentiert), Ordnung (Ordnerstruktur, aktuelle Dateien).
- Verspätete Abgabe wird nicht bewertet [LF 7]. Merkblatt Prüfungsamt beachten.

### 2.1 Bewertungskriterien schriftliche Arbeit [GS 2.2]
Systematische Vorgehensweise dokumentiert · Einsatz von Methoden/Werkzeugen · Erfüllung der Aufgabenstellung · Anwendung von Fachkenntnissen · Diskussion/kritische Beurteilung der Ergebnisse · Darstellung der Ausgangslage · Selbstständigkeit/eigene Ideen · Sorgfalt, Vollständigkeit, Verständlichkeit · äußere Form · Ausdruck, Stil, Rechtschreibung, Grammatik · Qualität der Quellen + Vollständigkeit der Recherche.

---

## 3. Aufbau der Arbeit

### 3.1 Gesamtstruktur
[LF 3.1]: Deckblatt → Erklärung → Inhaltsverzeichnis → Abbildungsverz. → Tabellenverz. → Formelverz. → Abkürzungsverz. → Hauptteil → Literaturverz. → Anhang → (Lebenslauf).

[REPO] Mapping:
| Datei | Kapitel | Entspricht |
|---|---|---|
| `Kapitel/00_Eigenständigkeitserklärung.tex` | Erklärung | [LF 4.6] |
| `Kapitel/01_Einleitung.tex` | 1 Einleitung | Einleitung und Zielstellung |
| `Kapitel/02_Grundlagen.tex` | 2 Grundlagen | Grundlagen |
| `Kapitel/03_Stand_der_Technik.tex` | 3 Stand der Technik | SdT/Stand der Forschung + Handlungsbedarf (letztes Unterkapitel) |
| `Kapitel/04_Methodik.tex` | 4 Methodik | Methodenteil |
| `Kapitel/05_Ergebnisse.tex` | 5 Ergebnisse | Ergebnisteil |
| `Kapitel/06_Diskussion.tex` | 6 Diskussion | Diskussionsteil |
| `Kapitel/07_Zusammenfassung.tex` | 7 Zusammenfassung und Ausblick | Schlussteil / Schlussfolgerungen |
| `Kapitel/Anhang_*.tex` | Anhang A, B, … | [LF 4.5] |

### 3.2 Umfang [GS 5.2, LF 3]
- BA gesamt: **ca. 60–80 Seiten** ohne Verzeichnisse und Anhang.
- Stand der Technik ≈ **1/3** der Arbeit (bei praktischer Arbeit) [GS].
- Methodik + Ergebnisse + Diskussion ≈ **2/3** der Arbeit [LF 3.7].
- Einleitung: i. d. R. **2 Seiten, max. 3** [LF 3.2].
- Zusammenfassung + Ausblick: **max. 3 Seiten** [LF 3.8].
- Gliederungspunkte sollen ähnliches Gewicht (Inhalt/Umfang) haben [LF 3.1].

### 3.3 Roter Faden [LF 3.1, CS 1.2]
- Beginnt in der Einleitung mit der zentralen Aufgabenstellung; Leser muss jederzeit erkennen, wie ein Teil mit der Aufgabenstellung zusammenhängt. Keine Nebensächlichkeiten.
- Storyline muss allein über die **Topic Sentences** erfassbar sein [CS 1.2.3].
- Storyline muss allein über die **Abbildungen/Tabellen** (inkl. Unterschriften) erfassbar sein [CS 2.1.4].
- Wenn möglich Kernaussage jedes Kapitels in einem Bild zusammenfassen [LF 2.3].
- Argumentation vom Allgemeinen zum Speziellen [LF 4.2].
- Alle Aussagen kausal begründen; Ergebnisse nicht nur auflisten, sondern begründen [LF 3.1].

### 3.4 Kapitel im Detail

**Kurzfassung** (nur falls gefordert, s. K3) [CS 1.1]: Gesamte Arbeit in kurz, alleinstehendes Dokument, Schema „Nature Summary Paragraph“. [ANNAHME: Nature-Schema = 1–2 Sätze Einstieg für breites Publikum → Hintergrund/Fachkontext → konkretes Problem/Lücke → „Hier wird gezeigt…“ Hauptergebnis → Einordnung ggü. bisherigem Wissen → allgemeine Bedeutung/Ausblick. Aktiv erlaubt (CS 1.4.2).]

**1 Einleitung** [LF 3.2, CS 1.1]:
- Schema **Situation → Komplikation → Lösungsansatz** (z. B. 3 Abschnitte) [CS].
- Inhalt [LF]: Hinführung + Relevanz im wissenschaftlichen Kontext; Thema vorstellen + Fragestellung skizzieren; Eingrenzung begründen (Schwerpunkt, was weggelassen wird, warum); ggf. Forschungslage/Lücken; Vorgehen/Methodik kurz; Aufbau der Arbeit.
- Funktion: Orientierung „Was erwartet mich?“. 2–3 Seiten.

**2 Grundlagen** [CS 1.1, LF 3.3]:
- Nur was über das Grundwissen eines Ingenieurs hinausgeht. Kein seitenlanges Lehrbuchwissen, prägnante Übersicht (Tabellen, Übersichtsbilder).
- Zentrale Begriffe definieren und festlegen, wie sie in der Arbeit verwendet werden (z. B. „Digitalisierung heißt hier …“) [LF 2.2, GS 2.1]. Definitionen nur, wenn nicht fachbekannt UND für die Arbeit relevant.

**3 Stand der Technik / Forschung** [LF 3.3, 3.4, CS 1.1, GS 2.1]:
- Überblick über verwandte Arbeiten, **wertungsfrei** dargestellt; nur für die Aufgabenstellung Relevantes; bei mehreren Theorien Überblick.
- Quellen: Zeitschriftenartikel (bevorzugt), Monografien, Konferenzbeiträge, Patente. Auf **Aktualität** achten.
- Systematische Literaturanalyse: Suche → Auswertung → Analyse/Interpretation im Kontext der Forschungsfrage [GS Abb. 1].
- **Handlungsbedarf** (letztes Unterkapitel): Jetzt **Wertung** der Literatur; ungelöste Fragen/Defizite → Forschungslücke → Fragestellung + konkretisierte Zielsetzung der Arbeit herleiten. Erklären: warum dieses Problem, für wen relevant, Beitrag zur Forschung (Theorie, Modell, Methoden, Fakten) + praktische Relevanz; Eingrenzung nach Machbarkeit; was erreicht werden soll, welche Ergebnisse wofür, welche Schlussfolgerungen möglich [LF 3.4].

**4 Methodik** [LF 3.5, CS 1.1]:
- Eigenes Vorgehen, Methoden, alle Arbeitsschritte und Hilfsmittel nachvollziehbar; zuerst Untersuchungsplan (was, wie, wo, wann, durch wen).
- **Reproduzierbarkeit**: andere Forschende müssen die Untersuchung wiederholen können.
- Methodenwahl begründen (warum diese, warum andere nicht; Vor-/Nachteile).
- Gütekriterien: Objektivität, Reliabilität, Validität.
- Stichprobe/Grundgesamtheit so detailliert wie nötig beschreiben + Angemessenheit begründen.
- Auswertungsverfahren nur ausführlich, wenn nicht allgemein üblich.
- Keine iterativen Entwicklungsgeschichten („System 1 hatte Schwächen, daher System 2…“); Zwischenlösungen sind irrelevant [LF 2.3]. Geräteentwicklungen nicht zu detailliert, nur wissenschaftlich relevante/übertragbare Details.

**5 Ergebnisse** [LF 3.6, CS 1.1]:
- **Kapitelbeginn: Kapitel 4 kurz zusammenfassen** („niemandem zuzumuten, Kapitel 4 zu lesen“) [CS].
- Resultate **wertungsfrei**, ohne Interpretation; Struktur orientiert an Theorie und Methodik; mit Grafiken/Tabellen veranschaulichen.

**6 Diskussion** [LF 3.7, CS 1.1]:
- Ergebnisse zusammenfassen, kritisch diskutieren, bzgl. Problem-/Zielstellung interpretieren.
- Wesentliche Beobachtungen/Erkenntnisse (Korrelationen, Kausalitäten).
- **In Stand der Forschung (Kap. 3) einordnen.**
- Bedeutung/Implikationen für Wissenschaft und Praxis.
- **Limitierungen** der Arbeit.

**7 Zusammenfassung und Ausblick / Schlussfolgerungen** [LF 3.8, CS 1.1]:
- An Problem-/Zielstellung der Einleitung anknüpfen; wichtigste Ergebnisse kompakt bzgl. der Fragestellung; in größeren Zusammenhang einordnen.
- Explizit **„Beiträge der Arbeit“** benennen [CS]. Aktiv erlaubt [CS 1.4.2].
- Offene Fragen + warum; Grenzen.
- **Ausblick**: zukünftige Forschung, Verbesserungen, praktische Schlussfolgerungen. Nur hier sind Konjunktiv und subjektive Einschätzungen erlaubt [CS 1.5.2, LF 2.3].
- Max. 3 Seiten.

---

## 4. Sprache & Stil

### 4.1 Grundsätze [LF 2.3]
- Präsens (s. K1), Nominalstil, unpersönlich, keine Füllwörter.
- Erst roten Faden/Argumentation entwerfen, dann formulieren. Jeder Satz muss sitzen, präzise.
- **Indikativ**; kein Konjunktiv (könnte, sollte, müsste, dürfte …), Ausnahme Ausblick [CS 1.5, LF 2.3]. ✗ „das Material könnte eingesetzt werden“ → ✓ „das Material kann eingesetzt werden“.
- Nomenbildung ist wissenschaftlich: ✗ „muss so bearbeitet werden, damit“ → ✓ „Zur bedarfsgerechten Bearbeitung ist auf die Einhaltung von xy zu achten.“

### 4.2 Absätze [CS 1.2, LF 4.3.1, CS 1.8]
- Ein Absatz = **genau ein Argument** (atomar).
- **Topic Sentence** zuerst (enthält das Argument), Folgesätze stützen es.
- Absatz alleinstehend verständlich; jeder Satz baut logisch auf dem vorherigen auf; keine logischen Sprünge zwischen Absätzen.
- **Mind. 2 Sätze** pro Absatz; kein Ein-Satz-Absatz.
- Keine „Wall of Text“.
- Keine Leerzeile zwischen Absätzen innerhalb eines Kapitels [LF 4.3.1]. (LaTeX: normaler Absatz, `\parindent=0` ist gesetzt.)

### 4.3 Verbotsliste / Ersatz [LF 2.3, CS 1.9]
| ✗ Vermeiden | Grund / ✓ Stattdessen |
|---|---|
| ich, wir, man | unpersönlich, Sach-Subjekt |
| Konjunktiv (außer Ausblick) | Indikativ |
| Relative Zeitangaben: kürzlich, später, modern, heute, aktuell, neuerdings | Arbeit wird über Jahre gelesen → absolute Angaben (Jahr) |
| Füllwörter / Verstärker: enorm, sehr, überaus, äußerst | ✗ „Recycling ist enorm bedeutend.“ |
| Implizite Meinung: „jedoch“, „überaus“ wertend; subjektive Einschätzungen | nur im Ausblick. „jedoch“ als neutraler Konnektor ist ok. |
| Unpräzise Adjektive: innovativ, intelligent, modern | konkrete, messbare Eigenschaft |
| Umschreibungen: im Allgemeinen, in der Regel, beispielsweise, teilweise | konkret, vollständig aufzählen |
| Beispiele statt Aufzählung | vollständig + überschneidungsfrei aufzählen (**MECE**), strukturieren, ggf. bewerten |
| Pleonasmen (weißer Schimmel), aufgeblähte Begriffe, erfundene Wörter, übertriebene Steigerungen | – |
| Anglizismen/Fremdwörter, wenn deutscher Begriff existiert | deutscher Fachbegriff |
| Umgangssprache, journalistische Floskeln, Redewendungen | Fachsprache |
| Rhetorische Fragen | klare Aussage |
| Wiederholungen (Wörter und Argumente) | – |
| Schachtelsätze, Substantiv-Ketten, verschachtelte Infinitivkonstruktionen | kurze klare Sätze |
| „ergibt sich“, „Aus der Betrachtung von xy folgt…“ | „resultieren“, s. K8 |
| Betonung von „technischen Herausforderungen“/Anwendungsnähe | wissenschaftliche Qualität, allgemeingültige, übertragbare Erkenntnisse betonen |
| Wörtliche Zitate (häufig) | selten, pointiert; besser Meinungen bewerten und weiterentwickeln |

### 4.4 Begriffe & Abkürzungen [CS 1.6, 1.9.3, LF 2.3]
- Fachbegriffe **konsistent** in Wahl und Schreibweise (✗ „3D-Druck“/„3D Druck“/„3-D-Druck“; immer „CAD-Modell“). Kein Ersatz durch unpassende Synonyme.
- Abkürzungen beim **ersten Auftreten einführen** („Liquid Additive Manufacturing (LAM)“), danach konsequent nutzen; keine unnötigen/unüblichen Abkürzungen; [LF]: nur wenn nötig. Alle ins Abkürzungsverzeichnis.
- LaTeX: `\acro{LAM}{Liquid Additive Manufacturing}` in main.tex, im Text `\ac{LAM}` (erste Nutzung automatisch ausgeschrieben).

### 4.5 Zahlen, Einheiten, Leerzeichen [LF 2.3, 4.3.3, CS 1.9]
- Zahlen **null bis zwölf ausschreiben**, ab 13 Ziffern [LF]. [ANNAHME: gilt nicht bei Wert+Einheit, Formeln, Tabellen, Versuchsnummern → dort Ziffern.]
- Einheiten nicht kursiv [CS 1.9.2].
- Geschütztes (schmales) Leerzeichen zwischen Wert und Einheit [CS: LaTeX `\,`]: `44\,mm`.
- Geschütztes Leerzeichen außerdem [LF 4.3.3]: Titel + Name (`Prof.~Dr.~X`), Datum (`19.~September~2007`), Abkürzungen (`z.\,B.`, `u.\,a.`, `d.\,h.`, `z.\,T.`), Zahlen mit Bezug (`Nr.~5`, `1.350~Personen`), Verweise (`Abbildung~\ref{}`, `Tabelle~\ref{}`, `Kapitel~\ref{}`).
- Nie doppelte Leerzeichen (LaTeX unkritisch).
- Tausenderpunkt im Deutschen: `1.350`; Dezimalkomma. [ANNAHME: in Mathe `{,}` verwenden: `$1{,}5$`.]

### 4.6 Konnektoren & Formulierungshilfen [LF 2.4, Tab. 1]
- Folge: sodass, deshalb, daher, folglich, somit, demnach, aus diesem Grund.
- Gegensatz: während, dagegen, im Gegensatz zu, vielmehr, im Vergleich zu.
- Ursache: weil, da, aufgrund, infolge, wegen.
- Einschränkung: obwohl, trotzdem, dennoch, zwar – aber, allerdings, jedoch.
- Erläuterung: nämlich, das heißt.
- Zeit: anschließend, im Anschluss daran, nachfolgend, im Folgenden, zuvor, schließlich.
- Aufzählung: sowie, außerdem, darüber hinaus, nicht zuletzt, zum einen – zum anderen, einerseits – andererseits.
- Betonung: insbesondere, vor allem, besonders.
- Bedingung: wenn, falls, sofern. Beispiel: z. B., u. a., exemplarisch.
- Verweis auf Darstellungen (variieren!): „In Abbildung X ist … dargestellt.“, „Tabelle X verdeutlicht/skizziert/bildet … ab/stellt den Zusammenhang zwischen … und … her.“, „Gemäß Abbildung X wird der Wirkzusammenhang von … ersichtlich.“, „Durch Gegenüberstellung von X und Y resultieren folgende Schlussfolgerungen …“.

---

## 5. Formalia & Layout [LF 4, CS 1.8, 3, GS 5.1]

- A4, Arial 12 pt, Zeilenabstand 1,2, **Blocksatz mit Silbentrennung** [LF 4.1, CS 1.8.1]. [REPO: erledigt via scrreprt 12pt, helvet, setstretch 1.2]
- Silbentrennung prüfen (Fehler wie „Maschine-nbau“) [LF 4.3.2]. LaTeX: bei Bedarf `\hyphenation{...}` oder `"-`.
- Keine **Schusterjungen/Hurenkinder** [CS 1.8.2]. [ANNAHME LaTeX: `\widowpenalty=10000 \clubpenalty=10000` bzw. am Ende manuell prüfen.]
- Hervorhebungen nur im Ausnahmefall; nicht unterstreichen [LF 4.1].
- Aufzählungszeichen: **quadratisch, FAPS-Grün**, keine runden [LF 4.1]. [REPO: per enumitem gesetzt; Ebene 2 aktuell „–“.]
- FAPS-Grün = **RGB 151, 193, 57** [LF Abb. 4]. [REPO: `FAPSGruen`]

### 5.1 Gliederung / Inhaltsverzeichnis [LF 4.2, CS 3]
- Max. **3 numerische Ebenen** (1, 1.1, 1.1.1); kein `\paragraph` nummeriert. Nach letzter Ziffer kein Punkt.
- **Wer A sagt, muss B sagen**: gibt es 1.1, muss es 1.2 geben (alle Ebenen).
- Hauptkapitel mit **mind. 3 Unterkapiteln** [LF]; ideal gleichmäßig (z. B. 5×4×3).
- Zu jeder Überschrift gehört Text; jedes Hauptkapitel beginnt mit kurzer Einleitung **vor** dem ersten Unterkapitel [LF 3.1].
- Überschriften aussagekräftig, konsistent, im Verzeichnis wörtlich gleich wie im Text.
- Ästhetischer Umbruch langer Überschriften: `\section[Kurzform fürs TOC]{Lange Überschrift}` [CS 3.2].
- Seitenzahlen: Verzeichnisse römisch (Deckblatt nicht gezählt), arabisch ab Einleitung [LF 4.2]. [REPO: erledigt]

### 5.2 Anhang [LF 4.5]
- Technische Zeichnungen, große Tabellen/Diagramme, ergänzende Dokumente. Jeder Anhang auf neuer Seite, Großbuchstaben: „Anhang A – Name des Anhangs“.
- Abbildungen im Anhang: „Anhang A – Abbildung 1“ usw., NICHT im Abbildungsverzeichnis [LF 4.4.1]. [ANNAHME/TODO LaTeX: im Anhang Zähler/Caption-Präfix umstellen und `\caption[]{}`-Einträge aus LOF ausschließen, z. B. `\captionsetup{list=no}`; Vorlage prüfen.]

### 5.3 Eidesstattliche Erklärung [LF 4.6, GS 3.4]
Gesondertes Blatt **ohne Seitennummer nach dem Deckblatt**, eigenhändig unterschrieben. Mustertext [LF]:
> Ich versichere, dass ich die Arbeit ohne fremde Hilfe und ohne Benutzung anderer als der angegebenen Quellen angefertigt habe und dass die Arbeit in gleicher oder ähnlicher Form noch keiner anderen Prüfungsbehörde vorgelegen hat und von dieser als Teil einer Prüfungsleistung angenommen wurde. Alle Ausführungen, die wörtlich oder sinngemäß übernommen wurden, sind als solche gekennzeichnet.
> Erlangen, den XX.XX.20XX — Vorname Nachname

(Einzige Stelle mit „ich“, da Formtext.)

---

## 6. Darstellungsobjekte (Abbildungen, Diagramme, Tabellen, Formeln)

### 6.1 Allgemein [LF 4.4, CS 2.1]
- Jedes Objekt **im Text referenziert**; nach der ersten Erwähnung und möglichst nah am Bezugstext platzieren (LaTeX: `[htbp]`, Referenz vor dem Float).
- Objekt + Unter-/Überschrift **alleinstehend verständlich**.
- Schrift in Objekten = Fließtext (Arial/Helvetica, Deutsch); Größe ~10 pt ok, aber **einheitlich** über alle Objekte.
- Objekte **zentriert**, Beschriftung **linksbündig** [LF]. [REPO: caption raggedright, small, italic]
- Einheitliches Farbschema, FAPS-Farben empfohlen; Flächen nur füllen, wenn Farbe Bedeutung trägt [LF 4.4.1].
- Platzbedarf vs. Inhalt kritisch prüfen; Größe sinnvoll [LF 4.4, CS 2.2.5].
- Fremde Bilder/Tabellen/Formeln: Quelle ins Literaturverzeichnis + `[n]` an Caption. Nachgebaut/vereinfacht/modifiziert: „in Anlehnung an [n]“ [LF 4.4.1].

### 6.2 Abbildungen [LF 4.4.1, CS 2.2, GS 5.4]
- **Unterschrift** (unter dem Bild), fortlaufend arabisch nummeriert, ins Abbildungsverzeichnis.
- Caption-Aufbau [CS]: **Titel im Nominalstil**, danach Zusatzinfos in ganzen Sätzen mit Satzzeichen. LaTeX: `\caption[Titel]{Titel. Erläuternder Satz.}` (Kurzform fürs Verzeichnis).
- **Hochaufgelöst**: bei 300 % Zoom im PDF keine Pixel → Vektor (PDF/SVG→PDF) bevorzugt [CS 2.2.4].
- Breite = Textbreite **16 cm** als Referenz [LF, GS]. [REPO: Textbreite 21−3−2 = 16 cm → `width=\textwidth`]
- Keine Rahmen um Abbildungen [LF].
- Eigene Grafiken > kopierte; einfache Grafiken aus Papern nachbauen, komplexe dürfen (mit Zitat) übernommen/erweitert werden [GS 5.4].
- Fotos vollständig beschriften (Komponenten, Bereiche, Grenzen); Komponenten, Achsen, Parameter vollständig bezeichnen; Legenden vollständig (insb. Prozessparameter) [LF].
- Objekt-Abbildungen (Fotos, Mikroskopie, CAD) brauchen **Maßstab** [CS 2.2.6].
- Abstand 12 pt vor Abbildung [LF] (in LaTeX via Float-Abstände, nicht manuell).
- **Titelbild** [LF 4.4.1, CS 2.6]: ansprechend, vermittelt eine Botschaft; keine Beschriftung/Nummer, nicht im Verzeichnis; Quellen ggf. unten auf der Folgeseite. [REPO: `\Titelbild` in main.tex]

### 6.3 Diagramme [LF 4.4.2, CS 2.4]
- Diagrammtyp sinnvoll wählen [CS 2.4.1].
- Nach **DIN 461**: Achsen beschriftet, Pfeil in Anstiegsrichtung (nicht bei Versuchsnummern o. Ä.), Einheit ersetzt die Zahl am **vorletzten** Achsenstrich, alle relevanten Infos im Diagramm, **Rahmen um Diagramm**. Schrift nicht zu klein, Arial. (s. K5)
- Diagramme werden als **Abbildung** beschriftet (kein eigener Typ).

### 6.4 Tabellen [LF 4.4.3, CS 2.3]
- **Überschrift** (über der Tabelle), Titel im Nominalstil + Zusatzsätze [CS]; arabisch nummeriert; Tabellenverzeichnis. [REPO: `captions=tableheading`]
- Referenz im Text **vor** der Tabelle.
- Inhalt linksbündig oder zentriert, **kein Blocksatz**; Schriftgröße einheitlich (oft 10 pt).
- Seitenumbruch nie innerhalb einer Zeile; bei Fortsetzung Tabellenkopf wiederholen (LaTeX: `longtable`/`xltabular` mit `\endhead`).
- Umfangreiche Tabellen in den Anhang.
- Stil: FAPS-Stil (grüner Kopf) oder schlicht [LF Tab. 2/3]. [REPO: booktabs vorhanden]

### 6.5 Formeln [LF 4.4.4, CS 2.5]
- In den Satz eingebunden, inkl. Satzzeichen nach der Formel („…ergibt sich zu $y=mx+t,$ wobei …“).
- Nummer rechtsbündig in runden Klammern, kapitelweise `(X.Y)`.
- Variablen unter der Formel erklären ([LF]: tabellarisch „mit: F: Kraft, m: Masse …“; [CS]: „wobei m die Steigung … symbolisiert“).
- Verweis: „Gleichung~\ref{eq:…}“ (s. K7).
- Formelverzeichnis: [REPO] `\formeleintrag{Beschreibung}` direkt nach der Gleichung; Schalter `\MitFormelverzeichnistrue` in main.tex.

---

## 7. Zitieren & Literatur [LF 5, CS 1.7, GS 5.3]

### 7.1 Stil
- **DIN ISO 690, numerisch**: `[n]` im Text, keine Seitenangabe nötig [LF 5.1]. [REPO: biblatex `style=iso-numeric`]
- Mehrere Quellen: getrennte Klammern `[1] [2]` (s. K4). Sammelzitationen am Absatzende vermeiden [CS 1.7.2].
- Literaturverzeichnis: nur tatsächlich zitierte Werke, **in Zitierreihenfolge** nummeriert, keine Untergliederung nach Quellentyp, hängender Einzug (Sondereinzug) [LF 5.1]. [REPO/ANNAHME: biblatex-iso690 sortiert standardmäßig nach Zitierreihenfolge; prüfen]

### 7.2 Platzierung [CS 1.7.1, LF 5.2.3]
- Beleg für **einen Satz**: am Satzende **vor** dem Punkt: `… Seilroboter~\cite{x}.`
- Beleg für **ganzen Absatz** (nur diese eine Quelle): am Absatzende **nach** dem Punkt: `… Satz. \cite{x}`

### 7.3 Zitatarten [LF 5.2.2–5.2.4]
- **Direkt**: buchstaben-/zeichengetreu, in Anführungszeichen (LaTeX `\enquote{}`), Quelle direkt danach; fremdsprachig im Original lassen; eigene Einfügungen `[ ]`, Auslassungen `[…]`, Fehler `[sic!]`, eigene Hervorhebung `[Hervorhebung durch verfassende Person]`; > 3 Zeilen: eingerückter Block, kursiv, ohne Anführungszeichen. Selten verwenden.
- **Indirekt** (Standardfall): sinngemäß, eigene Worte, ohne Anführungszeichen, mit `[n]`. Auch umformulierte/zusammengefasste Inhalte brauchen die Quelle.
- **Sekundärzitat**: möglichst Original zitieren; sonst Sekundärliteratur im Verzeichnis nachweisen.
- Übernommene Bilder/Tabellen/Formeln ebenfalls zitieren (§6.1).

### 7.4 Quellenqualität [LF 3.3, 5.3–5.5]
Kriterien: **zitierfähig** (öffentlich auffindbar; graue Literatur wie BA/MA, Skripte, Firmeninterna nur eingeschränkt), **zitierwürdig** (wissenschaftliche Fragestellung, klare Struktur, präzise Terminologie, Text-Text-Bezüge, angemessene Methodik, theoretische Fundierung), **relevant** (konkreter Bezug; aktuelle Quellen aus renommierten Journals > ältere/journalistische).

| Rangfolge | Quellentyp |
|---|---|
| ✓✓ | Fachzeitschriften/E-Journals (peer-reviewed), Konferenzbeiträge, Dissertationen, Patente, Normen, amtliche Veröffentlichungen |
| ✓ | Fachbücher/Monografien, Sammelwerk-Beiträge (einzeln), Fachlexika (für Definitionen) |
| ~ | Lehrbücher (Einstieg/Grundlagen), Arbeitspapiere/Forschungsberichte (Qualität prüfen), Unternehmens-/Marktstudien (Interessen prüfen) |
| ✗ (nur wenn selbst Untersuchungsgegenstand / keine Alternative) | Internetquellen ohne Qualitätssicherung, Zeitungen (nur aktuelle Meldungen), Social Media, Blogs, Wikipedia, Schülerduden/Brockhaus, hausarbeiten.de, GRIN |

- Internetquellen nur, wenn keine aktuelle Literatur in anderen Medien (z. B. Softwareentwicklung); Seriosität prüfen.
- Elektronische Quelle beantwortet **Wer? Was? Wo? Wann?**: kein Autor → Herausgeber/Organisation, sonst „o. V.“; ohne Titel → Beschreibung in `[ ]`; Medium in `[ ]` ([Podcast], [Film]); DOI bevorzugt, sonst vollständige URL + Abrufdatum (URL nie mit Bindestrich trennen); unsicheres Datum → „o. J.“/„o. D.“. Schema: `Nachname, Vorname (Jahr): Titel. [Angaben]. DOI oder online unter: URL (Abrufdatum).` Kein Punkt nach DOI.
- biblatex-Felder dafür: `doi`, `url`, `urldate`, `howpublished`, `organization`.

### 7.5 Recherche-Tipps [GS 5.3.2]
Dimensions, FAU-Katalog (VPN), Google Scholar (+ Alerts), Scopus, Web of Science; Patente: DEPATISnet, Google Patents. Surveys/Reviews für Überblick; Literaturverzeichnisse passender Paper durchgehen (Schneeball); Publikationen von Autoren/Instituten durchsuchen; Unzugängliches über Betreuer/UB beschaffen.

---

## 8. Schreibprozess [LF 2.1]
- Phasen: Orientierung/Planung → Auswertung/Datenerhebung/Gliederung → Rohfassung → Überarbeitung → Korrektur/Layout. Lesen und Schreiben laufen parallel.
- Erste Fassung = Rohfassung; mehrere Überarbeitungsrunden einplanen, jeweils mit Fokus auf: (1) Zielgruppe/Zweck, (2) Aufbau/Gliederung, (3) Inhalt (Lücken, Wiederholungen, Logik, Argumentation), (4) Sprache/Stil.
- Lesen mit Leseziel; aktiv lesen, Kerngedanken in eigenen Worten festhalten.

---

## 9. Abgabe [GS 3.4, LF 7]
- **1 gebundenes Exemplar**, doppelseitig (sofern nicht anders abgesprochen), **klebegebunden, klare Deckfolie, grünes Abschlussblatt (FAPS-Grün)**; persönlich beim Betreuer mit Datenträger.
- Zusätzlich elektronisch (PDF) + Abgabeordner in Teams/FAUbox, identisch mit Datenträger (CD/USB/SD), eindeutig benannte Dateien:
  - Arbeit digital (LaTeX-Quellen + PDF)
  - Literaturverwaltung (Citavi-Projekt; hier: `references.bib` + PDFs, s. K9)
  - Grafiken als Nativdaten + Austauschformat
  - Alle Arbeitsdateien dokumentiert/aufbereitet: Code (kommentiert), CAD, Messdaten
  - Dokumentation: Fotos, Videos, Code-Anleitungen
- Checkliste: Erklärung enthalten **und unterschrieben**? Datenträger dabei? **Korrektes Abgabedatum auf dem Titelblatt**?

## 10. Abschlussvortrag [GS 6]
- Pflicht bei BA. **20 min Vortrag + 10 min Fragen**. Aufbau **S-C-R** (Situation – Complication – Resolution). FAPS-PowerPoint-Vorlage. Ergebnisse (auch Literatur) möglichst visualisieren. Termin ±1 Woche um die Abgabe.

---

## 11. Prüfliste für Agents

### 11.1 Pro geschriebenem Absatz/Abschnitt
- [ ] Topic Sentence vorn, ein Argument, ≥ 2 Sätze, logisch an Vorabsatz angeschlossen
- [ ] Kein ich/wir/man; kein Konjunktiv (außer Ausblick); Tempus nach K1
- [ ] Keine Füllwörter, relativen Zeitangaben, vagen Adjektive, Floskeln, rhetorischen Fragen (§4.3)
- [ ] Jede fremde Aussage mit `\cite{}` an richtiger Position (§7.2); nur existierende Bib-Einträge (H1)
- [ ] Begriffe/Schreibweisen konsistent; Abkürzungen via `\ac{}` und im Verzeichnis
- [ ] Zahlen ≤ 12 ausgeschrieben (außer mit Einheit); `\,` zwischen Wert und Einheit; `z.\,B.` usw.
- [ ] Inhalt passt zur Rolle des Kapitels (SdT wertungsfrei, Ergebnisse ohne Interpretation, Wertung erst in Handlungsbedarf/Diskussion)

### 11.2 Pro Abbildung/Tabelle/Formel
- [ ] Im Text referenziert (`Abbildung~\ref{}`), vor/nahe dem Objekt
- [ ] Caption: Nominalstil-Titel + erläuternde Sätze; Abb. unten, Tab. oben; alleinstehend verständlich
- [ ] Quelle `[n]` bzw. „in Anlehnung an [n]“ bei Fremdinhalten
- [ ] Vektor/hochaufgelöst, Schrift einheitlich, Achsen nach DIN 461, Maßstab bei Objektfotos, Legende vollständig
- [ ] Formel im Satz mit Satzzeichen, Variablen erklärt, `\formeleintrag{}`

### 11.3 Vor Abgabe (Fragenkatalog [LF 6] + formale Checks)
- [ ] Zentrale Fragestellung in der Einleitung klar herausgearbeitet?
- [ ] Bedeutsame Literatur mit sinnvoller Schwerpunktsetzung besprochen (nicht maximal viel)?
- [ ] Herleitung Soll aus Ist nachvollziehbar; Ergebnisse umsetzungsfähig?
- [ ] Einordnung in bisherige Literatur erfolgt?
- [ ] Ausblick mit konkreten Ansätzen?
- [ ] Tabellen/Abbildungen klar? Storyline über Topic Sentences und über Abbildungen allein erfassbar?
- [ ] Knappe, vollständige Zusammenfassung vorhanden?
- [ ] Umfang ausreichend aber knapp (≈ 60–80 S.)? Alle Arbeitspunkte der Aufgabenstellung erfüllt?
- [ ] Gliederung: ≤ 3 Ebenen, kein einzelnes Unterkapitel, Text nach jeder Überschrift, TOC-Umbrüche schön
- [ ] Keine Schusterjungen/Hurenkinder, Silbentrennung geprüft, keine Overfull-Boxes
- [ ] Literaturverzeichnis vollständig, nur zitierte Werke, keine fiktive Quelle
- [ ] Erklärung unterschrieben, Abgabedatum auf Titelblatt korrekt, Datenträger komplett

---

## 12. Projektspezifische Absprachen (von Nils/Betreuer, hier ergänzen)
- *(noch leer — geklärte Konflikte aus §1 hier mit Datum eintragen, z. B. „2026-11-xx K1: Betreuer will Präteritum für Versuche“)*
- Offene Fragen an Betreuer: K1 Tempus, K2 Aktiv/Passiv, K3 Kurzfassung ja/nein, K4 Mehrfachzitate, K5 Achsbeschriftung, K9 .bib statt Citavi.
