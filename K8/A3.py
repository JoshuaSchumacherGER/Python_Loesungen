auto_Kosten = input("Wie viel kostet das Auto? ")
auto_Kosten = int(auto_Kosten)

klimaanlage = input("Hat das Auto eine Klimaanlage? Ja oder Nein? ")
if klimaanlage == "Ja":
    klimaanlage = True
else:
    klimaanlage = False


if auto_Kosten <= 20000 and klimaanlage == True:
    print("Auto kaufen!")

elif auto_Kosten <= 20000 and klimaanlage == False:
    print("Auto nicht kaufen, weil Klimaanlage fehlt!")
    
elif auto_Kosten > 20000 and klimaanlage == True:
    print("Auto ist zu Teuer! Aber es hat eine Klimaanlage!")
    
else:
    print("Auto ist zu Teuer! Und es hat keine Klimaanlage!")