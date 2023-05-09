class HAUS: 
    def __init__(self, street, number,color, price, floors, size):
        self.street = street
        self.number = number
        self.color = color
        self.price = price
        self.floors = floors
        self.size = size
    def __str__(self):
        return f"The House Data is: \n Address: {self.street} {self.number} \n Color: {self.color} \n Price: {self.price} \n Floors: {self.floors} \n Size: {self.size}"

    def neuer_anstrich(self,color):
        self.color = color

myHouse = HAUS("Strasse",1,"Blau",10000,3,45)
myHouse2 = HAUS("Strasse",2,"Rot",210000,3,45)
myHouse3 = HAUS("Strasse",3,"Gruen",10000,3,45)

haus_liste = [myHouse,myHouse2,myHouse3]

haus_liste.pop()

#for i in haus_liste:
#    print(str(i.street))


neue_haus_liste = []


for i in haus_liste:
    if i.price > 200000:
        pass
    else:
        neue_haus_liste.append(i)


for i in neue_haus_liste:
    print(str(i))
