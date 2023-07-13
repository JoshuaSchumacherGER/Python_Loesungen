import random

class Haus: 
    
    
    def __init__(self,Balkon,Farbe,Garten,Größe,preis):
        self.Balkon = Balkon 
        self.Farbe = Farbe 
        self.Garten = Garten 
        self.Größe = Größe
        self.preis =preis
    

    

Haus1 = Haus("ja","Gelb","ja","1000 Quadeadmeter", random.randint(1000,300000))

Haus2 = Haus("ja","Rot","Nein","850 Quadeadmeter", random.randint(1000,300000))

Haus3 = Haus("ja","Gelb","ja","1200 Quadeadmeter", random.randint(1000,300000))



liste = [Haus1,Haus2,Haus3]


for i in liste: 
    if i.preis > 200000:
        liste.remove (i)
        
    else: 
         
        print("Balkon:",i.Balkon)

        print("Farbe:",i.Farbe)

        print("Garten:",i.Garten)

        print("Balkon:",i.Größe)
        
        print("Preis:",i.preis)
