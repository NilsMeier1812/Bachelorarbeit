# CLAUDE.md – Bachelorarbeit Nils (Maschinenbau, FAU)

Du unterstützt Nils beim Schreiben seiner Bachelorarbeit in LaTeX (FAPS-Vorlage, Thema: Unitree-G1-Humanoid,
MuJoCo-Simulation, Sim-to-Real; Code und Experimente im Repo `NilsMeier1812/G1`). Der Text synct über GitHub
(Branch `main`) mit Overleaf. Die Nutzung von Claude ist mit dem Lehrstuhl abgestimmt.
**Nils ist Autor und trägt die Verantwortung** – du lieferst Entwürfe, Belege und Prüfungen, er entscheidet.

Zusätzlich gilt `Richtlinien-BA.md` (Schreibregeln des Lehrstuhls, vor jeder Textarbeit lesen). Bei Widerspruch
gilt für Quellen und Belege diese Datei, für Stil, Aufbau und Zitierform die Richtlinien.

## Grundprinzip

Du arbeitest **ausschließlich quellenbasiert**. Jede inhaltliche Aussage im Text muss auf eine konkrete,
wörtlich belegte Textstelle in einer Quelle aus Nils' Zotero-Bibliothek zurückführbar sein.
Dein Trainingswissen ist für Inhalte tabu – auch für Dinge, die „allgemein bekannt“ wirken
(Definitionen, Normwerte, Formeln, Materialkennwerte, historische Angaben).
Wenn du etwas nicht belegen kannst, **markierst du die Lücke**, statt sie zu füllen.

## Harte Regeln

1. **Nur Quellen aus Zotero.** Keine Quellen „aus dem Gedächtnis“, keine erfundenen Titel, Autoren,
   Seitenzahlen oder DOIs. Was nicht in `zotero-map.json` steht (= freigegeben: Sammlung „Bachelorarbeit“
   mit `Citation Key`), existiert für den Text nicht.
   Websuche ist **nur im Recherche-Modus** erlaubt, und nur um Quellen zu *finden* – nie, um Inhalte daraus
   direkt in den Text zu übernehmen. Inhalte kommen ausschließlich aus PDFs in Zotero.
2. **Jede Sachaussage trägt Zitat + Beleg-ID:** `\cite{Mueller2021}\ev{Mueller2021.03}`.
   Ohne passenden Beleg schreibst du `\qf{was fehlt}` (Quelle fehlt) und formulierst die Aussage nicht aus.
3. **Zitate in `evidence/` sind wörtlich** aus `sources-text/<key>.txt` kopiert – nie aus dem Gedächtnis,
   nie geglättet, nie übersetzt. `seite` ist die **gedruckte** Seitenzahl (das Label im Seitenmarker),
   nicht der PDF-Index.
4. **Die Paraphrase darf nicht mehr behaupten als der Beleg.** Keine Verallgemeinerung, Einschränkungen
   erhalten („bis zu“, „bei Raumtemperatur“, „im untersuchten Fall“), Zahlen und Einheiten exakt übernehmen,
   keine Kausalität erfinden, wo die Quelle nur Korrelation beschreibt.
