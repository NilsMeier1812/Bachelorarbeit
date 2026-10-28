# Bachelorarbeit

LaTeX-Quellen der Bachelorarbeit. Wird mit Overleaf über die GitHub-Synchronisierung bearbeitet.

## Aufbau

| Pfad | Inhalt |
| --- | --- |
| `main.tex` | Hauptdokument der FAPS-Vorlage (Präambel, Titelseite, Verzeichnisse, persönliche Daten) |
| `Kapitel/` | Ein `.tex`-File pro Kapitel sowie Eigenständigkeitserklärung und Anhänge |
| `Bilder/` | Abbildungen und Logos (werden über `\includegraphics{name}` gefunden) |
| `zotero.bib` | Literaturdatenbank, aus Zotero online verknüpft (in Overleaf nur per „Aktualisieren“ ändern, nicht von Hand; biblatex + biber, DIN ISO 690) |

Basiert auf der LaTeX-Vorlage des Lehrstuhls FAPS (FAU Erlangen-Nürnberg).

## Kompilieren

Overleaf: Compiler `pdfLaTeX`, Hauptdokument `main.tex`.

Lokal:

```sh
latexmk -pdf main.tex
```

## Arbeiten mit Overleaf und Git

Vor dem Bearbeiten in Overleaf über *Menu → GitHub → Pull GitHub changes* den aktuellen Stand holen,
danach mit *Push Overleaf changes* zurückschreiben.
