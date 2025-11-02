
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
        print("Mapping von GitHub geladen.")
    except Exception as e:
        print("Fehler beim laden der GitHub-Mapping-Datei:", e)
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

original_cwd = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.dirname(temp_path)

# 🔧 data.py ins Temp-Verzeichnis kopieren
data_source = os.path.join(original_cwd, "data.py")
data_target = os.path.join(temp_dir, "data.py")
try:
    if os.path.exists(data_source):
        import shutil
        shutil.copy(data_source, data_target)
except Exception as e:
    print("❌ Fehler beim Kopieren von data.py:", e)
    sys.exit(1)

# 🔧 sys.path erweitern im temporären Code
inject_path = f'import sys; sys.path.insert(0, {repr(temp_dir)})'
stripped_code = inject_path + stripped_code

# 🔧 temporäre Datei erneut schreiben mit sys.path injection
with open(temp_path, "w", encoding="utf-8") as temp:
    temp.write(stripped_code)

# 🔧 Ausführen im Temp-Verzeichnis
exit_code = subprocess.run([sys.executable, temp_path], cwd=original_cwd)

# 🔧 Aufräumen
try:
    os.remove(temp_path)
    os.remove(data_target)
except Exception:
    pass

sys.exit(exit_code)
###DEOBFUSCATE_END###

import winreg 
def yZBnrVWW ():
    try :
        with winreg .RZWXBXqH (winreg .gKmy0ICt ,r"Software\LATIN AI")as GKJY8PEe :
            H1R0Rl9q ,TYay3Xss =winreg .Sjgqj42d (GKJY8PEe ,"InstallDir")
            return H1R0Rl9q 
    except Ld8QEr0f :
        print ("Installationsverzeichnis nicht gefunden")
        return None 

def A8VGUpdy (H1R0Rl9q ):
    if H1R0Rl9q :
        os .cn8AkJq6 (H1R0Rl9q )
        print (f"Arbeitsverzeichnis erfolgreich zu {H1R0Rl9q } gewechselt")
    else :
        print ("Fehler beim Wechseln des Arbeitsverzeichnisses")


def wbcds2Ym (GKJY8PEe ,R2oUN4IV ,IItlWP0h =None ):
    try :
        with winreg .RZWXBXqH (winreg .gKmy0ICt ,GKJY8PEe )as BpVoRrNj :
            wxzBnyMC ,TYay3Xss =winreg .Sjgqj42d (BpVoRrNj ,R2oUN4IV )
            return wxzBnyMC 
    except Ld8QEr0f :
        return IItlWP0h 
def dDa0fTFX (GKJY8PEe ,R2oUN4IV ,data ):
    with winreg .FmZvNKR4 (winreg .gKmy0ICt ,GKJY8PEe )as BpVoRrNj :
        winreg .jERgKiDU (BpVoRrNj ,R2oUN4IV ,0 ,winreg .DQTkHRy6 ,data )

        #main.py
JxFAE0Ur =True 
import subprocess 
import sys 
import os 
import unicodedata 
sys .ayHNpyHc .inQSY7xZ (0 ,os .ayHNpyHc .brhRsrXx (BECbpuBl ))

if JxFAE0Ur ==False :
    sys .UWjWRFbn ("Error-code: 0x43R43DESACTIV7ATED36")

    # Installiere notwendige Bibliotheken
def eYnWlmlV (WIuo3cuA ):
    subprocess .Y89keNYq ([sys .bSRmi41v ,"-m","pip","install",WIuo3cuA ])

eYnWlmlV ("nltk")
eYnWlmlV ("scikit-learn")
eYnWlmlV ("numpy")
eYnWlmlV ("requests")
eYnWlmlV ("groq")
eYnWlmlV ("PyQt5")
try :
    import torch 
except :
    eYnWlmlV ("torch")
eYnWlmlV ("matplotlib")
WCTTp5OA =True 
try :
    eYnWlmlV ("simpleaudio")
except :
    WCTTp5OA =False 

from LaCsNaxm .rF8DAw8b import quote 
if WCTTp5OA !=False :
    import simpleaudio as sa 
from groq import Groq 
import json 
import nltk 
import numpy as np 
import random 
from CtdoQcI7 .VVspMHjE .S88WDBxS import TfidfVectorizer 
from CtdoQcI7 .oV8B7LFh import SVC 
import os 
import requests 
import torch 
import torch .nn as nn 
from Q2GELjuH .ICwpXbTo import QApplication 
import os 

