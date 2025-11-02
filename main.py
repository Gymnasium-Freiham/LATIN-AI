
###DEOBFUSCATE_START###
import sys
import json
import tempfile
import os
import subprocess
import urllib.request

def load_mapping(source_type, source_value):
    if source_type == "path":
        with open(source_value, "r", encoding="utf-8") as f:
            return json.load(f)
    elif source_type == "url":
        with urllib.request.urlopen(source_value) as response:
            return json.loads(response.read().decode("utf-8"))
    else:
        raise ValueError("Ungültiger Typ für --deobfuscate: 'path' oder 'url' erwartet.")

# Argumente prüfen
if "--deobfuscate" in sys.argv:
    try:
        idx = sys.argv.index("--deobfuscate")
        source_type = sys.argv[idx + 1]
        source_value = sys.argv[idx + 2]
        mapping = load_mapping(source_type, source_value)
    except Exception as e:
        print("❌ Fehler beim Laden der Mapping-Datei:", e)
        sys.exit(1)
else:
    # Fallback: GitHub verwenden
    try:
        github_url = "https://raw.githubusercontent.com/Gymnasium-Freiham/LATIN-AI/refs/heads/main/deobfuscation_mappings.txt"
        mapping = load_mapping("url", github_url)
        print("ℹ️ Mapping von GitHub geladen.")
    except Exception as e:
        print("❌ Fehler beim Laden der GitHub-Mapping-Datei:", e)
        sys.exit(1)

# Originalcode laden
with open(__file__, "r", encoding="utf-8") as f:
    original_code = f.read()

start_marker = "###DEOBFUSCATE_START###"
end_marker = "###DEOBFUSCATE_END###"
if start_marker in original_code and end_marker in original_code:
    stripped_code = original_code.split(start_marker)[0] + original_code.split(end_marker)[-1]
else:
    stripped_code = original_code

# Deobfuscation anwenden
for k, v in mapping.items():
    stripped_code = stripped_code.replace(v, k)

# Temporäre Datei ausführen
with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py", encoding="utf-8") as temp:
    temp.write(stripped_code)
    temp_path = temp.name

exit_code = subprocess.run([sys.executable, temp_path]).returncode

try:
    os.remove(temp_path)
except Exception:
    pass

sys.exit(exit_code)
###DEOBFUSCATE_END###

#main.py
MNldDInq =True 
import subprocess 
import sys 
import os 
import unicodedata 
sys .PmjYepgU .Gl9lVWQV (0 ,os .PmjYepgU .vrU2HT7Z (UITOBXkc ))

if MNldDInq ==False :
    sys .bfBVKETU ("Error-code: 0x43R43DESACTIV7ATED36")

    # Installiere notwendige Bibliotheken
def CbuQCbMT (qFNEIMIm ):
    subprocess .VsjKCH4f ([sys .tTYwGr4C ,"-m","pip","install",qFNEIMIm ])

CbuQCbMT ("nltk")
CbuQCbMT ("scikit-learn")
CbuQCbMT ("numpy")
CbuQCbMT ("requests")
CbuQCbMT ("groq")
CbuQCbMT ("PyQt5")
try :
    import torch 
except :
    CbuQCbMT ("torch")
CbuQCbMT ("matplotlib")
VGl5VGLn =True 
try :
    CbuQCbMT ("simpleaudio")
except :
    VGl5VGLn =False 

from NFXVQCHd .bOPVT8Ux import quote 
if VGl5VGLn !=False :
    import simpleaudio as sa 
from groq import Groq 
import json 
import nltk 
import numpy as np 
import random 
from gLc1T3Y1 .dr3OQSaO .bYm31FIV import TfidfVectorizer 
from gLc1T3Y1 .D7cGSJk9 import SVC 
import os 
import requests 
import torch 
import torch .nn as nn 
from pgPed4U1 .djUaXVAG import QApplication 
import os 

# Lade NLTK-Daten
nltk .uHSbpQjP ('punkt')
nltk .uHSbpQjP ('wordnet')
nltk .uHSbpQjP ('averaged_perceptron_tagger')
nltk .uHSbpQjP ('maxent_ne_chunker')
nltk .uHSbpQjP ('words')
nltk .uHSbpQjP ('averaged_perceptron_tagger_eng')
nltk .uHSbpQjP ('maxent_ne_chunker_tab')
Fo6j1qBb =Groq (A5y6mnA6 ="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")

