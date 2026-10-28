# Bachelorarbeit

LaTeX-Quellen der Bachelorarbeit. Wird mit Overleaf über die GitHub-Synchronisierung bearbeitet.

## Aufbau

| Pfad | Inhalt |
| --- | --- |
| `main.tex` | Hauptdokument (Präambel, Reihenfolge der Kapitel) |
| `chapters/` | Ein `.tex`-File pro Kapitel |
| `figures/` | Abbildungen (werden über `\includegraphics{name}` gefunden) |
| `literatur.bib` | Literaturdatenbank (biblatex + biber) |

## Kompilieren

Overleaf: Compiler `pdfLaTeX`, Hauptdokument `main.tex`.

Lokal:

```sh
latexmk -pdf main.tex
```

## Arbeiten mit Overleaf und Git

Vor dem Bearbeiten in Overleaf über *Menu → GitHub → Pull GitHub changes* den aktuellen Stand holen,
danach mit *Push Overleaf changes* zurückschreiben.
