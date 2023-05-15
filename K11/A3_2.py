#K11
#A3
tel={
    "Arbeit":{"Jan":"50","Mark":"81"},
    "private":{"Julia":"0151438924","Mark":"061932834"}
}

Eingabewert=input("Welchen Wert suchen sie? ")
def supersearch(d,value):
    for all in tel.values():
        if value in all.values():
            print(True)
            break
    else:
        print(False)
supersearch(tel,Eingabewert)