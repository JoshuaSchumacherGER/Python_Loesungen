# Kapitel 11 - Aufgabe 4
# Schreibe ein Programm, in dem	ein	Benutzer beliebig lange	Länder inkl. Hauptstädte eingeben kann, bis	er Beenden eintippt.
# Die Länder + Hauptstädte werden in einem Dictionary gespeichert.und danach in der Konsole ausgegeben.

# Das Ausgabeformat lautet:
# "   Land        | Hauptstadt"
# "1. Deutschland | Berlin"
# "2. Frankreich  | Paris"

def country_dictionary():
    country_dict = {}
    while True:
        country = input("Bitte geben Sie ein Land ein: ")
        if country == "Beenden" or country == "beenden":
            break

        capital = input("Bitte geben Sie die Hauptstadt ein: ")
        country_dict[country] = capital

    counter = 1
    longestCountry = 0
    for country in country_dict.keys():
        if len(country) > longestCountry:
            longestCountry = len(country)

    print(f"   Land{' ' * (longestCountry - 4)} | Hauptstadt")
    print('-' * (longestCountry + 16))
    for country, capital in country_dict.items():
        countryLength = len(country)
        print(
            f"{counter}. {country}{' ' * (longestCountry - countryLength)} | {capital}")
        counter += 1


country_dictionary()
