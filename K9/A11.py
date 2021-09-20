import random

# --------------------
# Erzeugung der Listen
# --------------------
anzahlReihen = 5
anzahlPlaetze = 8
anzahlReihenLoge = 2

belegung = [0] * anzahlReihen
belegungLoge = [0] * anzahlReihenLoge

for i in range(anzahlReihen):
    belegung[i] = [False] * anzahlPlaetze

for i in range(anzahlReihenLoge):
    belegungLoge[i] = [False] * anzahlPlaetze

# -----------------------------
# Zufällige Belegung der Plätze
# -----------------------------
random.seed()

for reihe in range(anzahlReihen):
    for platz in range(anzahlPlaetze):
        if random.randint(0, 1) == 1:
            belegung[reihe][platz] = True

for reihe in range(anzahlReihenLoge):
    for platz in range(anzahlPlaetze):
        if random.randint(0, 1) == 1:
            belegungLoge[reihe][platz] = True

# --------------------
# Ausgabe der Belegung
# --------------------

print("Aktuelle Belegung \n")
print("         |  Platz ")
print("         |  1 2 3 4 5 6 7 8")
print("-------------------------------")

for reihe in range(anzahlReihen):
 #  print(" {0}.Reihe | ".format(reihe + 1), end = "")
    print(reihe+1, "Reihe  | ", end="")
    for platz in range(anzahlPlaetze):
        if belegung[reihe][platz] == True:
            print("x", end=" ")
        else:
            print("-", end=" ")
    print()

print("------------------------------")

for reihe in range(anzahlReihenLoge):
    print(reihe+1, "Reihe  | ", end="")
    for platz in range(anzahlPlaetze):
        if belegungLoge[reihe][platz] == True:
            print("x", end=" ")
        else:
            print("-", end=" ")
    print()
