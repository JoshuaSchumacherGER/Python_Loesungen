import random

def crackingNumber():
    n = 0
    x = random.randint(0,100)
    while(n != 7):
        n += 1
        answer = int(input("Gebe eine zahl zwischen 0 und 100 ein: "))
        if answer > 100 or answer < 0:
            print("Deine Eingabe muss zwischen 0 und 100 liegen!")
        elif answer > x:
          print("Die gesuchte Zahl ist kleiner")
        elif answer < x:
            print("Die gesuchte Zahl ist größer")
        elif answer == x:
            print("Gewonnen!")
            break
    print("Verloren! Die gesuchte Zahl war" , x) 

crackingNumber()  
