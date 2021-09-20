regen = input("Regnet es? Ja oder Nein? ")
if regen == "Ja":
    regen = True

geld = input("Wie viel Geld hast du? ")
geld = int(geld)
    
freundin_Zahlt = input("Als ob die alte zahlt? Ja oder Nein? ")
if freundin_Zahlt == "Ja":
    freundin_Zahlt = True
    
if (geld >= 20 or freundin_Zahlt == True) and regen == False:
    print("Wir gehen ins Kino!")

else:
    print("Kein Kino!")