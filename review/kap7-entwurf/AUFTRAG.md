# Gemeinsamer Auftrag für die Schreib-Agenten Kap. „Umsetzung“ (27.11.2026)

Du schreibst ein Paket des Kapitels „Umsetzung“ (Label `chap:umsetzung`, Datei `Kapitel/07_Umsetzung.tex`) einer
Bachelorarbeit (Maschinenbau, FAU, Lehrstuhl FAPS) über eine Simulations- und Ausführungsumgebung für den humanoiden
Roboter Unitree G1. Autor ist Nils, du lieferst einen Entwurf, den er morgen korrigiert. Sprache Deutsch.

## Zuerst lesen (vollständig)
1. `/home/user/Bachelorarbeit/CLAUDE.md` (Belegsystem, Grafikregeln)
2. `/home/user/Bachelorarbeit/Richtlinien-BA.md` (mindestens §0, §4, §6, §7, §11, §12)
3. `/home/user/Bachelorarbeit/review/kap7-entwurf/plan-kap7.md`: Abschnitt „Festlegungen aus der Rückmeldung vom 26.11.“
   (gilt VOR allem anderen im Plan), §1 (Rolle, Abgrenzung, Schreibregeln), §2 (Gliederung, Umfang), den Abschnitt
   deines Pakets in §3, deine Abbildungen/Tabellen/Gleichungen in §4, §5 (Quellen), §6, §7 (Begriffe), §9.6 (AP 4).
4. `Kapitel/06_Konzept.tex` (Konzept, auf das du zurückverweist; nichts daraus wiederholen, nur per `\ref`
   aufbauen; der Kommentarblock unter `tab:schutzmechanismen` nennt die Auslegungswerte mit Fundstellen) und
   das Gerüst `Kapitel/07_Umsetzung.tex` (Labels). Für Vorverweise die Labels in `Kapitel/08_Evaluation.tex`,
   für Grundlagen die Labels in Kap. 2–4 (`grep -o '\\label{[^}]*}' Kapitel/0[2-4]*.tex`).
5. Vorhandene Belege: `evidence/*.yaml`, freigegebene Keys: `zotero-map.json`. PDF-Texte: `sources-text/<key>.txt`.

## Code
Code-Repo (nur lesen, NICHTS ändern, nichts committen): `/home/user/g1-ba` = Branch BA-Stable @ `6a40e47`
(außer dein Auftrag nennt einen anderen Worktree). Jede Aussage über den eigenen Code braucht eine selbst gelesene
Fundstelle. Doku unter `g1pilot/docs/` ist nur Wegweiser, kann veraltet sein.

## Harte Regeln
- Nichts erfinden. Kein Trainingswissen als Inhalt. Fremdes (MuJoCo, DDS, ROS 2, ONNX, Docker, Unitree-Firmware,
  Verfahren) nur mit `\cite{Key}\ev{Key.NN}` aus `evidence/`, mit Verweis `Abschnitt~\ref{…}` auf Kap. 2–4 oder als
  `\qf{was fehlt}`. Unklares als `\pruefen{…}`.
- Neue Belege aus vorhandenen PDFs: Du darfst `evidence/` NICHT ändern (andere Agenten laufen parallel). Schlage
  sie stattdessen in deiner Notizdatei vor: Key, gedruckte Seite (Seitenmarker in sources-text), wörtliches Zitat
  (exakt kopiert, 1–3 Sätze), Kernaussage. Im Text verwendest du dafür die ID `\ev{Key.NEU1}`, `\ev{Key.NEU2}` …
  (ich vergebe die echten Nummern). Nur Keys aus `zotero-map.json`.
- Eigenleistung: Jeder Absatz über die eigene Umsetzung endet mit einem LaTeX-Kommentar
  `% DB: <Pfad relativ zur Repo-Wurzel>:<Zeilen> @6a40e47` (mehrere Fundstellen durch Komma).
- Keine Messergebnisse (gehören in die Evaluation), keine Entwicklungsgeschichte, keine Bedienanleitung (für
  Bedienung ein Satz mit Verweis auf `Anhang~\ref{anh:dokumentation}`), keine Programm- und Dateinamen im Text
  (Funktionsbezeichnungen wie „der Armplaner“, „die Kopplungsschicht“ sind gut; Datenformate wie ONNX ok).
  Ausdrücklich sagen, was nur in der Simulation oder nur real gilt.
