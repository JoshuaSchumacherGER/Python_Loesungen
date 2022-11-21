print("Hallo Jonas")



#Aufgabe K8 | A2

def a2(a,b,c):
    if a > b > c:
        print(a, b, c)
    elif c > b > a:
        print(c, b, a)

    elif b > c > a:
        print(b, c, a)
    elif a > c > b:
        print (a, c, b)

    elif c > a > b:
        print(c, a, b)
    elif b > a > c:
        print(b, a, c)

    else:
        print("alle Zahlen sind gleich groß")

a2(5, 7, 112)