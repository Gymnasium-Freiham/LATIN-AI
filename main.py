
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
        github_url = "https://raw.githubusercontent.com/Gymnasium-Freiham/LATIN-AI/refs/heads/main/main_obfuscation_mappings.txt"
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

import winreg 
def VJoq16uq ():
    try :
        with winreg .XQtJvqfY (winreg .EdNDYeIT ,r"Software\LATIN AI")as eh9vPcfk :
            gY4vUBfR ,icQlAJdW =winreg .qd2jBJzc (eh9vPcfk ,"InstallDir")
            return gY4vUBfR 
    except ovBEMnmG :
        print ("Installationsverzeichnis nicht gefunden")
        return None 

def gbYq9yur (gY4vUBfR ):
    if gY4vUBfR :
        os .Y8pTGiRN (gY4vUBfR )
        print (f"Arbeitsverzeichnis erfolgreich zu {gY4vUBfR } gewechselt")
    else :
        print ("Fehler beim Wechseln des Arbeitsverzeichnisses")


def TLb4rxEp (eh9vPcfk ,lT9uUXHF ,pbzBJM6C =None ):
    try :
        with winreg .XQtJvqfY (winreg .EdNDYeIT ,eh9vPcfk )as r2JkqtAx :
            ib5tUHvM ,icQlAJdW =winreg .qd2jBJzc (r2JkqtAx ,lT9uUXHF )
            return ib5tUHvM 
    except ovBEMnmG :
        return pbzBJM6C 
def rXOVJBNs (eh9vPcfk ,lT9uUXHF ,data ):
    with winreg .VN3EnrPu (winreg .EdNDYeIT ,eh9vPcfk )as r2JkqtAx :
        winreg .Qg9dKcmv (r2JkqtAx ,lT9uUXHF ,0 ,winreg .vldaEva5 ,data )

        #main.py
JGoPxxxt =True 
import subprocess 
import sys 
import os 
import unicodedata 
sys .WWDVFKTW .wjZhyZg2 (0 ,os .WWDVFKTW .xQMoysIJ (Fy2KQBO5 ))

if JGoPxxxt ==False :
    sys .jra6tnhO ("Error-code: 0x43R43DESACTIV7ATED36")

    # Installiere notwendige Bibliotheken
def hOZ3QXOc (gCOgn5oh ):
    subprocess .P5cbbiYJ ([sys .IEZlOfA3 ,"-m","pip","install",gCOgn5oh ])

hOZ3QXOc ("nltk")
hOZ3QXOc ("scikit-learn")
hOZ3QXOc ("numpy")
hOZ3QXOc ("requests")
hOZ3QXOc ("groq")
hOZ3QXOc ("PyQt5")
try :
    import torch 
except :
    hOZ3QXOc ("torch")
hOZ3QXOc ("matplotlib")
ml6nJfyC =True 
try :
    hOZ3QXOc ("simpleaudio")
except :
    ml6nJfyC =False 

from Hl2PM8xm .koAI02JG import quote 
if ml6nJfyC !=False :
    import simpleaudio as sa 
from groq import Groq 
import json 
import nltk 
import numpy as np 
import random 
from whhQHFbh .ABGJApJk .cxJ6d7JN import TfidfVectorizer 
from whhQHFbh .l1GuvtWM import SVC 
import os 
import requests 
import torch 
import torch .nn as nn 
from r0NjvBIy .x4lwbTf2 import QApplication 
import os 

# Lade NLTK-Daten
nltk .SA5t95KJ ('punkt')
nltk .SA5t95KJ ('wordnet')
nltk .SA5t95KJ ('averaged_perceptron_tagger')
nltk .SA5t95KJ ('maxent_ne_chunker')
nltk .SA5t95KJ ('words')
nltk .SA5t95KJ ('averaged_perceptron_tagger_eng')
nltk .SA5t95KJ ('maxent_ne_chunker_tab')
fJYArGFY =Groq (fZMbd7MS ="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")

from nltk .TisTdG3x import word_tokenize 
from nltk .whihQgPq import PorterStemmer 
from nltk .whihQgPq import WordNetLemmatizer 
from nltk import pos_tag ,ne_chunk 

from data import load_training_data ,load_and_append_data ,fetch_wikipedia_summary ,fetch_wikipedia_variants ,fetch_wikipedia_page_text ,fetch_wiktionary_definition ,extract_subject_from_question 

