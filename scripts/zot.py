#!/usr/bin/env python3
"""Zotero-Brücke für die BA.

  python scripts/zot.py bib                  zotero-map.json aus Zotero erzeugen, Abgleich mit zotero.bib
  python scripts/zot.py text [key ...]       PDF-Text mit Seitenmarkern nach sources-text/
  python scripts/zot.py annotations <key>    Zotero-Markierungen als Belege nach evidence/<key>.yaml

Die zotero.bib selbst schreibt dieses Skript nicht: Overleaf verknüpft sie aus Zotero online und
pusht sie ins Repo.

Konfiguration über Umgebungsvariablen (siehe scripts/README.md):
  ZOTERO_API_BASE   Standard: https://api.zotero.org/users/22350426  (Web-API, Bibliothek von Nils)
                    lokal:    http://localhost:23119/api/users/0      (lokale API von Zotero 7)
  ZOTERO_API_KEY    für die Web-API (in Claudes Cloud-Umgebung setzt der Proxy den Schlüssel ein)
  ZOTERO_COLLECTION Standard: 99VAKC9A (Sammlung "Bachelorarbeit" = freigegebene Quellen); "" = alles
  ZOTERO_DATA_DIR   Standard: ~/Zotero  (enthält storage/; fehlt das PDF dort, wird es über die
                    Web-API nach .zotero-cache/ geladen)
  ZOTERO_LINKED_BASE  Basisordner für verknüpfte Dateien ("attachments:..."), falls genutzt
"""
import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from balib import (EVID_DIR, MAP_PATH, PDF_CACHE, TEXT_DIR, dump_evidence_file,  # noqa: E402
                   load_bib_keys, load_evidence_file, norm)

API_BASE = os.environ.get("ZOTERO_API_BASE", "https://api.zotero.org/users/22350426").rstrip("/")
WEB_API = API_BASE.startswith("https://api.zotero.org")
API_KEY = os.environ.get("ZOTERO_API_KEY") or ("dummy" if WEB_API else None)
COLLECTION = os.environ.get("ZOTERO_COLLECTION", "99VAKC9A")
DATA_DIR = Path(os.environ.get("ZOTERO_DATA_DIR", str(Path.home() / "Zotero"))).expanduser()
LINKED_BASE = os.environ.get("ZOTERO_LINKED_BASE")

SKIP_TYPES = {"attachment", "note", "annotation"}
CK_RE = re.compile(r"^\s*Citation Key:\s*(\S+)\s*$", re.I | re.M)


