
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
        github_url = "https://raw.githubusercontent.com/Gymnasium-Freiham/LATIN-AI/main/deobfuscation_mappings.txt"
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

import os 
import sys 
import winreg 
import subprocess 
import tempfile 
import shutil 
import webbrowser 
from nqXEThRb .IzLfqPhP import urlparse ,parse_qs 
import socket 

# Prüfen, ob der Parameter --no-connection übergeben wurde
o7QwRe9L ="--no-connection"in sys .rSETkpLu 
nO6bLYOj ="--gibberlink=true"in sys .rSETkpLu # oder False, je nach Bedarf
# Setze eine Umgebungsvariable, die von anderen Skripten gelesen werden kann
if o7QwRe9L :
    os .j6r11yXV ["NO_CONNECTION"]="1"
else :
    os .j6r11yXV ["NO_CONNECTION"]="0"
def VexFXKBy (X1jHHXJW ):
    if o7QwRe9L :
    # no network allowed
        return 
    try :
    # suppress pip output to avoid spamming the console
        subprocess .AXdlh0B5 ([sys .u7H9XNbY ,"-m","pip","install",X1jHHXJW ],
        IdmoTvU2 =subprocess .S3hzns5P ,lZdjfI07 =subprocess .S3hzns5P ,ddahA8pU =True )
    except subprocess .eKzn19Jf :
    # ignore install errors here; caller can handle logging if needed
        pass 


def biNUVCm4 (wlPcsW3t =3 ):
    try :
    # Versuche, eine Verbindung zu einem bekannten Server (Google DNS)
        socket .bUwd6gdt (wlPcsW3t )
        socket .socket (socket .bM9YyjJi ,socket .paFl41ll ).N9DXeMHY (("8.8.8.8",53 ))
        return True 
    except socket .F6WlIOB7 :
        return False 
try :
    import PyQt5 
except ItjSBkbL :
    VexFXKBy ("PyQt5")
try :
    import requests 
except ItjSBkbL :
    VexFXKBy ("requests")
try :
    import Flask 
except ItjSBkbL :
    VexFXKBy ("Flask")
try :
    import Flask_CORS 
except ItjSBkbL :
    VexFXKBy ("Flask-CORS")
from PyQt5 .UZO4LydB import QApplication ,QWidget ,QVBoxLayout ,QPushButton ,QLabel ,QHBoxLayout ,QTextEdit ,QMessageBox ,QCheckBox ,QSystemTrayIcon ,QMenu ,QAction ,QComboBox ,QFormLayout ,QGroupBox ,QInputDialog ,QProgressBar ,QFileDialog 
from PyQt5 .i2UqSIbE import QPixmap ,QFont ,QPalette ,QColor ,QIcon ,QMovie 
from PyQt5 .eUwgik3R import QProcess ,Qt ,QTimer ,QEvent ,QThread ,pyqtSignal 
import requests 

class QvyJqCAQ (QThread ):
    jFahCc91 =pyqtSignal (int )# Signal für Fortschrittsaktualisierung
    fEXvzaYd =pyqtSignal ()# Signal, wenn die Installation abgeschlossen ist

    def AXdlh0B5 (self ):
        AIuuISIf =["PyQt5","requests","Flask","Flask-CORS"]
        lmFeCvSc =len (AIuuISIf )
        for Mv59qCND ,X1jHHXJW in enumerate (AIuuISIf ,eSC2FBru =1 ):
            if o7QwRe9L :
            # skip network installs
                pass 
            else :
                try :
                    subprocess .AXdlh0B5 ([sys .u7H9XNbY ,"-m","pip","install",X1jHHXJW ],
                    IdmoTvU2 =subprocess .S3hzns5P ,lZdjfI07 =subprocess .S3hzns5P ,ddahA8pU =True )
                except Lj5pt76l as o8pWbs3W :
                # don't spam UI; keep silent on install failures here
                    pass 
            o8NtIjBD =int ((Mv59qCND /lmFeCvSc )*100 )
            self .jFahCc91 .Z1TTnM7m (o8NtIjBD )# Fortschritt aktualisieren
        self .fEXvzaYd .Z1TTnM7m ()# Installation abgeschlossen

