# Jana Theis

'''Aufgabe K15 | A1: Erstelle eine Klasse Haus inkl. Konstruktor, welches über folgende Attribute verfügt:
Straße, Hausnummer, Farbe, Preis, Stockwerksanzahl, Quadratmeter.'''

class Haus:
    def __init__(self, strasse, hausnr, farbe, preis, stockwerke, quadratmeter):
        self.strasse = strasse
        self.hausnr = hausnr
        self.farbe = farbe
        self.preis = preis
        self.stockwerke = stockwerke
        self.quadratmeter = quadratmeter

    def neuer_anstrich(self, neue_farbe):
        self.farbe = neue_farbe


'''Aufgabe K15 | A2:Erstelle ein Objekt der Klasse Haus mit beliebigen Werten. Gebe danach alle Werte auf der Konsole wieder aus.'''

erstes_haus = Haus('Binger Str.', 15, 'weiss', 210000, 3, 130 )
print(vars(erstes_haus))

'''Aufgabe K15 | A3: Erstelle 3 verschiedene Hausobjekte und speichere diese in einer Liste. Lösche danach das letzte Haus in der Liste
 und gebe die Liste entsprechend auf der Konsole aus.'''

ListeAnHaeusern = []

zweites_haus = Haus('Am Königsborn', 15, 'braun', 20000, 2, 100)
drittes_haus = Haus('Am Judensand', 37, 'weiss', 150000, 4, 520)
ListeAnHaeusern.extend([erstes_haus, zweites_haus,drittes_haus])

ListeAnHaeusern.pop()
for haus in ListeAnHaeusern:
    print(vars(haus))

'''Aufgabe K15 | A4:Füge der Klasse die Methode neuer_anstrich(farbe) hinzu, die eine neue Farbe nimmt und den Wert entsprechend abändert.
Erstelle dann ein Objekt, dessen Farbe nachträglich geändert wird und gebe diesen Wert auf der Konsole erneut aus.'''

viertes_haus = Haus('Am Judensand', 1, "blau", 4500000, 5, 270 )
print('Alte Farbe: ', viertes_haus.farbe)
viertes_haus.neuer_anstrich('schwarz')
print('Neue Farbe: ', viertes_haus.farbe)

'''Aufgabe K15 | A5:Erstelle eine neue Hausliste mit 3 Hausobjekten. Danach soll überprüft werden, ob ein Haus über 200.000€ kostet.
Falls ja, wird das Haus aus der Liste entfernt. Gebe anschließend die Liste auf der Konsole aus.'''

HausListe = []
haus1 = Haus('Mainzer Strasse', 1, 'gruen', 300000, 3, 120)
haus2 = Haus('Mainzer Strasse', 2, 'weiss', 120000, 2, 80)
haus3 = Haus('Mainzer Strasse', 3, 'rot', 400000, 4, 200)

HausListe.extend([haus1, haus2, haus3])
HausListe = [haus for haus in HausListe if haus.preis > 200000]
for haus in HausListe:
    print(vars(haus))