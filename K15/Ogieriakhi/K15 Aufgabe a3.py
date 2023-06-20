class Haus: 
    def __init__(self,Balkon,Farbe,Garten,Größe):
        self.Balkon = Balkon 
        self.Farbe = Farbe 
        self.Garten = Garten 
        self.Größe = Größe
        
    

    

Haus1 = Haus("ja","Gelb","ja","1000 Quadeadmeter")

Haus2 = Haus("ja","Rot","Nein","850 Quadeadmeter")

Haus3 = Haus("ja","Gelb","ja","1200 Quadeadmeter")


liste=[Haus1,Haus2,Haus3]

liste.remove(Haus3)

for i in liste:
    
    print("Balkon:",i.Balkon)

    print("Farbe:",i.Farbe)

    print("Garten:",i.Garten)

    print("Balkon:",i.Größe)