# To-do Nils: was nachzureichen ist

Gemeinsame Liste aller Kapitel-Threads (Wunsch Nils, 16.11.2026). Jeder Thread pflegt nur seinen eigenen Abschnitt,
vorher pullen. Abhaken mit `[x]`; die Antwort kann direkt in die Zeile oder in den Thread.
Kürzel verweisen auf die Fragen im jeweiligen Plan unter `review/plan-kap<N>.md`.

Regel seit 16.11.2026: Gesamtarbeit 60–80 Seiten, beim Ausarbeiten lieber zu viel, Nils kürzt selbst.

## Kapitel 5 – Handlungsbedarf, Anforderungen, Bewertungsmethodik

Plan: `review/plan-kap5.md`, bearbeitbar als Claude-Dokument https://claude.ai/artifact/1yNxU5TiVguZ9tJTpF8xFd (Fragen ganz oben, Antwort in die letzte Spalte). Wichtigstes zuerst.

**Entscheidungen**
- [x] **N1 Realversuche:** Abgabetermin und wie oft du bis dahin noch an den G1 kommst. → *Nils 16.11.: ab etwa
      23.11. quasi ständig.* Folge: V2, V7, V11 sind fest eingeplant; die Messmittel (N11) sollten bis dahin fertig sein.
- [ ] **N2 Zielwerte der Anforderungen:** *Nils 16.11.: „keine Ahnung“.* → Claude hat Vorschläge mit Begründung in
      `review/plan-kap5.md` Abschnitt 6 eingetragen (gelten vorläufig, die Ausarbeitung schreibt sie so). Bitte nur
      noch widersprechen, wenn dir ein Wert falsch vorkommt: A3 Echtzeitfaktor ≥ 0,95, Takttreue ≥ 95 % ·
      A4 Abweichung der Hand ≤ 2 cm · A5 Not-Halt ≤ 100 ms, Halt nach Ausfall ≤ 1 s · A6 Inbetriebnahme ≤ 60 min,
      erste Bewegung mit ≤ 5 Bedienhandlungen. A2 als „gleicher Programmstand, Unterschiede gezählt und begründet“.
- [ ] **N3 Nutzerstudie** mit 3–5 Personen ohne Robotikerfahrung: ja oder nein?
- [ ] **N7 Tabellen:** Merkmalstabelle der Stacks in 4.4 und in 5.1 nur Auswertung (Empfehlung)? Kernbild in 5.3.1?
- [ ] **N11 Messmittel** im G1-Repo bauen lassen (Echtzeitfaktor, Not-Halt-Zeit, Aufzeichnung der Gelenkwinkel,
      Planer-Messreihe, Code-Vergleich)? Nötig vor den Realversuchen.
- [ ] **N12 Recherche** zu den Lücken Q1 (Anforderungsliste), Q2 (Echtzeitfaktor, dringend), Q5, Q6 freigeben?

**Angaben und Material**
- [ ] **N4 Referenz-PC:** Prozessor, Arbeitsspeicher, Grafik, Betriebssystem; gibt es einen zweiten, schwächeren PC?
- [ ] **N5 Externes Projekt** für den Nachweis der Erweiterbarkeit (gleich mit Kap. 6, N10).
- [ ] **N8 Aufgabenstellung** des Lehrstuhls, falls schriftlich vorhanden (als PDF oder Text).
- [ ] **N9 Realtests Oktober:** Gibt es Aufzeichnungen, Videos, Notizen? Dürfen sie als Datenbasis dienen?
- [ ] **N10 Werbevideo:** wann, welche Funktionen, was musste angepasst werden.

**Durchführen (nach N1, N11)**
- [ ] Versuche am realen G1 nach `review/plan-kap5.md` Abschnitt 7.2: V2 Funktionsprüfung mit Protokoll, V7 gleiche
      Posenfolge in Simulation und am Roboter aufzeichnen, V11 neue Aufgabe am Roboter, optional V5/V8/V9 am Roboter.
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
- [ ] **N8 Benutzerhandbuch G1:** die hochgeladene Fassung ist eine Kopie von manualslib.com. Besser die Originaldatei
      von Unitree laden; dann lege ich den Zotero-Eintrag an.
- [ ] **N6 Doku deiner Realtests** (Datum, was getestet, was beobachtet, Fotos/Videos), z. B. Test mit schlaffer Taille
      am 15.10. Für 6.3.3 und Kap. 8 (gleich mit Kap. 5, N9).

**Entscheidungen**
- [ ] **N2 Entwurfsgrundsätze** in der Kapiteleinleitung (Erklärung im Thread): einverstanden?
- [ ] **N10 Nachweis der Erweiterbarkeit (8.4.1):** siehe Kap. 5, N5.

## Kapitel 7 – Umsetzung

Plan: `review/plan-kap7.md` (Fragen in Abschnitt 8, „E“). Liegt noch auf Branch `claude/project-thread-jepdj5`;
sag „auf main“, dann übernehme ich ihn.

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
