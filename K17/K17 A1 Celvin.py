
class Fahrzeug:
    def __init__(self, marke, farbe, baujahr, ps):
        self.marke = marke
        self.farbe = farbe
        self.baujahr = baujahr
        self.ps = ps

class Motorrad(Fahrzeug):
    def __init__(self, marke, farbe, baujahr, ps, hubraum):
        super().__init__(marke, farbe, baujahr, ps)
        self.hubraum = hubraum

class Auto(Fahrzeug):
    def __init__(self, marke, farbe, baujahr, ps, türen, sitzplätze):
        super().__init__(marke, farbe, baujahr, ps)
        self.türen = türen
        self.sitzplätze = sitzplätze

# Beispielverwendung
motorrad = Motorrad("Honda", "Rot", 2022, 150, 1000)
print(motorrad.marke)
print(motorrad.farbe)
print(motorrad.baujahr)
print(motorrad.ps)
print(motorrad.hubraum)

auto = Auto("Volkswagen", "Blau", 2019, 120, 4, 5)
print(auto.marke)
print(auto.farbe)
print(auto.baujahr)
print(auto.ps)
print(auto.türen)
print(auto.sitzplätze)