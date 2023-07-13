class Haus: 
    def __init__(self,Balkon,Farbe,Garten,Größe):
        self.Balkon = Balkon 
        self.Farbe = Farbe 
        self.Garten = Garten 
        self.Größe = Größe



Haus1 = Haus("ja","Gelb","ja","1000 Quadeadmeter")


print("Balkon:",Haus1.Balkon)

print("Farbe:",Haus1.Farbe)

print("Garten:",Haus1.Garten)

print("Balkon:",Haus1.Größe)