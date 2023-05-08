import random


"""A9:Erweitere das Spiel „crackingNumber“. Diesmal wählst du eine Zufallszahl aus und der Computer muss raten. Überlege dir vorher, mit welcher Strategie der Computer vorgehen soll, um mit möglichst wenigen Versuchen sein Ziel zu erreichen."""

def CrackingNumber():
    while True:    
        x = int (input("gebe eine Zahl an von 0 - 10 an die erraten werden soll:"))#random.randrange(0,100)
        if x < 11 and x > 0:
            for i in range(0,5):
                y = random.randrange(0,10)
                if (y < x):
                    print("Die gesuchte Zahl ist größer","Der Bot hat die Zahl", y, "geschätzt")
                elif (y > x):
                    print("Die gesuchte Zahl ist kleiner","Der Bot hat die Zahl", y, "geschätzt")
                else:
                    print("Der Computer sat Es ist die Zahl:", y)
                    return "0"
            print("Computer konnte deine Zahl net erraten.")
            print("Die gesuchte Zahl war: ", x)
            break
        else: 
            print("deine musst nicht an die Bedingung halten..")
            continue
              

#CrackingNumber()

while True:
    Abfrage=str(input("Hallo ich bin dein Computer lass uns ein spiel spielen du gibst eine Zahl an und Versuche diese in 5 veruschen zu erraten hättest du lust?(y/n):"))
    if Abfrage == "y":
        CrackingNumber()
        NeuAbfrage = str(input("Magst du weiter spielen?(y/n)"))
        if NeuAbfrage == "y":
            continue
        else:
            print("OK dann nicht... das hat mir spaß gemacht bis bald")
            break
    else:
        print("OK dann nicht...")
        break
