# Ein Mini-Spiel namens "CrackingNumber"
# Eine Zufallszahl von 0 bis 100 wird generiert.
# Der Benutzer hat 5 Eingabeversuche.
# Bei jeder Eingabe gibt es den Hinweis ob die Zahl
# größer oder kleiner ist.
# Wird die Zahl innerhalb von 5 Versuchen erraten,
# erscheint eine Sieger-Nachricht, ansonsten Verloren.

from random import randint


def cracking_numbers():
    x = randint(0, 100)
    # print(x)
    print("Finde die richtige Zahl! Du hast 5 Versuche!")

    for i in range(6):

        if i == 5:
            print("Du hast verloren!")
            break

        print("\n  Das ist dein " + str(i + 1) + ".ter Versuch!")
        guess = int(input("Gib eine Zahl von 0 bis 100 ein: "))

        if guess == x:
            print("Richtige Zahl! Du hast gewonnen!")
            break

        elif guess < x:
            print("Deine Zahl war zu klein.")

        else:
            print("Deine Zahl war zu hoch.")

    print("\nProgramm Ende")


cracking_numbers()
