# To-do Nils: was nachzureichen ist

Gemeinsame Liste aller Kapitel-Threads (Wunsch Nils, 16.11.2026). Jeder Thread pflegt nur seinen eigenen Abschnitt,
vorher pullen. Abhaken mit `[x]`; die Antwort kann direkt in die Zeile oder in den Thread.
Kürzel verweisen auf die Fragen im jeweiligen Plan unter `review/plan-kap<N>.md`.

Umfang (Betreuerin, 23.11.2026): 60–80 Seiten inkl. Abbildungen und Tabellen, von der Einleitung bis vor das
Literaturverzeichnis; 80 ist hart, Ziel 70–75. Entwürfe etwa Endumfang ÷ 0,6, Nils kürzt.
Weitere Ergebnisse des Betreuertreffens vom 23.11.: `Richtlinien-BA.md` §12.

## Kapitel 1 – Einleitung

Entwurf: `Kapitel/01_Einleitung.tex` (25.11.2026). Plan mit Fragen E1–E5 zum Bearbeiten:
[Claude-Dokument Kapitelplan Kap. 1](https://claude.ai/artifact/4mAyMppsMTB2uLoj3k4X9D), Antwort in die letzte Spalte.

**Entscheidungen**
- [ ] **E1 Forschungsfragen:** F3 ohne Bezug auf eine Nutzerbefragung, F4 als Entwurfsfrage „Wie lässt sich die Umgebung
      modular aufbauen?“ (Wortlaut im Plan). Hängt mit Kap. 5, P3 zusammen.
- [ ] **E2 / Q1 Recherche freigeben:** 1–2 Quellen, dass Unternehmen Nutzen, Kosten und Risiko eines Humanoiden vor einer
      Anschaffung schwer abschätzen können (einziges „Quelle fehlt“ in Kap. 1). Gleiche Lücke wie in Kap. 5.1.
- [ ] **E3–E5:** G1Pilot schon in 1.2 nennen (ja), Name der Umgebung erst nach deiner Wahl, Video nicht in der Einleitung.

**Angaben und Material**
- [ ] Overleaf `zotero.bib` aktualisieren: siehe Kap. 5 (Afzal2021 wird jetzt auch in Kap. 1 zitiert).

## Kapitel 4 – Fähigkeiten humanoider Roboter und verwandte Arbeiten

Entwurf: `Kapitel/04_Faehigkeiten_Verwandte_Arbeiten.tex`, Plan `review/plan-kap4.md`.

**Lesen und entscheiden**
- [ ] **K1 Entwurf Kap. 4 lesen.** Danach folgt die inhaltliche Prüfung aller Sätze gegen die Belege (Schritt 5).
- [x] **K2 MuJoCo-Dokumentation als Quelle** (als PDF ins Quellen-Repo) für „MuJoCo kollidiert Meshes nur über ihre
      konvexe Hülle“: einverstanden? → *Betreuerin 23.11.: offizielle Websites und GitHub-Repos sind als Quelle erlaubt, mit Abrufdatum (GitHub zusätzlich Commit-Hash).*
- [ ] **K3 Freigaben in `_Vorschläge`** für `tab:policies`: Zhao2026 (AGILE, gleich mit Kap. 7, E8), Zhang2025 (R2S2),
      Cadene2026 (LeRobot).
- [ ] **K4 Recherche freigeben** für die offenen Lücken: Grenzen der Greifkraft (z. B. ISO/TS 15066), Bedienung über
      Gamepad/Smartphone.

**PDFs über die FAU** (ins Quellen-Repo `pdf/`, Name `Nachname_Jahr_Kurztitel.pdf`, dann kurz Bescheid)
- [ ] **K5 Piazza2019** (Überblick Roboterhände) – am wichtigsten, für 4.2.4: Abwägung vielseitige Hand vs. einfacher,
      aufgabenspezifischer Greifer (Nils 16.11.). Ergänzend Billard2019, Controzzi2014.
- [ ] **K6 Taktile Sensorik:** Dahiya2010, Kappassov2015.
- [ ] **K7 Trochez2026** (PDF fehlt). Ma2017 und Mamou2009 siehe Kap. 7.

**Angaben und Material**
- [ ] **K8 Foto** von Rubber Hands, Inspire FTP und gedruckter Hand nebeneinander (eigene Aufnahme) für 4.2.4.
- [ ] **K9 Kenndaten Hände:** Gewicht der Rubber Hands (Datenblatt/Quelle) und der Haken gewogen (bisher 0,15 kg geschätzt).

## Kapitel 5 – Handlungsbedarf, Anforderungen, Bewertungsmethodik

Plan: `review/plan-kap5.md`, bearbeitbar als Claude-Dokument https://claude.ai/artifact/1yNxU5TiVguZ9tJTpF8xFd (Fragen ganz oben, Antwort in die letzte Spalte; Claudes Rückfragen direkt darunter). Wichtigstes zuerst.

**Entscheidungen**
- [ ] **Vorschläge P1–P7 nach dem Betreuergespräch** beantworten: Kap.-5-Dokument https://claude.ai/artifact/Pigwxc4wCMmMQajQLVK75B, Tab „Anpassungen nach Betreuergespräch“, letzte Spalte. Danach passe ich die .tex an.
- [x] **N1 Realversuche:** *ab etwa 23.11. quasi ständig; Abgabe 15.12.2026.* V2, V7, V11 fest eingeplant.
- [x] **N2 Zielwerte:** *„keine Ahnung“* → Claudes Vorschläge gelten (A3 ≥ 0,95 / ≥ 95 % · A4 ≤ 2 cm · A5 ≤ 100 ms / ≤ 1 s · A6 ≤ 60 min / ≤ 5). Nur widersprechen, wenn ein Wert falsch wirkt.
- [x] **N3 Nutzerstudie:** *entfällt (Betreuerin, 23.11.): technische Arbeit ohne Vorher-Vergleich, keine Umfrage.* Fragebogen und K6.4 fallen weg, Kap. 8 wird kürzer; V9 bleibt als technische Messung des Bedienaufwands (Vorschlag P1/P2).
- [x] **N5 Externes Projekt:** *keins, A7 bleibt Konzept.* Seit 23.11. (Betreuerin): Erweiterbarkeit wird nicht eigens nachgewiesen, sondern als Frage „wie modular?“ mit dem Docker-Container als Lösung geführt.
- [x] **Video als Ergebnis** (23.11., Betreuerin): erlaubt, aber nur sparsam.
- [x] **N7 Tabellen:** *wie empfohlen.*
- [x] **N8 Aufgabenstellung:** *keine.* Herleitung nur aus den Defiziten.
- [x] **N11 Messmittel:** *ja, Nils baut mit eigenem Agenten.* Prompt im Dokument (inkl. ausführlicher Armplaner-Messreihe).
- [x] **N12 Recherche:** *ja.* Claude recherchiert Q2, Q1, Q5, Q6 (Q3 falls N3 ja).

**Angaben und Material**
- [ ] **N4 Referenz-PC:** nur Prozessor, Arbeitsspeicher, Grafikkarte, Betriebssystem des PCs, auf dem die Simulation läuft (kein Benchmark, kein zweiter PC).
- [ ] **N10 Werbevideo** (Box von A nach B, Datenbasis V3): drei Sätze – wann gedreht, welche Funktionen genutzt, was angepasst werden musste.
- [x] **N9 Realtests Oktober:** *nur „alle Funktionen funktionieren“, kein Protokoll* → V2 wird neu mit Protokoll gemacht.

- [x] **PDFs Recherche Kap. 5:** *hochgeladen 16.11.* Claude hat die fünf Einträge mit Nils' Erlaubnis nach „Bachelorarbeit“ verschoben,
      Citation Keys gesetzt und exzerpiert (Pitonakova2018, Bender2021, Afzal2021, DINENISO13850, Valori2021); Norm-Eintrag auf DIN-Fassung 2016-05 umgestellt.
- [ ] **Optional ISO 13855:2024** (Gesamtreaktionszeit T, Sicherheitsabstand; `_Vorschläge` G3SXHFSB): PDF über FAU/UB (DIN Media), ins Quellen-Repo, freigeben. Nur nötig, wenn 5.2 die Norm direkt zitieren soll; die Kernaussage ist über DGUV2015 schon belegt.
- [ ] **Overleaf:** `zotero.bib` → *Aktualisieren* und pushen, sonst kennt LaTeX die fünf neuen Keys nicht.

**Durchführen**
- [ ] Messmittel mit dem Build-Prompt aus dem Dokument bauen lassen, vor dem 23.11.
- [ ] Realversuche ab 23.11.: Punkte im Dokument (V7, V2, V11, V5, je dreimal; Nutzerstudie entfällt seit 23.11.); Protokollblätter kommen vorher von Claude.
- [ ] Festen Code-Stand im G1-Repo markieren (Tag), an dem alle Messungen laufen (gleich mit Kap. 7, E4).

## Kapitel 6 – Konzept der Umgebung

Plan: `review/plan-kap6.md` (Fragen in Abschnitt 8).

**Angaben und Material**
- [ ] **N5 Liste der Lauf-Policies**, die du gefunden und verworfen hast, je Policy kurz: Herkunft, warum genommen
      oder nicht (Lizenz, lief in MuJoCo, Arme frei, …). Für 6.2.3 und `tab:policies` in 4.1 (zugesagt seit 09.11.).
- [x] **N8 Unitree-Entwicklerdoku:** *erledigt (Betreuerin, 23.11.): die Unitree-Support-Website darf mit Abrufdatum
      zitiert werden, ein offizielles Doku-PDF ist nicht nötig.* Für den wörtlichen Beleg braucht es nur noch einen
      Ausdruck der Seiten (Browser „Drucken → als PDF“, Datum im Dateinamen) im Quellen-Repo, siehe CLAUDE.md
      „Websites und GitHub-Repos als Quelle“. Alte Beschreibung zur Orientierung:
      Seiten zu den Zuständen
      des Onboard-Reglers (FSM, Damp/Preparation/Walk), zur Arm-Schnittstelle `arm_sdk` (Gewicht, Wirkung auf die
      Taille), zum Laufdienst (LocoClient) und zur Fernbedienung. Im Browser „Drucken → als PDF“, ins Quellen-Repo
      `pdf/` hochladen. Für Kap. 2.3, 3.4.3, 6.2.3, 6.3.1, 6.3.3.
      Löst in Kap. 6 die zwei „Quelle fehlt“-Stellen L23 (Fernbedienung) und L24 (arm_sdk).
      Suchhinweis (23.11., P16): auf support.unitree.com im G1-Entwicklerteil nach „arm_sdk“ suchen. Belegt werden muss,
      dass die Arme über `rt/arm_sdk` mit einem Gewicht zwischen Onboard-Regler und eigener Steuerung übergeblendet
      werden und dass das auch die Taille betrifft. Notlösung: offizielles Beispiel `g1_arm_sdk_dds_example.cpp`.
- [ ] **N8 Benutzerhandbuch G1:** die hochgeladene Fassung ist eine Kopie von manualslib.com. Besser die Originaldatei
      von Unitree laden; dann lege ich den Zotero-Eintrag an.
      Suchhinweis (23.11., P15): auf unitree.com bzw. support.unitree.com nach „G1 User Manual“ suchen. Gebraucht für
      die Fernbedienung als unabhängige Dämpfung (6.3.2). Notfalls geht die manualslib-Kopie.
- [ ] **N6 Doku deiner Realtests** (Datum, was getestet, was beobachtet, Fotos/Videos), z. B. Test mit schlaffer Taille
      am 15.10. Für Kap. 8 (gleich mit Kap. 5, N9); in 6.3.3 steht der Realtest seit 23.11. nicht mehr (P17).

**Entscheidungen**
- [ ] **N2 Entwurfsgrundsätze** in der Kapiteleinleitung (Erklärung im Thread): einverstanden?
- [x] **N10 Nachweis der Erweiterbarkeit (8.4.1):** *entfällt in dieser Form (Betreuerin, 23.11.):* kein Nachweis, sondern Frage „wie modular?“ mit dem Docker-Container als Lösung. Siehe Kap. 5, N5.
- [x] **Voll-Notaus in der Bedienoberfläche** (23.11.): Text und Abb. 6.3 sind angepasst. → Code ist in BA-Stable @ 6a40e47 (Knopf VOLL-NOTAUS 1,5 s halten), Datenbasis-Kommentar nachgetragen (24.11.).

## Kapitel 7 – Umsetzung

Plan zum Bearbeiten und Kommentieren: [Claude-Dokument Kapitelplan Kap. 7](https://claude.ai/artifact/TTAF3ZjZz9Esuakvih5DzC),
Entscheidungen ganz oben (Antwort direkt unter den Punkt). Markdown-Stand vom 16.11. auf Branch `claude/project-thread-jepdj5`.

**Entscheidungen**
- [x] **E1 Gliederung:** *wie empfohlen (24.11.)*
- [x] **E2 Umfang:** *Seitenbudget 24.11.: 15 S. Endfassung inkl. Abbildungen, Entwurf 20–40 % darüber*
- [x] **E3 Bezug zum Quelltext:** *keine Programm- und Dateinamen im Text, Funktionsnamen wie „der Armplaner“ sind ok (24.11.)*
- [x] **E4 Fester Code-Stand:** *am Planer ändert sich vermutlich nichts, Branch „BA-Stable“ angelegt (24.11.), Abgleich läuft über den Koordinator*
- [x] **E6 Messwerte:** *wie empfohlen, Kap. 8 misst neu (24.11.)*
- [ ] **E8 Freigaben in `_Vorschläge`:** Zhao2026 (AGILE) und Mamou2009 (V-HACD) freigeben? Die vier optionalen vom
      16.11. (Lloyd 1982, RFC 2104 HMAC, Dijkstra 1959, Nocedal/Wright 2006) nur, wenn die Verfahrensnamen im Text
      stehen sollen. *Noch offen.*
- [x] **E9 Smartphone:** *nur das Prinzip, keine Anleitung, keine echten Bedienschritte (24.11.)*

**Angaben und Material**
- [ ] **E5 Unitree-Entwicklerdoku als PDF:** Zitieren ginge auch als Website, aber Belege (`\ev{}`) entstehen nur aus PDFs.
      Deshalb bitte die Seiten als PDF speichern (G1 Basic Services, Arm-Schnittstelle, Sport/Loco-Dienste, gleiche Seiten
      wie Kap. 6, N8) und ins Quellen-Repo `pdf/` laden. Für 7.2.1, 7.3.2, 7.4.1.
- [ ] **E5 Szenen-Editor:** README des fremden Projekts `mujoco-scene-editor`, auf dem der eigene Editor aufbaut, als
      PDF ins Quellen-Repo; dann lege ich einen Software-Eintrag an.
- [ ] **PDFs über die FAU:** Mamou2009 (V-HACD, IEEE) und Ma2017 (OpenHand, IEEE, schon freigegeben, PDF fehlt).
- [x] **Szenen:** *keine Szene bildet einen echten Arbeitsplatz ab, im Text meist AP_1 verwenden, weil am vollständigsten (24.11.)*
- [x] **Haken-Hand:** *rund 110 g gesamt, nicht ganz sicher (24.11.), im Text als Schätzwert kennzeichnen*

**E7 Bildschirmfotos und Fotos für Kap. 7** (24.11., alles in einem Rutsch). Bitte in hoher Auflösung nach
`Bilder/kap7/` legen (Bildschirmfotos in voller Größe, Zuschnitt und Beschriftung mache ich), Dateiname wie in Klammern.
Pflicht wird sicher verwendet, Reserve nur, wenn Platz ist.
- [ ] **Pflicht: Demo-GUI Gesamtansicht** in der Simulation mit AP_1, Roboter steht (`demo-gui-gesamt.png`). Für 7.6.1.
- [ ] **Pflicht: Demo-GUI mit Not-Halt und Voll-Notaus** gut sichtbar, gern im Realbetrieb (`demo-gui-notaus.png`). Für 7.6.1.
- [ ] **Pflicht: MuJoCo-Fenster mit Szene AP_1** und daneben RViz mit demselben Weltmodell (`szene-mujoco-rviz.png`). Für 7.2.3.
- [ ] **Pflicht: Foto des realen G1 mit Inspire-Hand und mit Haken-Hand** (`hand-inspire.jpg`, `hand-haken.jpg`). Für 7.5.
- [ ] **Reserve: Startmenü** mit den Umgebungs-Kacheln (`startmenue.png`). Für 7.1.
- [ ] **Reserve: Demo-GUI Ansicht „Controller“** mit der Gamepad-Belegung (`demo-gui-controller.png`). Für 7.6.2.
- [ ] **Reserve: Smartphone-Bedienung**, ein Bildschirm mit verbundenem Roboter (`smartphone.png`). Für 7.6.3.
- [ ] **Reserve: Dialog „Neue Hand anlegen“** mit erkannter Montage (`hand-anlegen.png`). Für 7.5.2.
- [ ] **Reserve: Szenen-Editor** mit geöffneter Szene AP_1 (`szenen-editor.png`). Für 7.2.3.
- [ ] **Reserve: Planer in RViz**, Hand fährt um ein Hindernis, geplante Bahn sichtbar (`planer-bahn-rviz.png`). Für 7.4.3.

## Kapitel 9 – Zusammenfassung und Ausblick

Entwurf: `Kapitel/09_Zusammenfassung.tex` (ca. 4 S.), Plan mit Fragen Z1–Z9 als Claude-Dokument
https://claude.ai/artifact/XuFk1M5Ke3kRyD95SYhnTv (Antwort in die letzte Spalte, leer = wie empfohlen).
Kap. 9 wird als letztes fertig: die `\pruefen{}` in 9.1 lösen sich, sobald Kap. 5 und 8 stehen.

**Entscheidungen**
- [ ] **Z3 Wortlaut F4:** Modularität als Entwurfsfrage mit Container-Profilen und Andockpunkten als Antwort, ohne Nachweis? Hängt an Kap. 5 (P1–P7).
- [ ] **Z7 Ausblick-Themen:** Policy-Transfer, Abgleich mit Realdaten, Navigation mit Wahrnehmung, externes Projekt, Sicherheitsnachweis. Gibt es ein konkretes Folgeprojekt am Lehrstuhl?
- [ ] **Z8 Nutzerstudie im Ausblick** (ein Satz: sinnvoll, sobald eine zweite Fassung verglichen werden kann)?
- [ ] **Z9 Eigenname der Plattform:** siehe Kap. 6 bzw. Koordinator, Kap. 9 wird danach umbenannt.

**Abhängigkeiten** (kein Material von dir nötig, nur Hinweis)
- [ ] Ergebnisse Kap. 8 (V1–V9) und Abgleich A1–A7 in 8.4.1, siehe Kap. 5 „Durchführen“.
