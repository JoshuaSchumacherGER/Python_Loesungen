"""
Kapitel 15
Author: Ali Abas Arsalahn
Datum: 01.05.2022
"""


from arsaal_haus import Haus


def aufgabe_zwei() -> None:
    """
    Erstelle ein Objekt der Klasse Haus mit beliebigen werten. 
    Gebe danach alle Werte auf der Konsole wieder aus.
    """
    alis_haus = Haus("Doenerallee", 23, "rot", 275000, 1, 40)
    print(alis_haus.__str__())


def aufgabe_drei() -> None:
    """
    Erstelle 3 verschiedene Hausobjekte und speichere diese in einer Liste. 
    Lösche danach das letzte Haus in der Liste und gebe die Liste entsprechend auf der Konsole aus.
    """
    dieters_haus = Haus("Almanstraße", 42, "weiß", 800000, 3, 150)
    stefans_haus = Haus("Kaiserstraße", 10, 'gelb', 150000, 1, 50)
    juergens_haus = Haus("Schmittstraße", 5, 'grün', 17500, 2, 80)
    haus_liste = [dieters_haus, stefans_haus, juergens_haus]
    haus_liste.pop()
    print(haus_liste)


def aufgabe_vier() -> None:
    """
    Füge der Klasse die Methode neuer_anstrich(farbe) hinzu, 
    die eine neue Farbe bnimmt und den Wert entsprechend abändert.
    Erstelle dann ein Objekt, dessen Farbe nachträglich geändert wird 
    und gebe diesen Wert auf der Konsole erneut aus.
    """
    neues_haus = Haus("irgendwo-im-nirgendwo", 2, 'gelb', 12000, 1, 20)
    neues_haus.neuer_anstrich('rot')
    print(neues_haus.farbe)


def aufgabe_fünf() -> None:
    """
    Erstelle eine neue Hausliste mit 3 Hausobjekten. Danach soll überprüft werden, ob ein Haus über 200.00ß€ kostet.
    Falls ja, wird das Haus aus der Liste entfernt. Gebe anschließend die Liste auf der Konsole aus.
    """
    billiges_haus = Haus('guenstigstraße', 1, 'weiß', 90000, 1, 15)
    normales_haus = Haus('normalstraße', 12, 'rot', 15000, 2, 40)
    teures_haus = Haus('Paschastraße', 42, 'weiß', 400000, 4, 200)
    haus_liste = [billiges_haus, normales_haus, teures_haus]

    for haus in haus_liste:
        if haus.preis > 200000:
            haus_liste.remove(haus)
    print(haus_liste)

def main() -> None:
    """Main Funktion."""
    aufgabe_zwei()
    aufgabe_drei()
    aufgabe_vier()
    aufgabe_fünf()


if __name__ == '__main__':
    main()