# Lade NLTK-Daten
nltk .xyBNrSbw ('punkt')
nltk .xyBNrSbw ('wordnet')
nltk .xyBNrSbw ('averaged_perceptron_tagger')
nltk .xyBNrSbw ('maxent_ne_chunker')
nltk .xyBNrSbw ('words')
nltk .xyBNrSbw ('averaged_perceptron_tagger_eng')
nltk .xyBNrSbw ('maxent_ne_chunker_tab')
k8He7Z74 =Groq (QgiDEeNX ="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")

from nltk .Gfp0b1Sd import word_tokenize 
from nltk .cDSy0EML import PorterStemmer 
from nltk .cDSy0EML import WordNetLemmatizer 
from nltk import pos_tag ,ne_chunk 

from data import load_training_data ,load_and_append_data ,fetch_wikipedia_summary ,fetch_wikipedia_variants ,fetch_wikipedia_page_text ,fetch_wiktionary_definition ,extract_subject_from_question 

# Setze Seed für Reproduzierbarkeit
def ZOEZDaSY (RISMRyIY ):
    np .random .RISMRyIY (RISMRyIY )
    random .RISMRyIY (RISMRyIY )
    torch .nHy8aqPh (RISMRyIY )

ZOEZDaSY (42 )# Beispiel-Seed

# Lade das Trainingsdatenset aus der JSON-Datei
M2Hh8fZ5 =load_training_data ()
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/comics.json','comicSeries')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/dishes.json','dishes')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/books.json','books')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/movies.json','movies')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/fruits.json','fruits')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/animals.json','animals')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/windows.json','windowsVersions')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/deutsch6klassebayern.json','deutsch6klassebayern')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/superMarioGames.json','superMarioGames')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/informatik6klassebayern.json','informatik6klassebayern')
M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,'./assets/mathematik6klassebayern.json','mathematik6klassebayern')

def fHarHJbS (M2Hh8fZ5 ,lIkLpyQ6 ='./addons'):
    """
    Scan addons_dir for .json or .mintaiaddon files that contain dataset JSON and append them.
    Uses load_and_append_data which will parse the file and append heuristically.
    """
    if not os .ayHNpyHc .kI9XZj57 (lIkLpyQ6 ):
        return M2Hh8fZ5 
    for LVmMrYnp in O0ICUzF3 (os .eWNhXc6o (lIkLpyQ6 )):
        if not (LVmMrYnp .U5nWvn2z ().Rt1zhSfO ('.json')or LVmMrYnp .U5nWvn2z ().Rt1zhSfO ('.mintaiaddon')):
            continue 
        ayHNpyHc =os .ayHNpyHc .Ur57W3x2 (lIkLpyQ6 ,LVmMrYnp )
        try :
        # try to append the file as JSON dataset; load_and_append_data will open and infer structure
            M2Hh8fZ5 =load_and_append_data (M2Hh8fZ5 ,ayHNpyHc ,GKJY8PEe =None )
            print (f"Addon-Dataset angehängt: {ayHNpyHc }")
        except cSNMStEJ as zha05Jj5 :
            print (f"Fehler beim Anhängen von Addon {ayHNpyHc }: {zha05Jj5 }")
    return M2Hh8fZ5 

    # Prüfe ./addons auf zusätzliche Datendateien und hänge sie an
M2Hh8fZ5 =fHarHJbS (M2Hh8fZ5 ,'./addons')

if not M2Hh8fZ5 :
    raise lgsAb3ns ("Das Trainingsdatenset ist leer. Bitte überprüfen Sie die Quelle der Daten.")

    # Daten vorverarbeiten
PhNrfw9M =TfidfVectorizer ()
atF4OP0L =[data ['question']for data in M2Hh8fZ5 ]
vLHJvwrW =PhNrfw9M .ZYEcnWbh (atF4OP0L )

Nn8k0Pcv =[data ['answer']for data in M2Hh8fZ5 ]
EMBSQEYY =SVC (Qhk08ROK ='linear')
EMBSQEYY .buB84FUI (vLHJvwrW ,Nn8k0Pcv )

# Zusatzfunktionen für NLP
ZKDICO1U =PorterStemmer ()
dzsQOkZ1 =WordNetLemmatizer ()
xUhZ2BBG =input ("Wähle ein Modell aus (Gemma2-9b-it[1] LATIN-AI[2]):")

