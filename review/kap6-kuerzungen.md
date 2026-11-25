# Kap. 6 – Kürzungen gegenüber der Langfassung (20.11.2026)

Langfassung: `review/kap6-entwurf/06_Konzept_Langfassung.tex` (S. 29–51, 23 S.). Kurzfassung: `Kapitel/06_Konzept.tex` (S. 29–40, 12 S.).
Alle Gliederungspunkte, Labels, 5 Abbildungen, 6 Tabellen und alle 23 `\qf`/`\pruefen` sind erhalten. Je Punkt: was fehlt bzw. zusammengefasst ist.

## Kapiteleinleitung
- Überblicksabsatz über die Abschnitte 6.1–6.5 (`% Kann`) gestrichen.
- Drei Entwurfsgrundsätze in einem Satz statt drei Sätzen; Verweis auf Kap. 7/8 entfallen.

## 6.1 Ausgangsbasis und Abgrenzung
- 6.1.1: Satz „Den Preis der Entscheidung benennt …“ gestrichen; Armregler-Satz verkürzt („kartesische Zielvorgaben“ entfallen).
- 6.1.2: Liste „nicht übernommen“ (Dex3-Hand, Tastenoberfläche, LiDAR/Odometrie, Docker-Image) gestrichen.
- 6.1.2: Defizite gekürzt: A2 ohne „Armregler gibt Sollwinkel nur zur Anzeige aus“; A5 ohne „Begrenzung nur über einstellbare Gelenkgeschwindigkeit“ und ohne Verweis auf Abschnitt g1_armsdk; A6 ohne „Start setzt ROS-2-Kommandozeile voraus“; A1/A7 ohne „feste Grundstellung“.
- 6.1.3: Zeilenbilanz („etwa ein Zehntel“) nur noch in der Tabelle; zwei Absätze, die die Tabelle nacherzählen (übernommen/erweitert/neu), gestrichen.
- 6.1.3: Fremdbestandteile ohne Beschreibung „Lernprojekt mit MuJoCo als Physik-Backend“ und „browserbasiert“.

## 6.2 Gesamtarchitektur
- 6.2.1: Lesehilfe zur Abbildung (Pfeile, gestrichelte Container) gestrichen.
- 6.2.1: Vier Ebenen-Absätze zu einem Absatz mit den drei Architekturregeln zusammengefasst; entfallen: „Neue Bedienwege docken an, ohne die Regelung zu verändern“, „Prüfung, ob eine Armbewegung starten darf, an genau einer Stelle“, „Funktionsknoten kennen nur die Herstellerschnittstelle“, Hände real über eigene Netzwerkverbindung (steht in tab:sim_real), Begründung „Knoten kann dieselbe Domain nicht zweimal öffnen“.
- 6.2.2: Entwürfe nicht mehr als (a)/(b)/(c) nummeriert (der `\pruefen`-Text ist entsprechend umformuliert).
- 6.2.2: Durrani2026 (.01/.03, `% Kann`), Gu2024.04 (MuJoCo näher an Realität als Isaac Gym) und UnitreeMujoco.04 (MJCF-Modelle) gestrichen.
- 6.2.2: Domain/Loopback-Details und die zeilenweise Nacherzählung von tab:sim_real (6 Sätze) auf einen Satz reduziert; Satz „Unterschiede beschränken sich auf …“ gestrichen.
- 6.2.3: Einleitungssatz „einziger Funktionsbereich ohne Gegenstück“ und „Bedienwege unterscheiden deshalb nicht zwischen den Welten“ gestrichen.
- 6.2.3: Policy-Absatz (`% Kann`) auf einen Halbsatz verkürzt; entfallen: Herkunft der voreingestellten Policy (UnitreeRLMjlab.01 an dieser Stelle, UnitreeRLMjlab.04 ONNX), Armhaltung je Policy. `\qf` L14 und `\pruefen` N5 bleiben.
- 6.2.3: „Ersatzregler nutzt Größen, die nur die Simulation liefert“, Verweis auf Sim-to-Real-Lücke (sec:sim2real), Verweis auf Umsetzungsabschnitte und auf sec:limitierungen gestrichen.

## 6.3 Sicherheitskonzept
- 6.3.1: Prather2025.03 (gebremste Gelenke nicht sicher) und Subburaman2023.01/.07 (hoher Schwerpunkt, Sturzfolgen) gestrichen.
- 6.3.1: Ding2026.09 (zu abrupter Halt) und DINENISO13850.02 (Anhalten ohne zusätzliche Gefährdung) gestrichen.
- 6.3.1: Zustandsbeschreibung „Bereit = am Kran / in der Sim am Rumpf gehalten“, Gehvoraussetzungen (Balance, Hüfte mittig, Kniebelastung), zweite Bestätigung bei Dämpfen/Gehen und Quittieren-Details gestrichen (stehen in Abbildung bzw. tab:schutzmechanismen, Quittieren in 6.4.2).
- 6.3.1: Nacherzählung von tab:haltstufen auf einen Satz reduziert; Sim-Verhalten (Not-Halt dämpft Beine, Sturzerkennung) nur noch in Tabellen/Caption.
- 6.3.1: Analogie zu den Stoppkategorien 0/2 (`% Kann`, DGUV2015.10) gestrichen.
- 6.3.2: Gefährdungsliste verkürzt; die vier Absätze Begrenzen/Vermeiden/Überwachen/Anhalten zu einem Absatz „Orientierung an Vorgaben für Industrieroboter“ zusammengefasst (alle Normbelege DGUV .04/.06/.07/.09, Villani .09, DIN13850 .01 erhalten).
- 6.3.2: Entfallen: Aufzählung der begrenzten Größen, „Konfiguration wird beim Start korrigiert“, „harte Grenzen nur real“, Zeitüberwachungen und Smartphone-Sperre im Text, „Totmann nicht sicherheitsgerichtet ausgewertet“, „Smartphone-Not-Halt wirkt nicht, wenn der PC hängt“.
- 6.3.2: Ding2026.05 (Bordrechner keine zertifizierte Sicherheitslaufzeit) gestrichen; „Kran oder Traggurt bei den ersten Geh- und Balanceversuchen“ auf „Sicherung am Kran“ verkürzt.
- 6.3.3: Schwingen eines weit vorn stehenden Arms bei reiner Rampe, Ablehnen neuer Ziele während der Rückgabe, Zeitgrenze, Sim ohne Rampe (`% Kann`) gestrichen; vier Fälle in zwei Sätzen.
- 6.3.3: Realtest-Satz ohne „der Roboter lief los“; Nachweis nur noch Abschnitt eval_realtests (eval_sicherheit entfallen).