5. **Eigenleistung** (Nils' Messungen, Berechnungen, Konstruktionen, Auswertungen) braucht keine Quelle,
   aber einen Verweis auf die Datenbasis (Kapitel, Anhang, Datei). Erfinde **niemals** Ergebnisse, Messwerte
   oder Zahlen. Fehlen sie: `\pruefen{Wert aus Messung X einsetzen}`.
6. **Im Zweifel markieren:** `\pruefen{...}` statt raten. Eine sichtbare Lücke ist immer besser als eine
   plausible Erfindung.
7. **Zotero:** Lesen ist frei. Schreiben nur, um (a) im Feld *Extra* die Zeile `Citation Key: <key>` zu
   setzen (bei freigegebenen Einträgen in der Sammlung „Bachelorarbeit“) und (b) im Recherche-Modus neue
   Einträge **ausschließlich in der Sammlung `_Vorschläge`** anzulegen.
   Andere Metadaten nur nach Rückfrage ändern. Nichts eigenmächtig aus `_Vorschläge` herausverschieben.
   **Niemals** Einträge, Anhänge oder Annotationen löschen.
8. **Generierte Dateien nicht von Hand ändern:** `zotero.bib` (verknüpft Overleaf aus Zotero, nur über
   „Aktualisieren“ in Overleaf), `zotero-map.json`, `sources-text/`, `.zotero-cache/`.
9. **Bevor du eine Aufgabe als fertig meldest:** `python3 scripts/check.py` ausführen. 0 Fehler ist Pflicht;
   Warnungen nennst du Nils explizit. `\ev{*}` nur für reine Verweise ohne Sachaussage, nie um Fehler
   zu kaschieren.
10. Bei Sprache, Gliederung, Übergängen, LaTeX-Technik darfst du frei helfen – solange dabei keine neuen
    Inhalte ohne Beleg entstehen.

## Projektstruktur

```
Bachelorarbeit/           # Repo-Root = Overleaf-Projekt (Hauptdokument main.tex)
├── CLAUDE.md
├── Richtlinien-BA.md     # Schreibregeln des Lehrstuhls
├── main.tex              # Präambel lädt \input{ba-makros}
├── Kapitel/              # ein .tex pro Kapitel
├── Bilder/
├── ba-makros.tex         # \ev, \qf, \pruefen
├── zotero.bib            # von OVERLEAF aus Zotero online verknüpft und gepusht – nie selbst schreiben
├── zotero-map.json       # GENERIERT (zot.py bib): freigegebene citekeys -> Zotero-Item-Key
├── evidence/             # Belegdateien, eine pro Quelle: <citekey>.yaml
├── sources-text/         # GENERIERT, gitignored: PDF-Text mit Seitenmarkern
├── .zotero-cache/        # GENERIERT, gitignored: über die Web-API geladene PDFs
├── review/               # Kapitelpläne und Verifier-Berichte
├── requirements.txt
└── scripts/
    ├── zot.py            # bib | text | annotations
    ├── check.py          # mechanische Prüfung
    ├── balib.py          # gemeinsame Funktionen
    └── README.md         # Einrichtung und Stolpersteine
```

**Zotero:** nur Zotero online (zotero.org, Nutzer `NilsMeier18`, ID 22350426), keine Desktop-App, kein Better
BibTeX. Sammlung **„Bachelorarbeit“** (Key `99VAKC9A`) = freigegebene Quellen, darauf ist `zot.py`
standardmäßig beschränkt. Sammlung **`_Vorschläge`** (Key `3IKVZZGG`) = deine Recherche-Vorschläge. Overleaf importiert die
ganze Bibliothek als `zotero.bib` (nur Zitiertes wird gedruckt); deshalb entscheidet `zotero-map.json`, was
zitiert werden darf. Web-API: `https://api.zotero.org/users/22350426/...` mit Header
`Zotero-API-Key: dummy` – in Claudes Cloud-Umgebung setzt der Proxy den echten Schlüssel ein.

**Cloud-Sitzungen:** `sources-text/` und `.zotero-cache/` sind gitignored und in einer neuen Sitzung leer.
Vor dem Exzerpieren oder `check.py` also zuerst `python3 scripts/zot.py text` laufen lassen.

## Arbeitsablauf

### Kapitel-Workflow (z. B. „Kapitel 2.3 ist als Nächstes dran“)

Dieser Ablauf verbindet Recherche, Exzerpt und Schreiben. **Nach Schritt 2 und nach Schritt 4 wartest du
auf Nils.** Arbeitet Nils gerade nicht mit (unbeaufsichtigter Lauf), erledigst du Schritt 1–3 und hörst dort auf.

**1. Kapitelplan als Fragen** → `review/plan-<kapitel>.md`
- Lies vorhandene Kapitel, die Gliederung und vorhandene Belege in `evidence/`.
- Formuliere, was das Kapitel leisten soll, als **offene Fragen**, nicht als Aussagen:
  „Wie wirkt sich Oberflächenrauheit auf die Dauerfestigkeit aus, und ab welchem Bereich?“ –
  nicht „Rauheit senkt die Dauerfestigkeit ab Rz 25“. Dein Vorwissen hilft beim Fragen, nie beim Antworten.
- Markiere je Frage: durch vorhandene Belege abgedeckt / teilweise / offen.

**2. Recherche** (nur für offene Fragen) → Ergänzung in `review/plan-<kapitel>.md`
- Suchen in: Google Scholar, Crossref, Semantic Scholar, Verlagsseiten, Normenverzeichnisse, Katalog der
  UB Erlangen-Nürnberg. Bevorzugt: Fachbücher, Normen/Richtlinien (DIN, VDI, FKM), begutachtete Artikel,
  Dissertationen. **Nicht** als Quelle: Wikipedia, Blogs, Foren, Herstellerwerbung, KI-generierte Seiten
  (dürfen höchstens als Suchhinweis dienen).
- **Jede Quelle verifizieren, bevor du sie vorschlägst:** DOI über `https://api.crossref.org/works/<DOI>`
  oder die Verlagsseite abrufen und Titel, Autoren und Jahr abgleichen. Bücher/Normen über Verlags- oder
  Katalogeintrag (ISBN). Was du nicht im Netz bestätigt findest, schlägst du nicht vor.
- Vorher prüfen, ob DOI/ISBN schon in Zotero ist (keine Duplikate).
- Lege jede verifizierte Quelle in Zotero in der Sammlung `_Vorschläge` an (mit DOI/ISBN/URL, **ohne**
  `Citation Key` – den setzt du erst nach Nils' Freigabe) und notiere
  im Plan je Vorschlag: welche Frage sie beantworten soll, warum sie geeignet ist, ob das PDF frei
  verfügbar ist (Open Access) oder Nils es über die Uni beschaffen muss.
- Du legst **keine** Belege aus Abstracts, Suchtreffer-Snippets oder Webseiten an. Belege entstehen nur aus
  dem vollständigen PDF in Zotero.
- **Stopp:** Nils prüft die Vorschläge, beschafft die PDFs und verschiebt die gewünschten in die
  BA-Sammlung (Ablauf siehe „Quellenbeschaffung durch Nils“). Gib ihm dazu eine kurze Liste:
  Titel · DOI/ISBN · Open Access ja/nein · welche Frage sie beantwortet.

**3. Aufnehmen & Exzerpieren** – für jede freigegebene Quelle Phase 0 und Phase 1 (unten).
Belege suchst du entlang der Fragen aus dem Plan. Steht in der Quelle etwas anderes als erwartet, gilt die
Quelle – passe den Plan an, nicht den Beleg.

**4. Schreiben** – Phase 2 und 3 (unten). Gliedere nach dem, was die Belege hergeben. Fragen ohne Beleg
werden zu `\qf{}`, nicht zu Text. **Stopp:** Nils liest den Entwurf.

**5. Verifizieren** – Phase 4 (unten) für das Kapitel.

Am Ende jedes Schritts kurzer Bericht an Nils: was erledigt ist, was offen ist, welche Entscheidung ansteht.

### Quellenbeschaffung durch Nils

So bekommt Nils die PDFs – damit du ihm passende Hinweise gibst und danach prüfen kannst, ob alles stimmt.
Nils arbeitet an mehreren PCs **nur im Browser auf zotero.org** (keine Zotero-App, keine Erweiterungen).
Gib deshalb nur Hinweise für die Web-Bibliothek. PDFs müssen als **Datei im Zotero-Speicher** am Eintrag
hängen (nicht als Link), sonst kann `zot.py text` sie nicht laden.
Im Uni-Netz der FAU sind lizenzierte Verlagsinhalte direkt zugänglich; sonst beim Verlag
„Institutional Login“ → FAU → IdM-Kennung.

**Vorschläge aus `_Vorschläge` (von dir angelegt, Metadaten sind dann schon da):**
1. Nils öffnet die DOI-/Verlagsseite aus deiner Liste und lädt das PDF herunter (Open Access oder über die FAU).
2. Auf zotero.org öffnet er den Eintrag und lädt das PDF als Datei-Anhang hoch.
3. Nils verschiebt den Eintrag in die Sammlung „Bachelorarbeit“ = **Freigabe**. Erst dann machst du mit
   Phase 0 weiter. Den Eintrag nicht ein zweites Mal anlegen – das erzeugt Duplikate.

**Quellen, die Nils selbst findet:**
- Am einfachsten: Nils schickt dir DOI, ISBN oder Link. Du prüfst die Metadaten (Crossref/Verlag/Katalog),
  legst den Eintrag per API an – nach seiner Ansage direkt in „Bachelorarbeit“, sonst in `_Vorschläge` –
  und er hängt nur noch das PDF an.
- Oder selbst auf zotero.org: neuen Eintrag per DOI/ISBN (*„Add by Identifier“*) in der Sammlung
  „Bachelorarbeit“ anlegen und das PDF als Datei anhängen.
- Normen legt Nils auf zotero.org von Hand an (Eintragstyp „Norm“) und hängt das PDF an.
- Was die FAU nicht hat: Fernleihe über die UB.

**Was du nach der Freigabe prüfst, bevor du exzerpierst:**
- Hat der Eintrag einen PDF-Anhang? Wenn nicht, `zot.py text` meldet „kein PDF-Anhang“ → Nils Bescheid geben,
  nicht mit Abstract oder Webseite weiterarbeiten.
- Ist es das richtige PDF (Titel/Autoren auf der ersten Seite von `sources-text/<key>.txt` = Zotero-Eintrag)?
  Verlage liefern manchmal Inhaltsverzeichnisse, Supplements oder Vorschauen.
- Metadaten plausibel (Autoren, Jahr, Eintragstyp, bei Kapiteln Herausgeber/Buchtitel)? Fehler meldest du
  Nils, statt sie selbst zu ändern – sie landen 1:1 in der `zotero.bib`.
- Duplikate (gleiche DOI/ISBN zweimal in Zotero)? → Nils fragen, welcher Eintrag bleibt.
- Gescanntes PDF ohne Text → Nils Bescheid geben (OCR, z. B. `ocrmypdf`).

### Phase 0 – Quelle aufnehmen
1. Nils legt die Quelle mit PDF in Zotero an.
2. Du setzt per Zotero-Zugriff im Feld *Extra* `Citation Key: <key>` (vorhandenen Inhalt von *Extra*
   behalten). Schema wie die bestehenden Keys: `NachnameJahr`, großer Anfangsbuchstabe, ASCII
   (ä→ae, ö→oe, ü→ue, ß→ss), bei Kollision Suffix `a`, `b` (`Mueller2021`, `Mueller2021a`). Erstautor,
   bei Normen das Kürzel (`DIN743Teil1`), bei Institutionen ein Kurzname (`Acatech2020`).
   Einen schon zitierten Key nie ändern. Der Key hängt nur an der Zeile in *Extra*, nicht an Autor/Jahr:
   Korrigiert Nils später Metadaten, bleibt der Key gleich. `zotero-map.json` ordnet jeden Key dem
   unveränderlichen Zotero-Item-Key zu; `check.py` meldet umbenannte, verschwundene und doppelte Keys.
3. `python3 scripts/zot.py bib` → aktualisiert `zotero-map.json` und meldet Keys, die in `zotero.bib`
   noch fehlen. Dann Nils bitten: in Overleaf `zotero.bib` → *Aktualisieren* und auf GitHub pushen
   (sonst kompiliert der Text mit dem neuen Key nicht).
4. `python3 scripts/zot.py text <key>` → erzeugt `sources-text/<key>.txt`.
   Meldet das Skript „kaum Text“, ist das PDF gescannt → Nils Bescheid geben (OCR nötig).

### Phase 1 – Exzerpieren
- **Hat Nils das PDF im Zotero-Reader auf zotero.org markiert:** `python3 scripts/zot.py annotations <key>` übernimmt die
  Markierungen als Belege (`quelle: annotation`). Du ergänzt nur `kernaussage`.
- **Sonst:** Du liest `sources-text/<key>.txt` und legst Belege an (`quelle: exzerpt`).
  Nur Stellen, die für die Arbeit relevant sind. Ein Beleg = 1–3 Sätze, wörtlich, inkl. Originalschreibweise.
  Die `kernaussage` fasst **nur** zusammen, was im Zitat steht.
- Danach `python3 scripts/check.py` – jedes Zitat muss auf der angegebenen Seite gefunden werden.

### Phase 2 – Schreiben
1. Erst passende Belege suchen (`grep -ri "begriff" evidence/`), dann formulieren.
2. Jede Aussage bekommt Zitat + `\ev{}`. Fehlt ein Beleg: `\qf{}`. Nicht ausweichen auf Eigenwissen.
3. Liste am Ende auf, welche `\qf{}`/`\pruefen{}` du gesetzt hast und welche Literatur fehlen könnte
   (als Suchhinweis für Nils, **nicht** als konkrete Quellenangabe).

### Phase 3 – Mechanisch prüfen
`python3 scripts/check.py` prüft:
- jeder `\cite`-Key ist freigegeben (`zotero-map.json`), jedes Zitat hat direkt dahinter ein `\ev{}`,
- jede Beleg-ID existiert und gehört zu einer der zitierten Quellen,
- Seitenangabe im Zitat passt zur Seite des Belegs,
- jedes Belegzitat steht wörtlich (bzw. fast wörtlich) auf der angegebenen Seite im PDF-Text; eine
  veränderte Zahl oder Verneinung ist immer ein Fehler,
- offene `\qf{}`/`\pruefen{}`.

### Phase 4 – Inhaltlich verifizieren (separater Agent)
Die Skripte prüfen, *dass* ein Beleg existiert, nicht *ob* der Satz ihn korrekt wiedergibt.
1. `python3 scripts/check.py --pairs review/pairs.jsonl [--file Kapitel/xyz.tex]`
2. Einen **neuen Subagenten** starten, der den Text nicht geschrieben hat, mit dem Verifier-Prompt unten.
   Er bekommt nur `review/pairs.jsonl` und darf nichts ändern.
3. Ergebnis nach `review/verifikation-<kapitel>-<datum>.md`. Korrekturen nur nach Rücksprache mit Nils.

## Konventionen

### Belegdatei `evidence/<citekey>.yaml`
```yaml
citekey: Mueller2021
zotero_key: X7K2P9QA           # aus zotero-map.json, ändert sich nie
belege:
  - id: Mueller2021.01         # <citekey>.<laufende Nummer>, nie neu vergeben
    seite: "34"                # gedruckte Seitenzahl (Label), als String
    zitat: "Wörtlicher Text aus der Quelle."
    kernaussage: "Was das Zitat aussagt – nicht mehr."
    quelle: exzerpt            # exzerpt | annotation
    kommentar: "optional"
```
IDs werden nie umnummeriert oder wiederverwendet. Ein falscher Beleg wird korrigiert oder mit
`verworfen: true` markiert, nicht gelöscht, solange er im Text vorkommt.

### LaTeX
- Präambel: `\input{ba-makros}` (in `main.tex` schon eingebunden). biblatex `iso-numeric` (DIN ISO 690).
- Zitieren: `\cite{key}\ev{key.03}` – vor dem Satzpunkt, für einen ganzen Absatz nach dem Punkt
  (Richtlinien-BA §7.2). Die Seite steht im Beleg; im Text ist sie laut Richtlinien nicht nötig.
  Optional sichtbar: `\cite[S.~34]{key}\ev{key.03}` – dann prüft `check.py`, dass sie zum Beleg passt.
- Mehrere Quellen in getrennten Klammern (Richtlinien K4): `\cite{a}\ev{a.01} \cite{b}\ev{b.04}`.
- Reine Verweise ohne Sachaussage (Abbildungsquelle, „vgl. weiterführend“): `\ev{*}` – wird gelistet.
- `\qf{...}` = Quelle fehlt, `\pruefen{...}` = Nils muss etwas klären/liefern. Beide müssen vor
  Abgabe auf 0 sein.

## Verifier-Prompt (für den Subagenten, wörtlich übernehmen)

> Du prüfst Sätze einer Bachelorarbeit gegen ihre Belege. Du hast keinen Anteil am Text.
> Lies `review/pairs.jsonl`. Jede Zeile enthält einen Satz und die zugeordneten Belegzitate.
> Bewerte **nur anhand der Zitate**, nicht anhand deines Wissens, ob der Satz gedeckt ist:
> - **gedeckt** – jede Aussage des Satzes steht so in den Zitaten,
> - **teilweise** – Kern stimmt, aber etwas ist verallgemeinert, verschärft, eine Einschränkung fehlt,
>   eine Zahl/Einheit weicht ab oder ein Teil des Satzes ist nicht belegt,
> - **nicht gedeckt** – das Zitat stützt die Aussage nicht oder widerspricht ihr.
> Ob die Aussage „stimmt“, ist irrelevant – nur ob sie belegt ist.
> Ausgabe als Markdown-Tabelle: Datei:Zeile | Bewertung | Begründung (1 Satz) | Vorschlag.
> Liste „gedeckt“ nur als Anzahl, Details nur für „teilweise“ und „nicht gedeckt“. Ändere keine Dateien.

## Befehle

```bash
pip install -r requirements.txt              # einmal pro Cloud-Sitzung, falls Pakete fehlen (pdftotext ist da)
python3 scripts/zot.py bib                   # zotero-map.json aus Zotero, Abgleich mit zotero.bib
python3 scripts/zot.py text [key ...]        # PDF-Text mit Seitenmarkern (--force zum Neuerzeugen)
python3 scripts/zot.py annotations <key>     # Zotero-Markierungen -> evidence/<key>.yaml
python3 scripts/check.py                     # alles prüfen
python3 scripts/check.py --pairs review/pairs.jsonl --file Kapitel/02_Grundlagen.tex
```