# Setze Seed für Reproduzierbarkeit
def TS0sTxef (DjK1FxmX ):
    np .random .DjK1FxmX (DjK1FxmX )
    random .DjK1FxmX (DjK1FxmX )
    torch .FgNI2MWf (DjK1FxmX )

TS0sTxef (42 )# Beispiel-Seed

# Lade das Trainingsdatenset aus der JSON-Datei
q1LuUTJa =load_training_data ()
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/comics.json','comicSeries')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/dishes.json','dishes')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/books.json','books')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/movies.json','movies')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/fruits.json','fruits')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/animals.json','animals')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/windows.json','windowsVersions')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/deutsch6klassebayern.json','deutsch6klassebayern')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/superMarioGames.json','superMarioGames')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/informatik6klassebayern.json','informatik6klassebayern')
q1LuUTJa =load_and_append_data (q1LuUTJa ,'./assets/mathematik6klassebayern.json','mathematik6klassebayern')

def hUewr9ea (q1LuUTJa ,wzDWCRi9 ='./addons'):
    """
    Scan addons_dir for .json or .mintaiaddon files that contain dataset JSON and append them.
    Uses load_and_append_data which will parse the file and append heuristically.
    """
    if not os .WWDVFKTW .bUK36fjh (wzDWCRi9 ):
        return q1LuUTJa 
    for Sp4vLdLs in V49hoXZ1 (os .LYaO7GFf (wzDWCRi9 )):
        if not (Sp4vLdLs .WQxZWrkw ().yTkMFqwK ('.json')or Sp4vLdLs .WQxZWrkw ().yTkMFqwK ('.mintaiaddon')):
            continue 
        WWDVFKTW =os .WWDVFKTW .NmbdZurb (wzDWCRi9 ,Sp4vLdLs )
        try :
        # try to append the file as JSON dataset; load_and_append_data will open and infer structure
            q1LuUTJa =load_and_append_data (q1LuUTJa ,WWDVFKTW ,eh9vPcfk =None )
            print (f"Addon-Dataset angehängt: {WWDVFKTW }")
        except wT3SaHXi as MJ0QaHx4 :
            print (f"Fehler beim Anhängen von Addon {WWDVFKTW }: {MJ0QaHx4 }")
    return q1LuUTJa 

    # Prüfe ./addons auf zusätzliche Datendateien und hänge sie an
q1LuUTJa =hUewr9ea (q1LuUTJa ,'./addons')

if not q1LuUTJa :
    raise qlzS3ieI ("Das Trainingsdatenset ist leer. Bitte überprüfen Sie die Quelle der Daten.")

    # Daten vorverarbeiten
RGpmHwlH =TfidfVectorizer ()
ZW72dwWN =[data ['question']for data in q1LuUTJa ]
wsn1lJXb =RGpmHwlH .vrXobOww (ZW72dwWN )

Mi2cexaI =[data ['answer']for data in q1LuUTJa ]
Q3OIrOPk =SVC (kffzbHNo ='linear')
Q3OIrOPk .I25oaVPG (wsn1lJXb ,Mi2cexaI )

# Zusatzfunktionen für NLP
xP9upUxz =PorterStemmer ()
xINTHIsa =WordNetLemmatizer ()
KOVUiEI9 =input ("Wähle ein Modell aus (Gemma2-9b-it[1] LATIN-AI[2]):")

def c9yoaxLU (cxJ6d7JN ,Ewcqiy2w =False ):
    try :
    # Wähle den passenden Modus: audible (default) oder ultrasound
        mosnUcDq ="&p=4"if Ewcqiy2w else ""
        ikdSe6PS =quote (cxJ6d7JN )
        w5GT6WL0 =f"https://ggwave-to-file.ggerganov.com/?m={ikdSe6PS }{mosnUcDq }"
        jP0NYsrZ ="gibberlink.wav"

        # Lade die WAV-Datei herunter
        os .saIQi82v (f"curl -sS {w5GT6WL0 } --output {jP0NYsrZ }")

        # Prüfe, ob die Datei existiert und abspielbar ist
        if os .WWDVFKTW .yknDlt5d (jP0NYsrZ ):
            try :
                subprocess .CX8RWFqq (["python","./experimental/gibberlink.py",jP0NYsrZ ])
            except wT3SaHXi as EKQNtC10 :
                print (f"[Gibberlink] Audio konnte nicht abgespielt werden: {EKQNtC10 }")
        else :
            print ("[Gibberlink] WAV-Datei wurde nicht erfolgreich heruntergeladen.")
    except wT3SaHXi as MJ0QaHx4 :
        print (f"[Gibberlink] Fehler beim Senden des Tons: {MJ0QaHx4 }")
        # Transformer-Architektur
