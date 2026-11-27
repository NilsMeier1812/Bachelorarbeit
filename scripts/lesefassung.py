#!/usr/bin/env python3
"""Lesefassung eines Kapitels als Markdown für das Claude-Dokument erzeugen, und Nils' Korrekturen
als Änderungsliste zurückholen (W3, Nils 27.11.2026).

  python3 scripts/lesefassung.py Kapitel/07_Umsetzung.tex
        -> ../ba-build/lesefassung/<datei>.md + Bilder; Markdown abschnittsweise ins Claude-Dokument,
           Bilder per Upload (Docs-Guide topic.uploads) an die Stellen ![…](…)
  python3 scripts/lesefassung.py Kapitel/07_Umsetzung.tex --diff export.md
        -> nur die Absätze, die im Dokument (Markdown-Export des Tabs) anders sind als in der .tex,
           mit .tex-Zeile. Bewertet werden sie wie bisher vom Modell (Nils' Änderungen sind Vorschläge).

Braucht einen aktuellen Build (python3 scripts/build.py): Nummern von Abschnitten, Abbildungen, Tabellen
und Gleichungen kommen aus main.aux/main.toc, Abbildungen als Bild aus dem 12pt-PDF.
Darstellung wie in den bisherigen Lesefassungen: Zitate als [Key], \\qf als [QUELLE FEHLT: …],
\\pruefen als **[PRÜFEN: …]**, Inline-Formeln als $…$, nummerierte Gleichungen als latex-Block.
Unbekannte Makros meldet das Skript, statt sie zu verschlucken. Die .tex bleibt immer das Original.
"""
import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT.parent / "ba-build"
OUTDIR = BUILD / "lesefassung"

# Makros, die das Skript selbst behandelt oder die pandoc sauber umsetzt
BEKANNT = set("""
cite ev qf pruefen ref autoref cref Cref nameref pageref eqref label caption centering raggedright arraybackslash
textwidth linewidth tabstil tabkopf tabkopfzeile hline toprule midrule bottomrule cline multicolumn small footnotesize
chapter section subsection subsubsection paragraph emph textbf textit texttt enquote item begin end input
includegraphics fbox parbox formeleintrag phantomsection textsuperscript textsubscript url href footnote
mathrm mathbf mathsf mathit leq geq Delta tau alpha lambda xi pm dot vec sum frac tilde theta min max left right
in dots dagger bigl bigr quad qquad cdot times approx infty ldots newline setlength tabcolsep hfill vspace hspace
noindent par Titel omega mu sigma varphi phi beta gamma delta epsilon rho pi partial sqrt cos sin text neq
""".split())


def strip_comments(t):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", l) for l in t.split("\n"))


