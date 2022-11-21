regen = input("Regnet es? (JA/NEIN) ")
geld = int(input("Wie viel Geld habe ich noch? "))
freund = input("Zahlt mein Freund? (JA/NEIN) ")

if (regen == "JA"):
    regen = True
else:
    regen = False

if (freund == "JA"):
    freund = True
else:
    freund = False


if(regen == True):
    print("Kino fällt ins Wasser.")
elif(geld < 20):
    if(freund == True):
        print("Hab leider kein Geld mehr, aber mein Kumpel zahlt.")
    else:
        print("Geld reicht leider nicht aus")
else:
    print("Also in welchen Film wollen wir?")