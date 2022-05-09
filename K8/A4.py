phone_price = input("Handypreis: ")
phone_price = int(phone_price)

camera = input("Wieviele Kameras hat das Handy: ")
camera = int(camera)


lifetime = input("Wie lange hält der Akku in Tagen?")
lifetime = int(lifetime)

marke = input("Von welcher Marke ist das Handy?")

if phone_price < 1000 and camera >= 3 and lifetime >= 2 and marke ==("Apple" or "Samsung"):
    print("Handy kaufen!")
else:
    print("Handy nicht kaufen!")