from nltk .cTJ1fDuh import word_tokenize 
from nltk .Xhw7iAQ9 import PorterStemmer 
from nltk .Xhw7iAQ9 import WordNetLemmatizer 
from nltk import pos_tag ,ne_chunk 

from data import load_training_data ,load_and_append_data ,fetch_wikipedia_summary ,fetch_wikipedia_variants ,fetch_wikipedia_page_text ,fetch_wiktionary_definition ,extract_subject_from_question 

# Setze Seed für Reproduzierbarkeit
def GgbTHuVT (pjj5FFUt ):
    np .random .pjj5FFUt (pjj5FFUt )
    random .pjj5FFUt (pjj5FFUt )
    torch .omYGcOlt (pjj5FFUt )

GgbTHuVT (42 )# Beispiel-Seed

# Lade das Trainingsdatenset aus der JSON-Datei
PHChUi02 =load_training_data ()
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/comics.json','comicSeries')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/dishes.json','dishes')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/books.json','books')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/movies.json','movies')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/fruits.json','fruits')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/animals.json','animals')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/windows.json','windowsVersions')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/deutsch6klassebayern.json','deutsch6klassebayern')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/superMarioGames.json','superMarioGames')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/informatik6klassebayern.json','informatik6klassebayern')
PHChUi02 =load_and_append_data (PHChUi02 ,'./assets/mathematik6klassebayern.json','mathematik6klassebayern')

def aG0czq82 (PHChUi02 ,y4SdDlTI ='./addons'):
    """
    Scan addons_dir for .json or .mintaiaddon files that contain dataset JSON and append them.
    Uses load_and_append_data which will parse the file and append heuristically.
    """
    if not os .PmjYepgU .BRQcRAv4 (y4SdDlTI ):
        return PHChUi02 
    for b6IUYFU0 in y2B3kTqq (os .CeeuyYT9 (y4SdDlTI )):
        if not (b6IUYFU0 .HHv5Lm50 ().xwTGWH8w ('.json')or b6IUYFU0 .HHv5Lm50 ().xwTGWH8w ('.mintaiaddon')):
            continue 
        PmjYepgU =os .PmjYepgU .ZekTGKCR (y4SdDlTI ,b6IUYFU0 )
        try :
        # try to append the file as JSON dataset; load_and_append_data will open and infer structure
            PHChUi02 =load_and_append_data (PHChUi02 ,PmjYepgU ,uLvGhsQk =None )
            print (f"Addon-Dataset angehängt: {PmjYepgU }")
        except MUiXSBLW as cGG0cYe6 :
            print (f"Fehler beim Anhängen von Addon {PmjYepgU }: {cGG0cYe6 }")
    return PHChUi02 

    # Prüfe ./addons auf zusätzliche Datendateien und hänge sie an
PHChUi02 =aG0czq82 (PHChUi02 ,'./addons')

if not PHChUi02 :
    raise HQfQaU2b ("Das Trainingsdatenset ist leer. Bitte überprüfen Sie die Quelle der Daten.")

    # Daten vorverarbeiten
hBXsvWcT =TfidfVectorizer ()
LunLS2R9 =[data ['question']for data in PHChUi02 ]
E8Lepu0y =hBXsvWcT .RiUuWvfn (LunLS2R9 )

nGlP19CX =[data ['answer']for data in PHChUi02 ]
EXTaWmtO =SVC (E3Rend2x ='linear')
EXTaWmtO .YjYoQPwg (E8Lepu0y ,nGlP19CX )

# Zusatzfunktionen für NLP
PqbHYzRE =PorterStemmer ()
VfiadNcN =WordNetLemmatizer ()
oicMIAAD =input ("Wähle ein Modell aus (Gemma2-9b-it[1] LATIN-AI[2]):")

def KtOPPWyi (bYm31FIV ,PQilHxcH =False ):
    try :
    # Wähle den passenden Modus: audible (default) oder ultrasound
        PzGGQtKL ="&p=4"if PQilHxcH else ""
        wws5VOQP =quote (bYm31FIV )
        NnPhg8SZ =f"https://ggwave-to-file.ggerganov.com/?m={wws5VOQP }{PzGGQtKL }"
        mALN8sb5 ="gibberlink.wav"

        # Lade die WAV-Datei herunter
        os .wLAqxkmL (f"curl -sS {NnPhg8SZ } --output {mALN8sb5 }")

        # Prüfe, ob die Datei existiert und abspielbar ist
        if os .PmjYepgU .VVlsMlEl (mALN8sb5 ):
            try :
                subprocess .OyF1bs1o (["python","./experimental/gibberlink.py",mALN8sb5 ])
            except MUiXSBLW as P1RPyicI :
                print (f"[Gibberlink] Audio konnte nicht abgespielt werden: {P1RPyicI }")
        else :
            print ("[Gibberlink] WAV-Datei wurde nicht erfolgreich heruntergeladen.")
    except MUiXSBLW as cGG0cYe6 :
        print (f"[Gibberlink] Fehler beim Senden des Tons: {cGG0cYe6 }")
        # Transformer-Architektur