def arg_end(t, i):
    """t[i] == '{' -> Index nach der passenden Klammer."""
    d = 0
    j = i
    while j < len(t):
        c = t[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
            if d == 0:
                return j + 1
        j += 1
    return len(t)


def skip_ws(t, i):
    while i < len(t) and t[i] in " \t\n":
        i += 1
    return i


def replace_cmd(t, name, fn, nargs=1, opt=True):
    """Ersetzt \\name[opt]{a1}…{an} durch fn(opt, args). Klammern balanciert."""
    out, pos = [], 0
    rx = re.compile(r"\\" + name + r"\*?(?![a-zA-Z])")
    while True:
        m = rx.search(t, pos)
        if not m:
            out.append(t[pos:])
            return "".join(out)
        j = m.end()
        o = None
        if opt:
            k = skip_ws(t, j)
            if k < len(t) and t[k] == "[":
                e = t.find("]", k)
                o, j = t[k + 1:e], e + 1
        args, ok = [], True
        for _ in range(nargs):
            k = skip_ws(t, j)
            if k >= len(t) or t[k] != "{":
                ok = False
                break
            e = arg_end(t, k)
            args.append(t[k + 1:e - 1])
            j = e
        out.append(t[pos:m.start()])
        out.append(fn(o, args) if ok else m.group(0))
        pos = j if ok else m.end()


def aux_labels():
    aux = (BUILD / "main.aux").read_text(encoding="utf-8", errors="replace")
    return {m.group(1): m.group(2) for m in re.finditer(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux)}


def toc_nummern():
    toc = (BUILD / "main.toc").read_text(encoding="utf-8", errors="replace")
    return [(m.group(1), m.group(2), m.group(3)) for m in re.finditer(
        r"\\contentsline \{(chapter|section|subsection|subsubsection)\}\{\\numberline \{([^}]*)\}(.*?)\}\{[^}]*\}\{", toc)]


def norm_title(s):
    s = re.sub(r"\\[a-zA-Z]+\*?|[{}~\\]", "", s)
    return re.sub(r"\W+", "", s).lower()


def vorbereiten(tex_path, labels, toc, bilder, warn):
    t = strip_comments(Path(tex_path).read_text(encoding="utf-8"))
    eqs, tabs = [], []

    # Überschriften nummerieren (Reihenfolge und Titel wie im .toc, nur Einträge dieses Kapitels)
    kt = re.search(r"\\chapter\{([^}]*)\}", t)
    toc_iter = list(toc)
    if kt:
        st = next((i for i, e in enumerate(toc) if e[0] == "chapter" and norm_title(e[2]) == norm_title(kt.group(1))), None)
        if st is not None:
            en = next((i for i in range(st + 1, len(toc)) if toc[i][0] == "chapter"), len(toc))
            toc_iter = list(toc[st:en])

    def head(level, mdlevel):
        def fn(o, a):
            titel = a[0]
            nr = ""
            for i, (lv, n, tt) in enumerate(toc_iter):
                if lv == level and norm_title(tt) == norm_title(titel):
                    nr = n
                    del toc_iter[i]
                    break
            if not nr:
                warn.append(f"Überschrift ohne Nummer im .toc: {titel}")
            return f"\n\nLFH{mdlevel}LF{(nr + ' ') if nr else ''}{titel}\n\n"
        return fn
    for lv, md in (("chapter", 1), ("section", 2), ("subsection", 3), ("subsubsection", 4)):
        t = re.sub(r"\\" + lv + r"\*", r"\\LFSTAR" + lv, t)          # ungezählte merken
        t = replace_cmd(t, lv, head(lv, md))
        t = replace_cmd(t, "LFSTAR" + lv, lambda o, a, md=md: f"\n\nLFH{md}LF{a[0]}\n\n")
    t = replace_cmd(t, "paragraph", lambda o, a: f"\n\n\\textbf{{{a[0]}}} ")

    # Gleitobjekte
    def figure(m):
        body = m.group(0)
        lab = re.search(r"\\label\{(fig:[^}]+)\}", body)
        lab = lab.group(1) if lab else None
        cap = ""
        replace_cmd(body, "caption", lambda o, a: (caps.append(a[0]), "")[1])
        cap = caps.pop() if caps else ""
        nr = labels.get(lab, "?") if lab else "?"
        if not re.search(r"\\(input|includegraphics)", body):
            ph = re.search(r"\\parbox(?:\[[^\]]*\])*\{[^}]*\}\{(.*?)\}\}", body, re.S)
            txt = re.sub(r"\\[a-zA-Z]+\s*", "", ph.group(1)).strip() if ph else "Bild folgt"
            txt = re.sub(r"^Platzhalter:\s*", "", txt)
            return f"\n\nLFPH{nr}LF{txt}LFEND\n\n\\emph{{Abbildung {nr}: {cap}}}\n\n"
        img = bilder.get(lab)
        if not img:
            warn.append(f"Kein Bild für {lab or 'Abbildung ohne Label'}")
        return f"\n\nLFIMG{nr}LF{img or ''}LFEND\n\n\\emph{{Abbildung {nr}: {cap}}}\n\n"
    caps = []
    t = re.sub(r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}", figure, t, flags=re.S)

    def tabelle(body, umgebung_mit_caption=True):
        lab = re.search(r"\\label\{(tab:[^}]+)\}", body)
        lab = lab.group(1) if lab else None
        nr = labels.get(lab, "?") if lab else "?"
        cap = []
        replace_cmd(body, "caption", lambda o, a: (cap.append(a[0]), "")[1])
        m = re.search(r"\\begin\{(tabularx|xltabular|tabular|longtable)\}", body)
        if not m:
            return body
        env = m.group(1)
        j = m.end()
        nargs = 2 if env in ("tabularx", "xltabular") else 1
        for _ in range(nargs):
            k = skip_ws(body, j)
            if k < len(body) and body[k] == "{":
                j = arg_end(body, k)
        e = body.find(f"\\end{{{env}}}", j)
        inner = body[j:e]
        inner = re.sub(r"\\(toprule|midrule|bottomrule|hline|tabkopfzeile|endhead|endfirsthead|endfoot|endlastfoot)\b", "", inner)
        inner = re.sub(r"\\cline\{[^}]*\}", "", inner)
        inner = re.sub(r"\\caption(\[[^\]]*\])?\{.*?\}\s*\\\\", "", inner, flags=re.S)
        inner = re.sub(r"\\label\{[^}]*\}", "", inner)
        rows = [r.strip() for r in re.split(r"\\\\(?:\[[^\]]*\])?", inner) if r.strip()]
        cells = []
        for r in rows:
            cs = [c.strip() for c in re.split(r"(?<!\\)&", r)]
            out = []
            for c in cs:
                mc = re.match(r"\\multicolumn\{(\d+)\}\{[^}]*\}\{(.*)\}$", c, re.S)
                if mc:
                    out += [mc.group(2)] + [""] * (int(mc.group(1)) - 1)
                else:
                    out.append(c)
            cells.append(out)
        tabs.append(cells)
        capt = f"\\emph{{Tabelle {nr}: {cap[0]}}}\n\n" if cap else ""
        return f"\n\n{capt}LFTAB{len(tabs) - 1}LF\n\n"
    t = re.sub(r"\\begin\{table\*?\}.*?\\end\{table\*?\}", lambda m: tabelle(m.group(0)), t, flags=re.S)
    t = re.sub(r"\\begin\{(xltabular|longtable)\}.*?\\end\{\1\}", lambda m: tabelle(m.group(0)), t, flags=re.S)

    # Gleichungen
    def gleichung(m):
        body = m.group(2)
        lab = re.search(r"\\label\{([^}]+)\}", body)
        nr = labels.get(lab.group(1), "") if lab else ""
        body = re.sub(r"\\label\{[^}]*\}", "", body)
        body = replace_cmd(body, "formeleintrag", lambda o, a: "")
        body = body.replace("\\nonumber", "").strip()
        eqs.append((nr, body))
        return f"\n\nLFEQ{len(eqs) - 1}LF\n\n"
    t = re.sub(r"\\begin\{(equation|align|gather|multline)\*?\}(.*?)\\end\{\1\*?\}", gleichung, t, flags=re.S)
    t = re.sub(r"\\\[(.*?)\\\]", lambda m: gleichung(type("M", (), {"group": lambda s, i: m.group(1)})()), t, flags=re.S)

    t = inline(t, labels)
    return t, eqs, tabs


def inline(t, labels):
    t = replace_cmd(t, "formeleintrag", lambda o, a: "")
    t = replace_cmd(t, "ev", lambda o, a: "", opt=False)
    t = replace_cmd(t, "qf", lambda o, a: f"[QUELLE FEHLT: {a[0]}]", opt=False)
    t = replace_cmd(t, "pruefen", lambda o, a: f"\\textbf{{[PRÜFEN: {a[0]}]}}", opt=False)

    def cite(o, a):
        keys = ", ".join(k.strip() for k in a[0].split(","))
        return f"[{keys}{(', ' + o) if o else ''}]"
    for c in ("cite", "parencite", "textcite"):
        t = replace_cmd(t, c, cite)

    def ref(o, a):
        return ", ".join(labels.get(k.strip(), f"[?{k.strip()}]") for k in a[0].split(","))
    for c in ("ref", "autoref", "cref", "Cref", "nameref", "eqref"):
        t = replace_cmd(t, c, ref, opt=False)
    t = replace_cmd(t, "pageref", lambda o, a: "", opt=False)
    t = replace_cmd(t, "label", lambda o, a: "", opt=False)
    t = replace_cmd(t, "enquote", lambda o, a: f"„{a[0]}“", opt=False)
    t = replace_cmd(t, "tabkopf", lambda o, a: a[0], opt=False)
    hoch = {"2": "²", "3": "³", "1": "¹", "-1": "⁻¹", "-2": "⁻²"}
    t = replace_cmd(t, "textsuperscript", lambda o, a: hoch.get(a[0].strip(), "^" + a[0]), opt=False)
    t = re.sub(r"\\(tabstil|centering|phantomsection|small|footnotesize|tabkopfzeile|noindent)\b", "", t)
    return t


def unbekannte_makros(t):
    t = re.sub(r"\$[^$]*\$", "", t)
    return sorted({m for m in re.findall(r"\\([a-zA-Z]+)", t) if m not in BEKANNT and not m.startswith("LF")})


def pandoc(tex):
    r = subprocess.run(["pandoc", "-f", "latex", "-t", "gfm+tex_math_dollars", "--wrap=none"],
                       input=tex, capture_output=True, text=True)
    if r.returncode:
        sys.exit("pandoc-Fehler: " + r.stderr[-2000:])
    return r.stdout, r.stderr


def zelle(tex, labels):
    tex = inline(tex, labels)
    md, _ = pandoc(tex)
    return re.sub(r"\s+", " ", md).strip().replace("|", "\\|")


def nachbereiten(md, eqs, tabs, labels):
    md = re.sub(r"^LFH(\d)LF(.*)$", lambda m: "#" * int(m.group(1)) + " " + m.group(2).strip(), md, flags=re.M)
    md = re.sub(r"LFIMG([^L]*)LF(.*?)LFEND",
                lambda m: f"![Abbildung {m.group(1)}]({m.group(2)})" if m.group(2) else f"[Bild fehlt: Abbildung {m.group(1)}]", md)
    md = re.sub(r"LFPH([^L]*)LF(.*?)LFEND", lambda m: f"[Platzhalter Abbildung {m.group(1)}: {m.group(2)}]", md)
    md = re.sub(r"LFEQ(\d+)LF", lambda m: "```latex\n" + eqs[int(m.group(1))][1] + "\n```" +
                (f"\n\nGleichung ({eqs[int(m.group(1))][0]})" if eqs[int(m.group(1))][0] else ""), md)

    def tab(m):
        cells = tabs[int(m.group(1))]
        n = max(len(r) for r in cells)
        rows = [[zelle(c, labels) for c in r] + [""] * (n - len(r)) for r in cells]
        out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
        out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        return "\n".join(out)
    md = re.sub(r"LFTAB(\d+)LF", tab, md)
    md = md.replace("\\[", "[").replace("\\]", "]")
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


# ------------------------------------------------------------------ Rückweg
def absaetze(md):
    md = md.replace("&#91;", "[").replace("\\[", "[").replace("\\]", "]")
    out = []
    for block in re.split(r"\n\s*\n", md):
        b = block.strip()
        if not b:
            continue
        out.append(b)
    return out


GRIECH = {"tau": "τ", "Delta": "Δ", "delta": "δ", "alpha": "α", "beta": "β", "gamma": "γ", "lambda": "λ",
          "xi": "ξ", "theta": "θ", "mu": "μ", "omega": "ω", "sigma": "σ", "varphi": "φ", "phi": "φ",
          "epsilon": "ε", "rho": "ρ", "pi": "π", "in": "∈", "pm": "±", "leq": "≤", "geq": "≥", "sum": "∑",
          "partial": "∂", "infty": "∞", "approx": "≈", "cdot": "·", "times": "×"}


def skelett(s):
    """Vergleichsform ohne Formatierung: Formeln aus der .tex ($…$) und gerenderte Formeln aus dem
    Dokument (τv,i) werden gleich, Wortänderungen bleiben sichtbar."""
    import unicodedata

    def mathe(m):
        x = re.sub(r"\\([a-zA-Z]+)", lambda g: GRIECH.get(g.group(1), ""), m.group(1))
        return x
    s = re.sub(r"\$([^$]*)\$", mathe, s)
    s = re.sub(r"```latex.*?```", "", s, flags=re.S)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^\w∈±≤≥∑∂∞≈·×]", "", s)


