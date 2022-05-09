import random

def Kino():
    print("-------------------------------------------------------")
    for x in range(0,8):
        if x == 2:
            print("-------------------------------------------------------")
        a = []
        for y in range(0,9):
            random_num = random.randrange(0, 100)
            if random_num >= 50:
                a.append("X")
            else:
                a.append("-")
        print("Reihe", x + 1 , " ", a)
    print("-------------------------------------------------------")
            
Kino()