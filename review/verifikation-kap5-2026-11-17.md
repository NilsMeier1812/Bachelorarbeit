# Verifikation Kap. 5, 17.11.2026

Grundlage: `review/pairs.jsonl` (126 Satz-Beleg-Paare, zusammengefasst zu 89 Sätzen in `Kapitel/05_Handlungsbedarf_Methodik.tex`). Bewertet nur anhand der Zitate.

- **gedeckt:** 61
- **teilweise:** 28
- **nicht gedeckt:** 0

Die meisten „teilweise“-Fälle sind leicht: Der Satz nennt einen Bezug (Hersteller, G1, ISO/TS 15066, Onboard-Regler), den das Zitat nur über ein Pronomen („its“, „it“, „the standard“, „these robots“) oder gar nicht enthält. Gewichtung im Vorschlag: (gering) = Bezug oder Kontext ergänzen; (mittel) = Inhalt verschärft oder Einschränkung weggelassen.

| Datei:Zeile | Bewertung | Begründung (1 Satz) | Vorschlag |
|---|---|---|---|
| 05_Handlungsbedarf_Methodik.tex:39 | teilweise | Dass unitree_mujoco vom Hersteller stammt („des Herstellers“, „nach dessen Angabe“), steht nicht im Zitat; dort steht nur „developed based on Unitree sdk2 and mujoco“. | (gering) Beleg für die Urheberschaft ergänzen oder „des Herstellers“ streichen. |
| 05_Handlungsbedarf_Methodik.tex:41 | teilweise | Das Zitat sagt nur „its implementation is closed-source“; dass „its“ der Onboard-Regler des G1 für die Fortbewegung ist, geht aus dem Zitat nicht hervor. | (gering) Beleg mit dem Bezugswort (Satz davor in Hu2026) ergänzen. |
| 05_Handlungsbedarf_Methodik.tex:44 | teilweise | Der Teil „ob derselbe Programmstand ausgeführt wird, geht aus der Beschreibung nicht hervor“ ist eine Negativaussage, die das Zitat nicht prüfbar macht. | (gering) Als eigene Feststellung kenntlich lassen; Nils sollte die Projektbeschreibung gegenlesen. |
| 05_Handlungsbedarf_Methodik.tex:46 | teilweise | „ausschließlich“ verschärft „is based on MATLAB/Simulink simulation“, und dass die Realversuche als „künftige Arbeit“ genannt werden, zeigt Yu2026.11 nicht (nur ein Listenpunkt ohne Kontext). | (mittel) „ausschließlich“ streichen oder belegen; für „künftige Arbeit“ die Überschrift des Abschnitts in den Beleg aufnehmen. |
| 05_Handlungsbedarf_Methodik.tex:47 | teilweise | „einen Simulationsbetrieb beschreibt sie nicht“ ist eine Negativaussage ohne Beleg. | (gering) Als eigene Feststellung zur geprüften Fassung formulieren und gegenlesen. |
| 05_Handlungsbedarf_Methodik.tex:56 | teilweise | Den Kontext „Transfer gelernter Ganzkörperbewegungen auf den G1“ enthält das Zitat nicht. | (gering) Beleg für den Kontext (He2025) ergänzen oder die Einleitung kürzen. |
| 05_Handlungsbedarf_Methodik.tex:59 | teilweise | „these robots“ wird zu einer allgemeinen Aussage über das physische Testen; um welche Roboter es geht, fehlt. | (gering) Bezug aus Choi2021 übernehmen (z. B. „für die betrachteten Roboter“). |
| 05_Handlungsbedarf_Methodik.tex:60 | teilweise | Dass Kadian2020 eine „Arbeit zur Navigation“ ist, steht nicht in Kadian2020.01. | (gering) Zusätzlich `\ev{Kadian2020.02}` anfügen (nennt „navigation method“). |
| 05_Handlungsbedarf_Methodik.tex:69 | teilweise | „solche Aufbauten“ umfasst auch VR-Brillen, He2024.03 nennt aber nur Motion Capture und Exoskelette. | (gering) Beim He2024-Teil auf „Motion-Capture-Systeme und Exoskelette“ einschränken. |
| 05_Handlungsbedarf_Methodik.tex:70 | teilweise | Das Zitat spricht von „a Unitree humanoid robot“; dass es um den G1 geht und das Projekt vom Hersteller stammt, steht nicht darin. | (gering) Beleg mit G1-Bezug und Urheber ergänzen oder „für Unitree-Humanoide“ schreiben. |
| 05_Handlungsbedarf_Methodik.tex:73 | teilweise | Pot2009.06 knüpft „ohne eine Zeile C++ zu kompilieren“ an die gleichzeitige Nutzung beider Seiten; diese Bedingung fehlt im Satz. | (mittel) Bedingung ergänzen, wie in Zeile 323. |
| 05_Handlungsbedarf_Methodik.tex:74 | teilweise | Das Zitat beschränkt das eingeschränkte Bild auf die „user experiences“; der Satz lässt das Objekt weg und verallgemeinert. | (gering) „ein eingeschränktes Bild der Nutzererfahrungen“. |
| 05_Handlungsbedarf_Methodik.tex:75 | teilweise | Prather2025.06 sagt „Those standards cannot be applied directly“; ob damit „die meisten Robotiknormen“ gemeint sind, geht aus dem Zitat nicht hervor. | (gering) Bezugswort aus dem Kontext von S. 41 in den Beleg aufnehmen oder einschränken. |
| 05_Handlungsbedarf_Methodik.tex:113 | teilweise | Das Zitat schränkt auf die „Current version“ ein; die Tabellenzelle lässt das weg (Zeile 40 behält es). | (gering) „in der ausgewerteten Fassung“ ergänzen; Herstellerschaft siehe Zeile 39. |
| 05_Handlungsbedarf_Methodik.tex:115 | teilweise | „nur auf Simulation“ verschärft „is based on MATLAB/Simulink simulation“. | (gering) „beruht auf einer MATLAB/Simulink-Simulation“. |
| 05_Handlungsbedarf_Methodik.tex:119 | teilweise | Den Zusatz „das betrifft dort den Transfer gelernter Policies“ enthält das Zitat nicht. | (gering) Wie Zeile 56: Kontext belegen. |
| 05_Handlungsbedarf_Methodik.tex:124 | teilweise | Dass die Empfehlung vom Hersteller stammt, steht nicht im Zitat; „mindestens bis zum Kapitel ‚Application Development‘“ ist weggelassen. | (gering) Urheber belegen oder „die Projektbeschreibung empfiehlt“. |
| 05_Handlungsbedarf_Methodik.tex:269 | teilweise | Collins2019.06 gilt für „Scene 1“ und nennt „p“ nur als „mean position“; „Kennzahl ist dort“ verallgemeinert auf die ganze Arbeit. | (gering) „für Szene 1“ ergänzen bzw. Beleg zu Eq. 1 heranziehen. |
| 05_Handlungsbedarf_Methodik.tex:282 | teilweise | Wie Zeile 41: Das „its“ im Zitat ist nicht als Onboard-Regler ausgewiesen. | (gering) Wie Zeile 41. |
| 05_Handlungsbedarf_Methodik.tex:295 | teilweise | Villani2018.09 beginnt mit „it presents …“; dass „it“ die ISO/TS 15066 ist, steht nicht im Zitat. | (gering) Beleg um den vorangehenden Satz mit der Normbezeichnung erweitern. |
| 05_Handlungsbedarf_Methodik.tex:296 | teilweise | Prather2025.05 spricht von „the standard“; dass es sich um die ISO/TS 15066 handelt, geht aus dem Zitat nicht hervor. | (gering) Beleg mit Normbezeichnung ergänzen. |
| 05_Handlungsbedarf_Methodik.tex:323 | teilweise | Dass „both sides“ Flussdiagramm und Zeitleiste sind, steht nicht im Zitat. | (gering) Beleg aus Pot2009 ergänzen, der die beiden Seiten benennt. |
| 05_Handlungsbedarf_Methodik.tex:324 | teilweise | Dass xr_teleoperate vom Hersteller des G1 stammt, steht nicht im Zitat. | (gering) Wie Zeile 70. |
| 05_Handlungsbedarf_Methodik.tex:364 | teilweise | Wie Zeile 41: Das „its“ im Zitat ist nicht als Onboard-Regler ausgewiesen. | (gering) Wie Zeile 41. |
| 05_Handlungsbedarf_Methodik.tex:471 | teilweise | Aus Sekkat2024.13 geht nicht hervor, ob der Gelenkwinkelfehler in Fig. 7 den Vergleich mit dem realen Roboter oder mit Choregraphe betrifft. | (gering) In Sekkat2024 prüfen und ggf. präzisieren. |
| 05_Handlungsbedarf_Methodik.tex:479 | teilweise | Dass die Return-Differenz eine gelernte Policy voraussetzt, steht nicht im Zitat (eq. 2 ist dort nicht wiedergegeben). | (gering) Als eigene Begründung formulieren oder Beleg zu eq. 2 ergänzen. |
| 05_Handlungsbedarf_Methodik.tex:492 | teilweise | Wie Zeile 74: Das Objekt „user experiences“ und die Einschränkung auf „academic work“ fehlen. | (gering) „akademische Arbeiten … ein eingeschränktes Bild der Nutzererfahrungen“. |
| 05_Handlungsbedarf_Methodik.tex:502 | teilweise | Wie Zeile 59: Der Bezug „these robots“ fehlt, die Aussage wird verallgemeinert. | (gering) Wie Zeile 59. |