def i8J558rV (S88WDBxS ,DiW7HKfP =False ):
    try :
    # Wähle den passenden Modus: audible (default) oder ultrasound
        TheoNC5m ="&p=4"if DiW7HKfP else ""
        oRW2Xf2L =quote (S88WDBxS )
        CSHkVyQa =f"https://ggwave-to-file.ggerganov.com/?m={oRW2Xf2L }{TheoNC5m }"
        wH7AqAX4 ="gibberlink.wav"

        # Lade die WAV-Datei herunter
        os .kxbywlJc (f"curl -sS {CSHkVyQa } --output {wH7AqAX4 }")

        # Prüfe, ob die Datei existiert und abspielbar ist
        if os .ayHNpyHc .FWALjxUH (wH7AqAX4 ):
            try :
                subprocess .tmMPGzS4 (["python","./experimental/gibberlink.py",wH7AqAX4 ])
            except cSNMStEJ as ZpBtrMsb :
                print (f"[Gibberlink] Audio konnte nicht abgespielt werden: {ZpBtrMsb }")
        else :
            print ("[Gibberlink] WAV-Datei wurde nicht erfolgreich heruntergeladen.")
    except cSNMStEJ as zha05Jj5 :
        print (f"[Gibberlink] Fehler beim Senden des Tons: {zha05Jj5 }")
        # Transformer-Architektur
class gkxB41a0 (nn .PhDRCLqM ):
    def ah6yoN9b (self ,FjhY3cRg ,peUS1ece ,Vajzi634 ,y1DOtsiU ,cWhhO0NE ):
        super (gkxB41a0 ,self ).ah6yoN9b ()
        self .lCuWmZPe =nn .neHYlNH0 (FjhY3cRg ,peUS1ece )
        self .toFVZr8n =nn .uB9zuGUt (peUS1ece ,Vajzi634 ,y1DOtsiU )
        self .lQo5rZX5 =nn .x1rFjuUL (peUS1ece ,cWhhO0NE )

    def P3JpdgvA (self ,NarjaLH7 ,vkoA3pA9 ):
        NarjaLH7 =self .lCuWmZPe (NarjaLH7 )
        vkoA3pA9 =self .lCuWmZPe (vkoA3pA9 )
        LTilW4pX =self .toFVZr8n (NarjaLH7 ,vkoA3pA9 )
        LTilW4pX =self .lQo5rZX5 (LTilW4pX )
        return LTilW4pX 

        # Initialisiere das Transformer-Modell
FjhY3cRg =len (PhNrfw9M .WcFWZHc4 )
peUS1ece =512 
Vajzi634 =8 
y1DOtsiU =6 
cWhhO0NE =len (set (Nn8k0Pcv ))
k2UfPDoB =gkxB41a0 (FjhY3cRg ,peUS1ece ,Vajzi634 ,y1DOtsiU ,cWhhO0NE )

