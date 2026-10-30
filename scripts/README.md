# BA-Belegsystem – Kurzanleitung

Für Nils. Die Regeln für Claude stehen in `CLAUDE.md` im Repo-Root.

## Idee in einem Satz

Jede Aussage im Text zeigt per `\ev{id}` auf einen Beleg in `evidence/`, jeder Beleg enthält ein wörtliches
Zitat mit Seitenzahl, und `scripts/check.py` prüft mechanisch, dass das Zitat genau so auf dieser Seite im
PDF steht. Ob der Satz das Zitat *korrekt* wiedergibt, prüft zusätzlich ein separater Verifier-Agent.

```
Zotero online (Metadaten + PDF + Markierungen)
   │                                   │
   │ Overleaf „Aktualisieren“          │ zot.py bib / text / annotations (Web-API)
   ▼                                   ▼
zotero.bib (LaTeX)           zotero-map.json · sources-text/ · evidence/<key>.yaml  ◄── check.py: Zitat ↔ Seite
   │                                   │
   ▼                                   ▼
Kapitel/*.tex   \cite{Key}\ev{Key.03}                    ◄── check.py: Key freigegeben, Beleg-ID, Seite
                                                         ◄── Verifier-Agent: Inhalt
```

## Wie es in diesem Repo eingerichtet ist

- **Zotero online** (zotero.org) ist die einzige Quellenliste. Sammlung **„Bachelorarbeit“** = freigegebene
  Quellen, Sammlung **`_Vorschläge`** = Claudes Recherche-Vorschläge. Keine Desktop-App nötig.
- **`zotero.bib`** kommt weiterhin aus Overleafs Zotero-Verknüpfung. Nach neuen Quellen in Overleaf die Datei
  *Aktualisieren* und auf GitHub pushen. Die Skripte schreiben die `.bib` nie.
- **`zotero-map.json`** listet, was zitiert werden darf (Einträge der Sammlung „Bachelorarbeit“ mit
  `Citation Key:` im Feld *Extra*). Erzeugt von `zot.py bib`.
- **PDFs** müssen in Zotero als *Datei* am Eintrag hängen (Zotero-Speicher, kostenlos 300 MB). `zot.py text`
  lädt sie über die Web-API. Ein reiner Link reicht nicht.
- **`ba-makros.tex`** ist in `main.tex` eingebunden. Für einen Entwurf mit sichtbaren Beleg-IDs dort
  `\belegeanzeigentrue` setzen. `\qf{}` (rot) und `\pruefen{}` (orange) müssen vor Abgabe weg sein.
- Claude arbeitet in der Cloud: `pdftotext` ist dort installiert, der Zotero-Schlüssel wird vom Proxy
  eingesetzt. `sources-text/` und `.zotero-cache/` sind gitignored (Urheberrecht) und landen nie in Overleaf.

### Selbst ausführen (optional, nur wenn du lokal arbeiten willst)

```bash
pip install -r requirements.txt          # dazu pdftotext: apt install poppler-utils / brew install poppler
export ZOTERO_API_KEY=...                # zotero.org/settings/keys, Lesezugriff + Dateien
python3 scripts/zot.py bib
```
Mit Zotero 7 Desktop geht auch die lokale API: `export ZOTERO_API_BASE=http://localhost:23119/api/users/0`
(dann werden PDFs aus `~/Zotero/storage` gelesen).

## Ablauf pro Quelle

1. Du hängst das PDF in Zotero an und verschiebst den Eintrag in „Bachelorarbeit“ (= Freigabe).
2. Claude setzt `Citation Key: NachnameJahr`, ruft `zot.py bib` und `zot.py text <Key>` auf.
3. Du klickst in Overleaf bei `zotero.bib` auf *Aktualisieren* und pushst.
4. Claude exzerpiert (oder übernimmt mit `zot.py annotations <Key>` deine Markierungen aus dem Zotero-Reader)
   und prüft mit `check.py`.

## Was check.py erkennt – und was nicht

| erkennt | erkennt nicht |
|---|---|
| erfundene, falsch geschriebene oder nicht freigegebene Citekeys | ob die Paraphrase den Beleg korrekt wiedergibt → Verifier-Agent |
| `\cite` ohne Beleg-ID, Beleg-ID ohne `\cite` | Sachaussagen ganz ohne `\cite` → Verifier + deine Durchsicht |
| Beleg-ID, die zu einer anderen Quelle gehört | ob eine Quelle selbst seriös/passend ist |
| erfundene oder veränderte Zitate, auch eine einzelne geänderte Zahl oder Verneinung | Fehler in Formeln/Abbildungen aus Quellen |
| falsche Seitenzahlen (Zitat steht woanders) | |
| abweichende Seitenangabe, falls im `\cite[S.~x]` eine steht | |
| offene `\qf{}` / `\pruefen{}` | |

## Stolpersteine

- **Seitenzahlen:** Belege nutzen die *gedruckte* Seitenzahl. Bei Artikeln ohne Seitenlabels im PDF (z. B.
  arXiv) steht im Marker der PDF-Index – dann prüfen, ob das zur Seitenangabe im Artikel passt.
- **Gescannte PDFs:** `zot.py text` meldet „kaum Text“. Mit `ocrmypdf in.pdf out.pdf` eine Textebene ergänzen
  und in Zotero ersetzen.
- **Zweispaltige Paper:** pdftotext liest meist korrekt spaltenweise. Wird ein Zitat nur „fast wörtlich“
  gefunden, liegt es oft an Spalten- oder Tabellenumbrüchen – kurz im PDF nachsehen.
- **Vorlagen-Beispielsätze:** Die Beispieltexte der FAPS-Vorlage in `Kapitel/` haben `\cite` ohne `\ev` und
  erzeugen bis zu ihrer Ersetzung 6 Fehler in `check.py`.
- **Noch nicht mit echten PDFs aus Zotero getestet:** `zot.py bib` läuft gegen deine Bibliothek, `check.py`
  wurde mit einem Test-PDF geprüft. Der PDF-Download (`zot.py text`) läuft erst, sobald ein Eintrag ein PDF hat.