def sIDln7zr ():
    try :
        with winreg .akEGgwrm (winreg .CVq7ZJwG ,r"Software\Classes\mintai")as DkTPwTL6 :
            winreg .ky4fku6w (DkTPwTL6 ,"",0 ,winreg .wToA47fX ,"URL:mintai Protocol")
            winreg .ky4fku6w (DkTPwTL6 ,"URL Protocol",0 ,winreg .wToA47fX ,"")
        with winreg .akEGgwrm (winreg .CVq7ZJwG ,r"Software\Classes\mintai\shell\open\command")as DkTPwTL6 :
            winreg .ky4fku6w (DkTPwTL6 ,"",0 ,winreg .wToA47fX ,f'"{sys .u7H9XNbY }" "{os .JPfx64Lg .SRdrbrcP (YjzH58Sz )}" "%1"')
        print ("URL-Schema 'mintai' erfolgreich registriert")
    except Lj5pt76l as o8pWbs3W :
        print (f"Fehler beim Registrieren des URL-Schemas: {o8pWbs3W }")


def heoI2KbG (tRKitmB4 ):
    aPxi8ugY =urlparse (tRKitmB4 )
    if aPxi8ugY .eNj05c7T =='mintai'and aPxi8ugY .g0H2HzQy =='install-addon':
        qGZD08hc =parse_qs (aPxi8ugY .gIBf0baO )
        ZP2JcAkt =qGZD08hc .ubVPTDTG ('url',[None ])[0 ]
        if ZP2JcAkt :
            vn0b5nev .Fs2OrU40 .PcYCPh6d (ZP2JcAkt )

def KKngWwoB ():
    ASAcw53o =os .JPfx64Lg .Mp2xTuqg (os .JPfx64Lg .zUz5SSCN (YjzH58Sz ),'./browser-powered/addon_store.html')
    webbrowser .open (f'file://{ASAcw53o }')

def bmqAAGwP (RXeXPJwg ):
    if os .JPfx64Lg .vKWh1kg6 (RXeXPJwg ):
        with open (RXeXPJwg ,'r')as R9NmOejV :
            r2GBbOMt (R9NmOejV .RRIXzGPt (),iqXLXabq ())
    else :
        print (f"Addon {RXeXPJwg } nicht gefunden")

def UyketVbt (od0BLcYp ):
    if os .JPfx64Lg .vKWh1kg6 (od0BLcYp )and os .JPfx64Lg .lSFC17BY (od0BLcYp ):
        for gPas0E6Q in os .uriYUxu0 (od0BLcYp ):
            RXeXPJwg =os .JPfx64Lg .Mp2xTuqg (od0BLcYp ,gPas0E6Q )
            # executable addon (python) -> execute for effects
            if gPas0E6Q .eLjKtzok ('.mintaiaddon'):
                try :
                    bmqAAGwP (RXeXPJwg )
                except Lj5pt76l as o8pWbs3W :
                    print (f"Fehler beim Ausführen des Addons {gPas0E6Q }: {o8pWbs3W }")
                    # dataset files (.json) are intentionally left for main.py to pick up at startup
            elif gPas0E6Q .eLjKtzok ('.json'):
                print (f"Gefundenes Datenset-Addon (wird beim Programmstart von main.py verarbeitet): {gPas0E6Q }")
    else :
        print (f"Addons-Verzeichnis {od0BLcYp } nicht gefunden oder ist kein Verzeichnis")

def V0nSNi1x ():
    try :
        with winreg .FkoZfelO (winreg .CVq7ZJwG ,r"Software\LATIN AI")as DkTPwTL6 :
            ZWhILNlY ,e9h49Z9p =winreg .OPSnK0HZ (DkTPwTL6 ,"InstallDir")
            return ZWhILNlY 
    except peuJKTuV :
        print ("Installationsverzeichnis nicht gefunden")
        return None 

def mekOLFLE (ZWhILNlY ):
    if ZWhILNlY :
        os .r9eKo6Zo (ZWhILNlY )
        print (f"Arbeitsverzeichnis erfolgreich zu {ZWhILNlY } gewechselt")
    else :
        print ("Fehler beim Wechseln des Arbeitsverzeichnisses")


def BIEZboza (DkTPwTL6 ,fkNctKXg ,N58bcOxF =None ):
    try :
        with winreg .FkoZfelO (winreg .CVq7ZJwG ,DkTPwTL6 )as LdSP8mz9 :
            QQvhQCtG ,e9h49Z9p =winreg .OPSnK0HZ (LdSP8mz9 ,fkNctKXg )
            return QQvhQCtG 
    except peuJKTuV :
        return N58bcOxF 
def hm1JdrA4 (DkTPwTL6 ,fkNctKXg ,BRnHGUK1 ):
    with winreg .akEGgwrm (winreg .CVq7ZJwG ,DkTPwTL6 )as LdSP8mz9 :
        winreg .ky4fku6w (LdSP8mz9 ,fkNctKXg ,0 ,winreg .wToA47fX ,BRnHGUK1 )