def die(msg):
    print(f"FEHLER: {msg}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------- Zotero-API
def _get(path, stream=False, **params):
    headers = {"Zotero-API-Version": "3"}
    if API_KEY:
        headers["Zotero-API-Key"] = API_KEY
    url = f"{API_BASE}/{path.lstrip('/')}"
    try:
        r = requests.get(url, params=params, headers=headers, timeout=60, stream=stream)
    except requests.ConnectionError:
        die(f"Zotero nicht erreichbar unter {API_BASE}. Läuft Zotero, ist die lokale API aktiviert?")
    if r.status_code != 200:
        die(f"{r.status_code} bei {url}: {r.text[:300]}")
    return r


def get_all(path, **params):
    out, start = [], 0
    while True:
        r = _get(path, format="json", limit=100, start=start, **params)
        batch = r.json()
        out.extend(batch)
        total = int(r.headers.get("Total-Results", len(out)))
        start += len(batch)
        if not batch or start >= total:
            return out


def load_map():
    if not MAP_PATH.exists():
        die("zotero-map.json fehlt – zuerst `python scripts/zot.py bib` ausführen.")
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- bib
_TRANS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue", "ß": "ss"})


def suggest_key(d):
    """Schema der Arbeit: NachnameJahr, ASCII, großer Anfangsbuchstabe (Todorov2012, Bruendl2024)."""
    creators = d.get("creators") or []
    if creators:
        name = creators[0].get("lastName") or creators[0].get("name") or ""
    else:
        name = (d.get("title") or "quelle").split()[0]
    name = unicodedata.normalize("NFKD", name.translate(_TRANS)).encode("ascii", "ignore").decode()
    name = re.sub(r"[^A-Za-z0-9]", "", name) or "Quelle"
    year = re.search(r"\d{4}", d.get("date") or "")
    return name[0].upper() + name[1:] + (year.group(0) if year else "oJ")


def cmd_bib(_args):
    path = f"collections/{COLLECTION}/items/top" if COLLECTION else "items/top"
    items = get_all(path)
    mapping, missing, dups = {}, [], {}
    for it in items:
        d = it["data"]
        if d.get("itemType") in SKIP_TYPES:
            continue
        m = CK_RE.search(d.get("extra") or "")
        if not m:
            missing.append((it["key"], d.get("title", ""), suggest_key(d)))
            continue
        ck = m.group(1)
        if ck in mapping:
            dups.setdefault(ck, [mapping[ck]["zotero_key"]]).append(it["key"])
            continue
        mapping[ck] = {"zotero_key": it["key"], "titel": d.get("title", "")}

    MAP_PATH.write_text(json.dumps(mapping, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    print(f"{len(mapping)} freigegebene Quellen -> zotero-map.json")

    stale = sorted(set(mapping) - load_bib_keys())
    if stale:
        print(f"\n{len(stale)} Keys fehlen noch in zotero.bib – in Overleaf die Zotero-Datei aktualisieren "
              f"und pushen: {', '.join(stale)}", file=sys.stderr)
    if missing:
        print(f"\n{len(missing)} Einträge ohne 'Citation Key:' im Feld Extra:", file=sys.stderr)
        for zk, title, sug in missing:
            print(f"  {zk}  Vorschlag: {sug:<20} {title[:70]}", file=sys.stderr)
    if dups:
        print("\nDoppelte Citation Keys (nur der erste wurde übernommen):", file=sys.stderr)
        for ck, keys in dups.items():
            print(f"  {ck}: {', '.join(keys)}", file=sys.stderr)
        sys.exit(2)


# ---------------------------------------------------------------- text
def pdf_attachments(zotero_key):
    return [c for c in get_all(f"items/{zotero_key}/children")
            if c["data"].get("itemType") == "attachment"
            and c["data"].get("contentType") == "application/pdf"]


def locate(att):
    d = att["data"]
    mode = d.get("linkMode")
    if mode in ("imported_file", "imported_url"):
        folder = DATA_DIR / "storage" / att["key"]
        p = folder / d["filename"] if d.get("filename") else None
        if not p or not p.exists():
            pdfs = list(folder.glob("*.pdf"))
            p = pdfs[0] if pdfs else None
        return p
    if mode == "linked_file":
        raw = d.get("path") or ""
        if raw.startswith("attachments:"):
            if not LINKED_BASE:
                return None
            return Path(LINKED_BASE) / raw[len("attachments:"):]
        return Path(raw)
    return None


def download(att):
    """PDF über die Web-API nach .zotero-cache/<attachment-key>.pdf laden (Zotero-Dateispeicher)."""
    if not WEB_API or att["data"].get("linkMode") not in ("imported_file", "imported_url"):
        return None
    out = PDF_CACHE / f"{att['key']}.pdf"
    md5 = att["data"].get("md5")
    stamp = out.with_suffix(".md5")
    if out.exists() and md5 and stamp.exists() and stamp.read_text().strip() == md5:
        return out
    PDF_CACHE.mkdir(exist_ok=True)
    r = _get(f"items/{att['key']}/file", stream=True)
    with open(out, "wb") as fh:
        for chunk in r.iter_content(1 << 16):
            fh.write(chunk)
    if md5:
        stamp.write_text(md5)
    return out


def page_labels(pdf: Path, n):
    try:
        from pypdf import PdfReader
        labels = list(PdfReader(str(pdf)).page_labels)
        if len(labels) == n:
            return labels
    except Exception as e:  # noqa: BLE001
        print(f"  Hinweis: keine Seitenlabels lesbar ({e}), nutze PDF-Index", file=sys.stderr)
    return [str(i + 1) for i in range(n)]


def extract(pdf: Path, out: Path, header: str):
    try:
        res = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"],
                             capture_output=True, text=True, check=True)
    except FileNotFoundError:
        die("pdftotext nicht gefunden – poppler-utils installieren.")
    pages = res.stdout.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    labels = page_labels(pdf, len(pages))
    parts = [header, "# Seitenmarker: === PDF-Seite <index> | Seite <gedruckte Seitenzahl> ===", ""]
    for i, (txt, lab) in enumerate(zip(pages, labels), start=1):
        parts.append(f"=== PDF-Seite {i} | Seite {lab} ===")
        parts.append(txt.rstrip())
        parts.append("")
    out.write_text("\n".join(parts), encoding="utf-8")
    chars = sum(len(p.strip()) for p in pages)
    return len(pages), chars


def cmd_text(args):
    mapping = load_map()
    targets = args.keys or sorted(mapping)
    TEXT_DIR.mkdir(exist_ok=True)
    for ck in targets:
        if ck not in mapping:
            print(f"{ck}: nicht in zotero-map.json", file=sys.stderr)
            continue
        zk = mapping[ck]["zotero_key"]
        atts = pdf_attachments(zk)
        if not atts:
            print(f"{ck}: kein PDF-Anhang in Zotero", file=sys.stderr)
            continue
        if len(atts) > 1:
            print(f"{ck}: {len(atts)} PDFs, nutze das erste ({atts[0]['data'].get('title')})",
                  file=sys.stderr)
        pdf = locate(atts[0])
        if not pdf or not pdf.exists():
            pdf = download(atts[0])
        if not pdf or not pdf.exists():
            print(f"{ck}: PDF-Datei nicht gefunden (ZOTERO_DATA_DIR={DATA_DIR}, kein Download möglich)",
                  file=sys.stderr)
            continue
        out = TEXT_DIR / f"{ck}.txt"
        if out.exists() and out.stat().st_mtime >= pdf.stat().st_mtime and not args.force:
            print(f"{ck}: aktuell")
            continue
        n, chars = extract(pdf, out, f"# Quelle: {ck} | Zotero: {zk} | Datei: {pdf.name}")
        if chars < 50 * max(n, 1):
            print(f"{ck}: {n} Seiten, aber kaum Text – vermutlich gescannt, OCR nötig (z. B. ocrmypdf)",
                  file=sys.stderr)
        else:
            print(f"{ck}: {n} Seiten -> sources-text/{ck}.txt")


# ---------------------------------------------------------------- annotations
def cmd_annotations(args):
    mapping = load_map()
    ck = args.key
    if ck not in mapping:
        die(f"{ck} nicht in zotero-map.json")
    zk = mapping[ck]["zotero_key"]
    anns = []
    for att in pdf_attachments(zk):
        for c in get_all(f"items/{att['key']}/children"):
            d = c["data"]
            if (d.get("itemType") == "annotation"
                    and d.get("annotationType") in ("highlight", "underline")
                    and (d.get("annotationText") or "").strip()):
                anns.append(d)
    anns.sort(key=lambda d: d.get("annotationSortIndex", ""))
    if not anns:
        print(f"{ck}: keine Text-Markierungen gefunden.")
        return

    EVID_DIR.mkdir(exist_ok=True)
    path = EVID_DIR / f"{ck}.yaml"
    data = load_evidence_file(path) if path.exists() else {"citekey": ck, "zotero_key": zk, "belege": []}
    known = {norm(b.get("zitat", "")) for b in data["belege"]}
    nums = [int(m.group(1)) for b in data["belege"]
            if (m := re.search(r"\.(\d+)$", str(b.get("id", ""))))]
    nxt = max(nums, default=0) + 1

    added = 0
    for d in anns:
        q = re.sub(r"\s+", " ", d["annotationText"]).strip()
        if norm(q) in known:
            continue
        entry = {"id": f"{ck}.{nxt:02d}", "seite": str(d.get("annotationPageLabel") or "?"),
                 "zitat": q, "kernaussage": "", "quelle": "annotation"}
        if (d.get("annotationComment") or "").strip():
            entry["kommentar"] = d["annotationComment"].strip()
        data["belege"].append(entry)
        known.add(norm(q))
        nxt += 1
        added += 1
    dump_evidence_file(path, data)
    print(f"{ck}: {added} neue Belege aus Markierungen ({len(anns) - added} schon vorhanden) "
          f"-> evidence/{ck}.yaml – 'kernaussage' noch ausfüllen.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("bib").set_defaults(fn=cmd_bib)
    t = sub.add_parser("text")
    t.add_argument("keys", nargs="*")
    t.add_argument("--force", action="store_true")
    t.set_defaults(fn=cmd_text)
    a = sub.add_parser("annotations")
    a.add_argument("key")
    a.set_defaults(fn=cmd_annotations)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
