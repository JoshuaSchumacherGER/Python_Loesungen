preis = input("Wie viel kostet das Handy? ")
preis = int(preis)

kameras = input("Wie viele Rückkameras hat das Handy? ")
kameras = int(kameras)

lifetime = input("Wie viele Tage hält die Batterie? ")
lifetime = int(lifetime)

Marke = input("Von welcher Marke ist das Handy? ")


if preis < 1000 and kameras >= 3 and lifetime >= 2 and ((Marke == "Apple") or (Marke == "Samsung")):
    print("Ich werde das Handy kaufen!")

else:
    print("Ne das kacke, kauf ich nicht!")