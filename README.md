# Bachelorarbeit-Ablagebereich-
Dieses Repository wird als Ablagsystem verwendet und enthält alle relevanten Daten und Codes die im Zusammenhand mit der Bachelorarbeit stehen.

Zentrales Ziel dieser Arbeit war es, Greenwashing in Nachhaltigkeitsberichten zu erkennen, für das Verständnis des Codes empfiehlt für sich selbt einen Nachhaltigkeitsbericht zu downloaden und die verschiedenen Codebausteine damit zu testen. 

1.Schritt: Alle ganzen Sätze werden aus den Nachhaltigkeitsberichten herausgefiltert. Dies wurde mit dem Code "PDF-Dateien in CSV Datein abspeichern FERTIG.py" durchgeführt. Als Input für den Code, kann man einen/mehrere beliebige englischsprachige Nachhaltigkeitsbericht verwenden. Output ist eine/mehrere CSV-Datein mit allen ganzen Sätze eines/mehrerer Nachhaltigkeitsberichte. 

!!!Voraussetzungen für Schritt 2: Die Modelle climatebert/environmental_claims und Jaki01/vagueness-detection-large müssen lokal abgespeichert werden mit dem Code "Hugging Face Modelle fuer lokale Anwendung.py" -> Beachte, dass der Code verschiedene Funktionalitäten erfüllt (Funktion 1,2,3), in diesem Fall wird die 1-te Funktion genutzt.

2.Schritt: Alle ganzen Sätze werden darauf untersucht ob sie eine Umweltaussage sind, hiefür wird der Code "Hugging Face Modelle fuer lokale Anwendung.py" genutzt in seiner 2 ten-Funktion. Die gelabelten Sätze (Umwelaussage/keine Umweltaussage) werden in Form einer CSV-Datei abgespeichert. Input ist die im Schritt 1 geschaffene CSV-Datei. 

Information zum Modelltraining: 
Aus Schritt 2 wurde ein großer Datensatz zusammengetragen, welcher alle Umweltaussagen von 15.Nachhaltigkeitsberichten enthält (vgl. "Alle als Umweltaussage klassifizierten Sätze auf 15 Berichten.xslx"). Aus diesem wurde ein Auszug von 600 Sätzen zufällig ausgwählt/aufbereitet (vgl. "Datensatz für Modelltraining.csv") und durch eine Qualtricsumfrage gelabelt. Das Ergebnis aus der Umfrage wurde noch mal gesäubert (vgl. "Vorgehen Rohdaten zu Datensatz.xlsx"), was schließlich zu dem Finalen Datensatz (Datensatz für Modelltraing.csv") geführt hat. Das Modelltraining hat in dem Code "Modelltraining zur Wagnis Erkennung.ipynb" stattgefunden, wodurch das Modell "Jaki01/vagueness-detection-large" geschaffen wurde.

!!!Voraussetzung für Schritt 3: Es muss eine csv-Datei geben, die in Spalte 1 verschiedene Umweltaussagen (gelabelt durch Schritt 2) enthalten, andere Spalten/Zellen dürfen dafür nicht befüllt sein.

3.Schritt: Die Umweltaussagen werden darauf untersucht, ob sie vage formuliert sind durch den Code "Hugging Face Modelle fuer lokale Anwendung.py" in seiner 3-te Funktion. Das Ergebnis wird in einer CSV-Datei abgespeichert. 

Zusammenfassung: Das Ergebnis aller Codebausteine ist, dass man alle Sätze aus einem Nachhaltigkeitsbericht herausgefiltert hat, die eine "Umweltaussage" sind und "vage" Formuliert sind. Ein hoher Anteil dieser Sätze im Verhältnis zu den Umweltaussagen, könnte darauf hindeuten, dass Greenwashing stattfindet, wobei man diese Evidenz in weiteren wissenschafltichen Arbeiten untersuchen könnte. 
