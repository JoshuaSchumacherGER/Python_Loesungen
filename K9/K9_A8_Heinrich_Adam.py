# Eine Funktion "cancel",
# die solange Eingaben annimmt bis
# "Beenden" eingetippt wird.

def cancel():
    while True:
        x = input("Gib was ein: ")
        if x == "Beenden": break

    print("Programm Ende")


cancel()
