#!/usr/bin/env python3
"""Code-Fundstellen (`% DB:`-Kommentare) gegen den G1-Branch BA-Stable prüfen (W1, Nils 27.11.2026).

  python3 scripts/codebezug.py                     alle Kapitel gegen den Stand aus CLAUDE.md
  python3 scripts/codebezug.py --file Kapitel/07_Umsetzung.tex
  python3 scripts/codebezug.py --ziel <hash>       gegen einen neuen BA-Stable-Stand prüfen
  python3 scripts/codebezug.py --ziel <hash> --fix  reine Verschiebungen umschreiben (Zeilen + @hash)

Erkennt in `% DB:`-Zeilen Angaben wie `g1pilot/start.sh:243-253`, `datei.py:1,14-24` und Kurzformen
`, :120-125` (gleiche Datei wie davor). Der Stand einer Zeile ist das letzte `@hash` in ihr, ohne Hash gilt
der Zielstand. Geprüft wird:
  - Datei vorhanden (G1 am genannten Stand, sonst eigene Datei im Arbeits-Repo, z. B. Daten/...)
  - Zeilenbereich innerhalb der Datei
  - bei älterem Stand: Datei seither geändert? Bereich verschoben oder inhaltlich berührt?
Ergebnis: FEHLER (Datei/Zeile fehlt), PRÜFEN (Bereich inhaltlich geändert, Modell muss lesen),
VERSCHOBEN (neue Zeilen werden vorgeschlagen, mit --fix eingetragen), sonst ok.
--fix ändert nur Zeilen, in denen jede Angabe ok oder rein verschoben ist; alles andere bleibt.
Ob die Zeile inhaltlich trägt, was der Text sagt, prüft weiterhin das Modell.
"""
import argparse
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
G1 = ROOT.parent / "G1"
CHAPTER_DIR = ROOT / "Kapitel"

EXT = r"py|xml|ya?ml|sh|json|md|txt|cfg|toml|launch|urdf|cpp|hpp|h|c|js|ts|html|css|ini|csv|tex|onnx|mjcf"
PATH_RE = r"/?(?:[\w.\-*]+/)*(?:[\w.\-]*Dockerfile[\w.\-]*|[\w\-]+(?:\.[\w\-]+)*\.(?:" + EXT + r"))(?![\w/])"
RANGES_RE = r"\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*"
TOKEN_RE = re.compile(r"(?P<path>" + PATH_RE + r")(?::(?P<r1>" + RANGES_RE + r"))?"
                      r"|(?<![\w/.]):(?P<r2>" + RANGES_RE + r")")
HASH_RE = re.compile(r"@([0-9a-f]{7,40})\b")


def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(G1), *args], capture_output=True, text=True)
    if check and r.returncode:
        return None
    return r.stdout


def stand_aus_claude_md():
    m = re.search(r"\*\*Stand `([0-9a-f]{7,40})`", (ROOT / "CLAUDE.md").read_text(encoding="utf-8"))
    return m.group(1) if m else None


@lru_cache(None)
def full(h):
    out = git("rev-parse", "--verify", "--quiet", h + "^{commit}")
    return out.strip() if out else None


@lru_cache(None)
def tree(h):
    return (git("ls-tree", "-r", "--name-only", h) or "").split("\n")


@lru_cache(None)
def resolve(h, p):
    """-> (art, pfad, kandidaten) mit art in g1 | eigen | fehlt | mehrdeutig."""
    if "*" in p:
        return "muster", p, []
    if p.startswith("/"):
        return ("absolut" if Path(p).is_file() else "fehlt_abs"), p, []
    files = tree(h)
    if p in files:
        return "g1", p, []
    cand = [f for f in files if f.endswith("/" + p)]
    if len(cand) == 1:
        return "g1", cand[0], []
    if (ROOT / p).is_file():
        return "eigen", p, []
    if len(cand) > 1:
        return "mehrdeutig", p, cand
    eigen = [q for q in eigene_dateien() if q.endswith("/" + p)]
    if len(eigen) == 1:
        return "eigen", eigen[0], []
    return ("fehlt" if "/" in p else "unbekannt"), p, []


@lru_cache(None)
def eigene_dateien():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True).stdout
    return tuple(out.split("\n"))


