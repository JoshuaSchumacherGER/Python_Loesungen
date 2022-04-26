#Handykauf , >1000€ , < 3 Rückkameras , < 2 Tage Akkulaufzeit , Marke: Apple|Samsung
Preis = int(input("Wie viel kostet das Handy?"))
Kamera = int(input("Wie viele Rückkameras bestitzt das Handy?"))
Akku = int(input("Wie lange ist die Akkulaufzeit des Handys?(Angabe in Tagen)"))
Marke = str(input("Von welcher Marke ist das Handy?"))
if Preis >1000: 
    print("Kaufe das Handy nicht.1")
elif Kamera < 3:
    print("Kaufe das Handy nicht.2")
elif Akku < 2:
    print("Kaufe das Handy nicht.3")
elif Marke == "Apple" or "Samsung" or "apple" or "samsung":
    print("Kaufe das Handy")
