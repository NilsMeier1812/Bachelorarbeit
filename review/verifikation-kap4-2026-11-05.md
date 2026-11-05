# Verifikation Kap. 4.3/4.4 – 05.11.2026

Separater Prüf-Agent (Verifier-Prompt aus CLAUDE.md), Grundlage `review/pairs.jsonl` (48 Paare, 39 Sätze aus `Kapitel/04_Faehigkeiten_Verwandte_Arbeiten.tex`). Keine Dateien geändert. Korrekturen erst nach Rücksprache mit Nils.

**Ergebnis:** 28 gedeckt · 11 teilweise · 0 nicht gedeckt

| Datei:Zeile | Bewertung | Begründung (1 Satz) | Vorschlag |
|---|---|---|---|
| 04:37 | teilweise | Das Zitat sagt, dass Algorithmen sehr komplexe Entscheidungssysteme „often“ (oft) nicht abdecken; der Satz lässt „oft“ und „sehr komplex“ weg und verschärft die Aussage damit. | „Für Aufgaben, die sehr komplexe Entscheidungssysteme erfordern, die vorhandene Algorithmen oft nicht abdecken, …“ |
| 04:40 | teilweise | Das Zitat nennt Teleoperation „a powerful method“ zur Datensammlung; dass sie „vor allem“ dazu dient und das „in der Forschung“, steht nicht darin. | „Teleoperation ist eine leistungsfähige Methode, um Daten am Roboter für das Lernen aus Demonstrationen zu sammeln …“ |
| 04:41 | teilweise | Laut Zitat dienen haptische Geräte und VR-Geräte der Rückmeldung (VR „for visual feedbacks“) und nicht der Erfassung der Bewegungen des Bedieners. | „Bisherige Arbeiten zur Teleoperation nutzen Motion-Capture-Anzüge, Exoskelette, haptische Rückmeldegeräte und VR-Geräte für visuelles Feedback …“ |
| 04:43 | teilweise | Das Zitat beschreibt ein immersives, stereoskopisches und aktives Wahrnehmen; eine VR-Brille wird darin nicht erwähnt. | „über eine VR-Brille“ streichen oder einen Beleg ergänzen, der die VR-Brille nennt. |
| 04:57 | teilweise | Der Teil „Die Hürde ist hoch, da …“ ist eine Wertung und eine Begründung, die nicht im Zitat steht; belegt ist nur, welches Wissen nötig ist. | „Wirksame Roboterprogrammierung erfordert neben allgemeinen Programmierkenntnissen …“ ohne die Hürden-Wertung |
| 04:66 | teilweise | „so“ bezieht sich auf die Box Library im Satz davor; das Zitat nennt als Bedingung aber die gleichzeitige Nutzung beider Seiten (Flussdiagramm und Zeitleiste), und aus „play with … huge possibilities“ wird „bedienen“. | „Die gleichzeitige Nutzung von Flussdiagramm und Zeitleiste eröffnet laut den Autoren viele Möglichkeiten, mit dem Humanoiden zu arbeiten, ohne eine Zeile C++ zu kompilieren.“ |
| 04:75 | teilweise | Die Zeitangaben sind gedeckt, aber das Zitat Rudin2021.02 nennt den Vierbeiner ANYmal nicht (ANYmal steht nur in der Kernaussage). | Einen Beleg ergänzen, der ANYmal als Plattform nennt, oder „für den Vierbeiner ANYmal“ streichen. |
| 04:77 | teilweise | Das Zitat sagt nur „pairs it with MuJoCo Warp“; dass die Physik GPU-beschleunigt ist, steht nicht darin. | „GPU-beschleunigt“ streichen oder einen Beleg dafür ergänzen. |
| 04:78 | teilweise | Das Zitat sagt, dass Omniverse Installationsaufwand und Startverzögerung verursacht; dass die Autoren das als Grund für ein eigenes Framework nennen, steht nicht darin. | „Isaac Lab benötigt laut den Autoren die Omniverse-Laufzeitumgebung, was Installationsaufwand und Startverzögerung erhöht.“ |
| 04:79 | teilweise | Der erste Teil ist gedeckt; Beleg Zakka2026.04 ist aber nur eine Abbildungsunterschrift zu tanzenden G1, und „Referenzplattform“ ist eine Verschärfung. | „In einer Abbildung zeigen die Autoren Unitree-G1-Humanoide, die einen mit der BeyondMimic-Pipeline trainierten Tanz ausführen.“ |
| 04:93 | teilweise | Simulation in MATLAB/Simulink, das eigene Modell und die ausstehenden Versuche am realen G1 sind gedeckt; dass die Studie die Bewegungsplanung untersucht, steht in keinem der beiden Zitate. | Beleg zum Thema der Studie ergänzen oder neutral: „Für den G1 simuliert eine Studie ausschließlich in MATLAB/Simulink …“ |

Als gedeckt gewertet, aber kurz ansehen:
- **Zeile 52:** Zitat Cheng2024.05 nennt Open-TeleVision nicht ausdrücklich; Bezug ergibt sich nur aus der Quelle.
- **Zeile 91:** „daher“ stellt einen Zusammenhang zu Zeile 90 her, den die Zitate nicht ausdrücklich herstellen.
