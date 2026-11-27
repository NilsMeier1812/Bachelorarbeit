#!/usr/bin/env python3
"""Arbeit bauen, Kapitel-PDF ausschneiden, Seiten je Kapitel gegen das Budget zählen (W4, Nils 27.11.2026).

  python3 scripts/build.py                       bauen + Seitentabelle + Fehler/Overfull-Liste
  python3 scripts/build.py --kapitel 7           zusätzlich Kapitel-PDF ausschneiden
  python3 scripts/build.py --kapitel 7 --ablage kap7
                                                 Gesamt- und Kapitel-PDF mit Datum nach
                                                 /mnt/project-files/kap7/ legen (für Nils)
  python3 scripts/build.py --ohne-bauen          nur auswerten (letzter Build)

Build-Ordner: ../ba-build (außerhalb des Repos, Overleaf bleibt sauber). latexmk wie in latex-build.md.
Seiten: Kapitelanfang laut .toc, letzte Seite nach Füllstand (Pixel bis zur untersten Zeile/Grafik),
gezählt wie im Seitenbudget (Einleitung bis vor das Literaturverzeichnis). Die Zahlen sind Messwerte
des Arbeits-PDFs (12 pt), keine Bewertung: Was gekürzt wird, entscheidet weiter das Modell mit Nils.
"""
import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT.parent / "ba-build"
PDF = BUILD / "main.pdf"
ABLAGE = Path("/mnt/project-files")
ROMAN = re.compile(r"^[ivxlcdm]+$", re.I)


def bauen():
    BUILD.mkdir(exist_ok=True)
    r = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode",
                        f"-outdir={BUILD}", "main.tex"], cwd=ROOT, capture_output=True, text=True, errors="replace")
    if not PDF.exists():
        print(r.stdout[-3000:])
        sys.exit("Build fehlgeschlagen, kein PDF")
    return r.returncode


def log_auswerten():
    """-> (fehler, overfull, undefiniert) aus main.log, mit Datei:Zeile soweit erkennbar."""
    log = (BUILD / "main.log").read_text(encoding="latin-1")
    fehler, overfull, undef = [], [], set()
    # Zuordnung zur Datei: Abschnitt des Logs nach den Markern „chapter N.“, darin eine noch offene
    # TikZ-Datei (Bilder/...), sonst die Kapiteldatei. Hinter „chapter without number“ = Literaturverzeichnis.
    kapdatei = {}
    for f in sorted((ROOT / "Kapitel").glob("*.tex")):
        m = re.match(r"0?(\d+)_", f.name) or re.match(r"Anhang_([A-Z])", f.name)
        if m:
            kapdatei[m.group(1)] = f"Kapitel/{f.name}"
    marker = [(m.start(), m.group(1)) for m in
              re.finditer(r"^chapter (?:([0-9A-Z]+)\.|without number)$", log, re.M)]
    opens = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"\(\./(Bilder/[^\s()]+\.tex)", log)]

    def datei_bei(pos, zeile=0):
        kap = None
        for p, nr in marker:
            if p > pos:
                break
            kap = nr if nr else "bib"
        if kap is None:
            return "main.tex (Vorspann)"
        if kap == "bib":
            return "Literaturverzeichnis (Eintrag in Zotero)"
        for p, e, name in reversed(opens):
            if p < pos:
                if ")" not in log[e:pos]:
                    return name
                break
        return kapdatei.get(kap, f"Kapitel {kap}")
    for m in re.finditer(r"^! (.+?)\n(?:.*\n){0,6}?l\.(\d+)", log, re.M):
        fehler.append(f"{datei_bei(m.start(), int(m.group(2)))}:{m.group(2)}: {m.group(1)}")
    for m in re.finditer(r"^Overfull \\[hv]box \(([\d.]+)pt too \w+\) (?:in paragraph |detected )?at lines? (\d+)", log, re.M):
        if float(m.group(1)) >= 1.0:
            overfull.append(f"{datei_bei(m.start(), int(m.group(2)))}:{m.group(2)}: Overfull {m.group(1)} pt")
    for m in re.finditer(r"(?:Reference|Citation) [`']([^']+)' (?:on page \d+ )?undefined", log):
        undef.add(m.group(1))
    return fehler, overfull, sorted(undef)


def seiten_index():
    """Seitenlabel (arabisch, ab Kap. 1) -> PDF-Index (0-basiert)."""
    from pypdf import PdfReader
    labels = PdfReader(str(PDF)).page_labels
    start = next(i for i in range(1, len(labels)) if labels[i] == "1" and ROMAN.match(labels[i - 1]))
    return {labels[i]: i for i in range(start, len(labels))}, len(labels)


def kapitel_starts():
    toc = (BUILD / "main.toc").read_text(encoding="utf-8", errors="replace")
    out = []
    for m in re.finditer(r"\\contentsline \{chapter\}\{(?:\\numberline \{([^}]*)\})?(?:\\nonumberline )?(.*?)\}\{([^}]*)\}\{", toc):
        out.append((m.group(1) or "", m.group(2), m.group(3)))
    return out


