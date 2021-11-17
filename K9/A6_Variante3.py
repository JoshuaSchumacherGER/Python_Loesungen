# Erweitere deine Funktion „countingStars“ dahingehend, dass die Anzahl der Sterne wieder abnimmt.
# Beispiel Zahl = 3
# *
# **
# ***
# **
# *
stars = int(input("Enter your value: "))


def stars_function(stars):
# Mit 2 Schleifen
    for star_count in range(stars + 1):
        print(star_count * "#")
        if (star_count == (stars + 1)):
            break

    while star_count != 1:
        star_count -= 1
        print(star_count * "#")
# Mit einer Schleife
    for star_count in range((stars) * 2):
        if (star_count <= stars):
            print(star_count * "*")
        else:
            stars -= 1
            print(stars * "*")


stars_function(stars)
