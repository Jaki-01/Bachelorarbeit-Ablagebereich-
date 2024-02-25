# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:05:45 2023

@author: Jakob
"""

### ### ### ###

### Nutzen des Code: 
# Nachhaltigkeitsberichte (Pdf-Format) werden aufgerufen und alle ganzen Sätze werden extrahiert. 
# Diese ganzen Sätze werden für jeden Nachhaltigkeitsbericht in einer eigenen csv Datei abgespeichert. 

### ### ### ### 

import spacy
import fitz
import re

# Funktion extrahiert aus dem Bericht (in pdf Format) einen Bericht im txt Format
# Quelle: https://pymupdf.readthedocs.io/en/latest/
def read_through_pdf(file_path): 
    pdf_file_path = file_path
    # PDF oeffnen
    pdf_document = fitz.open(pdf_file_path)
   
    # leere Textzeile oeffenen
    text = ""

    # Durch jede Seite in der PDF gehen
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        text += page.get_text()

    # PDF schließen
    pdf_document.close()
    
    #print("Pdf-gelesen:")
    return text 
   

# verarbeitung durch die SpaCy -> erkennt alle ganzen Saetze und splitet diese-> nicht optimal
# Quelle: https://spacy.io/
def process_report(text_input):
    nlp = spacy.load("en_core_web_sm")
    
    text_input = nlp(text_input)
    sents = [str(i) for i in text_input.sents]
    len_sents = [len(i.split()) for i in sents]
    text_output = [sent for sent, length in zip(sents, len_sents) if length >= 5 and length < 40]
    
    print("preprocessing abgeschlossen")

    return text_output


# fuer jeden Nachhaltigkeitsbericht wird eine Csv-Datei geoeffnet mit allen ganzen Saetzen
# Quelle: https://docs.python.org/3/library/csv.html
def produce_csv_file(save_path, processed_text):
    
    # csv-Datei zum abspeichern der gruenen Saetze wird erzeugt 
    csvDatei=open(save_path,"w",encoding='utf-8')
    for r in range(len(processed_text)):
        processed_text[r] = str(re.sub(r'\n',' ',processed_text[r]))
        processed_text[r] = str(re.sub(r';',',',processed_text[r]))+"\n"
        csvDatei.write(processed_text[r])
    
    csvDatei.close()
    
    print("CSV-Datei erzeugt:"+save_path)


def main():      
       
    # Gib hier an welche Berichte aufgerufen werden und fuer welche Jahre (luecken zulaessig)
    firm = ["Alibaba", "Apple", "Aviva", "Biontech", "CleverlandCliffs", "CNRail", "ExxonMobil", "Ford", "GoldmanSachs", "KraftHeinz", "Linde", "Meta", "NVIDIA", "Qualys", "Verizon"]
    year = ["2023","2022","2021"]
    
    for firm_name in firm: 
        for year_date in year:
            try:
                # Pfad bei bedarf anpassen -> hier angeben wo die Nachhaltigkeitsberichte im Pdf Format gespeichert wurden im Format [Firmenname_Nachhaltigkeitsbericht_Jahr]
                source_path = r"C:\Users\Jakob\Documents\AA Bachelorarbeit Datein\Nachhaltigkeitsberichte\0.Orginal Nachhaltigkeitsberichte in Pdf/"+str(firm_name)+"_Nachhaltigkeitsbericht_"+str(year_date)+".pdf"
                
                # Pfad bei bedarf anpassen -> hier wird csv-Datei mit alle gruenen Saetzen abgespeichert 
                save_path = r"C:\Users\Jakob\Documents\AA Bachelorarbeit Datein\Nachhaltigkeitsberichte\1.Alle ganzen Saetze Nachhaltigkeitsberichte/"+str(firm_name)+"_Nachhaltigkeitsbericht_"+str(year_date)+".csv"
                
                text = read_through_pdf(source_path) # funktioniert
                processed_text = process_report(text)
                #print(processed_text)
                produce_csv_file(save_path, processed_text)
                
            except Exception as e:
                print(e)
                pass
            
if __name__ == "__main__":
    main()