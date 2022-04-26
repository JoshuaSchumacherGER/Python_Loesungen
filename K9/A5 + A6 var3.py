while(True):
    Star = int(input("Anzahl Sterne."))

    for x in range(1,Star+1):
        print(x*"*")
        continue
    for x in reversed(range(1,Star)):  #ab hier beginnt A6
        print(x*"*")