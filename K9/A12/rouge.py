import random


class Rouge:
    def __init__(self):
        self.initiative = random.randint(1, 10)
        self.live = random.randint(1, 8)
        self.nextattack = 0
        self.noDamage = False
        self.heal = False

    def sneakattack(self):
        attack = random.randint(1, 3)
        print("Next Attack", attack, "more damage")
        self.nextattack = self.nextattack+attack

    def daggerattack(self):
        attackOne = random.randint(1, 4)
        attackTwo = random.randint(1, 4)
        print("Damage: ", attackOne, attackTwo)
        return attackOne+attackTwo

    def dust(self):
        dust = random.randint(1, 3)
        if (dust == 2):
            self.noDamage = True
            print("Next Round no Damage")
        else:
            print("Dust no hit")

    def healthpotion(self):
        healing = random.randint(1, 6)
        self.live = self.live+healing
        print("Character healing ", healing)

    def attack(self):
        while (True):
            choise = input(
                "Which Attack? (1=SneakAttack, 2=DaggerAttack, 3=Dust, 4=HealthPotion): ")
            if (choise == "1"):
                self.sneakattack()
                return 0
            if (choise == "2"):
                temp = self.nextattack
                self.nextattack = 0
                return self.daggerattack()+temp
            if (choise == "3"):
                self.dust()
                return 0
            if (choise == "4"):
                if (self.heal == False):
                    self.heal = True
                    self.healthpotion()
                    return 0
                else:
                    print("Healing already used")
            print("Wrong Input")

    def printData(self):
        print("Live: ", self.live)
        if (self.heal):
            print("Healpotion already used")
        else:
            print("Healpotion is ready")
        if (self.noDamage):
            print("Next Attack. No Damage")

    def getDamage(self, damage):
        if (self.noDamage):
            self.noDamage = False
            print("No Damage because of Dust")
        else:
            self.live -= damage
