def wechselautomat(geld):
    scheine = geld // 20
    muenzen = abs(geld - (scheine*20)) # Differenz
    print(scheine, "x 20€-Schein(e) und", muenzen, "x 1€-Münze(n)")

geld = int(input("Betrag: "))
wechselautomat(geld)