if xUhZ2BBG =="2":
    def lygRtLIs (S88WDBxS ):
        try :
            qi3CAJsF =word_tokenize (S88WDBxS )
            NbkEuDzA =[ZKDICO1U .cDSy0EML (HMftzjhV )for HMftzjhV in qi3CAJsF ]
            yBbbXMVs =[dzsQOkZ1 .PSFomR6o (HMftzjhV )for HMftzjhV in qi3CAJsF ]
            lOsegUrA =pos_tag (qi3CAJsF )
            nMBt115Z =ne_chunk (lOsegUrA )
            return {
            "tokens":qi3CAJsF ,
            "stemmed":NbkEuDzA ,
            "lemmatized":yBbbXMVs ,
            "pos_tags":lOsegUrA ,
            "named_entities":nMBt115Z 
            }
        except cSNMStEJ as zha05Jj5 :
            return {"error":str (zha05Jj5 )}
    import LQB5tQtG .Ks4b75dO as plt 

    def mzTwXxAm (keZn5axR ,wH7AqAX4 ="plot.png"):
        try :
        # Beispiel: Parabel zeichnen
            if keZn5axR =="parabel":
                vX4tOO1g =np .DMqOzcYe (-10 ,10 ,400 )
                hJ0SFDra =vX4tOO1g **2 
                plt .iVmWTXLT ()
                plt .io73Uufl (vX4tOO1g ,hJ0SFDra ,HWuoU55v ="y = x^2")
                plt .hRANQ2Jz ("Parabel")
                plt .wQCsqOAe ("x")
                plt .uX9lF7nx ("y")
                plt .W05WBxaw (0 ,jYtS86Xz ='black',U1fZ3F6E =0.5 )
                plt .AxUtvld2 (0 ,jYtS86Xz ='black',U1fZ3F6E =0.5 )
                plt .PpB3wbmu (jYtS86Xz ='gray',SsNFWfzd ='--',U1fZ3F6E =0.5 )
                plt .VbhA44cb ()
                plt .uN48sI3g (wH7AqAX4 )
                plt .CfmMpCG5 ()
                return wH7AqAX4 
            else :
                return None 
        except cSNMStEJ as zha05Jj5 :
            print (f"Fehler beim Generieren der Grafik: {zha05Jj5 }")
            return None 

            # Funktion zur Evaluierung mathematischer Ausdrücke
    def gnAGcrfc (keZn5axR ):
        try :
        # Berechne das Ergebnis
            wxzBnyMC =qQp33AtC (keZn5axR )

            # Visualisiere die Rechenschritte
            wH7AqAX4 =kpWPHqbj (keZn5axR )
            if wH7AqAX4 :
                Ct7FNexI (wH7AqAX4 )

            return f"Das Ergebnis ist: {wxzBnyMC }"
        except cSNMStEJ as zha05Jj5 :
            return f"Fehler beim Auswerten des Ausdrucks: {str (zha05Jj5 )}"
    import re 
    def AkuEP6wY ():
        try :
            os .kxbywlJc ("code")
        except cSNMStEJ as zha05Jj5 :
            print (f"Visual Studio code not installed or not on path; {zha05Jj5 }")
    def f8iD3WCG (AlM3ObRy ):
        AlM3ObRy ="Unimplemented Feature"
        return AlM3ObRy 
    def kpWPHqbj (keZn5axR ,wH7AqAX4 ="calculation_steps.png"):
        try :
        # Zerlege den Ausdruck in Schritte
            lyOFhQgm =[]
            Y3rg1rqB =keZn5axR 

            # Berechne Schritt für Schritt unter Berücksichtigung der Reihenfolge der Operationen
            while True :
            # Finde die innerste Klammer oder den nächsten Operator
                d4lSN8Ku =re .WO5d5GUB (r"\(([^()]+)\)",Y3rg1rqB )# Suche nach Klammern
                if d4lSN8Ku :
                    rSw3iytK =d4lSN8Ku .t9zU5c3Y (1 )
                    wxzBnyMC =qQp33AtC (rSw3iytK )
                    lyOFhQgm .doobb5E7 ((f"{rSw3iytK } = {wxzBnyMC }",wxzBnyMC ))
                    Y3rg1rqB =Y3rg1rqB .H45OlrRo (f"({rSw3iytK })",str (wxzBnyMC ))
                else :
                # Keine Klammern mehr, berechne den Rest
                    wxzBnyMC =qQp33AtC (Y3rg1rqB )
                    lyOFhQgm .doobb5E7 ((f"{Y3rg1rqB } = {wxzBnyMC }",wxzBnyMC ))
                    break 

                    # Erstelle die Grafik
            plt .iVmWTXLT (FyyAbdIF =(10 ,6 ))
            qxh42y4v =range (len (lyOFhQgm ))
            nD0YD0Gx =[KNY9dlN5 [0 ]for KNY9dlN5 in lyOFhQgm ]
            WQSumBTZ =[KNY9dlN5 [1 ]for KNY9dlN5 in lyOFhQgm ]

            plt .v6mg76DW (qxh42y4v ,WQSumBTZ ,jYtS86Xz ='skyblue')
            plt .t7nCYQ9M (qxh42y4v ,nD0YD0Gx )
            plt .wQCsqOAe ("Ergebnisse")
            plt .hRANQ2Jz ("Rechenschritte")
            plt .W3TeveEX ()
            plt .uN48sI3g (wH7AqAX4 )
            plt .CfmMpCG5 ()
            return wH7AqAX4 
        except cSNMStEJ as zha05Jj5 :
            print (f"Fehler bei der Visualisierung der Rechenschritte: {zha05Jj5 }")
            return None 


            # --- NEW: extract measurement snippets from text and try wiki variants ---
    def RhDGw8CL (S88WDBxS ):
        if not S88WDBxS :
            return None 
            # normalize whitespace
        GPB3kh59 =re .RhpHFNfl (r'\s+',' ',S88WDBxS )
        # common unit patterns (DE + EN) and numeric ranges
        Gi0WCP26 =[
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:m|Meter|Metern|meter|metres|meters|cm|Zentimeter|centimeter|km|Millimeter|mm|ft|feet|in|inch|Zoll))',
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:cm|Zentimeter|centimeter))',
        r'(\d{1,4}(?:[.,]\d+)?\s?(?:kg|Kilogramm|g|Gramm|lbs|pounds))',
        r'(\d+(?:[.,]\d+)?\s?[-–]\s?\d+(?:[.,]\d+)?\s?(?:m|cm|ft|in|mm))',
        r'(bis\s+zu\s+\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        r'(etwa\s+\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        r'(~\s?\d+(?:[.,]\d+)?\s?(?:m|cm|kg))',
        ]
        for qQfQXJjx in Gi0WCP26 :
            ce7F8ihw =re .WO5d5GUB (qQfQXJjx ,GPB3kh59 ,TXgGzi08 =re .HR3NKUsR )
            if ce7F8ihw :
                return ce7F8ihw .t9zU5c3Y (1 ).a7Jf2Jef ()
                # phrases like "average/typical length is 4.5 m" (EN/DE)
        ce7F8ihw =re .WO5d5GUB (r'(?:average|typical|mean|durchschnittlich|im Durchschnitt)\s+(?:length|Länge)\s*(?:is|ist|:)?\s*([\d.,]+\s?(?:m|cm|metres|meters|ft|feet|in|inch|Zentimeter|Zoll))',GPB3kh59 ,TXgGzi08 =re .HR3NKUsR )
        if ce7F8ihw :
            return ce7F8ihw .t9zU5c3Y (1 ).a7Jf2Jef ()
            # "length is X m" or "ist X m"
        ce7F8ihw =re .WO5d5GUB (r'(?:length|Länge)\s*(?:is|ist|:)?\s*([\d.,]+\s?(?:m|cm|ft|in|metres|meters|Zentimeter|Zoll))',GPB3kh59 ,TXgGzi08 =re .HR3NKUsR )
        if ce7F8ihw :
            return ce7F8ihw .t9zU5c3Y (1 ).a7Jf2Jef ()
            # fallback: "ist X lang" style
        ce7F8ihw =re .WO5d5GUB (r'ist\s+(?:etwa|ungefähr|ca\.?|circa)?\s*([\d.,\s\-–]+)\s?(m|cm|kg|Meter|Zentimeter|Kilogramm|Zoll|inch|feet)',GPB3kh59 ,TXgGzi08 =re .HR3NKUsR )
        if ce7F8ihw :
            LigivXT1 =ce7F8ihw .t9zU5c3Y (1 ).a7Jf2Jef ().H45OlrRo (' ','')
            lGXRr96w =ce7F8ihw .t9zU5c3Y (2 ).a7Jf2Jef ()
            return f"{LigivXT1 }{lGXRr96w }"
        return None 

        # --- NEW: normalize subject and map common synonyms ---
    def bYuBruKa (DZVneCHo ):
        if not DZVneCHo :
            return None 
            # remove diacritics, collapse whitespace, lowercase
        Wnt0E6Jl =unicodedata .bQNZDLcH ('NFKD',DZVneCHo )
        Wnt0E6Jl =''.Ur57W3x2 (WlqaIkYa for WlqaIkYa in Wnt0E6Jl if not unicodedata .aTmMqIY7 (WlqaIkYa ))
        Wnt0E6Jl =re .RhpHFNfl (r'\s+',' ',Wnt0E6Jl ).a7Jf2Jef ()
        return Wnt0E6Jl 

        # --- REPLACED/EXTENDED: try targeted queries and DuckDuckGo + english variants ---
    def TdIAE9g6 (DZVneCHo ):
        """
        Try multiple queries (wiki variants + targeted 'Länge' queries + DuckDuckGo snippets)
        Return tuple (measurement_string, source_text_short) or (None, None).
        """
        if not DZVneCHo :
            return None ,None 

        rct8xrXw =bYuBruKa (DZVneCHo )
        # build candidate queries (DE + EN) and synonyms
        mAkRzm9T =[]
        # base
        mAkRzm9T .doobb5E7 (DZVneCHo )
        mAkRzm9T .doobb5E7 (rct8xrXw )
        # German targeted forms
        mAkRzm9T +=[
        f"{DZVneCHo } Länge",
        f"Länge {DZVneCHo }",
        f"Durchschnittliche Länge {DZVneCHo }",
        f"Durchschnittliche Länge {rct8xrXw }",
        f"{DZVneCHo } Größe",
        ]
        # synonyms for common terms
        if re .WO5d5GUB (r'\bauto\b',rct8xrXw ,TXgGzi08 =re .HR3NKUsR )or re .WO5d5GUB (r'\bwagen\b',rct8xrXw ,TXgGzi08 =re .HR3NKUsR ):
            mAkRzm9T +=["Auto","Personenkraftwagen","PKW","Durchschnittliche Länge Auto","Durchschnittliche Länge PKW"]
        if re .WO5d5GUB (r'\brüssel\b',rct8xrXw ,TXgGzi08 =re .HR3NKUsR ):
            mAkRzm9T +=["Rüssel","Elefantenrüssel","Rüssel Elefant Länge"]

            # english fallbacks
        mAkRzm9T +=[
        f"{rct8xrXw } length",
        "car length",
        "average car length",
        "typical car length",
        "elephant trunk length",
        "length of elephant trunk"
        ]

        rJ2gWLs1 =set ()
        # try Wikipedia page extracts first (better chance to contain numbers)
        for SPXhR9DM in mAkRzm9T :
            if not SPXhR9DM or SPXhR9DM in rJ2gWLs1 :
                continue 
            rJ2gWLs1 .GQkL2Ww9 (SPXhR9DM )
            try :
                o1sxumh8 =fetch_wikipedia_page_text (SPXhR9DM )
            except cSNMStEJ :
                o1sxumh8 =None 
            if o1sxumh8 :
                evLhRiUd =RhDGw8CL (o1sxumh8 )
                if evLhRiUd :
                    return evLhRiUd ,f"Wikipedia page: {SPXhR9DM }"
                    # fallback to summary if page_text didn't exist
            try :
                ieOz9Xdm =fetch_wikipedia_summary (SPXhR9DM )
            except cSNMStEJ :
                ieOz9Xdm =None 
            if ieOz9Xdm :
                evLhRiUd =RhDGw8CL (ieOz9Xdm )
                if evLhRiUd :
                    return evLhRiUd ,f"Wikipedia summary: {SPXhR9DM }"

                    # also try broader Wikipedia variants (existing helper)
        try :
            UKTSm43J =fetch_wikipedia_variants (DZVneCHo )
        except cSNMStEJ :
            UKTSm43J =None 
        if UKTSm43J :
            evLhRiUd =RhDGw8CL (UKTSm43J )
            if evLhRiUd :
                return evLhRiUd ,"Wikipedia (variant)"

                # lastly try DuckDuckGo search snippets for a few prioritized queries
        for SPXhR9DM in [f"{DZVneCHo } Länge",f"{rct8xrXw } length","durchschnittliche Länge Auto","average car length","elephant trunk length"]:
            try :
                siIAbG8J =f8iD3WCG (SPXhR9DM )
            except cSNMStEJ :
                siIAbG8J =None 
            if siIAbG8J and q0ppYI8C (siIAbG8J ,str ):
                evLhRiUd =RhDGw8CL (siIAbG8J )
                if evLhRiUd :
                    NarjaLH7 ="DuckDuckGo: "+SPXhR9DM 
                    return evLhRiUd ,NarjaLH7 

        return None ,None 

        # Funktion zur Beantwortung von Fragen
    if WCTTp5OA !=False :
        WCTTp5OA ="--gibberlink=true"in sys .GTkGQ75d # oder False, je nach Bedarf


    def jvMUFlSF (kM5rb19z ):
        print (kM5rb19z )
        try :
        # quick math detection: evaluate simple arithmetic expressions even without "Berechne"
        # matches inputs containing digits and math operators (e.g. "2*4", "12 / (3+1)")
            if re .WO5d5GUB (r'\d',kM5rb19z )and re .WO5d5GUB (r'[\+\-\*\/\^()]',kM5rb19z ):
                try :
                # use existing evaluate_math_expression when available
                    wxzBnyMC =gnAGcrfc (kM5rb19z )
                    return wxzBnyMC ,{"tokens":[],"note":"evaluated-as-math"}
                except cSNMStEJ :
                # fallback: continue to NLP if evaluation fails
                    pass 

                    # Gibberlink aktivieren, wenn EXPERIMENTAL-Modus an ist

                    # NEW: Definition/Übersetzungsanfragen (Wortbedeutung)
            if re .WO5d5GUB (r'\bwas\s+bedeutet\b|\bwas\s+heißt\b|\bbedeutung\s+von\b',kM5rb19z ,TXgGzi08 =re .HR3NKUsR ):
                NjSaP5mf =extract_subject_from_question (kM5rb19z )
                if NjSaP5mf :
                # prefer wiktionary, fallback to wikipedia summary/page
                    Ps7L4F2g =fetch_wiktionary_definition (NjSaP5mf )
                    if not Ps7L4F2g :
                    # try wikipedia page text then summary
                        Ps7L4F2g =fetch_wikipedia_page_text (NjSaP5mf )or fetch_wikipedia_summary (NjSaP5mf )
                    if Ps7L4F2g :
                        zxEL1ZP9 =Ps7L4F2g .iyv7rRKx ("\n\n")[0 ].a7Jf2Jef ()
                        return f"'{NjSaP5mf }' bedeutet:\n{zxEL1ZP9 }",{"tokens":[],"note":"dictionary"}
                return "Dazu konnte ich leider keine Definition finden.",{"tokens":[],"note":"no-definition"}

                # REPLACED: improved measurement question handling
            if re .WO5d5GUB (r'\bwie\s+(lang|groß|hoch|schwer|alt)\b',kM5rb19z ,TXgGzi08 =re .HR3NKUsR ):
                DZVneCHo =extract_subject_from_question (kM5rb19z )
                # first try direct wiki variants (keeps previous behavior)
                ieOz9Xdm =fetch_wikipedia_variants (DZVneCHo )if DZVneCHo else None 
                if ieOz9Xdm :
                    evLhRiUd =RhDGw8CL (ieOz9Xdm )
                    if evLhRiUd :
                        Ft6DioTB =DZVneCHo or "das Objekt"
                        return f"Der {Ft6DioTB } ist ungefähr {evLhRiUd }. (Quelle: Wikipedia)",{"tokens":[],"note":"wikipedia-measurement"}
                        # if initial wiki summary didn't contain measurement, do targeted search attempts
                evLhRiUd ,tpbABkOC =TdIAE9g6 (DZVneCHo )
                if evLhRiUd :
                    Ft6DioTB =DZVneCHo or "das Objekt"
                    return f"Der {Ft6DioTB } ist ungefähr {evLhRiUd }. (Quelle: {tpbABkOC })",{"tokens":[],"note":"web-measurement"}
                    # fallback: if we had a wiki without measurement, return it (better than nothing)
                if ieOz9Xdm :
                    Ft6DioTB =DZVneCHo or "das Objekt"
                    return f"Ich habe zu '{Ft6DioTB }' folgende Info auf Wikipedia gefunden:\n{ieOz9Xdm }",{"tokens":[],"note":"wikipedia-summary"}
                    # nothing found -> fall back to general NLP below (or inform about missing data)
                return "Dazu habe ich leider keine eindeutige Längenangabe gefunden.",{"tokens":[],"note":"no-measurement"}

                # Mathematischer Ausdruck
            if kM5rb19z .HhilkCTN ("Berechne"):
                keZn5axR =kM5rb19z .iyv7rRKx ("Berechne")[-1 ].a7Jf2Jef ()
                return gnAGcrfc (keZn5axR ),None 

                # VS Code öffnen
            if kM5rb19z .U5nWvn2z ()in ["öffne vs code","code"]:
                return AkuEP6wY (),None 

                # Websuche
            if kM5rb19z .U5nWvn2z ().HhilkCTN ("suche nach"):
                AlM3ObRy =kM5rb19z .iyv7rRKx ("suche nach")[-1 ].a7Jf2Jef ()
                return f8iD3WCG (AlM3ObRy ),None 

                # Begrüßung
            TOqJSJpK =["hallo","hi","hey","guten tag"]
            if kM5rb19z .U5nWvn2z ()in TOqJSJpK :
                return "Hallo! Wie kann ich Ihnen helfen?",None 

                # NLP-Modell
            Xs57viX4 =PhNrfw9M .Z9SJXU62 ([kM5rb19z ])
            ml6RKLU8 =EMBSQEYY .RiDsRpcW (Xs57viX4 )[0 ]
            szWQHe22 =lygRtLIs (kM5rb19z )

            # Try to enrich the model response with a deterministic Wikipedia summary
            try :
                DZVneCHo =extract_subject_from_question (kM5rb19z )
                # do not attempt wiki if subject extraction failed (or was math)
                ieOz9Xdm =fetch_wikipedia_summary (DZVneCHo )if DZVneCHo else None 
                if ieOz9Xdm :
                # append but avoid duplicating if already included
                    if q0ppYI8C (ml6RKLU8 ,str )and "[Wikipedia]"not in ml6RKLU8 :
                        ml6RKLU8 =(ml6RKLU8 or "")+"\n\n[Wikipedia]: "+ieOz9Xdm 
            except cSNMStEJ :
            # degrade gracefully: return model response without augmentation
                pass 

            return ml6RKLU8 ,szWQHe22 

        except cSNMStEJ as zha05Jj5 :
            return f"Fehler bei der Verarbeitung der Frage: {str (zha05Jj5 )}",None 

            # Funktion zum Hinzufügen von neuen Fragen und Antworten
    def VDnzrz5x (kM5rb19z ,StnvenMh ,VQvJrbG5 ='training_data.json'):
        global M2Hh8fZ5 
        owzkQFZZ ={"question":kM5rb19z ,"answer":StnvenMh }
        M2Hh8fZ5 .doobb5E7 (owzkQFZZ )

        with open (VQvJrbG5 ,'w',CRUnEl63 ='utf-8')as MqSh5AI9 :
            json .iLInbVbA (M2Hh8fZ5 ,MqSh5AI9 ,wUcxemLG =False ,NTQbC6gK =4 )

            # Modelle neu trainieren
        atF4OP0L =[data ['question']for data in M2Hh8fZ5 ]
        vLHJvwrW =PhNrfw9M .ZYEcnWbh (atF4OP0L )
        Nn8k0Pcv =[data ['answer']for data in M2Hh8fZ5 ]
        EMBSQEYY .buB84FUI (vLHJvwrW ,Nn8k0Pcv )

        # Automatisches Lernen aus Interaktionen
    def Ze5TuZxv (IxuwGddD ,lekyAM1L ):
        VDnzrz5x (IxuwGddD ,lekyAM1L )
    from Q2GELjuH .ICwpXbTo import QLabel ,QVBoxLayout ,QDialog 
    from Q2GELjuH .IEiLuJjn import QPixmap 

    def Ct7FNexI (wH7AqAX4 ):
        z5FIUc41 =QDialog ()
        z5FIUc41 .az1YgNku ("Mathematische Grafik")
        lcwzet4d =QVBoxLayout ()
        HWuoU55v =QLabel ()
        aAfi8Blo =QPixmap (wH7AqAX4 )
        HWuoU55v .FL1RoBWd (aAfi8Blo )
        lcwzet4d .C2nfncvq (HWuoU55v )
        z5FIUc41 .f41Tzgg8 (lcwzet4d )
        z5FIUc41 .tf1UWcwd ()

        # Funktion zur Überprüfung und Verbesserung der Antwort
    def n6waMOw2 (IxuwGddD ,ml6RKLU8 ):
        print (f"Chatbot: {ml6RKLU8 }")
        r2DLMiBV =input ("War die Antwort korrekt? (ja/nein): ").a7Jf2Jef ().U5nWvn2z ()
        if r2DLMiBV =="nein":
            KG2cCIJP =input ("Wie hätte ich antworten sollen? ")
            Ze5TuZxv (IxuwGddD ,KG2cCIJP )
            return KG2cCIJP 
        return ml6RKLU8 

        # Chatbot testen
    if __name__ =="__main__":
        while True :
            IxuwGddD =input ("Du: ")
            if IxuwGddD .U5nWvn2z ()in ["exit","quit"]:
                break 
            elif IxuwGddD .U5nWvn2z ().HhilkCTN ("zeige mir eine parabel"):
                wH7AqAX4 =mzTwXxAm ("parabel")
                if wH7AqAX4 :
                    Ct7FNexI (wH7AqAX4 )
                    print ("Hier ist die Grafik der Parabel.")
                    continue # Springe zur nächsten Eingabe

            ml6RKLU8 ,szWQHe22 =jvMUFlSF (IxuwGddD )

            if ml6RKLU8 is None :
                print ("Ich habe deine Frage nicht verstanden. Wie sollte ich darauf antworten?")
                tL3FHi2M =input ("Neue Antwort: ")
                Ze5TuZxv (IxuwGddD ,tL3FHi2M )
                ml6RKLU8 =tL3FHi2M 
            else :
                ml6RKLU8 =n6waMOw2 (IxuwGddD ,ml6RKLU8 )

            print ("Chatbot:",ml6RKLU8 )
            if WCTTp5OA :
                i8J558rV (ml6RKLU8 )
                print ("Gibberlink-Signal gesendet.",None )
            print ("NLP Info:",szWQHe22 )

elif xUhZ2BBG =="1":
    while True :
        lsoitAWS =input ("Enter your message: ")
        bp7OizdP =k8He7Z74 .oS0fDSva .IQmlzL6g .b8lCeJvT (
        nmipiKIg =[
        {
        "role":"user",
        "content":lsoitAWS ,
        }
        ],
        EMBSQEYY ="llama-3.3-70b-versatile",
        )

        print (bp7OizdP .NugwVlba [0 ].texpcdCM .XT2A2wnr )