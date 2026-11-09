"""Einheitlicher Plotstil für matplotlib – Gegenstück zu ba-grafik.tex.

Bevorzugter Weg für Diagramme ist pgfplots (Daten als CSV nach Daten/, Diagramm
in LaTeX), weil Schrift und Größe dann exakt zum Text passen. Dieses Modul ist
für Plots, die sich in pgfplots schlecht bauen lassen (z. B. sehr viele
Datenpunkte, Heatmaps, 3D, Plots direkt aus dem G1-Repo).

    from ba_plotstil import stil, FARBEN, speichern
    stil()
    fig, ax = plt.subplots(figsize=groesse())
    ax.plot(t, q, label="Reihe 1")
    ax.set_xlabel("Zeit in s"); ax.set_ylabel("Gelenkwinkel in rad")
    speichern(fig, "Bilder/plot-name.pdf")

Einbinden in LaTeX ohne Skalierung: \\includegraphics{plot-name.pdf}
(Breite stimmt schon, sonst passt die Schriftgröße nicht mehr zum Text).
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

# Gleiche Werte wie ba-grafik.tex – nur gemeinsam ändern.
FARBEN = {
    "gruen": "#97C139",      # FAPSGruen (151,193,57), Reihe 1
    "blau": "#04316A",       # FAU-Blau, Reihe 2
    "grau": "#595959",       # Reihe 3, Achsen/Text
    "hellblau": "#72A3CD",   # Reihe 4
    "akzent": "#D66000",     # nur Hervorhebung (gesucht, Grenzwert)
    "hellgrau": "#D9D9D9",   # Gitter, Hilfslinien
}
REIHEN = [FARBEN["gruen"], FARBEN["blau"], FARBEN["grau"], FARBEN["hellblau"]]
MARKER = ["o", "s", "^", "D"]

TEXTBREITE_CM = 16.0     # Textbreite der Vorlage (21 cm - 3 cm - 2 cm)
SCHRIFT_PT = 10.95       # \small bei 12 pt Grundschrift = Schrift in ba-grafik.tex


def groesse(breite: float = 1.0, verhaeltnis: float = 0.5) -> tuple[float, float]:
    """Figurgröße in Zoll: breite als Anteil der Textbreite, Höhe = Breite * verhaeltnis."""
    b = TEXTBREITE_CM * breite / 2.54
    return (b, b * verhaeltnis)


def stil() -> None:
    """Setzt die rcParams auf den Stil der Arbeit."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        # Arial/Helvetica wie im Fließtext; Ersatzschriften, falls nicht installiert
        "font.sans-serif": ["Arial", "Helvetica", "TeX Gyre Heros", "Nimbus Sans",
                            "Liberation Sans", "DejaVu Sans"],
        "font.size": SCHRIFT_PT,
        "axes.labelsize": SCHRIFT_PT,
        "axes.titlesize": SCHRIFT_PT,
        "xtick.labelsize": SCHRIFT_PT,
        "ytick.labelsize": SCHRIFT_PT,
        "legend.fontsize": SCHRIFT_PT,
        "mathtext.fontset": "custom",
        "mathtext.rm": "sans", "mathtext.it": "sans:italic", "mathtext.bf": "sans:bold",
        "axes.prop_cycle": cycler(color=REIHEN) + cycler(marker=MARKER),
        "lines.linewidth": 1.0,
        "lines.markersize": 4,
        "axes.edgecolor": FARBEN["grau"],
        "axes.linewidth": 0.6,
        "axes.labelcolor": "black",
        "axes.grid": True,
        "grid.color": FARBEN["hellgrau"],
        "grid.linewidth": 0.4,
        "axes.axisbelow": True,
        "xtick.direction": "in", "ytick.direction": "in",
        "xtick.color": FARBEN["grau"], "ytick.color": FARBEN["grau"],
        "xtick.labelcolor": "black", "ytick.labelcolor": "black",
        "legend.frameon": True,
        "legend.edgecolor": FARBEN["hellgrau"],
        "legend.fancybox": False,
        "axes.formatter.use_locale": False,
        "pdf.fonttype": 42,        # Schrift eingebettet, Text bleibt Text
        # feste Außenmaße (= Breite in LaTeX), Ränder innen automatisch
        "figure.constrained_layout.use": True,
    })


def dezimalkomma(ax) -> None:
    """Dezimalkomma statt -punkt an beiden Achsen (wie pgfplots 'use comma')."""
    from matplotlib.ticker import FuncFormatter

    def fmt(x, _pos):
        s = f"{x:g}"
        return s.replace(".", ",").replace("-", "−")

    ax.xaxis.set_major_formatter(FuncFormatter(fmt))
    ax.yaxis.set_major_formatter(FuncFormatter(fmt))


def speichern(fig, pfad: str) -> None:
    """Speichert als Vektor-PDF (für \\includegraphics ohne Skalierung)."""
    for ax in fig.axes:
        dezimalkomma(ax)
    fig.savefig(pfad)
    plt.close(fig)


if __name__ == "__main__":
    # Musterplot mit Platzhalterdaten (gleich wie das pgfplots-Muster)
    import sys
    import numpy as np

    stil()
    t = np.linspace(0, 4, 9)
    fig, ax = plt.subplots(figsize=groesse())
    ax.plot(t, 0.5 * t, label="Reihe 1")
    ax.plot(t, 1.2 * (1 - np.exp(-t)), label="Reihe 2")
    ax.plot(t, 0.8 + 0.3 * np.sin(2 * t), label="Reihe 3")
    ax.axhline(1.5, color=FARBEN["akzent"], lw=0.8, ls=(0, (4, 2)))
    ax.text(0.08, 1.53, "Grenzwert", color=FARBEN["akzent"], va="bottom")
    ax.set_xlim(0, 4)
    ax.set_xlabel("Zeit in s")
    ax.set_ylabel("Gelenkwinkel in rad")
    ax.legend(loc="lower right")
    speichern(fig, sys.argv[1] if len(sys.argv) > 1 else "muster-python.pdf")
