countdown = input("Wie lange soll der Countdown sein? ")
countdown = int(countdown)

a = countdown

for x in range(0, countdown):
    print (a)
    a -= 1