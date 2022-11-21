liste = {
    "Schere":"Schere",
    "Stein":"Stein",
    "Papier":"Papier"
}

auswahl = input("Wähle Schere, Stein oder Papier: ")

print(liste.get(auswahl, "Weder noch..."))