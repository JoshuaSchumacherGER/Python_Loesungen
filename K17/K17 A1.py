class Fahrzeug:
    def __init__ (self, Marke, PS, Tankfassung, Zylinderzahl, Gewicht, Hubraum) -> None:
        self.Marke =Marke
        self.PS = PS
        self.Tankfassung = Tankfassung
        self.Zylinderzahl = Zylinderzahl
        self.Gewicht = Gewicht
        self.Hubraum = Hubraum

class Auto(Fahrzeug):
    def __init__(self, Marke, PS, Tankfassung, Zylinderzahl, Gewicht, Hubraum, Füllvolumen) -> None:
        super().__init__(Marke, PS, Tankfassung, Zylinderzahl, Gewicht, Hubraum)
        self.Füllvolumen = Füllvolumen

class Motorrad(Fahrzeug):
    def __init__(self, Marke, PS, Tankfassung, Zylinderzahl, Gewicht, Hubraum) -> None:
        super().__init__(Marke, PS, Tankfassung, Zylinderzahl, Gewicht, Hubraum)

Nutzer1=Auto("Nissan",485,60,8,20,1700,10)

Nutzer2=Motorrad("Ducati",420,20,4,5,1500)
