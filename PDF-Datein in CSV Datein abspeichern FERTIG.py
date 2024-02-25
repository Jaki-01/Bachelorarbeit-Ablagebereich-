# -*- coding: utf-8 -*-
"""
Created on Mon Dez 11 15:05:45 2023

@author: Jakob
"""

### ### ### ###

### Nutzen des Codes: 
# Nachhaltigkeitsberichte (Pdf-Format) werden aufgerufen und alle ganzen Saetze werden extrahiert. 
# Diese ganzen Saetze werden für jeden Nachhaltigkeitsbericht in einer eigenen csv Datei abgespeichert. 

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
    firm = ["Firma_xy","Firma_yz"]
    year = ["2000","2002","2003"]
    
    for firm_name in firm: 
        for year_date in year:
            try:
                # Pfad bei bedarf anpassen -> hier angeben wo die Nachhaltigkeitsberichte im Pdf Format gespeichert wurden im Format [Firmenname_Nachhaltigkeitsbericht_Jahr]
                source_path = r"User/"+str(firm_name)+"_Nachhaltigkeitsbericht_"+str(year_date)+".pdf"
                
                # Pfad bei bedarf anpassen -> hier werden die csv-Datein mit allen ganzen Saetzen abgespeichert 
                save_path = r"User/"+str(firm_name)+"_Nachhaltigkeitsbericht_"+str(year_date)+".csv"
                
                text = read_through_pdf(source_path) # funktioniert
                processed_text = process_report(text)
                #print(processed_text)
                produce_csv_file(save_path, processed_text)
                
            except Exception as e:
                print(e)
                pass
            
if __name__ == "__main__":
    main()