- Begriffe: „Bedienoberfläche“ (nie Demo-GUI), „Controller“ (nie Gamepad). Keine festen Kapitelnummern, immer `\ref`.
- Stil (Richtlinien §4): Präsens, Sach-Subjekt, kein ich/wir/man, kein Konjunktiv, mindestens zwei Sätze je Absatz,
  Zahlen mit `\,` vor der Einheit, Abkürzungen mit `\ac{}` (vorhandene in `main.tex`/Abkürzungsliste prüfen; fehlende
  in der Notizdatei melden, nicht in main.tex eintragen). KEINE Semikolons, KEINE Gedankenstriche (–, —, ---) im
  Fließtext, Bis-Strich in Bereichen (3--5) bleibt. Erster Satz von Abschnitt/Unterabschnitt fasst den Inhalt als
  Aussage zusammen, wo es natürlich passt, nie „Im Folgenden …“. Keine Sätze „X et al. zeigen …“, Inhalte als
  Aussage, Quelle dahinter. Aufbau je Unterabschnitt: Rückbezug auf das Konzept (`\ref`, 1–2 Sätze), Lösung,
  wo passend 1 Satz Vorverweis auf die Evaluation (`\ref`).
- Gleichungen in den Satz einbinden, Variablen direkt darunter erklären, Verweis `Gleichung~\ref{eq:…}`.
- Abbildungen/Tabellen: vor der Umgebung im Text mit `\ref` einführen, danach erläutern. `[htbp]`. TikZ als eigene
  Datei `Bilder/tikz/<name>.tex` mit `\begin{tikzpicture}[ba]`, nur Stile/Farben aus `ba-grafik.tex`, NIE skalieren,
  max. 16 cm breit. Muster: `Bilder/tikz/ik-vorwaerts-invers.tex`, `Bilder/tikz/dds-domains.tex`. Tabellen nach
  CLAUDE.md (Gitter mit `\tabkopfzeile`/`\tabkopf{}` bzw. booktabs, `\tabstil`, `tabularx`). Für Bildschirmfotos, die
  Nils noch liefert, einen Platzhalter: `\fbox{\parbox[c][5cm][c]{0.9\textwidth}{\centering Platzhalter: …}}` plus
  `\pruefen{Bild von Nils: Bilder/kap7/<datei>}`.
- Grafik prüfen: Kompiliere jede eigene Grafik in einem Testdokument, das die echte Präambel nutzt
  (Vorschlag: Kopie von `main.tex` in dein Scratch-Verzeichnis mit nur deinem Abschnitt, oder kleines Dokument mit
  `\documentclass[12pt]{…}` wie main.tex, `\input{ba-grafik}` nach den Farbdefinitionen). Mit `latexmk -pdf` und
  `-outdir` außerhalb des Repos. Rendere die Seite als PNG (`pdftoppm -r 110 -png`) und sieh sie dir mit dem Read-Tool
  an: keine Überlappungen, gleichartige Elemente gleich hoch, Kanten bündig, Innenabstände gleich. 1–2 Runden.
- Dateien: Schreibe NUR die Dateien deines Pakets (unten) und neue `Bilder/tikz/*.tex`, eigene CSV in `Daten/`.
  NICHT ändern: `main.tex`, `Kapitel/*`, `evidence/`, `zotero.bib`, `zotero-map.json`, `sources-text/`, andere
  Agenten-Dateien. Kein git commit/push.
- `/mnt/project-files` ist ein Netzlaufwerk: Pfade mit Schrägstrich am Ende, nie den ganzen Ordner durchsuchen.
- Umfang ist ein Richtwert: Seitenzahl deines Pakets einhalten (± 15 %). Eine Seite Fließtext ≈ 330 Wörter, eine
  mittelgroße Abbildung ≈ 0,4 S., eine Tabelle je nach Größe 0,3–0,6 S. Nicht mehr schreiben.

## Lieferung
1. `review/kap7-entwurf/<paket>.tex`: LaTeX-Abschnitte mit `\section`/`\subsection` und den Labels aus dem Gerüst,
   direkt in `07_Umsetzung.tex` einfügbar (keine Präambel).
2. `review/kap7-entwurf/<paket>-notizen.md`: (a) kurzes Faktenblatt: je Kernaussage Fundstelle und Werte;
   (b) vorgeschlagene neue Belege (Format oben); (c) Liste aller `\qf{}`/`\pruefen{}`; (d) Abweichungen vom Plan mit
   Grund; (e) fehlende Abkürzungen; (f) geschätzter Umfang in Seiten.
3. Als Antwort an mich: 10–15 Zeilen Zusammenfassung (was steht, was offen ist).
