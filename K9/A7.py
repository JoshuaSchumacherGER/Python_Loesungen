import random

random_num = random.randrange(0, 100)

tries_Left = 5

while(tries_Left > 0):
    print("Rate die Zahl. Du hast noch: ", tries_Left, "Versuche.")
    zahl = input("")
    zahl = int(zahl)
    
    tries_Left -= 1
    
    if zahl == random_num:
        print("Gewonnen!")
        break
    elif zahl > random_num:
        print("Gesuchte Zahl ist groesser")
    else:
        print("Gesuchte Zahl ist kleiner")