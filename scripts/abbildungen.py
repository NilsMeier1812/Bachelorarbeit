#!/usr/bin/env python3
"""Abbildungen aus dem Arbeits-PDF (12 pt) als Bilder zum Ansehen ausgeben (W5, Nils 27.11.2026).

  python3 scripts/abbildungen.py --kapitel 7          alle Abbildungen von Kap. 7
  python3 scripts/abbildungen.py --label fig:bridge   nur diese Abbildung(en)
  python3 scripts/abbildungen.py --kapitel 7 --seite  ganze Seiten statt Ausschnitt

Braucht einen aktuellen Build (python3 scripts/build.py). Schreibt PNGs nach ../ba-build/abbildungen/ und
listet je Abbildung Seite, Datei der Grafik und Overfull-Meldungen aus dem Log. Der Ausschnitt reicht von
der letzten Fließtextzeile über der Abbildung bis unter die Bildunterschrift und schneidet nie in die Grafik
(im Zweifel lieber zu groß). Ob etwas überlappt oder schief sitzt, beurteilt weiter das Modell am Bild.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT.parent / "ba-build"
PDF = BUILD / "main.pdf"
OUT = BUILD / "abbildungen"
DPI = 110


def seiten_index():
    from pypdf import PdfReader
    labels = PdfReader(str(PDF)).page_labels
    start = next(i for i in range(1, len(labels)) if labels[i] == "1" and re.match(r"^[ivxlcdm]+$", labels[i - 1], re.I))
    return {labels[i]: i for i in range(start, len(labels))}


def figuren():
    aux = (BUILD / "main.aux").read_text(encoding="utf-8", errors="replace")
    out = []
    for m in re.finditer(r"\\newlabel\{(fig:[^}]+)\}\{\{([^}]*)\}\{([^}]*)\}", aux):
        out.append((m.group(1), m.group(2), m.group(3)))
    return out


def grafikdatei(label):
    """Datei der Grafik: \\input{Bilder/...} oder \\includegraphics in derselben figure-Umgebung."""
    for f in sorted((ROOT / "Kapitel").glob("*.tex")):
        t = f.read_text(encoding="utf-8")
        i = t.find("\\label{" + label + "}")
        if i < 0:
            continue
        a = t.rfind("\\begin{figure", 0, i)
        e = t.find("\\end{figure", i)
        body = t[a:e if e > 0 else i]
        m = re.findall(r"\\(?:input|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}", body)
        return f"Kapitel/{f.name}", m
    return None, []


def zeilen(idx):
    xml = subprocess.run(["pdftotext", "-f", str(idx + 1), "-l", str(idx + 1), "-bbox-layout", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    page = re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml)
    W, H = float(page.group(1)), float(page.group(2))
    lines = []
    for m in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', xml, re.S):
        words = re.findall(r">([^<]*)</word>", m.group(5))
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        lines.append((x0, y0, x1, y1, " ".join(words)))
    return W, H, lines


def ausschnitt(idx, nummer):
    """-> (y_oben, y_unten) in pt oder None, wenn die Bildunterschrift nicht gefunden wird."""
    W, H, lines = zeilen(idx)
    cap = [l for l in lines if re.match(r"Abbildung\s+" + re.escape(nummer) + r"[:.]", l[4])]
    if not cap:
        return None, W, H
    c = cap[0]
    unten = c[3]
    for l in sorted(lines, key=lambda l: l[1]):            # Folgezeilen der Bildunterschrift
        if l[1] > unten and l[1] - unten < 6 and abs((l[3] - l[1]) - (c[3] - c[1])) < 0.5:
            unten = l[3]
    breite = max((l[2] - l[0]) for l in lines) if lines else W
    body = [l for l in lines if l[3] < c[1] and (l[3] - l[1]) >= 10.3 and (l[2] - l[0]) > 0.6 * breite
            and l[1] > 60]
    oben = max((l[3] for l in body), default=60.0)
    if c[1] - oben < 40:          # kaum Platz über der Bildunterschrift: Ausschnitt unsicher -> ganze Seite
        return "unsicher", W, H
    return (oben + 2, min(H, unten + 6)), W, H


def overfull_fuer(dateien):
    log = (BUILD / "main.log").read_text(encoding="latin-1")
    out = []
    for d in dateien:
        name = d if d.endswith(".tex") else d + ".tex"
        m = re.search(r"\(\./" + re.escape(name) + r"(.*?)\)", log, re.S)
        if m:
            for o in re.findall(r"Overfull \\[hv]box \(([\d.]+)pt too \w+\)", m.group(1)):
                out.append(f"{name}: Overfull {o} pt")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kapitel")
    ap.add_argument("--label", action="append")
    ap.add_argument("--seite", action="store_true", help="ganze Seite statt Ausschnitt")
    a = ap.parse_args()
    if not PDF.exists():
        sys.exit("Kein Build vorhanden: python3 scripts/build.py")
    idx = seiten_index()
    figs = figuren()
    if a.label:
        figs = [f for f in figs if f[0] in a.label]
    elif a.kapitel:
        figs = [f for f in figs if f[1].split(".")[0] == a.kapitel]
    if not figs:
        sys.exit("Keine passende Abbildung im Build gefunden")
    OUT.mkdir(parents=True, exist_ok=True)
    for label, nummer, seite in figs:
        i = idx.get(seite)
        if i is None:
            print(f"{label}: Seite {seite} nicht gefunden")
            continue
        name = OUT / f"abb-{nummer}-{label.split(':', 1)[1]}"
        box, W, H = (None, 0, 0) if a.seite else ausschnitt(i, nummer)
        cmd = ["pdftoppm", "-f", str(i + 1), "-l", str(i + 1), "-r", str(DPI), "-png", "-singlefile"]
        hinweis = ""
        if box == "unsicher":
            box, hinweis = None, " (Ausschnitt unsicher, z. B. Platzhalter, ganze Seite)"
        if box:
            s = DPI / 72
            cmd += ["-x", "0", "-y", str(int(box[0] * s)), "-W", str(int(W * s)), "-H", str(int((box[1] - box[0]) * s))]
        elif not a.seite and not hinweis:
            hinweis = " (Bildunterschrift nicht gefunden, ganze Seite)"
        subprocess.run(cmd + [str(PDF), str(name)], check=True)
        tex, grafik = grafikdatei(label)
        of = overfull_fuer([g for g in grafik if g.startswith("Bilder/") and not g.endswith((".pdf", ".png", ".jpg"))])
        print(f"Abb. {nummer} ({label}), S. {seite} = PDF-Seite {i + 1}{hinweis}")
        print(f"  Bild: {name}.png")
        print(f"  Quelle: {tex}" + (f", Grafik: {', '.join(grafik)}" if grafik else ""))
        for o in of:
            print(f"  {o}")


if __name__ == "__main__":
    main()
