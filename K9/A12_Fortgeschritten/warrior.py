import random


class Warrior:
    def __init__(self):
        self.initiative = random.randint(1, 8)
        self.live = random.randint(1, 10)
        self.heal = False
        self.schield = 0

    def swordstroke(self):
        damage = random.randint(1, 7)
        print("Damage: ", damage)
        return damage

    def schieldblock(self):
        schield = random.randint(1, 4)
        print("Next Attack decrease by", schield)
        self.schield = self.schield+schield

    def healthpotion(self):
        healing = random.randint(1, 6)
        self.live = self.live+healing
        print("Character healing ", healing)

    def attack(self):
        while (True):
            choise = input(
                "Which Attack? (1=SwordStroke, 2=SchieldBlock, 3=Healthpotion): ")
            if (choise == "1"):
                return self.swordstroke()
            if (choise == "2"):
                self.schieldblock()
                return 0
            if (choise == "3"):
                if (self.heal == False):
                    self.heal = True
                    self.healthpotion()
                    return 0
                else:
                    print("Healing allready used")
            print("Wrong Input")

    def getDamage(self, damage):
        if (self.schield != 0):
            damage = damage-self.schield
            if (damage < 0):
                self.schield = +damage
                damage = 0

        self.live -= damage

    def printData(self):
        print("Live: ", self.live)
        if (self.heal):
            print("Healpotion already used")
        else:
            print("Healpotion is ready")
        if (self.schield != 0):
            print("Schield: ", self.schield)
        else:
            print("No Schield")