def fuellstand(idx):
    """Anteil der genutzten Satzspiegelhöhe auf Seite idx (0..1), aus dem Rasterbild."""
    r = subprocess.run(["pdftoppm", "-f", str(idx + 1), "-l", str(idx + 1), "-r", "36", "-gray", str(PDF)],
                       capture_output=True)
    d = r.stdout
    parts = d.split(b"\n", 3)
    w, h = map(int, parts[1].split())
    px = parts[3]
    top, bottom = 70 / 841.89 * h, 760 / 841.89 * h       # unter dem Kopf, bis zur letzten Textzeile
    rows = [i for i in range(int(top), h) if min(px[i * w:(i + 1) * w]) < 200]
    if not rows:
        return 0.0
    return max(0.0, min(1.0, (max(rows) - top) / (bottom - top)))


def budget():
    p = ROOT / "review" / "seitenbudget.md"
    ziel = {}
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*(\d+)\s[^|]*\|[^|]*\|\s*([\d,]+)\s*\|\s*([^|]*)\|", line)
            if m:
                ziel[m.group(1)] = (float(m.group(2).replace(",", ".")), m.group(3).strip())
    return ziel


def seitentabelle():
    idx, n = seiten_index()
    starts = kapitel_starts()
    ziel = budget()
    zeilen, gesamt = [], 0.0
    kap_bereich = {}
    for i, (nr, titel, label) in enumerate(starts):
        if not nr or not nr.isdigit():
            continue
        a = idx.get(label)
        nxt = starts[i + 1][2] if i + 1 < len(starts) else None
        b = idx.get(nxt, n) if nxt else n                  # erster Index des Folgekapitels
        last = b - 1
        while last > a and fuellstand(last) == 0.0:        # Leerseiten vor dem nächsten Kapitel
            last -= 1
        seiten = (last - a) + fuellstand(last)
        kap_bereich[nr] = (a, last)
        gesamt += seiten
        z = ziel.get(nr)
        zeilen.append((nr, titel, seiten, z))
    return zeilen, gesamt, kap_bereich


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kapitel", help="Kapitelnummer für das Einzel-PDF")
    ap.add_argument("--ablage", help="Unterordner in /mnt/project-files für die PDFs (z. B. kap7)")
    ap.add_argument("--ohne-bauen", action="store_true")
    a = ap.parse_args()
    if not a.ohne_bauen:
        print("Baue main.tex ...", flush=True)
        bauen()
    fehler, overfull, undef = log_auswerten()
    zeilen, gesamt, bereich = seitentabelle()
    print(f"\nPDF: {PDF}")
    print("\n| Kap. | Titel | Ist (S.) | Ziel Endfassung | Entwurf laut Budget |")
    print("|---|---|---|---|---|")
    for nr, titel, s, z in zeilen:
        print(f"| {nr} | {titel[:45]} | {s:.1f} | {z[0]:g} | {z[1]} |" if z else f"| {nr} | {titel[:45]} | {s:.1f} | – | – |")
    print(f"| | Summe Einleitung bis vor Literaturverzeichnis | {gesamt:.1f} | 69 | Obergrenze 80 |")
    print(f"\nLaTeX-Fehler: {len(fehler)}")
    for f in fehler:
        print("  " + f)
    bib = [f for f in overfull if f.startswith("Literaturverzeichnis")]
    rest = [f for f in overfull if not f.startswith("Literaturverzeichnis")]
    print(f"Overfull-Boxen ab 1 pt: {len(rest)} im Text" + (f", {len(bib)} im Literaturverzeichnis (lange URLs/DOIs)" if bib else ""))
    for f in rest:
        print("  " + f)
    if undef:
        print(f"Undefinierte Verweise/Zitate: {len(undef)}: " + ", ".join(undef[:20]))
    if a.kapitel:
        from pypdf import PdfReader, PdfWriter
        if a.kapitel not in bereich:
            sys.exit(f"Kapitel {a.kapitel} nicht im PDF gefunden")
        s, e = bereich[a.kapitel]
        w = PdfWriter()
        rd = PdfReader(str(PDF))
        for i in range(s, e + 1):
            w.add_page(rd.pages[i])
        out = BUILD / f"kap{a.kapitel}.pdf"
        with open(out, "wb") as fh:
            w.write(fh)
        print(f"\nKapitel-PDF: {out} (PDF-Seiten {s + 1}–{e + 1})")
        if a.ablage:
            ziel = ABLAGE / a.ablage
            ziel.mkdir(parents=True, exist_ok=True)
            heute = dt.date.today().isoformat()
            shutil.copy(out, ziel / f"kap{a.kapitel}-entwurf-{heute}.pdf")
            shutil.copy(PDF, ziel / f"arbeit-gesamt-{heute}.pdf")
            print(f"Abgelegt: {ziel}/kap{a.kapitel}-entwurf-{heute}.pdf, {ziel}/arbeit-gesamt-{heute}.pdf "
                  f"(an post_message als attached_outputs hängen)")
    elif a.ablage:
        ziel = ABLAGE / a.ablage
        ziel.mkdir(parents=True, exist_ok=True)
        heute = dt.date.today().isoformat()
        shutil.copy(PDF, ziel / f"arbeit-gesamt-{heute}.pdf")
        print(f"Abgelegt: {ziel}/arbeit-gesamt-{heute}.pdf")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
