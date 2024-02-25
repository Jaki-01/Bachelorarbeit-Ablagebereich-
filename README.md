# Bachelorarbeit-Ablagebereich

Dieses Repository dient als Ablagesystem und enthält alle relevanten Daten und Codes im Zusammenhang mit der Bachelorarbeit.

Das zentrale Ziel dieser Arbeit besteht darin, Greenwashing in Nachhaltigkeitsberichten zu erkennen. Zur besseren Verständlichkeit des Codes wird empfohlen, einen Nachhaltigkeitsbericht herunterzuladen und mit diesem die verschiedenen Codebausteine zu testen.

Schritt 1: Alle ganzen Sätze werden aus den Nachhaltigkeitsberichten herausgefiltert. Dies wurde mit dem Code "PDF-Dateien in CSV-Dateien abspeichern FERTIG.py" durchgeführt. Als Input für den Code können ein oder mehrere beliebige englischsprachige Nachhaltigkeitsberichte verwendet werden. Der Output besteht aus einer oder mehreren CSV-Dateien mit allen ganzen Sätzen der entsprechenden Nachhaltigkeitsberichte.

Voraussetzungen für Schritt 2: Die Modelle climatebert/environmental_claims und Jaki01/vagueness-detection-large müssen lokal gespeichert werden, indem der Code "Hugging Face Modelle für lokale Anwendung.py" ausgeführt wird. Beachten Sie, dass der Code verschiedene Funktionalitäten erfüllt (Funktionen 1, 2 und 3). FÜr diesen Fall wird die erste Funktion genutzt.

Schritt 2: Alle ganzen Sätze werden daraufhin untersucht, ob sie eine Umweltaussage darstellen. Hierfür wird der Code "Hugging Face Modelle für lokale Anwendung.py" in seiner zweiten Funktion verwendet. Die gelabelten Sätze (Umweltaussage/keine Umweltaussage) werden in Form einer CSV-Datei abgespeichert. Als Input dient die im ersten Schritt erstellte CSV-Datei.

Informationen zum Modelltraining: Durch das Modell aus Schritt 2 wurde ein großer Datensatz zusammengestellt, der alle Umweltaussagen aus 15 Nachhaltigkeitsberichten enthält (vgl. "Alle als Umweltaussage klassifizierten Sätze auf 15 Berichten.xlsx"). Aus diesem Datensatz wurde eine zufällige Auswahl von 600 Sätzen ausgewählt und durch eine Qualtricsumfrage gelabelt (vgl. "Datensatz für Modelltraining.csv"). Die Ergebnisse der Umfrage wurden bereinigt (vgl. "Vorgehen Rohdaten zu Datensatz.xlsx"), was schließlich zu dem finalen Datensatz ("Datensatz für Modelltraining.csv") führte. Das Modelltraining wurde im Code "Modelltraining zur Wagnis-Erkennung.ipynb" in einer Google Colab Umgebung durchgeführt, wodurch das Modell "Jaki01/vagueness-detection-large" erstellt wurde.

Voraussetzung für Schritt 3: Es muss eine CSV-Datei vorhanden sein, die in Spalte 1 verschiedene Umweltaussagen (gelabelt durch Schritt 2) enthält. Andere Spalten/Zellen dürfen nicht befüllt sein.

Schritt 3: Die Umweltaussagen werden daraufhin untersucht, ob sie vage formuliert sind, durch den Code "Hugging Face Modelle für lokale Anwendung.py" in seiner dritten Funktion. Das Ergebnis wird in einer CSV-Datei abgespeichert.

Zusammenfassung: Das Ergebnis aller Codebausteine ist, dass alle Sätze aus einem Nachhaltigkeitsbericht herausgefiltert wurden, die eine "Umweltaussage" darstellen und "vage" formuliert sind. Ein hoher Anteil dieser Sätze im Verhältnis zu den Umweltaussagen könnte darauf hindeuten, dass Greenwashing stattfindet. Mögliche Evidenz hierzu könnten in folgenden Arbeiten untersucht werden.
