# Quicksort

Liste = [5,64,12,35,11,99,23]
pivot = len(Liste)-1
a = 0
b = pivot -1 
print(Liste)

while (a != b):
    while (Liste[a] < Liste[pivot]):
        a += 1
    
    Liste[b] = Liste[a]
    if (a != b):
        while (Liste[b] > Liste[pivot]):
            b -= 1

        Liste[a] = Liste[b]

Liste[a] = Liste[pivot]
print(Liste)