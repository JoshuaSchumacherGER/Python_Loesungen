def wechselautomat(geld):
    coins = geld % 20
    banknote = geld // 20

    print("Der Automat gibt ", coins, " Münzen aus.")
    print("Der Automat gibt ", banknote, " Scheine aus.")

geld = input("Geben Sie eine ganze positive Zahl ein.")
geld = int(geld)
wechselautomat(geld)