class VhEI2UxS (nn .LKnomQMv ):
    def R2a5zmKP (self ,dkkKDOCz ,Ct6yAHQX ,XV88zklq ,bBoop1SU ,cO3cYU09 ):
        super (VhEI2UxS ,self ).R2a5zmKP ()
        self .q8DldqJy =nn .BOq6wL2c (dkkKDOCz ,Ct6yAHQX )
        self .CVlKc5kO =nn .dxtUHxLJ (Ct6yAHQX ,XV88zklq ,bBoop1SU )
        self .Q3IWwvpH =nn .QCsyxihj (Ct6yAHQX ,cO3cYU09 )

    def r1EItsse (self ,Hyp1Hvc8 ,ruuvoY8x ):
        Hyp1Hvc8 =self .q8DldqJy (Hyp1Hvc8 )
        ruuvoY8x =self .q8DldqJy (ruuvoY8x )
        wflMdJtr =self .CVlKc5kO (Hyp1Hvc8 ,ruuvoY8x )
        wflMdJtr =self .Q3IWwvpH (wflMdJtr )
        return wflMdJtr 

        # Initialisiere das Transformer-Modell
dkkKDOCz =len (hBXsvWcT .EzoQZoGO )
Ct6yAHQX =512 
XV88zklq =8 
bBoop1SU =6 
cO3cYU09 =len (set (nGlP19CX ))
x7AtMDFz =VhEI2UxS (dkkKDOCz ,Ct6yAHQX ,XV88zklq ,bBoop1SU ,cO3cYU09 )