class f53csAKa (QWidget ):
    def m9kouxi5 (self ):
        super ().m9kouxi5 ()
        self .FBlQYaLb =None # Initialisiere self.movie als Instanzattribut
        self .GHJHyTHw ()
        self .oZQFsbPH =QvyJqCAQ ()
        self .oZQFsbPH .jFahCc91 .N9DXeMHY (self .Er49JA56 )
        self .oZQFsbPH .fEXvzaYd .N9DXeMHY (self .S79EfBaD )

    def GHJHyTHw (self ):
        self .cnIG8pmI ('Laden...')
        self .Fat2LSr1 ()# Ladebildschirm im Vollbildmodus anzeigen

        u8DZn2D1 =QVBoxLayout ()

        # Ladebalken
        self .v75BeZgD =QProgressBar (self )
        self .v75BeZgD .issvLooE (0 ,100 )
        u8DZn2D1 .WDQ4fgvP (self .v75BeZgD )

        # Animiertes Logo
        self .d0i26QZA =QLabel (self )
        self .FBlQYaLb =QMovie ("./logo.gif")# Initialisiere das QMovie-Objekt
        self .d0i26QZA .ctauWoE8 (self .FBlQYaLb )
        self .d0i26QZA .pZ3mEbJA (Qt .JilvCLL2 )# Zentriere das GIF
        u8DZn2D1 .WDQ4fgvP (self .d0i26QZA )

        self .zwWu3qCq (u8DZn2D1 )

        self .FBlQYaLb .eSC2FBru ()

    def V1xfYsZz (self ,co7utjg9 ):
        """Skaliere das GIF und das QLabel, wenn das Fenster die Größe ändert."""
        if self .FBlQYaLb :# Überprüfe, ob self.movie korrekt initialisiert wurde
            TgF6b03B =self .TgF6b03B ()# Verwende die Fenstergröße
            self .d0i26QZA .xhjzw0pi (TgF6b03B )# Passe die Größe des QLabel an
            self .FBlQYaLb .Dxj6iA3O (TgF6b03B )# Passe die Größe des GIFs an das QLabel an
        super ().V1xfYsZz (co7utjg9 )

    def IvGcr1V4 (self ):
        self .oZQFsbPH .eSC2FBru ()

    def Er49JA56 (self ,fkNctKXg ):
        self .v75BeZgD .KhC8swBN (fkNctKXg )

    def S79EfBaD (self ):
        self .B3TY5yfi ()
        self .bBYD4Ghs ()

    def bBYD4Ghs (self ):
        self .J0oeMsG7 =iZCtyAwK ()
        self .J0oeMsG7 .uKAJuLuu ()


