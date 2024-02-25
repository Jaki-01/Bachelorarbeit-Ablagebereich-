# Bachelorarbeit-Ablagebereich-
Dieses Repository wird als Ablagsystem verwendet und enthält alle relevanten Daten und Codes die im Zusammenhand mit der Bacheloararbeit stehen.

Die Arbeit hat ist wie folgt aufgebaut:

1.Schritt: alle ganzen Sätze werden(einzeln) aus den Nachhaltigkeitsberichten herausgefiltert wurde. Dies wurde mit dem Code "PDF-Datein in CSV Datein abspeichern FERTIG.py" durchgeführt. Als Input für den Code, kann man einen beliebigen englischsprachigen Nachhaltigkeitsbericht verwenden. Output ist eine CSV-Datei mit allen ganzen Sätzen.

!!!Voraussetzungen für Schritt 2: Das climatebert/environmental_claims und Jaki01/vagueness-detection-large müssen lokal abgespeichert werden mit dem Code "Hugging Face Modelle fuer lokale Anwendung.py" -> Beachte, dass der Code verschiedene Funktionen erfüllt (Funktion 1,2,3), hierfür wird nur Funktion 1 genutzt.

2.Schritt: alle ganzen Sätze werden darauf untersucht ob sie eine Umweltaussage sind, hiefür wird der Code "Hugging Face Modelle fuer lokale Anwendung.py" genutzt in seiner Funktion 2. Die gelabelten Sätze (Umwelaussage/keine Umweltaussage) werden in Form einer CSV-Datei abgespeichert. Input ist die im Schritt 1 geschaffene CSV-Datei. 

Hinweis: Durch Schritt 2 wurde ein großer Datensatz erstellt welcher alle Umweltaussagen von 15.Nachhaltigkeitsberichten enthält und zu einem späteren Zeitpunkt noch relevant ist diese nennt sich "Datensatz für Modelltraining.csv" wodurch mit dem Google Colab Code "Code zum Training des Wagnis

!!!Voraussetzung für Schritt 3: Es muss eine csv-Datei geben, die in Spalte 1 verschiedene Umweltaussagen (gelabelt durch Schritt 2) enthalten, andere Spalten/Zellen dürfen dafür nicht befüllt sein.

3.Schritt: alle Umweltaussagen werden darauf Untersucht, ob sie vage formuliert sind. Das Ergebnis wird 
