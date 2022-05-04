def sortiere(Liste):
    y = len(Liste)
    lauf = 0


    # Sortierschleife
    while(y > 0):
        a,b = 0,1
        y -= 1
        x = len(Liste) -1
        while (x > 0):
            x -= 1
            if (Liste[a] < Liste[b]) or Liste[a] == Liste[b]:
                a += 1
                b += 1
            else :
                Liste[a],Liste[b] = Liste[b],Liste[a]
                a += 1
                b += 1
    return Liste


Liste = [3,7,9,1,3,4,7,6,9,8,3,1,1,4,9,6,7,3,5,2]

print(Liste)
sortiere(Liste)
print(Liste)