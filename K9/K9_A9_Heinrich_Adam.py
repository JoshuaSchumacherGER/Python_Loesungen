# Erweiterung von "cracking_number" aus K9_A7
# Diesmal soll der Computer raten und
# du sollst eine Zahl zwischen 0 und 100 vorgeben.

# Hier deine Zufallszahl eingeben:
zufallszahl = 69


# Die Zahl guess ist die Zahl mit der geraten werden soll.
def cracking_number():

    guess = 50
    x = guess

    while (True):

        # Verhindert Endlosschleife, falls die Zufallszahl <= 1 ist.
        if x <= 1:
            x = 2

        if guess == zufallszahl:
            print("Die Zahl ist ", guess)
            break
        elif guess > zufallszahl:
            guess -= x // 2
            print(guess)
        else:
            guess += x // 2
            print(guess)

        x //= 2


cracking_number()
