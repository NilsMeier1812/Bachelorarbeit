#!/usr/bin/env python3
"""Mechanische Prüfung des Belegsystems.

  python scripts/check.py                       alles prüfen (Exit-Code 1 bei Fehlern)
  python scripts/check.py --no-text             Zitat-gegen-PDF-Prüfung überspringen
  python scripts/check.py --pairs review/pairs.jsonl [--file Kapitel/x.tex]
                                                Satz/Beleg-Paare für den Verifier-Agenten exportieren
"""
import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from balib import (CHAPTER_DIR, MAIN_TEX, MAP_PATH, ROOT, evidence_files,  # noqa: E402
                   bib_key_counts, load_bib_keys, load_evidence_file, load_map_keys, load_pages,
                   norm)

try:
    from rapidfuzz import fuzz as _rf
except ImportError:
    _rf = None

FUZZY_OK = 97          # ab hier: "fast wörtlich" (nur Warnung, z. B. Silbentrennung/OCR)
FUZZY_ABWEICHUNG = 85  # 85–97 %: Stelle gefunden, aber Wortlaut verändert (Fehler)
MIN_QUOTE_LEN = 25  # kürzere Zitate sind zu unspezifisch (Warnung)

CITE_RE = re.compile(
    r"\\(?P<cmd>[Cc]ite|[Pp]arencite|[Tt]extcite|[Aa]utocite|[Ff]ootcite|[Ss]martcite|"
    r"[Ff]ootcitetext|citep|citet|citealp|citealt)\*?"
    r"(?P<opts>(?:\s*\[[^\]]*\]){0,2})\s*\{(?P<keys>[^}]+)\}")
EV_AFTER_RE = re.compile(r"\s*\\ev\{([^}]*)\}")
EV_RE = re.compile(r"\\ev\{([^}]*)\}")
MARK_RE = re.compile(r"\\(qf|pruefen)\{([^}]*)\}")


class Report:
    def __init__(self):
        self.errors, self.warnings, self.infos = [], [], []

    def err(self, where, msg): self.errors.append(f"{where}: {msg}")
    def warn(self, where, msg): self.warnings.append(f"{where}: {msg}")
    def info(self, where, msg): self.infos.append(f"{where}: {msg}")

    def print(self):
        for title, items in (("FEHLER", self.errors), ("WARNUNGEN", self.warnings), ("HINWEISE", self.infos)):
            if items:
                print(f"\n== {title} ({len(items)}) ==")
                for i in items:
                    print("  " + i)
        print(f"\nErgebnis: {len(self.errors)} Fehler, {len(self.warnings)} Warnungen, "
              f"{len(self.infos)} Hinweise")


