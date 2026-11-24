# Kap. 4 – Einstiegssätze prüfen (Regel Nils 24.11.: erster Satz fasst zusammen, nie Ankündigung, nie erzwungen)

Vorschläge für die nächste Überarbeitung (kommen als Punkte in den Rückmeldungs-Tab; .tex erst nach Einigung).

| Stelle | Jetzt | Bewertung | Vorschlag |
|---|---|---|---|
| Kap. 4 Einleitung | „Dieses Kapitel stellt die Fähigkeiten vor, …“ | Ankündigung → umbauen | „Fortbewegung, Manipulation mit Armen und Händen sowie die Bedienung durch Menschen sind die Fähigkeiten, auf denen die Umgebung aufbaut; verwandte Arbeiten verbinden sie bereits mit Simulation und realem Roboter.“ |
| 4.1 Fortbewegung | Einzelaussage zur Stabilität (Saeedvand) | passt, aber kein Überblick | Zusammenfassung voranstellen: modellbasiert (ZMP) oder lernbasiert (RL), für den G1 öffentliche Policies – Belege Saeedvand2019.09, Tong2024 prüfen |
| 4.2 Manipulation | „Die Arme und Hände des G1 werden … geführt.“ | gut | – |
| 4.2.1 IK | Vorwärtskinematik-Definition | Einstieg ins Detail | „Die IK bestimmt aus einer Zielpose die Gelenkwinkel; bei redundanten Armen ist sie mehrdeutig und wird meist numerisch gelöst.“ (Aristidou2018, Aristidou2009) |
| 4.2.2 Kollision | Rechenzeit der Kollisionsprüfung | fast gut | um „… weshalb Körper mit einfachen Hüllkörpern angenähert werden“ ergänzen (LaValle2006) |
| 4.2.3 Bahnplanung | Definition Konfigurationsraum | Einstieg ins Detail | „Ein Bahnplaner sucht im Konfigurationsraum einen kollisionsfreien Pfad, sampling- oder optimierungsbasiert, und parametriert ihn anschließend zeitlich.“ (LaValle2006, Schulman2014, Pham2018) |
| 4.2.4 Hände | beginnt mit Prüf-/Quelle-fehlt-Markern | umbauen | Marker nach unten; Einstieg über die Bandbreite der Hände am G1 (Inspire mit Sensorik bis einfache gedruckte Greifer; Eigenleistung + Inspire2024) |
| 4.3 Bedienung | Einteilung autonom/teilautonom/ferngesteuert | gut | – |
| 4.3.1 Teleoperation | Teleoperation verbindet Mensch und Roboter | gut | – |
| 4.3.2 Laienbedienung | „Einen anderen Zugang verfolgt …“ | gut | – |
| 4.4 Verwandte Arbeiten | „Mehrere Arbeiten nutzen MuJoCo als Prüfstand …“ | gut | – |
