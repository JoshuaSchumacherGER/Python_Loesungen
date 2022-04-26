#A2 Teil 1
def Spritkosten(Kilometer,Spritverbrauch,Kosten_Liter):
    return (Kilometer/100*Spritverbrauch*Kosten_Liter)
Kilometer = int (input("Bitte gib die Kilometer ein."))
Spritverbrauch = int (input("Bitte gib den Ø Spritverbrauch auf 100 km ein."))
Kosten_Liter = float (input("Bitte gib die Kosten pro Liter ein."))



print ("Die Spritkosten betragen" , Spritkosten(Kilometer,Spritverbrauch,Kosten_Liter) , "€.")