class iZCtyAwK (QWidget ):
    def m9kouxi5 (self ):
        super ().m9kouxi5 ()
        self .GHJHyTHw ()
        self .ru9x7EOV ()
        self .JaoGnSkH =[]
        # track a short-lived launch state to avoid rapid repeated clicks
        self .KkljP4Lf =False 
        vn0b5nev .B1NBpNJx (self )

    def GHJHyTHw (self ):
        self .cnIG8pmI ('LATIN AI Launcher')
        self .fyGAgCzg (100 ,100 ,800 ,600 )

        # Hintergrundfarbe
        self .yjPSv7u1 (True )
        D6lLuAAQ =self .D6lLuAAQ ()
        D6lLuAAQ .guSwfGNB (QPalette .udbdOKNr ,QColor (50 ,50 ,50 ))
        self .OdhfT4lc (D6lLuAAQ )

        # Layout
        u8DZn2D1 =QVBoxLayout ()

        # Logo (falls vorhanden)
        self .AN8mJE2Z =QLabel (self )
        self .jc469RiC =QPixmap ("./logo.png")
        self .jc469RiC =self .jc469RiC .L8gAQmFH (200 ,200 ,Qt .UFAuO8wW ,Qt .Tof9jrAQ )
        self .AN8mJE2Z .bVRz6Q05 (self .jc469RiC )
        self .AN8mJE2Z .pZ3mEbJA (Qt .JilvCLL2 )
        u8DZn2D1 .WDQ4fgvP (self .AN8mJE2Z )

        # Titel
        self .x1VVm3Ix =QLabel ('Welcome to LATIN AI Launcher!',self )
        self .x1VVm3Ix .pZ3mEbJA (Qt .JilvCLL2 )
        self .x1VVm3Ix .UBsDB1rP (QFont ('Arial',24 ))
        self .x1VVm3Ix .fO2rS123 ("color: white;")
        u8DZn2D1 .WDQ4fgvP (self .x1VVm3Ix )


        # Button zum Starten des Hauptprogramms
        self .jVlas015 =QPushButton ('Start LATIN AI',self )
        self .jVlas015 .UBsDB1rP (QFont ('Arial',18 ))
        self .jVlas015 .fO2rS123 ("background-color: green; color: white; padding: 10px;")
        self .jVlas015 .IzZWCbPb .N9DXeMHY (self .FqTzbEa9 )
        u8DZn2D1 .WDQ4fgvP (self .jVlas015 )

        # Button zum Suchen von Updates
        self .uMznDgx5 =QPushButton ('Updates suchen',self )
        self .uMznDgx5 .UBsDB1rP (QFont ('Arial',18 ))
        self .uMznDgx5 .fO2rS123 ("background-color: blue; color: white; padding: 10px;")
        self .uMznDgx5 .IzZWCbPb .N9DXeMHY (self .COJrGyhB )
        u8DZn2D1 .WDQ4fgvP (self .uMznDgx5 )

        # Button zum Beenden
        self .ugqr2poM =QPushButton ('Beenden',self )
        self .ugqr2poM .UBsDB1rP (QFont ('Arial',18 ))
        self .ugqr2poM .fO2rS123 ("background-color: red; color: white; padding: 10px;")
        self .ugqr2poM .IzZWCbPb .N9DXeMHY (self .B3TY5yfi )
        u8DZn2D1 .WDQ4fgvP (self .ugqr2poM )

        # Button zum Installieren eines Addons
        self .TszqEhfA =QPushButton ('Addon installieren',self )
        self .TszqEhfA .UBsDB1rP (QFont ('Arial',18 ))
        self .TszqEhfA .fO2rS123 ("background-color: purple; color: white; padding: 10px;")
        self .TszqEhfA .IzZWCbPb .N9DXeMHY (self .CB6lIHnJ )
        u8DZn2D1 .WDQ4fgvP (self .TszqEhfA )

        # Button zum Öffnen des Addon-Stores
        self .VxIdTxcF =QPushButton ('Addon Store öffnen',self )
        self .VxIdTxcF .UBsDB1rP (QFont ('Arial',18 ))
        self .VxIdTxcF .fO2rS123 ("background-color: orange; color: white; padding: 10px;")
        self .VxIdTxcF .IzZWCbPb .N9DXeMHY (KKngWwoB )
        u8DZn2D1 .WDQ4fgvP (self .VxIdTxcF )

        # Entwickleroptionen
        self .BLPSH4Oe =QGroupBox ("Entwickleroptionen")
        self .BV2Yv9od =QFormLayout ()

        self .OKgWCilx =QCheckBox ("Updates verhindern",self )
        self .OKgWCilx .YHXv5ROp .N9DXeMHY (self .hfiJPiZG )
        self .BV2Yv9od .PoMEmaSQ (self .OKgWCilx )

        self .z34JFMH9 =QCheckBox ("Schnellzugriffslogos deaktivieren",self )
        self .z34JFMH9 .YHXv5ROp .N9DXeMHY (self .hfiJPiZG )
        self .BV2Yv9od .PoMEmaSQ (self .z34JFMH9 )

        self .kPVyLvZJ =QCheckBox ("Gibberlink aktivieren",self )
        self .kPVyLvZJ .YHXv5ROp .N9DXeMHY (self .hfiJPiZG )
        self .BV2Yv9od .PoMEmaSQ (self .kPVyLvZJ )

        self .p5hVuC81 =QPushButton ("Uninstall LATIN-AI Launcher",self )
        self .p5hVuC81 .IzZWCbPb .N9DXeMHY (self .VQu0WrDf )
        self .BV2Yv9od .PoMEmaSQ (self .p5hVuC81 )

        # Button zum Deinstallieren eines Addons
        self .CWh1gPCL =QPushButton ('Addon deinstallieren',self )
        self .CWh1gPCL .UBsDB1rP (QFont ('Arial',18 ))
        self .CWh1gPCL .fO2rS123 ("background-color: red; color: white; padding: 5px;")
        self .CWh1gPCL .IzZWCbPb .N9DXeMHY (self .EgEAzKeU )
        self .BV2Yv9od .PoMEmaSQ (self .CWh1gPCL )

        self .BLPSH4Oe .zwWu3qCq (self .BV2Yv9od )
        u8DZn2D1 .WDQ4fgvP (self .BLPSH4Oe )

        # Textbereich für Ausgabe
        self .sM11NZjy =QTextEdit (self )
        self .sM11NZjy .tEtYmSrC (True )
        self .sM11NZjy .fO2rS123 ("background-color: black; color: white;")
        u8DZn2D1 .WDQ4fgvP (self .sM11NZjy )

        # Setze Layout
        u8DZn2D1 .pZ3mEbJA (Qt .JilvCLL2 )
        self .zwWu3qCq (u8DZn2D1 )

    def EgEAzKeU (self ):
        ZWhILNlY =V0nSNi1x ()
        od0BLcYp =os .JPfx64Lg .Mp2xTuqg (ZWhILNlY ,'addons')
        if not os .JPfx64Lg .vKWh1kg6 (od0BLcYp ):
            QMessageBox .C0ghuzQh (self ,"Fehler","Keine Addons installiert.")
            return 

        hRXCD9bu =[DJPFjl2a for DJPFjl2a in os .uriYUxu0 (od0BLcYp )if DJPFjl2a .eLjKtzok ('.mintaiaddon')]
        if not hRXCD9bu :
            QMessageBox .C0ghuzQh (self ,"Fehler","Keine Addons installiert.")
            return 

        vm7iEMLd ,yyoswvKs =QInputDialog .ytAbjJoc (self ,"Addon deinstallieren","Wählen Sie ein Addon aus:",hRXCD9bu ,0 ,False )
        if yyoswvKs and vm7iEMLd :
            RXeXPJwg =os .JPfx64Lg .Mp2xTuqg (od0BLcYp ,vm7iEMLd )
            try :
                os .YCp2H442 (RXeXPJwg )
                self .sM11NZjy .XltUx6jP (f"Addon {vm7iEMLd } erfolgreich deinstalliert.")
            except Lj5pt76l as o8pWbs3W :
                QMessageBox .mtYtSnMl (self ,"Fehler",f"Fehler beim Deinstallieren des Addons: {o8pWbs3W }")


                # System Tray Icon erstellen
        self .VDUmbFwe =QSystemTrayIcon (self )
        self .VDUmbFwe .T7PUKPC8 (QIcon ("./logo.png"))

        # System Tray Icon Menü erstellen
        bEQrmxd1 =QMenu (self )
        oRekQjLq =QAction ("Show",self )
        rCBTo3Yl =QAction ("Quit",self )
        oRekQjLq .HgasgHej .N9DXeMHY (self .uKAJuLuu )
        rCBTo3Yl .HgasgHej .N9DXeMHY (QApplication .XZTHqK29 ().ItSR2c9G )
        bEQrmxd1 .sQ9jQ81U (oRekQjLq )
        bEQrmxd1 .sQ9jQ81U (rCBTo3Yl )
        self .VDUmbFwe .XUJ10Hp6 (bEQrmxd1 )

        # System Tray Icon anzeigen
        self .VDUmbFwe .uKAJuLuu ()

        # QProcess zum Ausführen des Skripts
        self .fssnxNvy =QProcess (self )
        self .fssnxNvy .GozG0AwG .N9DXeMHY (self .aoRdMEpt )
        self .fssnxNvy .HDRB7N2o .N9DXeMHY (self .KZOhXSPV )

    def CB6lIHnJ (self ):
        rr2rJ30g ,yyoswvKs =QInputDialog .cBl298Fv (self ,"Addon installieren","Haben Sie ein Addon heruntergeladen? (ja/nein)")
        if yyoswvKs and rr2rJ30g .UXbKQFp9 ()=='ja':
            b3xTSqFx =QFileDialog .vgH2iucU ()
            b3xTSqFx |=QFileDialog .ABwNoy8Q 
            gPas0E6Q ,e9h49Z9p =QFileDialog .vyQ74GcZ (self ,"Addon auswählen","","Addon Dateien (*.mintaiaddon *.json);;Alle Dateien (*)",b3xTSqFx =b3xTSqFx )
            if gPas0E6Q :
            # copy selected file into the install's addons directory
                ZWhILNlY =V0nSNi1x ()or os .yZrEe7r7 ()
                od0BLcYp =os .JPfx64Lg .Mp2xTuqg (ZWhILNlY ,'addons')
                os .AIWYqlxQ (od0BLcYp ,H5fjSFdd =True )
                cxzLzA6R =os .JPfx64Lg .Mp2xTuqg (od0BLcYp ,os .JPfx64Lg .YjowrUz1 (gPas0E6Q ))
                try :
                    shutil .d9Vov5pc (gPas0E6Q ,cxzLzA6R )
                    self .JaoGnSkH .XltUx6jP (cxzLzA6R )
                    self .sM11NZjy .XltUx6jP (f"Addon {gPas0E6Q } wurde nach {od0BLcYp } kopiert und wird beim nächsten Start verarbeitet.")
                except Lj5pt76l as o8pWbs3W :
                    QMessageBox .mtYtSnMl (self ,"Fehler",f"Fehler beim Installieren des Addons: {o8pWbs3W }")
        else :
        # Auswahl zwischen den vorgegebenen Addons
            vm7iEMLd ,yyoswvKs =QInputDialog .ytAbjJoc (self ,"Addon auswählen","Wählen Sie ein Addon aus:",["Blackbig","Blueforever","Dark","Light","Blue","Green","Red"],0 ,False )
            if yyoswvKs and vm7iEMLd :
                if vm7iEMLd =="Blackbig":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-blackbig/addon-newstyle.mintaiaddon"
                elif vm7iEMLd =="Blueforever":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-blueforever/addon-newstyle.mintaiaddon"
                elif vm7iEMLd =="Dark":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-dark/addon-newstyle.mintaiaddon"
                elif vm7iEMLd =="Light":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-light/addon-newstyle.mintaiaddon"
                elif vm7iEMLd =="Blue":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-blue/addon-newstyle.mintaiaddon"
                elif vm7iEMLd =="Green":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-green/addon-newstyle.mintaiaddon"
                elif vm7iEMLd =="Red":
                    tRKitmB4 ="https://raw.githubusercontent.com/Gymnasium-Freiham/MINT-AI-Addons/refs/heads/main/style-red/addon-newstyle.mintaiaddon"
                self .PcYCPh6d (tRKitmB4 )

    def PcYCPh6d (self ,tRKitmB4 ):
        try :
            sX48kxyP =requests .ubVPTDTG (tRKitmB4 )
            sX48kxyP .iuonvK5Z ()
            eyaiyRDm =sX48kxyP .N65ONgFQ 
            ZWhILNlY =V0nSNi1x ()or os .yZrEe7r7 ()
            od0BLcYp =os .JPfx64Lg .Mp2xTuqg (ZWhILNlY ,'addons')
            if not os .JPfx64Lg .vKWh1kg6 (od0BLcYp ):
                os .AIWYqlxQ (od0BLcYp )
            JPgi3Ccu =os .JPfx64Lg .YjowrUz1 (tRKitmB4 )
            RXeXPJwg =os .JPfx64Lg .Mp2xTuqg (od0BLcYp ,JPgi3Ccu )
            with open (RXeXPJwg ,'w',EFkVDfiY ='utf-8')as R9NmOejV :
                R9NmOejV .ddSDd0Gn (eyaiyRDm )
            self .JaoGnSkH .XltUx6jP (RXeXPJwg )
            self .sM11NZjy .XltUx6jP (f"Addon von {tRKitmB4 } erfolgreich heruntergeladen und nach {od0BLcYp } gespeichert.")
            # if it is a dataset (json) inform user; main.py will pick it up on next start or when started now
            if JPgi3Ccu .UXbKQFp9 ().eLjKtzok ('.json'):
                QMessageBox .TH7j53DR (self ,"Addon installiert",f"Datendatei {JPgi3Ccu } wurde in {od0BLcYp } installiert. Starte das Hauptprogramm, um sie zu laden.")
            else :
            # start main program immediately as before
                self .FqTzbEa9 ()
        except requests .u0OYcPbE as o8pWbs3W :
            QMessageBox .mtYtSnMl (self ,"Fehler",f"Fehler beim Herunterladen des Addons: {o8pWbs3W }")



    def k3sHPD3U (self ,MYOBEVuI ):
    # Beispiel: Ändern Sie die Hintergrundfarbe basierend auf dem geladenen Addon
        if "blueforever"in MYOBEVuI .UXbKQFp9 ():
            D6lLuAAQ =self .D6lLuAAQ ()
            D6lLuAAQ .guSwfGNB (QPalette .udbdOKNr ,QColor (0 ,0 ,255 ))# Blau
            self .OdhfT4lc (D6lLuAAQ )
        elif "blackbig"in MYOBEVuI .UXbKQFp9 ():
            D6lLuAAQ =self .D6lLuAAQ ()
            D6lLuAAQ .guSwfGNB (QPalette .udbdOKNr ,QColor (0 ,0 ,0 ))# Schwarz
            self .OdhfT4lc (D6lLuAAQ )
            # Fügen Sie hier weitere Addon-Effekte hinzu

    def y6febiUQ (self ,co7utjg9 ):
    # Temporäre Addon-Dateien löschen
        for kHrbsuaD in self .JaoGnSkH :
            try :
                os .YCp2H442 (kHrbsuaD )
            except Do0zOcTP as o8pWbs3W :
                print (f"Fehler beim Löschen der temporären Datei {kHrbsuaD }: {o8pWbs3W }")
        co7utjg9 .Aefo1Cnj ()

    def jLjDSp7W (BfOA7FiH ):
        vn0b5nev .Fs2OrU40 =BfOA7FiH 
        vn0b5nev .Fs2OrU40 .uKAJuLuu ()

    def Vr2xkq4u (self ,sYNIBL9r ,co7utjg9 ):
        if co7utjg9 .type ()==QEvent .pA7cG6Od :
            tRKitmB4 =co7utjg9 .tRKitmB4 ().Hjc8SWUp ()
            heoI2KbG (tRKitmB4 )
            return True 
        return super ().Vr2xkq4u (sYNIBL9r ,co7utjg9 )

    def VQu0WrDf (self ):
        bJGYhtkq =QMessageBox .pC1q1fOo (self ,'Bestätigung',
        'Sind Sie sicher, dass der LATIN-AI-Launcher deinstalliert werden soll?',
        QMessageBox .zP2mfS4W |QMessageBox .HHs1nQG6 ,QMessageBox .HHs1nQG6 )

        if bJGYhtkq ==QMessageBox .zP2mfS4W :
            bJGYhtkq =QMessageBox .pC1q1fOo (self ,'Bestätigung',
            'Sind Sie wirklich sicher, dass der LATIN-AI-Launcher deinstalliert werden soll?',
            QMessageBox .zP2mfS4W |QMessageBox .HHs1nQG6 ,QMessageBox .HHs1nQG6 )

            if bJGYhtkq ==QMessageBox .zP2mfS4W :
                bJGYhtkq =QMessageBox .pC1q1fOo (self ,'Bestätigung',
                'Ist es sicher Ihre letzte Entscheidung?',
                QMessageBox .zP2mfS4W |QMessageBox .HHs1nQG6 ,QMessageBox .HHs1nQG6 )

                if bJGYhtkq ==QMessageBox .zP2mfS4W :
                    try :
                        os .dICupRc3 ("sudo ./Uninstall.exe")
                        QMessageBox .TH7j53DR (self ,"Deinstallation","LATIN-AI-Launcher wurde erfolgreich deinstalliert.")
                        self .B3TY5yfi ()
                    except Lj5pt76l as o8pWbs3W :
                        QMessageBox .mtYtSnMl (self ,"Fehler",f"Fehler bei der Deinstallation: {o8pWbs3W }")

    def FqTzbEa9 (self ):
    # Hauptprogramm starten
        self .sM11NZjy .XltUx6jP ("Das Hauptprogramm wird gestartet...")# Ausgabe im Textbereich
        # prevent very rapid repeated launches
        if self .KkljP4Lf :
            self .sM11NZjy .XltUx6jP ("Start wird bereits ausgeführt. Bitte warten...")
            return 
        self .KkljP4Lf =True 
        self .jVlas015 .URWcAwwj (False )
        rBPpesuH =sys .u7H9XNbY 
        W7mpNmzd =['test.py']+(['--gibberlink=true']if nO6bLYOj else [])
        try :
        # Start detached so launcher does NOT capture child's stdout/stderr
            QProcess .ikUO3pP2 (rBPpesuH ,W7mpNmzd )
            self .sM11NZjy .XltUx6jP ("Hauptprogramm (test.py) im Hintergrund gestartet.")
        except Lj5pt76l as o8pWbs3W :
            QMessageBox .mtYtSnMl (self ,"Fehler",f"Fehler beim Starten des Skripts: {o8pWbs3W }")
            # re-enable button after a short interval to prevent accidental flooding
        QTimer .cvc6uYy8 (1000 ,lambda :(wEynw70W (self ,"_launch_in_progress",False ),self .jVlas015 .URWcAwwj (True )))

    def COJrGyhB (self ):
    # Updates suchensa
        if self .OKgWCilx .O6LSVy9H ():
            self .sM11NZjy .XltUx6jP ("Updates sind derzeit deaktiviert.")
            QMessageBox .TH7j53DR (self ,"Updates deaktiviert","Updates sind in den Entwickleroptionen deaktiviert.")
            return 

        if biNUVCm4 ():
            self .sM11NZjy .XltUx6jP ("Nach Updates suchen...")# Ausgabe im Textbereich
            try :
                QQvhQCtG =subprocess .AXdlh0B5 ([sys .u7H9XNbY (),'update-isolated.py'],joC0LlkP =True ,N65ONgFQ =True )
                self .sM11NZjy .XltUx6jP (QQvhQCtG .IdmoTvU2 )
                if QQvhQCtG .ppYEVMgN !=0 :
                    self .sM11NZjy .XltUx6jP (QQvhQCtG .lZdjfI07 )
            except Lj5pt76l as o8pWbs3W :
                QMessageBox .mtYtSnMl (self ,"Fehler",f"Fehler beim Suchen nach Updates: {o8pWbs3W }")
        else :
            self .sM11NZjy .XltUx6jP ("Keine Internetverbindung. Updates konnten nicht gesucht werden.")
            QMessageBox .C0ghuzQh (self ,"Keine Internetverbindung","Es besteht keine Internetverbindung. Bitte stellen Sie eine Verbindung her, um nach Updates zu suchen.")

    def hfiJPiZG (self ):
        hm1JdrA4 (r"Software\MINT-AI","PreventUpdates","True"if self .OKgWCilx .O6LSVy9H ()else "False")
        hm1JdrA4 (r"Software\MINT-AI","DisableLogos","True"if self .z34JFMH9 .O6LSVy9H ()else "False")
        nO6bLYOj =True if self .kPVyLvZJ .O6LSVy9H ()else False 
        self .Maqf3tFO ()

    def Maqf3tFO (self ):
        if self .z34JFMH9 .O6LSVy9H ():
            self .AN8mJE2Z .i6JZuNp9 ()
        else :
            self .AN8mJE2Z .uKAJuLuu ()

    def ru9x7EOV (self ):
        if BIEZboza (r"Software\MINT-AI","PreventUpdates","False")=="True":
            self .OKgWCilx .eaRewCOn (True )
        if BIEZboza (r"Software\MINT-AI","DisableLogos","False")=="True":
            self .z34JFMH9 .eaRewCOn (True )
            self .AN8mJE2Z .i6JZuNp9 ()

    def aoRdMEpt (self ):
        xAfqXIJM =self .pGzxx7om ()
        if xAfqXIJM is None :
            return 
        try :
            Jx3ovKXP =xAfqXIJM .dfX3fWHo ().BRnHGUK1 ().vigGSETj ('latin-1')
            if Jx3ovKXP :
                self .sM11NZjy .XltUx6jP (Jx3ovKXP )
        except Lj5pt76l :
            pass 
    def KZOhXSPV (self ):
        xAfqXIJM =self .pGzxx7om ()
        if xAfqXIJM is None :
            return 
        try :
            L36yrpVJ =xAfqXIJM .bqsX27K4 ().BRnHGUK1 ().vigGSETj ('latin-1')
            if L36yrpVJ :
                self .sM11NZjy .XltUx6jP (L36yrpVJ )
        except Lj5pt76l :
            pass 