@lru_cache(None)
def nlines(art, h, p):
    if art == "absolut":
        return len(Path(p).read_text(encoding="utf-8", errors="replace").splitlines())
    if art == "eigen":
        return len((ROOT / p).read_text(encoding="utf-8", errors="replace").splitlines())
    out = git("show", f"{h}:{p}")
    return None if out is None else len(out.splitlines())


@lru_cache(None)
def hunks(old, new, p):
    out = git("diff", "-U0", "--no-color", old, new, "--", p) or ""
    hs = []
    for m in re.finditer(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", out, re.M):
        a, b = int(m.group(1)), int(m.group(2) or 1)
        c, d = int(m.group(3)), int(m.group(4) or 1)
        hs.append((a, b, c, d))
    return hs


def map_range(lo, hi, hs):
    """Alten Bereich lo-hi in neuen abbilden -> (neu_lo, neu_hi, berührt)."""
    touched = False
    for a, b, _c, _d in hs:
        if b > 0 and not (a + b - 1 < lo or a > hi):
            touched = True
        if b == 0 and lo <= a < hi:          # Einfügung mitten im Bereich
            touched = True

    def shift(L):
        s = 0
        for a, b, _c, d in hs:
            if (b > 0 and a + b - 1 < L) or (b == 0 and a < L):
                s += d - b
        return L + s
    return shift(lo), shift(hi), touched


def parse_ranges(s):
    out = []
    for part in s.split(","):
        lo, _, hi = part.partition("-")
        out.append((int(lo), int(hi or lo)))
    return out


def fmt_ranges(rs):
    return ",".join(str(lo) if lo == hi else f"{lo}-{hi}" for lo, hi in rs)


def check_line(text, ziel, ziel_kurz):
    """Prüft eine DB-Zeile. -> (befunde, neue_zeile_oder_None)."""
    hm = HASH_RE.findall(text)
    stand = hm[-1] if hm else None
    h = full(stand) if stand else ziel
    befunde = []
    if len(set(hm)) > 1:
        befunde.append(("HINWEIS", f"mehrere Stände in einer Zeile ({', '.join(sorted(set(hm)))}), "
                        f"alle gegen @{stand} geprüft, Zeile aufteilen"))
    if stand and not h:
        return [("FEHLER", f"Stand @{stand} gibt es im G1-Repo nicht")], None
    alles_fixbar, geaendert = True, False
    last = None   # (art, pfad)

    def repl(m):
        nonlocal last, alles_fixbar, geaendert
        if m.group("path"):
            art, p, cand = resolve(h, m.group("path"))
            if art == "fehlt":
                befunde.append(("FEHLER", f"{m.group('path')}: Datei gibt es am Stand {h[:7]} nicht"))
                alles_fixbar, last = False, None
                return m.group(0)
            if art in ("muster", "unbekannt", "fehlt_abs"):
                text_ = {"muster": "Muster mit *, nicht geprüft",
                         "unbekannt": "weder in G1 noch im Arbeits-Repo gefunden, nicht geprüft",
                         "fehlt_abs": "absoluter Pfad, hier nicht vorhanden, nicht geprüft"}[art]
                befunde.append(("HINWEIS", f"{m.group('path')}: {text_}"))
                last = None
                return m.group(0)
            if art == "mehrdeutig":
                befunde.append(("HINWEIS", f"{m.group('path')}: mehrdeutig ({len(cand)} Dateien), "
                                f"nicht geprüft, Pfad genauer angeben"))
                last = None
                return m.group(0)
            last = (art, p)
            rs = m.group("r1")
            prefix = m.group("path") + ":"
        else:
            rs = m.group("r2")
            prefix = ":"
            if last is None:
                return m.group(0)
        if not rs:
            # nur Datei, keine Zeilen: am Ziel vorhanden?
            art, p = last
            if art == "g1" and h != ziel and resolve(ziel, p)[0] != "g1":
                befunde.append(("FEHLER", f"{p}: am Zielstand {ziel_kurz} nicht mehr vorhanden"))
                alles_fixbar = False
            return m.group(0)
        art, p = last
        n = nlines(art, h, p)
        ranges = parse_ranges(rs)
        for lo, hi in ranges:
            if n is not None and (hi > n or lo < 1 or lo > hi):
                befunde.append(("FEHLER", f"{p}:{lo}-{hi}: Datei hat am Stand {h[:7]} nur {n} Zeilen"))
                alles_fixbar = False
        if art in ("eigen", "absolut") or h == ziel:
            return m.group(0)
        if resolve(ziel, p)[0] != "g1":
            befunde.append(("FEHLER", f"{p}: am Zielstand {ziel_kurz} nicht mehr vorhanden"))
            alles_fixbar = False
            return m.group(0)
        hs = hunks(h, ziel, p)
        if not hs:
            return m.group(0)
        neu = []
        for lo, hi in ranges:
            nlo, nhi, touched = map_range(lo, hi, hs)
            if touched:
                befunde.append(("PRÜFEN", f"{p}:{lo}-{hi}: Bereich zwischen {h[:7]} und {ziel_kurz} "
                                f"geändert (jetzt etwa {nlo}-{nhi}), Inhalt lesen"))
                alles_fixbar = False
            elif (nlo, nhi) != (lo, hi):
                befunde.append(("VERSCHOBEN", f"{p}:{fmt_ranges([(lo, hi)])} -> {fmt_ranges([(nlo, nhi)])}"))
                geaendert = True
            neu.append((nlo, nhi))
        return prefix + fmt_ranges(neu)

    new_text = TOKEN_RE.sub(repl, text)
    if stand is None:
        befunde.append(("HINWEIS", f"ohne @hash, gegen Zielstand {ziel_kurz} geprüft"))
    fix = None
    if h != ziel and alles_fixbar:
        new_text = HASH_RE.sub("@" + ziel_kurz, new_text) if stand else new_text
        fix = new_text if (geaendert or stand) else None
    return befunde, fix


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", action="append", help="nur diese .tex-Datei(en)")
    ap.add_argument("--ziel", help="Ziel-Stand (Standard: Stand aus CLAUDE.md)")
    ap.add_argument("--fix", action="store_true", help="reine Verschiebungen in die .tex schreiben")
    ap.add_argument("--alle", action="store_true", help="auch ok-Zeilen und Verschiebungen einzeln zeigen")
    a = ap.parse_args()
    if not (G1 / ".git").exists():
        sys.exit(f"G1-Repo fehlt unter {G1} (bash scripts/setup.sh)")
    ziel_in = a.ziel or stand_aus_claude_md()
    if not ziel_in:
        sys.exit("Kein Zielstand: --ziel angeben oder Stand in CLAUDE.md eintragen")
    ziel = full(ziel_in)
    if not ziel:
        git("fetch", "-q", "origin", "BA-Stable", check=False)
        ziel = full(ziel_in)
    if not ziel:
        sys.exit(f"Stand {ziel_in} im G1-Repo nicht gefunden (git -C ../G1 fetch origin BA-Stable)")
    zk = ziel_in[:7]
    files = [ROOT / f for f in a.file] if a.file else sorted(CHAPTER_DIR.glob("*.tex"))
    zaehl = {"FEHLER": 0, "PRÜFEN": 0, "VERSCHOBEN": 0, "HINWEIS": 0}
    n_zeilen = n_fix = 0
    for f in files:
        lines = f.read_text(encoding="utf-8").split("\n")
        changed = False
        for i, line in enumerate(lines):
            if "% DB:" not in line:
                continue
            n_zeilen += 1
            befunde, fix = check_line(line, ziel, zk)
            for art, msg in befunde:
                zaehl[art] += 1
                if art in ("FEHLER", "PRÜFEN") or a.alle or (art == "HINWEIS" and "ohne @hash" not in msg):
                    print(f"{f.relative_to(ROOT)}:{i + 1}: {art}: {msg}")
                elif art == "VERSCHOBEN" and not a.fix:
                    print(f"{f.relative_to(ROOT)}:{i + 1}: {art}: {msg}")
            if a.fix and fix is not None and fix != line:
                lines[i] = fix
                changed = True
                n_fix += 1
        if changed:
            f.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nZielstand {zk}: {n_zeilen} DB-Zeilen, {zaehl['FEHLER']} Fehler, {zaehl['PRÜFEN']} zu prüfen, "
          f"{zaehl['VERSCHOBEN']} verschoben, {zaehl['HINWEIS']} Hinweise"
          + (f", {n_fix} Zeilen umgeschrieben" if a.fix else ""))
    sys.exit(1 if zaehl["FEHLER"] else 0)


if __name__ == "__main__":
    main()