## 6.4 Bedienkonzept
- Einleitung: Gliederungssatz der drei Unterabschnitte gestrichen.
- 6.4.1: Leitgedanken je ein Halbsatz; entfallen: Begründung „Oberfläche mit allen Funktionen lässt offen, welche Eingabe wirkt“ (`\qf` Q4 bleibt beim 1. Leitgedanken), Zustände aktiv/wechselnd/inaktiv, Sicherheitsbestätigung beim Realstart, Not-Halt aus gesperrtem Gamepad und Rolle Ansicht, Fernbedienung als PC-unabhängige Stufe.
- 6.4.2: Nacherzählung von tab:bedienwege (Rolle der einzelnen Bedienwege) gestrichen; Bedienzustand ohne Felder (Modus, Hand, Tempostufen) und ohne „Fahrbefehle nicht enthalten“, „Tempostufe je Bedienweg begrenzt“, „manuelle Eingabe bricht geplante Bewegung ab“.
- 6.4.2: Smartphone: „nur eine Sitzung“ und „verspäteter Befehl wirkungslos“ gestrichen.
- 6.4.3: Pot2009.05 (Bibliothek vorprogrammierter Verhalten) und Villani2018.06 (Abgrenzung zur Handführung) gestrichen; Beschreibung der drei Bausteine nur noch in der Abbildung.
- 6.4.3: Ausführungsarten (fortlaufend/schrittweise, real schrittweise voreingestellt), Ablage außerhalb der Container und Ajaykumar2021.07/.08 (Offline-Programmierung, `% Kann`) gestrichen; Verweis auf sec:limitierungen entfallen.

## 6.5 Erweiterungskonzept
- 6.5.1: Die vier Ebenen-Absätze auf einen Absatz reduziert; entfallen: Namensregel Hindernis/Greifobjekt in Szenen, ROS-2-Ebene mit Navigation als Beispiel, Macenski2022.04 an der Arm-API, „nur DDS-Domain und Netzwerkschnittstelle umstellen“, Eignung der untersten Ebene für Projekte mit eigenem Regler, Nachweis der Datenebene (eval_aufgaben) und Satz zu den Umsetzungsabschnitten.
- 6.5.1: Satz „Ein Projekt dockt auf der höchsten Ebene an, die seinen Bedarf deckt“ gestrichen.
- 6.5.2: Host-Netzwerk, gemeinsamer Quellstand, Umgebungsvariablen ohne Neubau, Simulationscontainer ohne ROS 2, Liste der externen Daten und Verweis auf eval_bedienaufwand gestrichen.
- 6.5.2: Absatz zu Grenzen von Containern (`% Kann`, Boettiger2015.10, Struhar2020.03/.04) gestrichen.

## Tabellen
- tab:eigenleistung: 14 → 10 Zeilen (zusammengelegt: Roboterzustand+Navigation, Kollision+Planer+Sicherheitsfunktionen, Posen/Abläufe+Arm-API, Bereitstellung+Tests/Doku); Einzelprozente je Datei, Herkunft der Policies (eine/zwei), „Dex3 entfernt“, Verweis Anhang gestrichen; `\pruefen`-Texte gekürzt.
- tab:sim_real: Spalte „gleich?“ gestrichen (Aussage steht in der Caption); Zellen gekürzt.
- tab:haltstufen: Auslöser zu „jeder Bedienweg“ zusammengefasst, Zellen gekürzt; Caption-Verweis auf tab:sim_real entfallen.
- tab:schutzmechanismen: 16 → 12 Zeilen, als normales Gleitobjekt statt xltabular; Spalte „Gefährdung“ gestrichen; Sim-Werte (Tempo 1,5 rad/s / 0,5 m/s, Rampe 0 s, Gehbereich der Policy) und Trichter 15 cm gestrichen; „Funkprüfung“ heißt „Funk“; Abschnittsverweise teils reduziert.
- tab:bedienwege: Zeile „Simulation / real“ in die Caption verschoben; Zellen auf Stichworte gekürzt; `\pruefen` Zielgruppe aus der Zelle in den Einführungssatz verschoben.
- tab:andockpunkte: Zellen gekürzt, Spalte „Detail in“ → „Abschn.“ ohne Anhang- und sec:ersatzregler-Verweis; Caption-Zusatz zum Zielkonflikt gestrichen (steht in Abbildungs-Caption).

## Technik
- tab:schutzmechanismen und die beiden Floats in 6.5.1 mit `[!ht]` statt `[htbp]`, damit keine halbleeren Float-Seiten entstehen.
