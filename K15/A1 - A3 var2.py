
#Aufgabe K15 | A1: Erstelle eine Klasse Haus inkl. Konstruktor, welches über folgende Attribute verfügt: 
# Straße, Hausnummer, Farbe, Preis, Stockwerksanzahl, Quadratmeter.

class House():
    def __init__(self,street, housenumber, color, price, floors, sqmeters):
        self.street = street
        self.housenumber = housenumber
        self.color = color
        self.price = price
        self.floors = floors
        self.sqmeters = sqmeters

#Aufgabe K15 | A2 Erstelle ein Objekt der Klasse Haus mit beliebigen Werten. 
#Gebe danach alle Werte auf der Konsole wieder aus.

house_midtown = House("Rotebeetestraße",10,"orange",350.000,3,60)
print(vars(house_midtown))

#Aufgabe K15 | A3 Erstelle 3 verschiedene Hausobjekte und speichere diese in einer Liste. 
#Lösche danach das letzte Haus in der Liste und gebe die Liste entsprechend auf der Konsole aus.

house_downtown = House("Birnenpfad",85,"weiß",650.000,5,600)
house_avenue = House("Kolrabisquare",4,"grün",400.000,1,5000)

HouseSale = [house_midtown,house_downtown,house_avenue]
HouseSale.pop()
print(HouseSale)


