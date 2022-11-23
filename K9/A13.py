#K9 / A13

def wechselautomat(geld):
    geld = int(input("Eingezahltes Geld eingeben: "))
    rueckgabe = {}
    
    if geld % 20 >= 0:
        rueckgabe[20] = int(geld / 20)
        geld = geld - int(geld / 20) * 20
    if geld % 1 >= 0:
        rueckgabe[1] = int(geld / 1)
        geld = geld - int(geld / 1) * 1
    return rueckgabe
  
print(wechselautomat(""))
