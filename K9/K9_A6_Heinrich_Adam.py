# Die Funktion "counting_stars" aus K9_A5 erweitern,
# sodass die Sterne auch wieder abnehmen

def counting_stars(n):

    for i in range(1, n+1):
        print("*" * i)

    for i in range(n-1, 0, -1):
        print("*" * i)


counting_stars(4)
