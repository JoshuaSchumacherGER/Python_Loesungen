car_price = input("Was kostet das Auto?: ")
car_price = int(car_price)

klimaanlage = input("Hat das Auto eine Klimaanlage(Ja oder nein): ")
if klimaanlage == "Ja":
    klimaanlage = True
else:
    klimaanlage = False

if car_price <= 20000 and klimaanlage == True:
    print("Auto kaufen!")
    
elif car_price <= 20000 and klimaanlage == False:
    print("Klimaanlage nicht vorhanden, nicht kaufen!")
    
elif car_price > 20000 and klimaanlage == True:
    print("Pries zu hoch!")

else:
    print("Preis zu hoch und keine Klimaanlage!")