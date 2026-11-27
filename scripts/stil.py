#!/usr/bin/env python3
"""Stil-Linter für die mechanisch prüfbaren Schreibregeln (W2, Nils 27.11.2026).

  python3 scripts/stil.py                         alle Kapitel, jede Fundstelle einzeln
  python3 scripts/stil.py --file Kapitel/03_Simulation_Infrastruktur.tex
  python3 scripts/stil.py --summe                 nur Anzahl je Datei und Regel

Regeln (Richtlinien-BA.md §4.3, §12, CLAUDE.md):
  semikolon        ; im Fließtext
  gedankenstrich   ---, —, gespaltener Halbgeviertstrich ( -- / – ) als Einschub; Bis-Strich 3--5 bleibt
  ich-wir          ich, wir, uns, unser…, mein…
  begriff          Begriffsliste scripts/stil-begriffe.txt (z. B. Demo, Gamepad)
  gleitobjekt      figure/table ohne [htbp]
  textbezug        Abbildung/Tabelle ohne \\ref davor im Text
  et-al            „Name et al.“ im Satz (nur Hinweis: an einzelnen Stellen erlaubt, §12)
Geprüft wird Fließtext inkl. Captions und Tabellenzellen. Ausgenommen: Kommentare, Formeln, TikZ,
\\texttt/\\url/\\href/\\lstinline/verbatim, Labels, Verweise, Zitate. Alles sind Hinweise an das Modell,
das Umformulieren bleibt Textarbeit. Exit-Code ist immer 0.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIR = ROOT / "Kapitel"
BEGRIFFE = Path(__file__).resolve().parent / "stil-begriffe.txt"

ENV_SKIP = r"(?:tikzpicture|equation\*?|align\*?|gather\*?|multline\*?|displaymath|math|verbatim|lstlisting|minted|axis)"
CMD_ARG_SKIP = r"(?:qf|pruefen|texttt|url|href|lstinline|label|ref|autoref|cref|Cref|eqref|pageref|nameref|input|include|" \
               r"includegraphics|cite|parencite|textcite|ev|begin|end|usetikzlibrary|tikzset|pgfplotsset|" \
               r"addbibresource|newcommand|renewcommand|setlength|hypersetup|SI|si|num|qty|unit|ang|" \
               r"definecolor|colorlet|path|draw|node|tabkopf|hline|cline|multicolumn|column\w*|" \
               r"captionsetup|setcounter|addtocounter|vspace|hspace|rule)"


def blank(text, start, end):
    """Bereich durch Leerzeichen ersetzen, Zeilenumbrüche erhalten (Zeilennummern bleiben gültig)."""
    seg = text[start:end]
    return text[:start] + re.sub(r"[^\n]", " ", seg) + text[end:]


def blank_all(text, pattern, flags=0, group=0):
    for m in reversed(list(re.finditer(pattern, text, flags))):
        text = blank(text, m.start(group), m.end(group))
    return text


def balanced_end(text, i):
    """i zeigt auf '{' -> Index nach der passenden '}'."""
    depth = 0
    for j in range(i, len(text)):
        c = text[j]
        if c == "\\":
            continue
        if c == "{" and (j == 0 or text[j - 1] != "\\"):
            depth += 1
        elif c == "}" and text[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return j + 1
    return len(text)


def prose(text):
    text = blank_all(text, r"(?<!\\)%.*")                                   # Kommentare
    text = blank_all(text, r"\\begin\{" + ENV_SKIP + r"\}.*?\\end\{" + ENV_SKIP + r"\}", re.S)
    text = blank_all(text, r"\\\[.*?\\\]", re.S)
    text = blank_all(text, r"(?<!\\)\$\$.*?(?<!\\)\$\$", re.S)
    text = blank_all(text, r"(?<!\\)\$.*?(?<!\\)\$", re.S)
    text = blank_all(text, r"\\verb(.).*?\1")
    # Befehle mit Argumenten, deren Inhalt kein Fließtext ist (inkl. optionaler Argumente)
    for m in reversed(list(re.finditer(r"\\" + CMD_ARG_SKIP + r"\*?(?![a-zA-Z])", text))):
        j = m.end()
        while True:
            k = j
            while k < len(text) and text[k] in " \t":
                k += 1
            if k < len(text) and text[k] == "[":
                e = text.find("]", k)
                j = e + 1 if e > 0 else k + 1
            elif k < len(text) and text[k] == "{":
                j = balanced_end(text, k)
            else:
                break
        text = blank(text, m.start(), j)
    return text


def load_begriffe():
    rules = []
    if BEGRIFFE.exists():
        for line in BEGRIFFE.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = [p.strip() for p in line.split(" | ")]
            rules.append((re.compile(parts[0], re.I), parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else ""))
    return rules


def lineno(text, pos):
    return text.count("\n", 0, pos) + 1


def snippet(raw, pos, n=50):
    a = max(0, pos - n)
    s = raw[a:pos + n].replace("\n", " ")
    return re.sub(r"\s+", " ", s).strip()


def check_file(f, begriffe):
    raw = f.read_text(encoding="utf-8")
    p = prose(raw)
    out = []   # (zeile, regel, meldung, pos)

    def add(pos, regel, msg):
        out.append((lineno(raw, pos), regel, msg, pos))

    for m in re.finditer(r";", p):
        add(m.start(), "semikolon", "Semikolon")
    for m in re.finditer(r"---|—|(?<=\s)(?:--|–)(?=\s)", p):
        before, after = p[max(0, m.start() - 3):m.start()], p[m.end():m.end() + 3]
        if (re.search(r"\d\s*$", before) and re.match(r"\s*\d", after)) or \
                (re.search(r"&\s*$", before) and re.match(r"\s*(&|\\\\)", after)):
            continue                                    # 3 -- 5: Bereich
        add(m.start(), "gedankenstrich", "Gedankenstrich als Einschub")
    for m in re.finditer(r"(?<![\w\\])(ich|wir|uns|unser\w*|mein\w*|mir|mich)(?![\w\-])", p, re.I):
        add(m.start(), "ich-wir", f"„{m.group(0)}“")
    for rx, ersatz, quelle in begriffe:
        for m in rx.finditer(p):
            add(m.start(), "begriff", f"„{m.group(0)}“ -> {ersatz} ({quelle})")
    for m in re.finditer(r"[A-ZÄÖÜ][\w\-]+(?:\s+(?:und|and|&)\s+[A-ZÄÖÜ][\w\-]+)?\s+et\s+al\.", p):
        add(m.start(), "et-al", f"„{m.group(0)}“ im Satz, wenn möglich als eigene Aussage mit \\cite dahinter")

    # Gleitobjekte und Textbezug arbeiten auf dem Rohtext ohne Kommentare
    nc = blank_all(raw, r"(?<!\\)%.*")
    refs = [(m.start(), m.group(1)) for m in re.finditer(r"\\(?:ref|autoref|cref|Cref|nameref)\{([^}]+)\}", nc)]
    for m in re.finditer(r"\\begin\{(figure|table|xltabular|longtable)\*?\}(\[[^\]]*\])?", nc):
        env, opt = m.group(1), m.group(2)
        if env in ("figure", "table"):
            o = (opt or "")[1:-1]
            if sorted(o.replace("!", "")) != sorted("htbp"):
                add(m.start(), "gleitobjekt", f"\\begin{{{env}}}{opt or ''} statt [htbp]")
        end = nc.find(f"\\end{{{env}", m.end())
        body = nc[m.start():end if end > 0 else len(nc)]
        for lab in re.findall(r"\\label\{([^}]+)\}", body):
            if not re.match(r"(fig|tab|abb)", lab):
                continue
            before = [r for r in refs if lab in [x.strip() for x in r[1].split(",")] and r[0] < m.start()]
            after = [r for r in refs if lab in [x.strip() for x in r[1].split(",")] and r[0] > m.start()]
            if not before and not after:
                add(m.start(), "textbezug", f"{lab}: kein \\ref im Kapitel")
            elif not before:
                add(m.start(), "textbezug", f"{lab}: erster \\ref erst nach dem Objekt (Zeile {lineno(raw, after[0][0])})")
    out.sort()
    return raw, out


def files_from(only):
    if only:
        return [Path(x).resolve() for x in only]
    # Eigenständigkeitserklärung: vorgegebener Wortlaut der Uni, nicht prüfen
    return sorted(f for f in CHAPTER_DIR.glob("*.tex") if not f.name.startswith("00_"))


def run(only=None):
    """Für check.py: -> Liste (datei, regel, anzahl, beispielzeile)."""
    begriffe = load_begriffe()
    res = []
    for f in files_from(only):
        _raw, out = check_file(f, begriffe)
        c = Counter(r for _, r, _, _ in out)
        for regel, n in c.items():
            first = next(z for z, r, _, _ in out if r == regel)
            res.append((f, regel, n, first))
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", action="append")
    ap.add_argument("--summe", action="store_true")
    ap.add_argument("--regel", action="append", help="nur diese Regel(n)")
    a = ap.parse_args()
    begriffe = load_begriffe()
    total = Counter()
    for f in files_from(a.file):
        raw, out = check_file(f, begriffe)
        if a.regel:
            out = [o for o in out if o[1] in a.regel]
        rel = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
        c = Counter(r for _, r, _, _ in out)
        total.update(c)
        if a.summe:
            if c:
                print(f"{rel}: " + ", ".join(f"{r} {n}" for r, n in sorted(c.items())))
            continue
        for z, regel, msg, pos in out:
            print(f"{rel}:{z}: {regel}: {msg} | …{snippet(raw, pos)}…")
    print(f"\nSumme: " + (", ".join(f"{r} {n}" for r, n in sorted(total.items())) or "keine Funde"))


if __name__ == "__main__":
    main()
