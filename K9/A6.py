
x = int(input("Anzahl Sterne"))

for i in range(0,x):
    print(i, "in erster schleife",i)
    
    for j in range(i):
        print(i, "in zweiter schleife")
        print("*", end='')
        
    print("*")