class a8qLJrvi (nn .EO3g6taO ):
    def HcUPobv3 (self ,IccI8CDE ,ntNLrGTn ,xkjX7FCS ,AnpPH5Ul ,LEgesqKn ):
        super (a8qLJrvi ,self ).HcUPobv3 ()
        self .J6ik1xhq =nn .zlLQruIY (IccI8CDE ,ntNLrGTn )
        self .IfZdZYvl =nn .d7VelXzi (ntNLrGTn ,xkjX7FCS ,AnpPH5Ul )
        self .BCZ41z00 =nn .hVUrRuKQ (ntNLrGTn ,LEgesqKn )

    def O1L8O8x5 (self ,dJE25XLt ,TqYF84xI ):
        dJE25XLt =self .J6ik1xhq (dJE25XLt )
        TqYF84xI =self .J6ik1xhq (TqYF84xI )
        DzZVrMtQ =self .IfZdZYvl (dJE25XLt ,TqYF84xI )
        DzZVrMtQ =self .BCZ41z00 (DzZVrMtQ )
        return DzZVrMtQ 

        # Initialisiere das Transformer-Modell
IccI8CDE =len (RGpmHwlH .uqGVIxqc )
ntNLrGTn =512 
xkjX7FCS =8 
AnpPH5Ul =6 
LEgesqKn =len (set (Mi2cexaI ))
UYGP9jQK =a8qLJrvi (IccI8CDE ,ntNLrGTn ,xkjX7FCS ,AnpPH5Ul ,LEgesqKn )

