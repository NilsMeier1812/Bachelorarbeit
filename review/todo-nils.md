# To-do Nils: was nachzureichen ist

Gemeinsame Liste aller Kapitel-Threads (Wunsch Nils, 16.11.2026). Jeder Thread pflegt nur seinen eigenen Abschnitt,
vorher pullen. Abhaken mit `[x]`; die Antwort kann direkt in die Zeile oder in den Thread.
Kürzel verweisen auf die Fragen im jeweiligen Plan unter `review/plan-kap<N>.md`.

Regel seit 16.11.2026: Gesamtarbeit 60–80 Seiten, beim Ausarbeiten lieber zu viel, Nils kürzt selbst.

## Kapitel 4 – Fähigkeiten humanoider Roboter und verwandte Arbeiten

Entwurf: `Kapitel/04_Faehigkeiten_Verwandte_Arbeiten.tex`, Plan `review/plan-kap4.md`.

**Lesen und entscheiden**
- [ ] **K1 Entwurf Kap. 4 lesen.** Danach folgt die inhaltliche Prüfung aller Sätze gegen die Belege (Schritt 5).
- [ ] **K2 MuJoCo-Dokumentation als Quelle** (als PDF ins Quellen-Repo) für „MuJoCo kollidiert Meshes nur über ihre
      konvexe Hülle“: einverstanden?
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
- [x] **N1 Realversuche:** *ab etwa 23.11. quasi ständig; Abgabe 15.12.2026.* V2, V7, V11 fest eingeplant.
- [x] **N2 Zielwerte:** *„keine Ahnung“* → Claudes Vorschläge gelten (A3 ≥ 0,95 / ≥ 95 % · A4 ≤ 2 cm · A5 ≤ 100 ms / ≤ 1 s · A6 ≤ 60 min / ≤ 5). Nur widersprechen, wenn ein Wert falsch wirkt.
- [x] **N3 Nutzerstudie:** *Nils 17.11.: „werd es versuchen“, Zeit unsicher.* → geplant als Kann-Versuch (V9 mit K6.4); fällt sie aus, Ausblick. Claude liefert Ablauf und Fragebogen.
- [x] **N5 Externes Projekt:** *keins, A7 bleibt Konzept.* Optional kleines Beispielprogramm (Punkt 6 im Build-Prompt).
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
- [ ] Realversuche ab 23.11.: fünf Punkte im Dokument (V7, V2, V11, V5, V9, je dreimal); Protokollblätter kommen vorher von Claude.
- [ ] Festen Code-Stand im G1-Repo markieren (Tag), an dem alle Messungen laufen (gleich mit Kap. 7, E4).

## Kapitel 6 – Konzept der Umgebung

Plan: `review/plan-kap6.md` (Fragen in Abschnitt 8).

**Angaben und Material**
- [ ] **N5 Liste der Lauf-Policies**, die du gefunden und verworfen hast, je Policy kurz: Herkunft, warum genommen
      oder nicht (Lizenz, lief in MuJoCo, Arme frei, …). Für 6.2.3 und `tab:policies` in 4.1 (zugesagt seit 09.11.).
- [ ] **N8 Unitree-Entwicklerdoku als PDF** (support.unitree.com blockt automatische Abrufe): Seiten zu den Zuständen
      des Onboard-Reglers (FSM, Damp/Preparation/Walk), zur Arm-Schnittstelle `arm_sdk` (Gewicht, Wirkung auf die
      Taille), zum Laufdienst (LocoClient) und zur Fernbedienung. Im Browser „Drucken → als PDF“, ins Quellen-Repo
      `pdf/` hochladen. Für Kap. 2.3, 3.4.3, 6.2.3, 6.3.1, 6.3.3.
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
- [ ] **N10 Nachweis der Erweiterbarkeit (8.4.1):** siehe Kap. 5, N5.
- [ ] **Voll-Notaus in der Bedienoberfläche** (23.11.): Text und Abb. 6.3 sind angepasst. Sobald der Code im G1-Repo ist, kurz Bescheid geben (Commit), damit die Datenbasis im Kommentar stimmt.

## Kapitel 7 – Umsetzung

Plan zum Bearbeiten und Kommentieren: [Claude-Dokument Kapitelplan Kap. 7](https://claude.ai/artifact/TTAF3ZjZz9Esuakvih5DzC),
Entscheidungen ganz oben (Antwort direkt unter den Punkt). Markdown-Stand vom 16.11. auf Branch `claude/project-thread-jepdj5`.

**Entscheidungen** (zu jeder gibt es eine Empfehlung, „wie empfohlen“ genügt)
- [ ] **E1 Gliederung:** 7.5 „Roboterhände“ mit eigenen Händen (7.5.2), `tab:bedienwege` nach 6.4.2, kein eigener
      Sicherheitsabschnitt, Streamdeck entfällt. Einverstanden?
- [ ] **E3 Bezug zum Quelltext:** keine Programm- und Dateinamen im Fließtext, dafür Zuordnungstabelle im Anhang?
- [ ] **E4 Fester Code-Stand:** Ändert sich bis zur Abgabe noch etwas an Planer, Händen oder Bedienwegen? Dann Tag im
      G1-Repo setzen (gleich mit Kap. 5).
- [ ] **E6 Messwerte** aus der Technik-Doku nicht in Kap. 7, sondern für Kap. 8 neu messen?
- [ ] **E8 Freigaben in `_Vorschläge`:** Zhao2026 (AGILE) und Mamou2009 (V-HACD) freigeben; die vier optionalen vom
      16.11. (Lloyd 1982, RFC 2104 HMAC, Dijkstra 1959, Nocedal/Wright 2006) nur, wenn die Verfahrensnamen im Text
      stehen sollen.
- [ ] **E9 Smartphone:** nur das Prinzip (Kopplung, Prüfcode, Rollen, Zeitgrenzen), kein Protokolldetail?

**Angaben und Material**
- [ ] **E5 Unitree-Entwicklerdoku als PDF:** siehe Kap. 6, N8 (gleiche Seiten). Für 7.2.1, 7.3.2, 7.4.1.
- [ ] **E5 Szenen-Editor:** README des fremden Projekts `mujoco-scene-editor`, auf dem der eigene Editor aufbaut, als
      PDF ins Quellen-Repo; dann lege ich einen Software-Eintrag an.
- [ ] **PDFs über die FAU:** Mamou2009 (V-HACD, IEEE) und Ma2017 (OpenHand, IEEE, schon freigegeben, PDF fehlt).
- [ ] **E7 Bildschirmfotos** in hoher Auflösung nach `Bilder/`: Demo-Oberfläche (Pflicht) und eine Arbeitsplatz-Szene
      in MuJoCo neben RViz (optional).
- [ ] **Szenen:** Welche mitgelieferte Szene (A5, AP_1 bis AP_3) bildet welchen realen Arbeitsplatz ab?
- [ ] **Haken-Hand wiegen:** Masse im Hand-Profil ist mit 0,15 kg nur geschätzt.
