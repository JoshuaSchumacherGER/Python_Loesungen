class Haus:
    def __init__(self, Straße, Hausnummer, Farbe, Preis, Stockwerkzahl, Quardratmeter) -> None:
        self.straße = Straße
        self.hausnummer = Hausnummer
        self.farbe = Farbe
        self.preis = Preis
        self.stockwerkzahl = Stockwerkzahl
        self.quadratmeter = Quardratmeter
        pass
    
    @property
    def preis(self):
        return self._preis
    
    @property
    def quadratmeter(self):
        return self._quadratmeter
    
    @preis.setter
    def preis(self, value):
        if value <= 0:
            print('Eingabe ungültig!')
        else:    
            self._preis = value
    
    @quadratmeter.setter
    def quadratmeter(self, value):
        if value <= 0:
            print('Eingabe ungültig!')
        else: self._quadratmeter = value

haus1 = Haus('Musterstraße', 8, 'red', 150000, 4, 120)
haus1.preis = -1
print(haus1.preis)
haus1.preis = 900000
print(haus1.preis)
haus1.quadratmeter = -1
print(haus1.quadratmeter)
haus1.quadratmeter = 130
print(haus1.quadratmeter)
