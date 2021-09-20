zahl = input("Wie viel?")
zahl = int(zahl)

def rekursive(zahl):
    if zahl == 0:
        return 0
    elif zahl == 1:
        return 1
    else:
        return rekursive(zahl -1) + rekursive(zahl -2)
    
print(rekursive(zahl))