# ---------------------------------------------------------------- Fuzzy-Suche
def partial_ratio(q, text):
    if _rf:
        return _rf.partial_ratio(q, text)
    n = len(q)
    if n == 0 or not text:
        return 0
    if len(text) <= n:
        return SequenceMatcher(None, q, text).ratio() * 100
    best, step = 0.0, max(1, n // 10)
    for i in range(0, len(text) - n + 1, step):
        sm = SequenceMatcher(None, q, text[i:i + n])
        if sm.quick_ratio() * 100 <= best:
            continue
        best = max(best, sm.ratio() * 100)
    return best


_NEG = {"not", "no", "never", "nicht", "kein", "keine", "keinen", "keinem", "keiner", "nie", "niemals"}


def changed_words(q, text):
    """Wörter des (normalisierten) Zitats, die im Seitentext gar nicht vorkommen."""
    return [w for w in re.findall(r"\w+(?:[.,]\d+)*", q) if w not in text]


def find_quote(zitat, seite, pages):
    """-> (status, detail). status: ok | fuzzy | wrong_page | missing"""
    q = norm(zitat)
    npages = [(lab, norm(txt)) for _, lab, txt in pages]
    idx = [i for i, (lab, _) in enumerate(npages) if lab == str(seite)]

    def window(i):  # Seite + Folgeseite, damit Zitate über einen Seitenumbruch gehen dürfen
        nxt = npages[i + 1][1] if i + 1 < len(npages) else ""
        return npages[i][1] + " " + nxt

    def only_on_next(i):
        return i + 1 < len(npages) and q in npages[i + 1][1]

    for i in idx:
        if q in window(i) and not only_on_next(i):
            return "ok", ""
    for lab, t in npages:
        if q in t:
            return "wrong_page", f"steht wörtlich auf S. {lab}"
    best_here = max((partial_ratio(q, window(i)) for i in idx), default=0)
    if best_here >= FUZZY_OK:
        here = " ".join(window(i) for i in idx)
        diff = changed_words(q, here)
        # Eine geänderte Zahl oder Verneinung ist nie ein Umbruch-/OCR-Artefakt.
        bad = [w for w in diff if re.search(r"\d", w) or w in _NEG]
        if bad:
            return "missing", (f"fast wörtlich ({best_here:.0f} %), aber {', '.join(bad)} steht so nicht "
                               "auf der Seite – Zahl/Verneinung verändert? Exakt aus sources-text kopieren")
        extra = f" (abweichend: {', '.join(diff[:5])})" if diff else ""
        return "fuzzy", (f"nur fast wörtlich gefunden ({best_here:.0f} %){extra} – vermutlich Umbruch/OCR, "
                         "im PDF prüfen")
    if best_here >= FUZZY_ABWEICHUNG:
        return "missing", (f"weicht vom Original ab ({best_here:.0f} %) – Wortlaut verändert? "
                           "Exakt aus sources-text kopieren")
    best_lab, best = None, 0
    for lab, t in npages:
        r = partial_ratio(q, t)
        if r > best:
            best_lab, best = lab, r
    if best >= FUZZY_ABWEICHUNG:
        return "wrong_page", f"ähnlich auf S. {best_lab} ({best:.0f} %) – Seite und Wortlaut prüfen"
    if not idx:
        return "missing", f"Seite '{seite}' existiert nicht im Text; beste Übereinstimmung {best:.0f} %"
    return "missing", f"nicht gefunden (beste Übereinstimmung {best:.0f} % auf S. {best_lab})"


# ---------------------------------------------------------------- Evidence
def check_evidence(rep, bib, check_text, renamed):
    zmap = json.loads(MAP_PATH.read_text(encoding="utf-8")) if MAP_PATH.exists() else {}
    by_item = {v["zotero_key"]: k for k, v in zmap.items()}
    index = {}
    for path in evidence_files():
        where = f"evidence/{path.name}"
        try:
            data = load_evidence_file(path)
        except Exception as e:  # noqa: BLE001
            rep.err(where, f"YAML nicht lesbar: {e}")
            continue
        ck = data.get("citekey") or path.stem
        if ck != path.stem:
            rep.err(where, f"citekey '{ck}' passt nicht zum Dateinamen")
        if ck not in bib:
            new = by_item.get(data.get("zotero_key"))
            if new:
                renamed[ck] = new
                rep.err(where, f"citekey '{ck}' wurde in Zotero zu '{new}' umbenannt – Datei, IDs und "
                               "\\cite anpassen (oder den alten Key in Zotero wiederherstellen)")
            else:
                rep.err(where, f"citekey '{ck}' nicht in der BA-Sammlung (zotero-map.json)")
        if zmap and ck in zmap and data.get("zotero_key") != zmap[ck]["zotero_key"]:
            rep.err(where, f"zotero_key {data.get('zotero_key')} ≠ {zmap[ck]['zotero_key']} laut zotero-map.json")

        pages = load_pages(ck) if check_text else None
        if check_text and pages is None:
            rep.err(where, f"sources-text/{ck}.txt fehlt – Zitate nicht prüfbar (`zot.py text {ck}`)")

        for b in data["belege"]:
            bid = str(b.get("id", ""))
            w = f"{where} [{bid or '?'}]"
            if not re.fullmatch(re.escape(ck) + r"\.\d{2,}", bid):
                rep.err(w, f"ID muss '{ck}.NN' sein")
            if bid in index:
                rep.err(w, "ID doppelt vergeben")
            for f in ("seite", "zitat", "kernaussage"):
                if not str(b.get(f, "")).strip():
                    (rep.warn if f == "kernaussage" else rep.err)(w, f"Feld '{f}' leer")
            index[bid] = {**b, "citekey": ck}
            if b.get("verworfen"):
                continue
            z = str(b.get("zitat", ""))
            if z and len(norm(z)) < MIN_QUOTE_LEN:
                rep.warn(w, "Zitat sehr kurz – kaum eindeutig prüfbar")
            if pages and z and str(b.get("seite", "")).strip():
                status, detail = find_quote(z, b["seite"], pages)
                if status == "fuzzy":
                    rep.warn(w, detail)
                elif status != "ok":
                    rep.err(w, f"Zitat {detail}")
    return index


# ---------------------------------------------------------------- LaTeX
def strip_comments(text):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in text.split("\n"))


