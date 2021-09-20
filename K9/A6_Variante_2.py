zahl = input("Gib mir eine Zahl. ")
zahl = int(zahl)

def countingstars(zahl):
    for x in range(0, zahl):
        print((x+1) * "*")
    while(x > 0):
        print(x * "*")
        x -= 1
    
    
countingstars(zahl)