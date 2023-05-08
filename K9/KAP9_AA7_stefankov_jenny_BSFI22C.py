import random
def CrackingNumber():
        x = random.randrange(0,100)
        for i in range(0,5):
            n = int(input("Geben Sie eine Zahl ein:"))
            if (n < x):
                print("Die gesuchte Zahl ist größer")
            elif (n > x):
                print("Die gesuchte Zahl ist kleiner")
            else:
                print("Sie haben die Zahl erraten")
                return "0"
        print("Sie haben keine Versuche mehr")
        print("Die gesuchte Zahl war: ", x)

CrackingNumber()
