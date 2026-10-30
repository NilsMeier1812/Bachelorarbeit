"""Gemeinsame Funktionen für zot.py und check.py."""
import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MAIN_TEX = ROOT / "main.tex"
CHAPTER_DIR = ROOT / "Kapitel"
# zotero.bib verknüpft Overleaf aus Zotero online und pusht sie ins Repo – nie von Hand/per Skript ändern.
BIB_PATH = ROOT / "zotero.bib"
MAP_PATH = ROOT / "zotero-map.json"
TEXT_DIR = ROOT / "sources-text"
PDF_CACHE = ROOT / ".zotero-cache"
EVID_DIR = ROOT / "evidence"

PAGE_MARKER = re.compile(r"^=== PDF-Seite (\d+) \| Seite (.+?) ===$", re.M)

_QUOTES = "\"'„“”‚‘’«»‹›`´"
_DASH_RE = re.compile(r"\s*[-\u2010\u2011\u2012\u2013\u2014\u2212]\s*")


def norm(s: str) -> str:
    """Normalisierung für den Zitatvergleich (symmetrisch auf Zitat und Quelltext anwenden).

    Ligaturen auflösen (NFKC), weiche Trennstriche entfernen, Bindestriche/Trennungen samt
    umgebendem Leerraum entfernen (so matcht 'Dauer-\\nfestigkeit' auf 'Dauerfestigkeit'),
    Anführungszeichen entfernen, casefold, Leerraum zusammenfassen.
    """
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u00ad", "")
    s = _DASH_RE.sub("", s)
    s = s.translate({ord(c): None for c in _QUOTES})
    s = s.casefold()
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def load_pages(citekey: str):
    """Liest sources-text/<key>.txt -> Liste von (pdf_index, label, text). None, wenn nicht vorhanden."""
    p = TEXT_DIR / f"{citekey}.txt"
    if not p.exists():
        return None
    raw = p.read_text(encoding="utf-8")
    marks = list(PAGE_MARKER.finditer(raw))
    pages = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(raw)
        pages.append((int(m.group(1)), m.group(2).strip(), raw[m.end():end]))
    return pages


def load_map_keys():
    """Citekeys der freigegebenen Quellen (BA-Sammlung in Zotero) laut zotero-map.json."""
    import json
    if not MAP_PATH.exists():
        return set()
    return set(json.loads(MAP_PATH.read_text(encoding="utf-8")))


def load_bib_keys():
    if not BIB_PATH.exists():
        return set()
    txt = BIB_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"^@\w+\s*\{\s*([^,\s]+)\s*,", txt, re.M))


def load_evidence_file(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data.setdefault("belege", [])
    return data


def dump_evidence_file(path: Path, data):
    path.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )


def evidence_files():
    if not EVID_DIR.exists():
        return []
    return sorted(p for p in EVID_DIR.glob("*.yaml") if not p.name.startswith("_"))
