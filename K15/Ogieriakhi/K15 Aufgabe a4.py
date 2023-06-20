class Haus: 
    def __init__(self,Balkon,Farbe,Garten,Größe):
        self.Balkon = Balkon 
        self.Farbe = Farbe 
        self.Garten = Garten 
        self.Größe = Größe
        
    
    def neuer_Anstrich(self, Farbe):
        
        self.Farbe = Farbe

Haus1 = Haus("ja","Gelb","ja","1000 Quadeadmeter")


print("alte Farbe:", Haus1.Farbe)

Haus1.neuer_Anstrich ("Blau")


print("Neue Farbe:", Haus1.Farbe)