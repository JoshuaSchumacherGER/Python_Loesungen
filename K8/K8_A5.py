
# Fragestellungen mit Eingabe
regen = input("Regnet es? (Ja/Nein): ")
budget = input("Wie viel Geld steht zur Verfügung? ")
freundin_bezahlt = input("Bezahlt dein/e Freund/in ? (Ja/Nein): ")

# Bedingungen die überprüft werden und eine entsprechende Ausgabe machen

if regen == "Ja" or regen == "ja":
    if int(budget)>= 20 or freundin_bezahlt == "Ja" or freundin_bezahlt == "ja" and regen == False:
        print("Wir gehen ins Kino heute!")
    else:
        print("Wir bleiben heute zu Hause.")
elif regen == "Nein" or regen == "nein":
    print("Das Wetter ist sehr gut heute, deswegen bleiben wir zu Hause.")
    
    
# Zuerst werden die Bedingungen abgefragt und wenn diese zutreffen, wird angezeigt das man ins Kino geht.
# Wenn dies nicht der Fall ist bleibt ihr zu Hause. 