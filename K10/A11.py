#K10|A11 Schreibe eine Funktion, die eine Liste als Parameter nimmt. Entweder wird das letzte Element der Liste
#zurückgeliefert oder (falls die Liste leer sein sollte), wird der String „Leere Liste“ zurückgeliefert

def checkliste():
    mylist = [2,4,5,123,4,31]
    if  len(mylist) == 0:
        print("Leere Liste") 
    else:
        x = len(mylist)
        print(mylist[x-1])
checkliste()