if KOVUiEI9 =="2":
    def QPGwrvxu (cxJ6d7JN ):
        try :
            ugoHk4nz =word_tokenize (cxJ6d7JN )
            HZf5PjbH =[xP9upUxz .whihQgPq (Fb6cv0cT )for Fb6cv0cT in ugoHk4nz ]
            xjXPOpad =[xINTHIsa .LGiKAN2f (Fb6cv0cT )for Fb6cv0cT in ugoHk4nz ]
            W7tVGi7q =pos_tag (ugoHk4nz )
            LvZtLGd5 =ne_chunk (W7tVGi7q )
            return {
            "tokens":ugoHk4nz ,
            "stemmed":HZf5PjbH ,
            "lemmatized":xjXPOpad ,
            "pos_tags":W7tVGi7q ,
            "named_entities":LvZtLGd5 
            }
        except wT3SaHXi as MJ0QaHx4 :
            return {"error":str (MJ0QaHx4 )}
    import CMG7cNjq .gBCfZ6GD as plt 

    def Vkw0ujsQ (jXexuAdD ,jP0NYsrZ ="plot.png"):
        try :
        # Beispiel: Parabel zeichnen
            if jXexuAdD =="parabel":
                lT10nR1R =np .tfsqOLIT (-10 ,10 ,400 )
                tdMDlerf =lT10nR1R **2 
                plt .yiSO1sQD ()
                plt .Br2HeN8A (lT10nR1R ,tdMDlerf ,A69i8P1J ="y = x^2")
                plt .ArBSN4oB ("Parabel")
                plt .alAvO03K ("x")
                plt .Wyh4Jan9 ("y")
                plt .Zdd34fYP (0 ,suoE4tzh ='black',XhaaLglC =0.5 )
                plt .XCmZPzio (0 ,suoE4tzh ='black',XhaaLglC =0.5 )
                plt .aD9Nqypc (suoE4tzh ='gray',RIYVjIlA ='--',XhaaLglC =0.5 )
                plt .pHbQ9ryJ ()
                plt .AglgPH0d (jP0NYsrZ )
                plt .JLoGlvkM ()
                return jP0NYsrZ 
            else :
                return None 
        except wT3SaHXi as MJ0QaHx4 :
            print (f"Fehler beim Generieren der Grafik: {MJ0QaHx4 }")
            return None 

            # Funktion zur Evaluierung mathematischer Ausdrücke
    def ekVR3aZ2 (jXexuAdD ):
        try :
        # Berechne das Ergebnis
            ib5tUHvM =zneb9Fsf (jXexuAdD )

            # Visualisiere die Rechenschritte
            jP0NYsrZ =ZAObNofq (jXexuAdD )
            if jP0NYsrZ :
                nETi1472 (jP0NYsrZ )

            return f"Das Ergebnis ist: {ib5tUHvM }"
        except wT3SaHXi as MJ0QaHx4 :
            return f"Fehler beim Auswerten des Ausdrucks: {str (MJ0QaHx4 )}"
    import re 
    def iujXM5Ao ():
        try :
            os .saIQi82v ("code")
        except wT3SaHXi as MJ0QaHx4 :
            print (f"Visual Studio code not installed or not on path; {MJ0QaHx4 }")
    def JYezLFom (yrrV2DIj ):
        yrrV2DIj ="Unimplemented Feature"
        return yrrV2DIj 
    def ZAObNofq (jXexuAdD ,jP0NYsrZ ="calculation_steps.png"):
        try :
        # Zerlege den Ausdruck in Schritte
            ZMs3YxhM =[]
            fEYzQFo4 =jXexuAdD 

            # Berechne Schritt für Schritt unter Berücksichtigung der Reihenfolge der Operationen
            while True :
            # Finde die innerste Klammer oder den nächsten Operator
                Xuy8GAwj =re .wt4L20KJ (r"\(([^()]+)\)",fEYzQFo4 )# Suche nach Klammern
                if Xuy8GAwj :
                    cyAsEnp2 =Xuy8GAwj .Xlw1tRwn (1 )
                    ib5tUHvM =zneb9Fsf (cyAsEnp2 )
                    ZMs3YxhM .gmQPJ3CV ((f"{cyAsEnp2 } = {ib5tUHvM }",ib5tUHvM ))
                    fEYzQFo4 =fEYzQFo4 .V071qi1q (f"({cyAsEnp2 })",str (ib5tUHvM ))
                else :
                # Keine Klammern mehr, berechne den Rest
                    ib5tUHvM =zneb9Fsf (fEYzQFo4 )
                    ZMs3YxhM .gmQPJ3CV ((f"{fEYzQFo4 } = {ib5tUHvM }",ib5tUHvM ))
                    break 

                    # Erstelle die Grafik
            plt .yiSO1sQD (mhGl6TCw =(10 ,6 ))
            O2lE2GtP =range (len (ZMs3YxhM ))
            FJ31rcRV =[QEOb7kYe [0 ]for QEOb7kYe in ZMs3YxhM ]
            y1p3Nw1b =[QEOb7kYe [1 ]for QEOb7kYe in ZMs3YxhM ]

            plt .FqnfCNkF (O2lE2GtP ,y1p3Nw1b ,suoE4tzh ='skyblue')
            plt .aHAAl5Vq (O2lE2GtP ,FJ31rcRV )
            plt .alAvO03K ("Ergebnisse")
            plt .ArBSN4oB ("Rechenschritte")
            plt .y8mlA8qa ()
            plt .AglgPH0d (jP0NYsrZ )
            plt .JLoGlvkM ()
            return jP0NYsrZ 
        except wT3SaHXi as MJ0QaHx4 :
            print (f"Fehler bei der Visualisierung der Rechenschritte: {MJ0QaHx4 }")
            return None 


            # --- NEW: extract measurement snippets from text and try wiki variants ---
    def IcqwncWi (cxJ6d7JN ):
        if not cxJ6d7JN :
            return None 
            # normalize whitespace
        JIRy1Bqz =re .osGWSfk3 (r'\s+',' ',cxJ6d7JN )
        # common unit patterns (DE + EN) and numeric ranges
        u1uP3w7T =[
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:m|Meter|Metern|meter|metres|meters|cm|Zentimeter|centimeter|km|Millimeter|mm|ft|feet|in|inch|Zoll))',
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:cm|Zentimeter|centimeter))',
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:kg|Kilogramm|g|Gramm|lbs|pounds))',
        r'(\d+(?:[.,]\d+)?\s?[-–]\s?\d+(?:[.,]\d+)?\s?(?:m|cm|ft|in|mm))',
        r'(bis\s+zu\s+\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        r'(etwa\s+\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        r'(~\s?\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        ]
        for yNDotmcj in u1uP3w7T :
            uHbHOlJ3 =re .wt4L20KJ (yNDotmcj ,JIRy1Bqz ,G0cUW5Uq =re .XT37wjxp )
            if uHbHOlJ3 :
                return uHbHOlJ3 .Xlw1tRwn (1 ).Lls0axdD ()
                # phrases like "average/typical length is 4.5 m" (EN/DE)
        uHbHOlJ3 =re .wt4L20KJ (r'(?:average|typical|mean|durchschnittlich|im Durchschnitt)\s+(?:length|Länge)\s*(?:is|ist|:)?\s*([\d.,]+\s?(?:m|cm|metres|meters|ft|feet|in|inch|Zentimeter|Zoll))',JIRy1Bqz ,G0cUW5Uq =re .XT37wjxp )
        if uHbHOlJ3 :
            return uHbHOlJ3 .Xlw1tRwn (1 ).Lls0axdD ()
            # "length is X m" or "ist X m"
        uHbHOlJ3 =re .wt4L20KJ (r'(?:length|Länge)\s*(?:is|ist|:)?\s*([\d.,]+\s?(?:m|cm|ft|in|metres|meters|Zentimeter|Zoll))',JIRy1Bqz ,G0cUW5Uq =re .XT37wjxp )
        if uHbHOlJ3 :
            return uHbHOlJ3 .Xlw1tRwn (1 ).Lls0axdD ()
            # fallback: "ist X lang" style
        uHbHOlJ3 =re .wt4L20KJ (r'ist\s+(?:etwa|ungefähr|ca\.?|circa)?\s*([\d.,\s\-–]+)\s?(m|cm|kg|Meter|Zentimeter|Kilogramm|Zoll|inch|feet)',JIRy1Bqz ,G0cUW5Uq =re .XT37wjxp )
        if uHbHOlJ3 :
            AQWcgSV1 =uHbHOlJ3 .Xlw1tRwn (1 ).Lls0axdD ().V071qi1q (' ','')
            YVqskJAM =uHbHOlJ3 .Xlw1tRwn (2 ).Lls0axdD ()
            return f"{AQWcgSV1 }{YVqskJAM }"
        return None 

        # --- NEW: normalize subject and map common synonyms ---
    def bXoeNNsg (alKwuntH ):
        if not alKwuntH :
            return None 
            # remove diacritics, collapse whitespace, lowercase
        hTE9Ycdt =unicodedata .IMgOqNhj ('NFKD',alKwuntH )
        hTE9Ycdt =''.NmbdZurb (pDpp8aAR for pDpp8aAR in hTE9Ycdt if not unicodedata .gMEmHKSz (pDpp8aAR ))
        hTE9Ycdt =re .osGWSfk3 (r'\s+',' ',hTE9Ycdt ).Lls0axdD ()
        return hTE9Ycdt 

        # --- REPLACED/EXTENDED: try targeted queries and DuckDuckGo + english variants ---
    def LzwZvbWl (alKwuntH ):
        """
        Try multiple queries (wiki variants + targeted 'Länge' queries + DuckDuckGo snippets)
        Return tuple (measurement_string, source_text_short) or (None, None).
        """
        if not alKwuntH :
            return None ,None 

        KiJOeIfS =bXoeNNsg (alKwuntH )
        # build candidate queries (DE + EN) and synonyms
        JNJvD8C1 =[]
        # base
        JNJvD8C1 .gmQPJ3CV (alKwuntH )
        JNJvD8C1 .gmQPJ3CV (KiJOeIfS )
        # German targeted forms
        JNJvD8C1 +=[
        f"{alKwuntH } Länge",
        f"Länge {alKwuntH }",
        f"Durchschnittliche Länge {alKwuntH }",
        f"Durchschnittliche Länge {KiJOeIfS }",
        f"{alKwuntH } Größe",
        ]
        # synonyms for common terms
        if re .wt4L20KJ (r'\bauto\b',KiJOeIfS ,G0cUW5Uq =re .XT37wjxp )or re .wt4L20KJ (r'\bwagen\b',KiJOeIfS ,G0cUW5Uq =re .XT37wjxp ):
            JNJvD8C1 +=["Auto","Personenkraftwagen","PKW","Durchschnittliche Länge Auto","Durchschnittliche Länge PKW"]
        if re .wt4L20KJ (r'\brüssel\b',KiJOeIfS ,G0cUW5Uq =re .XT37wjxp ):
            JNJvD8C1 +=["Rüssel","Elefantenrüssel","Rüssel Elefant Länge"]

            # english fallbacks
        JNJvD8C1 +=[
        f"{KiJOeIfS } length",
        "car length",
        "average car length",
        "typical car length",
        "elephant trunk length",
        "length of elephant trunk"
        ]

        ZSJjOsfR =set ()
        # try Wikipedia page extracts first (better chance to contain numbers)
        for GO856sYT in JNJvD8C1 :
            if not GO856sYT or GO856sYT in ZSJjOsfR :
                continue 
            ZSJjOsfR .Jl9dPJ8N (GO856sYT )
            try :
                tAuHLmdR =fetch_wikipedia_page_text (GO856sYT )
            except wT3SaHXi :
                tAuHLmdR =None 
            if tAuHLmdR :
                ormsc39m =IcqwncWi (tAuHLmdR )
                if ormsc39m :
                    return ormsc39m ,f"Wikipedia page: {GO856sYT }"
                    # fallback to summary if page_text didn't exist
            try :
                vjdeK1uc =fetch_wikipedia_summary (GO856sYT )
            except wT3SaHXi :
                vjdeK1uc =None 
            if vjdeK1uc :
                ormsc39m =IcqwncWi (vjdeK1uc )
                if ormsc39m :
                    return ormsc39m ,f"Wikipedia summary: {GO856sYT }"

                    # also try broader Wikipedia variants (existing helper)
        try :
            T0rKdORk =fetch_wikipedia_variants (alKwuntH )
        except wT3SaHXi :
            T0rKdORk =None 
        if T0rKdORk :
            ormsc39m =IcqwncWi (T0rKdORk )
            if ormsc39m :
                return ormsc39m ,"Wikipedia (variant)"

                # lastly try DuckDuckGo search snippets for a few prioritized queries
        for GO856sYT in [f"{alKwuntH } Länge",f"{KiJOeIfS } length","durchschnittliche Länge Auto","average car length","elephant trunk length"]:
            try :
                EDuNo8ss =JYezLFom (GO856sYT )
            except wT3SaHXi :
                EDuNo8ss =None 
            if EDuNo8ss and It6s7go3 (EDuNo8ss ,str ):
                ormsc39m =IcqwncWi (EDuNo8ss )
                if ormsc39m :
                    dJE25XLt ="DuckDuckGo: "+GO856sYT 
                    return ormsc39m ,dJE25XLt 

        return None ,None 

        # Funktion zur Beantwortung von Fragen
    if ml6nJfyC !=False :
        ml6nJfyC ="--gibberlink=true"in sys .lBQBIWfd # oder False, je nach Bedarf


    def CGPfCvxa (IbktzBKM ):
        print (IbktzBKM )
        try :
        # quick math detection: evaluate simple arithmetic expressions even without "Berechne"
        # matches inputs containing digits and math operators (e.g. "2*4", "12 / (3+1)")
            if re .wt4L20KJ (r'\d',IbktzBKM )and re .wt4L20KJ (r'[\+\-\*\/\^()]',IbktzBKM ):
                try :
                # use existing evaluate_math_expression when available
                    ib5tUHvM =ekVR3aZ2 (IbktzBKM )
                    return ib5tUHvM ,{"tokens":[],"note":"evaluated-as-math"}
                except wT3SaHXi :
                # fallback: continue to NLP if evaluation fails
                    pass 

                    # Gibberlink aktivieren, wenn EXPERIMENTAL-Modus an ist

                    # NEW: Definition/Übersetzungsanfragen (Wortbedeutung)
            if re .wt4L20KJ (r'\bwas\s+bedeutet\b|\bwas\s+heißt\b|\bbedeutung\s+von\b',IbktzBKM ,G0cUW5Uq =re .XT37wjxp ):
                F9MNH10q =extract_subject_from_question (IbktzBKM )
                if F9MNH10q :
                # prefer wiktionary, fallback to wikipedia summary/page
                    WNXpiLf7 =fetch_wiktionary_definition (F9MNH10q )
                    if not WNXpiLf7 :
                    # try wikipedia page text then summary
                        WNXpiLf7 =fetch_wikipedia_page_text (F9MNH10q )or fetch_wikipedia_summary (F9MNH10q )
                    if WNXpiLf7 :
                        CtC6X9lK =WNXpiLf7 .EI1g74Xy ("\n\n")[0 ].Lls0axdD ()
                        return f"'{F9MNH10q }' bedeutet:\n{CtC6X9lK }",{"tokens":[],"note":"dictionary"}
                return "Dazu konnte ich leider keine Definition finden.",{"tokens":[],"note":"no-definition"}

                # REPLACED: improved measurement question handling
            if re .wt4L20KJ (r'\bwie\s+(lang|groß|hoch|schwer|alt)\b',IbktzBKM ,G0cUW5Uq =re .XT37wjxp ):
                alKwuntH =extract_subject_from_question (IbktzBKM )
                # first try direct wiki variants (keeps previous behavior)
                vjdeK1uc =fetch_wikipedia_variants (alKwuntH )if alKwuntH else None 
                if vjdeK1uc :
                    ormsc39m =IcqwncWi (vjdeK1uc )
                    if ormsc39m :
                        gFIALebi =alKwuntH or "das Objekt"
                        return f"Der {gFIALebi } ist ungefähr {ormsc39m }. (Quelle: Wikipedia)",{"tokens":[],"note":"wikipedia-measurement"}
                        # if initial wiki summary didn't contain measurement, do targeted search attempts
                ormsc39m ,ite7EdCF =LzwZvbWl (alKwuntH )
                if ormsc39m :
                    gFIALebi =alKwuntH or "das Objekt"
                    return f"Der {gFIALebi } ist ungefähr {ormsc39m }. (Quelle: {ite7EdCF })",{"tokens":[],"note":"web-measurement"}
                    # fallback: if we had a wiki without measurement, return it (better than nothing)
                if vjdeK1uc :
                    gFIALebi =alKwuntH or "das Objekt"
                    return f"Ich habe zu '{gFIALebi }' folgende Info auf Wikipedia gefunden:\n{vjdeK1uc }",{"tokens":[],"note":"wikipedia-summary"}
                    # nothing found -> fall back to general NLP below (or inform about missing data)
                return "Dazu habe ich leider keine eindeutige Längenangabe gefunden.",{"tokens":[],"note":"no-measurement"}

                # Mathematischer Ausdruck
            if IbktzBKM .AJf23Z0Y ("Berechne"):
                jXexuAdD =IbktzBKM .EI1g74Xy ("Berechne")[-1 ].Lls0axdD ()
                return ekVR3aZ2 (jXexuAdD ),None 

                # VS Code öffnen
            if IbktzBKM .WQxZWrkw ()in ["öffne vs code","code"]:
                return iujXM5Ao (),None 

                # Websuche
            if IbktzBKM .WQxZWrkw ().AJf23Z0Y ("suche nach"):
                yrrV2DIj =IbktzBKM .EI1g74Xy ("suche nach")[-1 ].Lls0axdD ()
                return JYezLFom (yrrV2DIj ),None 

                # Begrüßung
            Mhkbw9Oj =["hallo","hi","hey","guten tag"]
            if IbktzBKM .WQxZWrkw ()in Mhkbw9Oj :
                return "Hallo! Wie kann ich Ihnen helfen?",None 

                # NLP-Modell
            xbkja7nZ =RGpmHwlH .Hl3bZh7o ([IbktzBKM ])
            ee3XqTlu =Q3OIrOPk .JmPHxaQ9 (xbkja7nZ )[0 ]
            vWCUVgz1 =QPGwrvxu (IbktzBKM )

            # Try to enrich the model response with a deterministic Wikipedia summary
            try :
                alKwuntH =extract_subject_from_question (IbktzBKM )
                # do not attempt wiki if subject extraction failed (or was math)
                vjdeK1uc =fetch_wikipedia_summary (alKwuntH )if alKwuntH else None 
                if vjdeK1uc :
                # append but avoid duplicating if already included
                    if It6s7go3 (ee3XqTlu ,str )and "[Wikipedia]"not in ee3XqTlu :
                        ee3XqTlu =(ee3XqTlu or "")+"\n\n[Wikipedia]: "+vjdeK1uc 
            except wT3SaHXi :
            # degrade gracefully: return model response without augmentation
                pass 

            return ee3XqTlu ,vWCUVgz1 

        except wT3SaHXi as MJ0QaHx4 :
            return f"Fehler bei der Verarbeitung der Frage: {str (MJ0QaHx4 )}",None 

            # Funktion zum Hinzufügen von neuen Fragen und Antworten
    def qtv3TMwa (IbktzBKM ,WrDXu9Ah ,ruyQgtNB ='training_data.json'):
        global q1LuUTJa 
        bbmv3AIQ ={"question":IbktzBKM ,"answer":WrDXu9Ah }
        q1LuUTJa .gmQPJ3CV (bbmv3AIQ )

        with open (ruyQgtNB ,'w',qdqRAwTY ='utf-8')as VASkKN1w :
            json .niP0Q3uW (q1LuUTJa ,VASkKN1w ,Dpgm5LYr =False ,RKVNeTyy =4 )

            # Modelle neu trainieren
        ZW72dwWN =[data ['question']for data in q1LuUTJa ]
        wsn1lJXb =RGpmHwlH .vrXobOww (ZW72dwWN )
        Mi2cexaI =[data ['answer']for data in q1LuUTJa ]
        Q3OIrOPk .I25oaVPG (wsn1lJXb ,Mi2cexaI )

        # Automatisches Lernen aus Interaktionen
    def Om4atwT0 (JT2Vtu3G ,RyIWTnR9 ):
        qtv3TMwa (JT2Vtu3G ,RyIWTnR9 )
    from r0NjvBIy .x4lwbTf2 import QLabel ,QVBoxLayout ,QDialog 
    from r0NjvBIy .y4ENfkVB import QPixmap 

    def nETi1472 (jP0NYsrZ ):
        yoTQcZqW =QDialog ()
        yoTQcZqW .jA6ZJVLA ("Mathematische Grafik")
        I7bUAbAV =QVBoxLayout ()
        A69i8P1J =QLabel ()
        IHKBIxRM =QPixmap (jP0NYsrZ )
        A69i8P1J .XgCRlUvv (IHKBIxRM )
        I7bUAbAV .ELkmesmI (A69i8P1J )
        yoTQcZqW .ao76oBXe (I7bUAbAV )
        yoTQcZqW .JxIMYFoz ()

        # Funktion zur Überprüfung und Verbesserung der Antwort
    def vYfCGviW (JT2Vtu3G ,ee3XqTlu ):
        print (f"Chatbot: {ee3XqTlu }")
        BQNPi6JA =input ("War die Antwort korrekt? (ja/nein): ").Lls0axdD ().WQxZWrkw ()
        if BQNPi6JA =="nein":
            bZ5eshBx =input ("Wie hätte ich antworten sollen? ")
            Om4atwT0 (JT2Vtu3G ,bZ5eshBx )
            return bZ5eshBx 
        return ee3XqTlu 

        # Chatbot testen
    if __name__ =="__main__":
        while True :
            JT2Vtu3G =input ("Du: ")
            if JT2Vtu3G .WQxZWrkw ()in ["exit","quit"]:
                break 
            elif JT2Vtu3G .WQxZWrkw ().AJf23Z0Y ("zeige mir eine parabel"):
                jP0NYsrZ =Vkw0ujsQ ("parabel")
                if jP0NYsrZ :
                    nETi1472 (jP0NYsrZ )
                    print ("Hier ist die Grafik der Parabel.")
                    continue # Springe zur nächsten Eingabe

            ee3XqTlu ,vWCUVgz1 =CGPfCvxa (JT2Vtu3G )

            if ee3XqTlu is None :
                print ("Ich habe deine Frage nicht verstanden. Wie sollte ich darauf antworten?")
                R6BuoO8L =input ("Neue Antwort: ")
                Om4atwT0 (JT2Vtu3G ,R6BuoO8L )
                ee3XqTlu =R6BuoO8L 
            else :
                ee3XqTlu =vYfCGviW (JT2Vtu3G ,ee3XqTlu )

            print ("Chatbot:",ee3XqTlu )
            if ml6nJfyC :
                c9yoaxLU (ee3XqTlu )
                print ("Gibberlink-Signal gesendet.",None )
            print ("NLP Info:",vWCUVgz1 )

elif KOVUiEI9 =="1":
    while True :
        JkhyMkAj =input ("Enter your message: ")
        MvftyOAF =fJYArGFY .S9xeXuf1 .IZwIJm5s .pC1GbEDU (
        v0wZyqGM =[
        {
        "role":"user",
        "content":JkhyMkAj ,
        }
        ],
        Q3OIrOPk ="llama-3.3-70b-versatile",
        )

        print (MvftyOAF .wtit6gg5 [0 ].R5nxAufw .jGuRasqP )