def GJHd7zL4 ():
    try :
        sX48kxyP =requests .ubVPTDTG ('http://localhost:5001/install_dir')
        if sX48kxyP .vvFCWVC5 ==200 :
            print ("Server läuft bereits auf Port 5001")
            return 
    except requests .N93hK9aD :
        print ("Server läuft nicht, starte server.py")
        # avoid invalid escape sequences and build a safe path
        os .wOieiZ8z (os .JPfx64Lg .Mp2xTuqg (ZWhILNlY ,'server.py'))

if __name__ =="__main__":
    ZWhILNlY =V0nSNi1x ()
    GJHd7zL4 ()
    mekOLFLE (ZWhILNlY )
    sIDln7zr ()

    vn0b5nev =QApplication (sys .rSETkpLu )
    # Alle Addons ausführen
    od0BLcYp =os .JPfx64Lg .Mp2xTuqg (ZWhILNlY ,'addons')
    UyketVbt (od0BLcYp )
    # Ladebildschirm anzeigen und Installation starten
    ee059DPc =f53csAKa ()
    ee059DPc .uKAJuLuu ()
    ee059DPc .IvGcr1V4 ()


    sys .H5LOY7OG (vn0b5nev .tvtqC4b7 ())

    # Alle Addons ausführen
    od0BLcYp =os .JPfx64Lg .Mp2xTuqg (ZWhILNlY ,'addons')
    UyketVbt (od0BLcYp )
