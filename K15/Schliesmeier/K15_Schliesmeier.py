'''Erstelle	eine	Klasse	Haus	inkl.	Konstruktor,	welches	über	folgende	Attribute	verfügt:	
Straße,	Hausnummer,	Farbe,	Preis,	Stockwerksanzahl,	Quadratmeter.'''

class Haus:
    def __init__ (self,Strasse, Hausnummer, Farbe, Preis, Stockwerkanzahl,Quadratmeter):
        self.Strasse = Strasse
        self.Hausnummer= Hausnummer
        self.Farbe= Farbe
        self.Preis = Preis 
        self.Stockwerkanzahl= Stockwerkanzahl
        self.Quadratmeter = Quadratmeter
'''Erstelle	ein	Objekt	der	Klasse	Haus	mit	beliebigen	Werten.	Gebe	danach	alle	Werte	auf	
der	Konsole	wieder	aus'''


mein_Haus=Haus("teststrasse",2,"rot",200000,2,4)
print(vars (mein_Haus))

'''Erstelle	3	verschiedene	Hausobjekte	und	speichere	diese	in	einer	Liste.	Lösche	danach	
das	letzte	Haus	in	der	Liste	und	gebe	die	Liste	entsprechend	auf	der	Konsole	aus'''

haus1=Haus("test2",4,"blau",30000,4,89)
haus2=Haus("test3",5,"grau",4657,4,67)
haus3=Haus("test6",59,"gelb",48459,7,3)

Liste1=[]
haeuser=(vars(haus1),vars(haus2),vars(haus3))
Liste1.extend(haeuser)
del Liste1 [2]
print(Liste1)

'''Füge	der	Klasse	die	Methode	neuer_anstrich(farbe)	hinzu,	die	eine	neue	Farbe	nimmt	
und	den	Wert	entsprechend	abändert.	Erstelle	dann	ein	Objekt,	dessen	Farbe	nachträglich	geändert	wird	
und	gebe	diesen	Wert	auf	der	Konsole	erneut	aus'''

def farbewechseln (self,neuer_anstrich,farbe):
    self.neuer_anstrich =neuer_anstrich
    self.farbe=farbe 
    if neuer_anstrich != '':
       farbe=  neuer_anstrich
    print(farbe) 

'''  Erstelle	eine	neue	Hausliste	mit	3	Hausobjekten.	Danach	soll	überprüft	werden,	ob	ein	
Haus	über	200.000€	kostet.	Falls	ja,	wird	das	Haus	aus	der	Liste	entfernt.	Gebe	anschließend	die	Liste	auf	
der	Konsole	aus'''
Haus4=Haus("teststrasse1",23,"blau",4,30000,300)
Haus5=Haus("teststrasse2",3,"grün",23,345000,456)
Haus6=Haus("teststrasse1",57,"pink",2,900000,200)
NeueHausliste=[]
neue_haeuser=(vars(Haus4),vars(Haus5),vars(Haus6))
NeueHausliste.extend(neue_haeuser) 
if Haus4.Preis >200000:
    NeueHausliste.remove(Haus4.Preis)
if Haus5.Preis > 200000:
    NeueHausliste.remove (Haus5.Preis)
if Haus6.Preis >200000:
    NeueHausliste.remove (Haus6.Preis)
print(NeueHausliste)