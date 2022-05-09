weather = input("Wie ist das Wetter?")
if weather == "Regen":
    weather = True

money = input("Wieviel Geld hast du noch übrig?")
money = int(money)

gf_pays = input("Zahlt deine Freundin?")
if gf_pays == "Ja":
    gf_pays = True
else:
    gf_pays = False #Andere Freundin suchen!!!

if weather == True and money >= 20 or gf_pays == True:
    print("Auf ins Kino!")
else:
    print("Zuhause bleiben...")