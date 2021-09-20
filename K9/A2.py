zahl = input("Wie hoch soll die Fibonacci-Folge berechnet werden?")
zahl = int(zahl)

def fib(b):
    erg = 0
    zahl1 = 0
    zahl2 = 1
    for x in range(0, b):
        if b == 0:
            erg = 0
            break
        zahl1 = zahl2
        zahl2 = erg       
        erg = zahl1 + zahl2
    return erg
               
print(fib(zahl))