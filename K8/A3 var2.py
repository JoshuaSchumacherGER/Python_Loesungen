#Autokauf, Bedingung: 20 000€ , Klimaanlage
Preis = int(input("Was kostet das Auto?"))
Klimaanlage = str(input("Hat das Auto eine Klimaanlage?"))
if Preis < 20000 and Klimaanlage == ("Ja") or Klimaanlage == ("JA"):
    print("Kaufe das Auto.")
else: 
    print("Kaufe das Auto nicht.")