# Kap. 5 – Kürzung 28 → 12 Seiten (17.11.2026, Claude)

Neu: `Kapitel/05_Handlungsbedarf_Methodik.tex`, im PDF S. 28–39 (12 Seiten). **Alles Gestrichene steht wörtlich in
`review/kap5-entwurf/05_lang_28S.tex`** – zum Zurückholen dort den Absatz suchen.
Unverändert: alle Kürzel (D1–D4, F1–F4, A1–A7, K…, V1–V11), alle Zielwerte, alle Labels, auf die andere Kapitel
verweisen (`sec:handlungsbedarf`, `sec:bewertungsmethodik`), sowie alle `\ref` auf Kap. 6–8.

## Darstellungen
- Behalten: `tab:anforderungen` (jetzt **mit Kennzahlen**, mehrseitig als `xltabular`), `tab:versuchsplan`,
  `tab:testumgebung`, `fig:bewertungslogik`, `fig:handtoleranz`, `fig:schutzzeiten`.
- Entfernt (Dateien in `Bilder/tikz/` bleiben): `tab:defizite`, `tab:kennzahlen` (Inhalt in `tab:anforderungen`:
  Größe, Einheit, Nachweisart je K; K1.3/K6.4/K7.2 als „ohne Zielwert“), `fig:programmstand`, `fig:zielkonflikte`,
  `fig:versuchsmatrix`, `fig:inbetriebnahme`, `fig:echtzeitfaktor` (zuletzt gestrichen, um unter 12 S. zu kommen –
  erster Kandidat zum Zurückholen, kostet ca. ½ Seite).
- „Float too large“ ist weg (Tabelle läuft jetzt über zwei Seiten mit wiederholtem Kopf).
- Versuchsplan/Testumgebung mit `[!ht]` statt `[htbp]` (sonst je eine halbleere Float-Seite).

## 5.1 Handlungsbedarf
- `tab:defizite` gestrichen (doppelte den Text).
- Je Defizit nur noch die tragenden Belege; gestrichen u. a.: Tong .06/.08/.14, Chi .01, Sekkat .05/.09,
  OpenWBT, Durrani .01/.02/.04/.05, Yu .03/.11, G1Pilot .01, Collins .09, Choi .18, Kadian .01, Fu .01,
  He2024 .03/.04, Zhao .01, AliPour .01, Pot .02/.06, Ajaykumar .12, Prather .03, Ding .05, unitree_rl_mjlab,
  Ze .01, Saeedvand .13, ROS-2-Absatz (Macenski nur noch in 5.2).
- „Aus Dx folgt Fx“ in den ersten Satz des Absatzes gezogen; Eingrenzung (kein Training, keine Navigation,
  kein Sicherheitsnachweis) in einen Satz.

## 5.2 Anforderungen
- Bender nur noch .04 (Zielkonflikt operational/lösungsneutral); Nutzergruppen-Absatz gestrichen.
- Alle „Verfehlt ist Ax, wenn …“-Sätze ersetzt durch eine Regel: verfehlt, sobald eine Kennzahl ihren Zielwert
  verfehlt.
- Je Anforderung nur Begründung des Zielwerts; Wiederholung der Tabelle gestrichen. Gestrichen u. a.:
  He2025 .09, MRL .04, DIN EN ISO 13850 (.01, .02 – Quelle steht damit nicht mehr in Kap. 5), DGUV .02/.17,
  Prather .05 (ersetzt durch Prather .06), Pot .04/.06, Ajaykumar .11, Macenski .11, SUS-Satz (Ajaykumar .09).
- Randbedingungen auf einen Satz (quelloffen); Zielkonflikte als ein Absatz ohne Abbildung.

## 5.3 Bewertungsmethodik
- 5.3.1: Kennzahl-Erläuterungen je Forschungsfrage gestrichen (stehen in der Tabelle); Collins .03/.06 nur noch
  hier (nicht mehr doppelt in 5.2). Gestrichen: Sekkat .07/.13, Collins .04, Gu .02, Tan .12, Ajaykumar .13/.14,
  Pitonakova-Doppel; Gütekriterien/Validität auf einen Absatz.
- 5.3.2: SIL/HIL-Einordnung der Attrappe (Afzal .03, Mihalic .08), Afzal .02, Choi .05 (und die Wiederholung von Choi .02), Pitonakova .02 und die
  Einzelbeschreibung je Versuch gestrichen (steht in `tab:versuchsplan`); Grundsätze in zwei Sätze.
- 5.3.3: Kronauer .05/.13, Boettiger .02, Liste der Testgruppen-Inhalte, „nicht abgedeckt“-Liste, Detail zur
  Attrappe (Takttreue-Variante) und Einzel-Liste der Messmittel gestrichen. Alle `\pruefen` zur Testumgebung
  bleiben (zwei doppelte Textsätze entfallen, ihr Inhalt steht in den Tabellenzellen).

## Offen
- `\qf`: 2 (Hemmnisse Unternehmen; Bezugswert 100 ms) – wie vorher. `\pruefen`: 22 (vorher 24, nur Dopplungen weg).
- `zotero.bib` fehlt Bender2021, Pitonakova2018, Afzal2021 (DINENISO13850, Valori2021): in Overleaf aktualisieren.