def norm_abs(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)|\[image:[^\]]*\]", "[BILD]", s)
    s = re.sub(r"[*_`#>]", "", s)
    s = re.sub(r"\s*\|\s*", "|", s)
    s = re.sub(r"-{3,}", "---", s)
    s = s.replace("\\", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def tex_zeile(tex_lines, text):
    """Zeile in der .tex, die am besten zum Absatz passt (über die ersten Wörter)."""
    words = re.findall(r"\w{4,}", text)[:8]
    best, bz = 0, None
    for i, l in enumerate(tex_lines):
        if l.lstrip().startswith("%"):
            continue
        n = sum(1 for w in words if w in l)
        if n > best:
            best, bz = n, i + 1
    return bz if best >= min(3, len(words)) else None


def diff(tex_path, gen_md, doc_md):
    ra, rb = absaetze(gen_md), absaetze(doc_md)
    erste = next((i for i, x in enumerate(rb) if re.match(r"#+\s*\d", x)), 0)
    rb = rb[erste:]
    a = [skelett(x) for x in ra]
    b = [skelett(x) for x in rb]                       # Kopf des Dokuments (Titel, Datum, Hinweis) überspringen
    formeln = 0
    tex_lines = Path(tex_path).read_text(encoding="utf-8").split("\n")
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        alt, neu = [norm_abs(x) for x in ra[i1:i2]], [norm_abs(x) for x in rb[j1:j2]]
        sk_alt, sk_neu = a[i1:i2], b[j1:j2]
        # Paare ähnlicher Absätze zeigen Wortänderungen
        for k in range(max(len(alt), len(neu))):
            x = alt[k] if k < len(alt) else ""
            y = neu[k] if k < len(neu) else ""
            if x == y or (k < len(sk_alt) and k < len(sk_neu) and sk_alt[k] == sk_neu[k]):
                continue
            z = tex_zeile(tex_lines, x or y)
            if x and y:
                wa, wb = x.split(), y.split()
                s2 = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
                hunks = []
                for o2, p1, p2, q1, q2 in s2.get_opcodes():
                    if o2 == "equal":
                        continue
                    if "$" in " ".join(wa[p1:p2]) or (p1 == p2 and "$" in " ".join(wa[max(0, p1 - 1):p1 + 1])):
                        formeln += 1         # Formel: im Dokument gerendert, nicht wortgleich vergleichbar
                        continue
                    hunks.append((" ".join(wa[max(0, p1 - 4):p2 + 4]) or "–", " ".join(wb[max(0, q1 - 4):q2 + 4]) or "–"))
                if not hunks:
                    hunks.append(("(nur in einer Formel)", "Formel im Dokument geändert? Absatz von Hand vergleichen"))
                n += 1
                print(f"--- Änderung {n}" + (f" (etwa {tex_path}:{z})" if z else ""))
                for h1, h2 in hunks:
                    print(f"  .tex: {h1}")
                    print(f"  Doc:  {h2}")
                continue
            n += 1
            print(f"--- Änderung {n}" + (f" (etwa {tex_path}:{z})" if z else ""))
            if x:
                print(f"  nur in .tex (im Dokument gelöscht?): {x[:300]}")
            else:
                print(f"  nur im Dokument (neu?): {y[:300]}")
    print(f"\n{n} abweichende Absätze" + (f", {formeln} Formelstellen nicht verglichen (im Dokument gerendert, "
          f"Formeln bei Bedarf von Hand ansehen)" if formeln else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tex")
    ap.add_argument("--diff", metavar="EXPORT_MD", help="Markdown-Export des Dokument-Tabs vergleichen")
    ap.add_argument("--ohne-bilder", action="store_true")
    a = ap.parse_args()
    if not (BUILD / "main.aux").exists():
        sys.exit("Kein Build: python3 scripts/build.py")
    labels, toc = aux_labels(), toc_nummern()
    tex_path = Path(a.tex)
    bilder = {}
    if not a.ohne_bilder:
        kap = re.match(r"0?(\d+)_", tex_path.name)
        if kap:
            subprocess.run([sys.executable, str(ROOT / "scripts" / "abbildungen.py"), "--kapitel", kap.group(1)],
                           capture_output=True, text=True)
        for p in (BUILD / "abbildungen").glob("abb-*.png"):
            m = re.match(r"abb-[\d.]+-(.+)\.png", p.name)
            if m:
                bilder["fig:" + m.group(1)] = str(p)
    warn = []
    tex, eqs, tabs = vorbereiten(tex_path, labels, toc, bilder, warn)
    unbekannt = unbekannte_makros(tex)
    md, err = pandoc(tex)
    md = nachbereiten(md, eqs, tabs, labels)
    ohne_mathe = re.sub(r"```latex.*?```|\$[^$\n]*\$", "", md, flags=re.S)
    rest = re.findall(r"\\[a-zA-Z]+|LF[A-Z]+\d*", ohne_mathe)
    for lab in sorted(set(re.findall(r"\[\?([^\]]+)\]", md))):
        warn.append(f"Verweis {lab} nicht aufgelöst (Label fehlt im Build)")
    if a.diff:
        diff(tex_path, md, Path(a.diff).read_text(encoding="utf-8"))
        return
    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / (tex_path.stem + ".md")
    out.write_text(md, encoding="utf-8")
    print(f"Lesefassung: {out} ({len(md)} Zeichen, {md.count('![')} Bilder, {len(tabs)} Tabellen, {len(eqs)} Gleichungen)")
    for w in warn:
        print("WARNUNG: " + w)
    if unbekannt:
        print("WARNUNG: unbekannte Makros (Ausgabe an diesen Stellen prüfen): " + ", ".join(unbekannt))
    if rest:
        print("WARNUNG: im Markdown stehen noch LaTeX-Reste: " + ", ".join(sorted(set(rest))[:20]))
    if err.strip():
        print("pandoc meldet: " + err.strip()[:1000])


if __name__ == "__main__":
    main()
