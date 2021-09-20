def spritkosten(kilometer, verbrauch, preis_Liter):
    return (((verbrauch/100)*kilometer)*preis_Liter)

    #print(round(spritkosten(30, 6, 1.36),2), "€")

def spritmitinput():
    kilometer = input("Wie viele Kilometer fahrt ihr? ")
    kilometer = int(kilometer)
                
    verbrauch = input("Der Spritverbrauch deines Autos? ")
    verbrauch = int(verbrauch)
                
    preis_Liter = input("Wie hoch ist der aktuelle Benzin preis? ")
    preis_Liter = int(preis_Liter)
                
    erg = ((verbrauch/100)*kilometer)*preis_Liter
                    
    print(round(erg, 2))
                

"""
Laufende Kosten werden hier nicht mit einberechnet.
Es fehlen zum Beispiel Versicherungskosten, Wertverlust, Verschleiß oder auch Steuern.
"""