"""
Kapitel 15
Author: Ali Abas Arsalahn
Datum: 01.05.2022
"""


class Haus:
    """
    Klasse Haus
    Eigenschaften: Straße, Hausnummer, Farbe, Preis, Stockwerksanzahl, Quadratmeter
    """
    # Aufgabe 1

    def __init__(self, straße: str, hausnummer: int, farbe: str, preis: int,
                 stockwerksanzahl: int, quadratmeter: int):
        """Haus Konstruktor"""
        self.straße = straße
        self.hausnummer = hausnummer
        self.farbe = farbe
        self.preis = preis
        self.stockwerksanzahl = stockwerksanzahl
        self.quadratmeter = quadratmeter

    # Aufgabe 2
    def __str__(self) -> str:
        return f"""
    Straße: {self.straße}
    Hausnummer: {self.hausnummer}
    Farbe: {self.farbe}
    Preis: {self.preis}
    Stockwerkanzahl: {self.stockwerksanzahl}
    Quadratmeter: {self.quadratmeter}
    """

    # Aufgabe 4
    def neuer_anstrich(self, neue_farbe: str) -> None:
        """Nimmt eine neue Farbe als Argument. Ändert die Farbe des Objekts
        wenn diese sich in der Liste der verfügbaren Farben befindet."""
        FARBEN: list = ['rot', 'blau', 'gelb', 'grün', 'weiß']
        if neue_farbe in FARBEN:
            self.farbe = neue_farbe
