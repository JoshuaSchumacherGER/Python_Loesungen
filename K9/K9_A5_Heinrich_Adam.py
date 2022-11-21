# Eine Funktion "countingStars",
# welche eine Zahl nimmt und
# Sterne von 1 bis n in aufsteigender
# Reihenfolge ausgibt.

def counting_stars(n):

    for i in range(1, n+1):
        print("*" * i)


counting_stars(9)