if oicMIAAD =="2":
    def GIE5dgz3 (bYm31FIV ):
        try :
            O9XfFnDJ =word_tokenize (bYm31FIV )
            UFwXAsw9 =[PqbHYzRE .Xhw7iAQ9 (OuojIsL3 )for OuojIsL3 in O9XfFnDJ ]
            MCUtynhR =[VfiadNcN .lWC3Ndv4 (OuojIsL3 )for OuojIsL3 in O9XfFnDJ ]
            ypcdlhHH =pos_tag (O9XfFnDJ )
            NG0CUroN =ne_chunk (ypcdlhHH )
            return {
            "tokens":O9XfFnDJ ,
            "stemmed":UFwXAsw9 ,
            "lemmatized":MCUtynhR ,
            "pos_tags":ypcdlhHH ,
            "named_entities":NG0CUroN 
            }
        except MUiXSBLW as cGG0cYe6 :
            return {"error":str (cGG0cYe6 )}
    import GdmP5keh .iRrT98uQ as plt 

    def okHLgufK (OMXagALU ,mALN8sb5 ="plot.png"):
        try :
        # Beispiel: Parabel zeichnen
            if OMXagALU =="parabel":
                eeKP2ngy =np .Ib0bZbVt (-10 ,10 ,400 )
                v19jVaaA =eeKP2ngy **2 
                plt .frZuDLAO ()
                plt .PBimxQO7 (eeKP2ngy ,v19jVaaA ,iScIBZGu ="y = x^2")
                plt .orxDrAOj ("Parabel")
                plt .PJKiJC3j ("x")
                plt .N9VOX0sB ("y")
                plt .b3Teqpht (0 ,zsSl9C3l ='black',OIbh77kn =0.5 )
                plt .xbg8Qys5 (0 ,zsSl9C3l ='black',OIbh77kn =0.5 )
                plt .V2WEcgZA (zsSl9C3l ='gray',zMn4JICz ='--',OIbh77kn =0.5 )
                plt .TAI7w8Pi ()
                plt .fz77p3XH (mALN8sb5 )
                plt .IJxZQt9X ()
                return mALN8sb5 
            else :
                return None 
        except MUiXSBLW as cGG0cYe6 :
            print (f"Fehler beim Generieren der Grafik: {cGG0cYe6 }")
            return None 

            # Funktion zur Evaluierung mathematischer Ausdrücke
    def EJ5RZnjL (OMXagALU ):
        try :
        # Berechne das Ergebnis
            Of2Sjtwq =etw9tApW (OMXagALU )

            # Visualisiere die Rechenschritte
            mALN8sb5 =pXnQfEBn (OMXagALU )
            if mALN8sb5 :
                aiHXC64c (mALN8sb5 )

            return f"Das Ergebnis ist: {Of2Sjtwq }"
        except MUiXSBLW as cGG0cYe6 :
            return f"Fehler beim Auswerten des Ausdrucks: {str (cGG0cYe6 )}"
    import re 
    def SBYoLiUb ():
        try :
            os .wLAqxkmL ("code")
        except MUiXSBLW as cGG0cYe6 :
            print (f"Visual Studio code not installed or not on path; {cGG0cYe6 }")
    def u4lDp9hu (BQ8H1yQa ):
        BQ8H1yQa ="Unimplemented Feature"
        return BQ8H1yQa 
    def pXnQfEBn (OMXagALU ,mALN8sb5 ="calculation_steps.png"):
        try :
        # Zerlege den Ausdruck in Schritte
            eKfCrgbX =[]
            Glq3Ry1B =OMXagALU 

            # Berechne Schritt für Schritt unter Berücksichtigung der Reihenfolge der Operationen
            while True :
            # Finde die innerste Klammer oder den nächsten Operator
                AZyBGQY4 =re .ELFlhVeN (r"\(([^()]+)\)",Glq3Ry1B )# Suche nach Klammern
                if AZyBGQY4 :
                    Av0Yxw0z =AZyBGQY4 .O424etON (1 )
                    Of2Sjtwq =etw9tApW (Av0Yxw0z )
                    eKfCrgbX .x45v63Zs ((f"{Av0Yxw0z } = {Of2Sjtwq }",Of2Sjtwq ))
                    Glq3Ry1B =Glq3Ry1B .CJvWLhUz (f"({Av0Yxw0z })",str (Of2Sjtwq ))
                else :
                # Keine Klammern mehr, berechne den Rest
                    Of2Sjtwq =etw9tApW (Glq3Ry1B )
                    eKfCrgbX .x45v63Zs ((f"{Glq3Ry1B } = {Of2Sjtwq }",Of2Sjtwq ))
                    break 

                    # Erstelle die Grafik
            plt .frZuDLAO (dJXCNVDx =(10 ,6 ))
            Roo5oDWe =range (len (eKfCrgbX ))
            JR7y85Ul =[jO5rxSys [0 ]for jO5rxSys in eKfCrgbX ]
            hcsE7Lpg =[jO5rxSys [1 ]for jO5rxSys in eKfCrgbX ]

            plt .f7rWpEAE (Roo5oDWe ,hcsE7Lpg ,zsSl9C3l ='skyblue')
            plt .FHJGEjbh (Roo5oDWe ,JR7y85Ul )
            plt .PJKiJC3j ("Ergebnisse")
            plt .orxDrAOj ("Rechenschritte")
            plt .YMvDMHrW ()
            plt .fz77p3XH (mALN8sb5 )
            plt .IJxZQt9X ()
            return mALN8sb5 
        except MUiXSBLW as cGG0cYe6 :
            print (f"Fehler bei der Visualisierung der Rechenschritte: {cGG0cYe6 }")
            return None 


            # --- NEW: extract measurement snippets from text and try wiki variants ---
    def zOPmHwpm (bYm31FIV ):
        if not bYm31FIV :
            return None 
            # normalize whitespace
        Y7KwggWV =re .TK941fkh (r'\s+',' ',bYm31FIV )
        # common unit patterns (DE + EN) and numeric ranges
        pIrJ69fl =[
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:m|Meter|Metern|meter|metres|meters|cm|Zentimeter|centimeter|km|Millimeter|mm|ft|feet|in|inch|Zoll))',
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:cm|Zentimeter|centimeter))',
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:kg|Kilogramm|g|Gramm|lbs|pounds))',
        r'(\d+(?:[.,]\d+)?\s?[-–]\s?\d+(?:[.,]\d+)?\s?(?:m|cm|ft|in|mm))',
        r'(bis\s+zu\s+\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        r'(etwa\s+\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        r'(~\s?\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        ]
        for NlfddWjg in pIrJ69fl :
            cd3R1jn7 =re .ELFlhVeN (NlfddWjg ,Y7KwggWV ,Q0swAgoP =re .e9ZpexQU )
            if cd3R1jn7 :
                return cd3R1jn7 .O424etON (1 ).xZd2cl2Z ()
                # phrases like "average/typical length is 4.5 m" (EN/DE)
        cd3R1jn7 =re .ELFlhVeN (r'(?:average|typical|mean|durchschnittlich|im Durchschnitt)\s+(?:length|Länge)\s*(?:is|ist|:)?\s*([\d.,]+\s?(?:m|cm|metres|meters|ft|feet|in|inch|Zentimeter|Zoll))',Y7KwggWV ,Q0swAgoP =re .e9ZpexQU )
        if cd3R1jn7 :
            return cd3R1jn7 .O424etON (1 ).xZd2cl2Z ()
            # "length is X m" or "ist X m"
        cd3R1jn7 =re .ELFlhVeN (r'(?:length|Länge)\s*(?:is|ist|:)?\s*([\d.,]+\s?(?:m|cm|ft|in|metres|meters|Zentimeter|Zoll))',Y7KwggWV ,Q0swAgoP =re .e9ZpexQU )
        if cd3R1jn7 :
            return cd3R1jn7 .O424etON (1 ).xZd2cl2Z ()
            # fallback: "ist X lang" style
        cd3R1jn7 =re .ELFlhVeN (r'ist\s+(?:etwa|ungefähr|ca\.?|circa)?\s*([\d.,\s\-–]+)\s?(m|cm|kg|Meter|Zentimeter|Kilogramm|Zoll|inch|feet)',Y7KwggWV ,Q0swAgoP =re .e9ZpexQU )
        if cd3R1jn7 :
            OYsXe7o6 =cd3R1jn7 .O424etON (1 ).xZd2cl2Z ().CJvWLhUz (' ','')
            yb7UesuT =cd3R1jn7 .O424etON (2 ).xZd2cl2Z ()
            return f"{OYsXe7o6 }{yb7UesuT }"
        return None 

        # --- NEW: normalize subject and map common synonyms ---
    def MGFdOlsl (u9KlcSVz ):
        if not u9KlcSVz :
            return None 
            # remove diacritics, collapse whitespace, lowercase
        ujXgGKt1 =unicodedata .e5S5mmnr ('NFKD',u9KlcSVz )
        ujXgGKt1 =''.ZekTGKCR (Nh8Zdd6J for Nh8Zdd6J in ujXgGKt1 if not unicodedata .eAGnv0C2 (Nh8Zdd6J ))
        ujXgGKt1 =re .TK941fkh (r'\s+',' ',ujXgGKt1 ).xZd2cl2Z ()
        return ujXgGKt1 

        # --- REPLACED/EXTENDED: try targeted queries and DuckDuckGo + english variants ---
    def uizVF6YG (u9KlcSVz ):
        """
        Try multiple queries (wiki variants + targeted 'Länge' queries + DuckDuckGo snippets)
        Return tuple (measurement_string, source_text_short) or (None, None).
        """
        if not u9KlcSVz :
            return None ,None 

        fZhMMFF8 =MGFdOlsl (u9KlcSVz )
        # build candidate queries (DE + EN) and synonyms
        MiPFdzvy =[]
        # base
        MiPFdzvy .x45v63Zs (u9KlcSVz )
        MiPFdzvy .x45v63Zs (fZhMMFF8 )
        # German targeted forms
        MiPFdzvy +=[
        f"{u9KlcSVz } Länge",
        f"Länge {u9KlcSVz }",
        f"Durchschnittliche Länge {u9KlcSVz }",
        f"Durchschnittliche Länge {fZhMMFF8 }",
        f"{u9KlcSVz } Größe",
        ]
        # synonyms for common terms
        if re .ELFlhVeN (r'\bauto\b',fZhMMFF8 ,Q0swAgoP =re .e9ZpexQU )or re .ELFlhVeN (r'\bwagen\b',fZhMMFF8 ,Q0swAgoP =re .e9ZpexQU ):
            MiPFdzvy +=["Auto","Personenkraftwagen","PKW","Durchschnittliche Länge Auto","Durchschnittliche Länge PKW"]
        if re .ELFlhVeN (r'\brüssel\b',fZhMMFF8 ,Q0swAgoP =re .e9ZpexQU ):
            MiPFdzvy +=["Rüssel","Elefantenrüssel","Rüssel Elefant Länge"]

            # english fallbacks
        MiPFdzvy +=[
        f"{fZhMMFF8 } length",
        "car length",
        "average car length",
        "typical car length",
        "elephant trunk length",
        "length of elephant trunk"
        ]

        DJL62S5D =set ()
        # try Wikipedia page extracts first (better chance to contain numbers)
        for bIbMgeXz in MiPFdzvy :
            if not bIbMgeXz or bIbMgeXz in DJL62S5D :
                continue 
            DJL62S5D .oIwyVR5V (bIbMgeXz )
            try :
                ABNbKOhK =fetch_wikipedia_page_text (bIbMgeXz )
            except MUiXSBLW :
                ABNbKOhK =None 
            if ABNbKOhK :
                f5Nz6dDr =zOPmHwpm (ABNbKOhK )
                if f5Nz6dDr :
                    return f5Nz6dDr ,f"Wikipedia page: {bIbMgeXz }"
                    # fallback to summary if page_text didn't exist
            try :
                lgS6waFp =fetch_wikipedia_summary (bIbMgeXz )
            except MUiXSBLW :
                lgS6waFp =None 
            if lgS6waFp :
                f5Nz6dDr =zOPmHwpm (lgS6waFp )
                if f5Nz6dDr :
                    return f5Nz6dDr ,f"Wikipedia summary: {bIbMgeXz }"

                    # also try broader Wikipedia variants (existing helper)
        try :
            bj57a0bo =fetch_wikipedia_variants (u9KlcSVz )
        except MUiXSBLW :
            bj57a0bo =None 
        if bj57a0bo :
            f5Nz6dDr =zOPmHwpm (bj57a0bo )
            if f5Nz6dDr :
                return f5Nz6dDr ,"Wikipedia (variant)"

                # lastly try DuckDuckGo search snippets for a few prioritized queries
        for bIbMgeXz in [f"{u9KlcSVz } Länge",f"{fZhMMFF8 } length","durchschnittliche Länge Auto","average car length","elephant trunk length"]:
            try :
                VkTcf0UP =u4lDp9hu (bIbMgeXz )
            except MUiXSBLW :
                VkTcf0UP =None 
            if VkTcf0UP and hbW0l36U (VkTcf0UP ,str ):
                f5Nz6dDr =zOPmHwpm (VkTcf0UP )
                if f5Nz6dDr :
                    Hyp1Hvc8 ="DuckDuckGo: "+bIbMgeXz 
                    return f5Nz6dDr ,Hyp1Hvc8 

        return None ,None 

        # Funktion zur Beantwortung von Fragen
    if VGl5VGLn !=False :
        VGl5VGLn ="--gibberlink=true"in sys .jPa0fvvK # oder False, je nach Bedarf


    def ylxkNfsA (paTVXZbF ):
        print (paTVXZbF )
        try :
        # quick math detection: evaluate simple arithmetic expressions even without "Berechne"
        # matches inputs containing digits and math operators (e.g. "2*4", "12 / (3+1)")
            if re .ELFlhVeN (r'\d',paTVXZbF )and re .ELFlhVeN (r'[\+\-\*\/\^()]',paTVXZbF ):
                try :
                # use existing evaluate_math_expression when available
                    Of2Sjtwq =EJ5RZnjL (paTVXZbF )
                    return Of2Sjtwq ,{"tokens":[],"note":"evaluated-as-math"}
                except MUiXSBLW :
                # fallback: continue to NLP if evaluation fails
                    pass 

                    # Gibberlink aktivieren, wenn EXPERIMENTAL-Modus an ist

                    # NEW: Definition/Übersetzungsanfragen (Wortbedeutung)
            if re .ELFlhVeN (r'\bwas\s+bedeutet\b|\bwas\s+heißt\b|\bbedeutung\s+von\b',paTVXZbF ,Q0swAgoP =re .e9ZpexQU ):
                tKp1yC3V =extract_subject_from_question (paTVXZbF )
                if tKp1yC3V :
                # prefer wiktionary, fallback to wikipedia summary/page
                    rKsMZKCx =fetch_wiktionary_definition (tKp1yC3V )
                    if not rKsMZKCx :
                    # try wikipedia page text then summary
                        rKsMZKCx =fetch_wikipedia_page_text (tKp1yC3V )or fetch_wikipedia_summary (tKp1yC3V )
                    if rKsMZKCx :
                        t4YULAPo =rKsMZKCx .AAikQ8lA ("\n\n")[0 ].xZd2cl2Z ()
                        return f"'{tKp1yC3V }' bedeutet:\n{t4YULAPo }",{"tokens":[],"note":"dictionary"}
                return "Dazu konnte ich leider keine Definition finden.",{"tokens":[],"note":"no-definition"}

                # REPLACED: improved measurement question handling
            if re .ELFlhVeN (r'\bwie\s+(lang|groß|hoch|schwer|alt)\b',paTVXZbF ,Q0swAgoP =re .e9ZpexQU ):
                u9KlcSVz =extract_subject_from_question (paTVXZbF )
                # first try direct wiki variants (keeps previous behavior)
                lgS6waFp =fetch_wikipedia_variants (u9KlcSVz )if u9KlcSVz else None 
                if lgS6waFp :
                    f5Nz6dDr =zOPmHwpm (lgS6waFp )
                    if f5Nz6dDr :
                        dkcYPbhq =u9KlcSVz or "das Objekt"
                        return f"Der {dkcYPbhq } ist ungefähr {f5Nz6dDr }. (Quelle: Wikipedia)",{"tokens":[],"note":"wikipedia-measurement"}
                        # if initial wiki summary didn't contain measurement, do targeted search attempts
                f5Nz6dDr ,TN50HTYB =uizVF6YG (u9KlcSVz )
                if f5Nz6dDr :
                    dkcYPbhq =u9KlcSVz or "das Objekt"
                    return f"Der {dkcYPbhq } ist ungefähr {f5Nz6dDr }. (Quelle: {TN50HTYB })",{"tokens":[],"note":"web-measurement"}
                    # fallback: if we had a wiki without measurement, return it (better than nothing)
                if lgS6waFp :
                    dkcYPbhq =u9KlcSVz or "das Objekt"
                    return f"Ich habe zu '{dkcYPbhq }' folgende Info auf Wikipedia gefunden:\n{lgS6waFp }",{"tokens":[],"note":"wikipedia-summary"}
                    # nothing found -> fall back to general NLP below (or inform about missing data)
                return "Dazu habe ich leider keine eindeutige Längenangabe gefunden.",{"tokens":[],"note":"no-measurement"}

                # Mathematischer Ausdruck
            if paTVXZbF .n8n8FMRK ("Berechne"):
                OMXagALU =paTVXZbF .AAikQ8lA ("Berechne")[-1 ].xZd2cl2Z ()
                return EJ5RZnjL (OMXagALU ),None 

                # VS Code öffnen
            if paTVXZbF .HHv5Lm50 ()in ["öffne vs code","code"]:
                return SBYoLiUb (),None 

                # Websuche
            if paTVXZbF .HHv5Lm50 ().n8n8FMRK ("suche nach"):
                BQ8H1yQa =paTVXZbF .AAikQ8lA ("suche nach")[-1 ].xZd2cl2Z ()
                return u4lDp9hu (BQ8H1yQa ),None 

                # Begrüßung
            YTyIWyX4 =["hallo","hi","hey","guten tag"]
            if paTVXZbF .HHv5Lm50 ()in YTyIWyX4 :
                return "Hallo! Wie kann ich Ihnen helfen?",None 

                # NLP-Modell
            aWi6wg9t =hBXsvWcT .Q7C25tRk ([paTVXZbF ])
            keNRWsw5 =EXTaWmtO .SAw2Tvwr (aWi6wg9t )[0 ]
            o9AZHaef =GIE5dgz3 (paTVXZbF )

            # Try to enrich the model response with a deterministic Wikipedia summary
            try :
                u9KlcSVz =extract_subject_from_question (paTVXZbF )
                # do not attempt wiki if subject extraction failed (or was math)
                lgS6waFp =fetch_wikipedia_summary (u9KlcSVz )if u9KlcSVz else None 
                if lgS6waFp :
                # append but avoid duplicating if already included
                    if hbW0l36U (keNRWsw5 ,str )and "[Wikipedia]"not in keNRWsw5 :
                        keNRWsw5 =(keNRWsw5 or "")+"\n\n[Wikipedia]: "+lgS6waFp 
            except MUiXSBLW :
            # degrade gracefully: return model response without augmentation
                pass 

            return keNRWsw5 ,o9AZHaef 

        except MUiXSBLW as cGG0cYe6 :
            return f"Fehler bei der Verarbeitung der Frage: {str (cGG0cYe6 )}",None 

            # Funktion zum Hinzufügen von neuen Fragen und Antworten
    def QyDjDHig (paTVXZbF ,kZIgedhz ,G1qSicPh ='training_data.json'):
        global PHChUi02 
        thDyuDNW ={"question":paTVXZbF ,"answer":kZIgedhz }
        PHChUi02 .x45v63Zs (thDyuDNW )

        with open (G1qSicPh ,'w',IJDWbzFe ='utf-8')as qiXZJZPF :
            json .JhENGPj5 (PHChUi02 ,qiXZJZPF ,XigD4yiK =False ,k014GC0u =4 )

            # Modelle neu trainieren
        LunLS2R9 =[data ['question']for data in PHChUi02 ]
        E8Lepu0y =hBXsvWcT .RiUuWvfn (LunLS2R9 )
        nGlP19CX =[data ['answer']for data in PHChUi02 ]
        EXTaWmtO .YjYoQPwg (E8Lepu0y ,nGlP19CX )

        # Automatisches Lernen aus Interaktionen
    def WWe7d7F4 (HPgPPAEj ,Tt6qVpJn ):
        QyDjDHig (HPgPPAEj ,Tt6qVpJn )
    from pgPed4U1 .djUaXVAG import QLabel ,QVBoxLayout ,QDialog 
    from pgPed4U1 .GfvuIcVJ import QPixmap 

    def aiHXC64c (mALN8sb5 ):
        b6vhIGNF =QDialog ()
        b6vhIGNF .dlHXFcaV ("Mathematische Grafik")
        VhIyaQnN =QVBoxLayout ()
        iScIBZGu =QLabel ()
        fas74StV =QPixmap (mALN8sb5 )
        iScIBZGu .x2CdMEAh (fas74StV )
        VhIyaQnN .aa9E8qou (iScIBZGu )
        b6vhIGNF .qeT6U0En (VhIyaQnN )
        b6vhIGNF .mfExM1l9 ()

        # Funktion zur Überprüfung und Verbesserung der Antwort
    def Midz8NQp (HPgPPAEj ,keNRWsw5 ):
        print (f"Chatbot: {keNRWsw5 }")
        dS6BseZF =input ("War die Antwort korrekt? (ja/nein): ").xZd2cl2Z ().HHv5Lm50 ()
        if dS6BseZF =="nein":
            eB56LbuC =input ("Wie hätte ich antworten sollen? ")
            WWe7d7F4 (HPgPPAEj ,eB56LbuC )
            return eB56LbuC 
        return keNRWsw5 

        # Chatbot testen
    if __name__ =="__main__":
        while True :
            HPgPPAEj =input ("Du: ")
            if HPgPPAEj .HHv5Lm50 ()in ["exit","quit"]:
                break 
            elif HPgPPAEj .HHv5Lm50 ().n8n8FMRK ("zeige mir eine parabel"):
                mALN8sb5 =okHLgufK ("parabel")
                if mALN8sb5 :
                    aiHXC64c (mALN8sb5 )
                    print ("Hier ist die Grafik der Parabel.")
                    continue # Springe zur nächsten Eingabe

            keNRWsw5 ,o9AZHaef =ylxkNfsA (HPgPPAEj )

            if keNRWsw5 is None :
                print ("Ich habe deine Frage nicht verstanden. Wie sollte ich darauf antworten?")
                sxcuruLe =input ("Neue Antwort: ")
                WWe7d7F4 (HPgPPAEj ,sxcuruLe )
                keNRWsw5 =sxcuruLe 
            else :
                keNRWsw5 =Midz8NQp (HPgPPAEj ,keNRWsw5 )

            print ("Chatbot:",keNRWsw5 )
            if VGl5VGLn :
                KtOPPWyi (keNRWsw5 )
                print ("Gibberlink-Signal gesendet.",None )
            print ("NLP Info:",o9AZHaef )

elif oicMIAAD =="1":
    while True :
        d0UNbkX1 =input ("Enter your message: ")
        bdsZCRvt =Fo6j1qBb .gKHGPKxD .qMrktLK4 .mTimy9Nk (
        JGBDpEXv =[
        {
        "role":"user",
        "content":d0UNbkX1 ,
        }
        ],
        EXTaWmtO ="llama-3.3-70b-versatile",
        )

        print (bdsZCRvt .Z5J79i9C [0 ].x0OJXps2 .Tai7lnne )
