import random
x = random.randint(0,100)
g=int(5)
while(True):
    while(g>0):
        g=g-1
        i = int (input("Gib eine Zahl zwischen 0 und 100 ein."))
        if(i<x):
            print("Deine Zahl " , i , ".Die Zahl ist größer, Versuch es noch einmal. Du hast noch",g,"Versuche übrig")
        #    print(x) #opt. Kontrolle der Zahl. Code Testing
        elif(i>x):
            print("Deine Zahl " , i , ".Die Zahl ist niedriger, Versuch es noch einmal. Du hast noch" ,g, "Versuche übrig")
        #    print(x) #opt. Kontrolle der Zahl. Code Testing
        elif(i==x):
            break
    if(g==0):
        print("Du hast verloren.")
    elif(i==x):
            print("Deine Zahl ist" , i , ". Du hast die Zahl erraten.")
            print("Das Spiel ist beendet, du hast gewonnen.")
    break