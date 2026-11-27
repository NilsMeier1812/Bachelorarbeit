#!/usr/bin/env bash
# Sitzungsstart in einem Befehl (W6, Nils 27.11.2026).
#   bash scripts/setup.sh            alles vorbereiten
#   bash scripts/setup.sh --kein-text  ohne Quellen-Texte (schneller, wenn nur Code/Build gebraucht wird)
#
# 1. Python-Pakete aus requirements.txt (nur fehlende)
# 2. Quellen-Repo bachelorarbeit_quellen als Nachbarordner (klonen bzw. aktualisieren)
# 3. zot.py bib (zotero-map.json) und zot.py text nur für Quellen ohne sources-text/<key>.txt
# 4. G1-Repo als Nachbarordner, Branch BA-Stable holen und mit dem Stand aus CLAUDE.md vergleichen
set -u
cd "$(dirname "$0")/.."
ROOT=$(pwd)
PARENT=$(dirname "$ROOT")
TEXT=1
[ "${1:-}" = "--kein-text" ] && TEXT=0
WARN=0
warn() { echo "WARNUNG: $*"; WARN=$((WARN+1)); }

echo "== 1/4 Python-Pakete"
if ! python3 -c "import requests, yaml, pypdf, rapidfuzz" 2>/dev/null; then
  pip install -q -r requirements.txt 2>&1 | grep -v "^\[notice\]" | tail -3
fi
python3 -c "import requests, yaml, pypdf" 2>/dev/null || warn "Pakete fehlen weiter (pip install -r requirements.txt)"
command -v pdftotext >/dev/null || warn "pdftotext fehlt (apt install poppler-utils)"
command -v latexmk >/dev/null || warn "latexmk fehlt (TeX Live, siehe Setup-Skript der Umgebung)"
command -v pandoc >/dev/null || warn "pandoc fehlt (nur für scripts/lesefassung.py nötig)"

echo "== 2/4 Quellen-Repo"
Q="$PARENT/bachelorarbeit_quellen"
if [ -d "$Q/.git" ]; then
  { git -C "$Q" fetch -q origin main && git -C "$Q" merge -q --ff-only FETCH_HEAD; } 2>/dev/null \
    || warn "Quellen-Repo: Aktualisieren fehlgeschlagen (lokale Änderungen?)"
else
  git clone -q --filter=blob:none https://github.com/NilsMeier1812/bachelorarbeit_quellen "$Q" \
    || warn "Quellen-Repo konnte nicht geklont werden"
fi

echo "== 3/4 Zotero"
python3 scripts/zot.py bib || warn "zot.py bib fehlgeschlagen"
if [ $TEXT = 1 ]; then
  MISSING=$(python3 - <<'EOF'
import json, pathlib
m = json.loads(pathlib.Path("zotero-map.json").read_text(encoding="utf-8"))
print(" ".join(k for k in sorted(m) if not pathlib.Path(f"sources-text/{k}.txt").exists()))
EOF
)
  if [ -n "$MISSING" ]; then
    echo "Texte fehlen für $(echo $MISSING | wc -w) Quellen, lade nach ..."
    python3 scripts/zot.py text $MISSING 2>&1 | grep -v ": aktuell$" | grep -iE "kein|nicht|kaum|fehl|error" || true
  else
    echo "alle Quellen-Texte vorhanden"
  fi
fi

echo "== 4/4 G1-Repo BA-Stable"
G="$PARENT/G1"
SOLL=$(grep -oE '\*\*Stand `[0-9a-f]{7,40}`' CLAUDE.md | head -1 | grep -oE '[0-9a-f]{7,40}')
if [ ! -d "$G/.git" ]; then
  git clone -q --filter=blob:none https://github.com/NilsMeier1812/G1 "$G" || warn "G1 konnte nicht geklont werden"
fi
if [ -d "$G/.git" ]; then
  git -C "$G" fetch -q origin BA-Stable 2>/dev/null || warn "BA-Stable konnte nicht geholt werden"
  IST=$(git -C "$G" rev-parse --short=7 FETCH_HEAD 2>/dev/null)
  if [ -z "$SOLL" ]; then
    warn "kein Stand in CLAUDE.md gefunden"
  elif [ "${IST:-}" != "${SOLL:0:7}" ]; then
    warn "BA-Stable steht auf ${IST:-?}, CLAUDE.md nennt ${SOLL}. Neuen Hash mit Nils klären und in CLAUDE.md eintragen."
  else
    echo "BA-Stable = $IST (wie CLAUDE.md)"
  fi
fi

echo
[ $WARN = 0 ] && echo "Sitzung bereit." || echo "Sitzung bereit mit $WARN Warnung(en), siehe oben."
