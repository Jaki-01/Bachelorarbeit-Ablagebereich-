# -*- coding: utf-8 -*-
"""
Created on Mon Dec  20 14:51:27 2023

@author: Jakob
"""

### ### ### ###

### Der Code hat drei Zentrale funktionen (vgl. main funktion): 
# 1. Der Code installiert (einzeln) lokal die beiden Modelle (dazu def install_model(): anpassen und huggingface account erstellen/API erstellen) 
# Falls als Bedingug beide Modelle heruntergeladen wurden, kann der Code,
# 2. das "envirmental-claims" Modell aufrufen (aus .csv) und alle Umweltaussagen klassifizieren/abspeichern (als .csv)
# 3. das "vagueness-detection-large" Modell aufrufen (aus .csv) und alle vagen Sätze klassifizieren/abspeichern (als .csv)

### ### ### ### 

import pandas as pd
import os 
import sys
from transformers import AutoTokenizer, pipeline, AutoModelForSequenceClassification 

# Modelle installieren -> hierfür wird ein Huggingface.co Account benötigt
# Hinweis: Download kann nur mit einer guten Internetverbindung durchgeführt werden (sonst Connection Error) und das Modell lädt, auch wenn kein Fortschritt in der Downloadleiste Angezeigt wird.
# Quelle: https://www.youtube.com/watch?v=Ay5K4tog5NQ 
def install_model():
    import datasets
    from tqdm.auto import tqdm
    from transformers.pipelines.pt_utils import KeyDataset
    from huggingface_hub import hf_hub_download

    hugging_face_ipe =  os.environ.get('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') # hier deine huggingface IPE eintragen (https://huggingface.co/)

    model_id = 'Jaki01/vagueness-detection-large' # Pfad anpassen, je nachdem welches Modell man downloaden moechte: Jaki01/vagueness-detection-large (zur Wagnis Erkennung); climatebert/environmental_claims (Erkennung Umweltaussagen)
    filenames = [ # gib hier die Filenamen an welche auf Huggingface unter "files and versions" angegeben ist

        ".gitattributes",
        "README.md",
        "config.json",
        "model.safetensors",
        "special_tokens_map.json",
        "tokenizer.json",
        "tokenizer_config.json",
        "vocab.txt"

         ]

    for filename in filenames:
        downloaded_model_path = hf_hub_download(
            repo_id = model_id,
            filename = filename,
            token = hugging_face_ipe
        )
    print(downloaded_model_path) 
    
# oeffnet das Modell zur erkennung von Wagnis
# Quelle: HIER DAS HUGGING FACE MODELL ANGEBEN UND GOOGLECOLAB Quelle
def vague_sentence_detection():
    
        # hier wird das Modell zur Erkennung von Wagnis aufgerufen 
        global model_name_vague
        model_name_vague = "Jaki01/vagueness-detection-large"

        global tokenizer_vague
        tokenizer_vague = AutoTokenizer.from_pretrained(model_name_vague, max_length = 512, legacy = False) # legacy = False -> neuster Tokenizer wird verwendet

        global model_vague
        model_vague = AutoModelForSequenceClassification .from_pretrained(model_name_vague)

        #https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.pipeline -> infos zur pipeline Funktion
        global pipeline
        pipeline = pipeline("text-classification", model = model_vague, tokenizer = tokenizer_vague)
        
        print("Modell zur erkennung von Wagnis geoeffnet")


# oeffnet das Modell zur erkennung von gruenen Saetzen
# Quelle:https://github.com/dominiksinsaarland/environmental_claims
def green_sentence_detection():      
        # Hier wird das Modell zur Erkennung von Umweltaussage aufgerufen
        global model_name_green
        model_name_green = "climatebert/environmental-claims"

        global tokenizer_green
        tokenizer_green = AutoTokenizer.from_pretrained(model_name_green, max_length = 512, legacy = False) # legacy = False -> neuster Tokenizer wird verwendet

        global model_green
        model_green = AutoModelForSequenceClassification .from_pretrained(model_name_green)

        #https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.pipeline -> infos zur pipeline Funktion
        global pipeline
        pipeline = pipeline("text-classification", model = model_green, tokenizer = tokenizer_green)
    
        print("Modell zur erkennung von gruenen Saetzen geoeffnet")


# produziert eine csv-File mit allen gruenen/vagen Saetzen
# Quelle: https://docs.python.org/3/library/csv.html
def produce_csv_with_green_or_vague_sentences(report_savefile,result_green,text_array):
    
    csvDatei=open(report_savefile,"w",encoding='utf-8')
    csvDatei.write("label, label_text, text"+"\n")
    
    # CSV-Datei wird mit den gruenen Saetzen (array greensentences) befuellt
    for r in range(len(result_green)):
        if "no" in str(result_green[r]):
            csvDatei.write("0"+";"+"no"+";"+str(text_array[r]+"\n"))
        else:
            csvDatei.write("1"+";"+"yes"+";"+str(text_array[r]+"\n"))
    csvDatei.close()
    
    
def main ():
    # Welche Funktion soll ausgefuehrt werden (1/2/3 Eingeben) -> im Fall von 1.die Funktion def install model(): entsprechend der Beschreibung anpassen
    Auswahl = 2
    
    if Auswahl == 1:
        install_model()
        sys.exit()
    if Auswahl == 2: 
        print("2")
        vague_sentence_detection()
    if Auswahl == 3: 
        green_sentence_detection()
        
    # hier angeben wo der zu verarbeitende (wagnis erkennen/Umweltaussagen erkennen) Nachhaltigkeitsbericht gespeichert ist (Format = .csv)
    report_source = r"C:\Users\Jakob\Documents\AA Bachelorarbeit Datein\Nachhaltigkeitsberichte\2.Alle gruenen Saetze/Verizon_Nachhaltigkeitsbericht_2022.csv"    
 
    # hier angeben wo die Datei (CSV-Format) gespeicht werden soll, in welcher die Saetze klassifiziert(vage/Umwelaussage)sind
    report_savefile = r"C:\Users\Jakob\Documents\AA Bachelorarbeit Datein\Nachhaltigkeitsberichte\2.Alle gruenen Saetze/Vage_Verizon_2022.csv"
    
    text = pd.read_csv(report_source, header=None, delimiter=';',encoding='utf-8')
    
    # fuellt einen array mit alles Saetzen aus der Csv-Datei
    text_array = []
    r = 0
    while r < len(text) and text.iloc[r, 0]:  # Solange text.iloc[r, 0] nicht leer ist
        text_array.append(text.iloc[r, 0])
        r += 1
    
    result_green = [pipeline(row, truncation=True, max_length=512) for row in text_array]
    produce_csv_with_green_or_vague_sentences(report_savefile,result_green,text_array)

if __name__ == "__main__":
    main()