def page_tokens(post):
    toks = set()
    for a, b in re.findall(r"(\d+)\s*(?:[-–]+\s*(\d+))?", post):
        if b:
            toks.update(str(i) for i in range(int(a), int(b) + 1))
        else:
            toks.add(a)
    toks.update(t.lower() for t in re.findall(r"\b[ivxlcdm]+\b", post, re.I))
    return toks


def tex_files(only=None):
    if only:
        return [Path(f).resolve() for f in only]
    return [MAIN_TEX] + sorted(CHAPTER_DIR.rglob("*.tex"))


def lineno(text, pos):
    return text.count("\n", 0, pos) + 1


def sentence_around(text, start, end):
    s = max(text.rfind("\n\n", 0, start), max((m.end() for m in re.finditer(r"[.!?](?=\s)", text[:start])), default=0))
    m = re.search(r"[.!?](\s|$)|\n\s*\n", text[end:])
    e = end + (m.start() + 1 if m else len(text) - end)
    return text[s:e]


def detex(s):
    s = EV_RE.sub("", s)
    s = re.sub(r"\\(?:sub)*section\*?\{[^}]*\}", "", s)
    s = s.replace("\\percent", "%")
    s = CITE_RE.sub(lambda m: f"[{m.group('keys')}{(' ' + m.group('opts').strip()) if m.group('opts').strip() else ''}]", s)
    s = re.sub(r"\\(?:emph|textbf|textit|enquote|SI|si|num|unit|qty)\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    s = re.sub(r"[{}~]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def check_tex(rep, bib, latex_bib, renamed, index, files, pairs_out=None):
    used, marks, stars = set(), [], []
    pairs = []
    for f in files:
        try:
            rel = f.relative_to(ROOT)
        except ValueError:
            rel = f
        text = strip_comments(f.read_text(encoding="utf-8"))
        consumed = set()
        for m in CITE_RE.finditer(text):
            where = f"{rel}:{lineno(text, m.start())}"
            keys = [k.strip() for k in m.group("keys").split(",") if k.strip()]
            for k in keys:
                if k not in bib:
                    if k in renamed:
                        rep.err(where, f"Citekey '{k}' wurde in Zotero zu '{renamed[k]}' umbenannt")
                    elif k in latex_bib:
                        rep.err(where, f"Citekey '{k}' steht in zotero.bib, ist aber nicht freigegeben "
                                       "(nicht in der BA-Sammlung oder ohne 'Citation Key:')")
                    else:
                        rep.err(where, f"Citekey '{k}' existiert nicht in Zotero")
            ev = EV_AFTER_RE.match(text, m.end())
            if not ev:
                rep.err(where, f"\\{m.group('cmd')}{{{','.join(keys)}}} ohne direkt folgendes \\ev{{}}")
                continue
            consumed.add(ev.start(1))
            ids = [i.strip() for i in ev.group(1).split(",") if i.strip()]
            if ids == ["*"]:
                stars.append(f"{where}: {','.join(keys)}")
                continue
            opts = re.findall(r"\[([^\]]*)\]", m.group("opts"))
            post = opts[-1] if opts else ""
            ptoks = page_tokens(post)
            belege = []
            for bid in ids:
                b = index.get(bid)
                if not b:
                    rep.err(where, f"Beleg-ID '{bid}' existiert nicht")
                    continue
                used.add(bid)
                if b.get("verworfen"):
                    rep.err(where, f"Beleg '{bid}' ist als verworfen markiert")
                if b["citekey"] not in keys:
                    rep.err(where, f"Beleg '{bid}' gehört zu '{b['citekey']}', zitiert ist {keys}")
                if len(keys) == 1:
                    s = str(b.get("seite", "")).strip().lower()
                    # Seitenangabe im \cite ist optional (DIN ISO 690 numerisch, Richtlinien-BA §7);
                    # die Seite steht im Beleg. Wird eine angegeben, muss sie passen.
                    if post.strip() and s and s not in ptoks:
                        rep.warn(where, f"Seitenangabe '{post}' ≠ Seite {b.get('seite')} von Beleg '{bid}'")
                belege.append(b)
            if pairs_out is not None and belege:
                pairs.append({
                    "ort": where,
                    "satz": detex(sentence_around(text, m.start(), ev.end())),
                    "belege": [{"id": b["id"], "seite": b.get("seite"), "zitat": b.get("zitat"),
                                "kernaussage": b.get("kernaussage")} for b in belege],
                })
        for ev in EV_RE.finditer(text):
            if ev.start(1) not in consumed:
                rep.err(f"{rel}:{lineno(text, ev.start())}", f"\\ev{{{ev.group(1)}}} ohne Zitat davor")
        for mk in MARK_RE.finditer(text):
            marks.append(f"{rel}:{lineno(text, mk.start())}: \\{mk.group(1)}{{{mk.group(2)}}}")

    for m in marks:
        rep.info("offen", m)
    for s in stars:
        rep.info("\\ev{*}", s)
    unused = sorted(set(index) - used)
    if unused:
        rep.info("evidence", f"{len(unused)} Belege noch nicht im Text verwendet")
    if pairs_out is not None:
        Path(pairs_out).parent.mkdir(parents=True, exist_ok=True)
        with open(pairs_out, "w", encoding="utf-8") as fh:
            for p in pairs:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
        print(f"{len(pairs)} Satz/Beleg-Paare -> {pairs_out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-text", action="store_true", help="Zitate nicht gegen PDF-Text prüfen")
    ap.add_argument("--pairs", metavar="DATEI", help="Satz/Beleg-Paare als JSONL exportieren")
    ap.add_argument("--file", action="append", help="nur diese .tex-Datei(en) prüfen/exportieren")
    args = ap.parse_args()

    rep = Report()
    bib = load_map_keys()          # freigegebene Quellen (BA-Sammlung, mit Citation Key)
    latex_bib = load_bib_keys()    # was LaTeX tatsächlich sieht (von Overleaf gepflegt)
    if not bib:
        rep.err("zotero-map.json", "fehlt oder leer – `python scripts/zot.py bib` ausführen")
    for k in sorted(bib - latex_bib):
        rep.warn("zotero.bib", f"'{k}' fehlt noch – in Overleaf die Zotero-Datei aktualisieren und pushen")
    for k, n in sorted(bib_key_counts().items()):
        if n > 1:
            rep.err("zotero.bib", f"Key '{k}' kommt {n}-mal vor – in Zotero eindeutigen 'Citation Key:' setzen")
    renamed = {}
    index = check_evidence(rep, bib, not args.no_text, renamed)
    check_tex(rep, bib, latex_bib, renamed, index, tex_files(args.file), args.pairs)
    rep.print()
    sys.exit(1 if rep.errors else 0)


if __name__ == "__main__":
    main()
