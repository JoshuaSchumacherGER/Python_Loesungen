import random


class Mage:
    def __init__(self):
        self.initiative = random.randint(1, 6)
        self.live = random.randint(1, 6)
        self.charged = False
        self.heal = False
        self.noDamage = 0

    def fireball(self):
        damage = random.randint(2, 7)
        print("Damage: ", damage)
        return damage

    def magicMissile(self):
        damage = random.randint(1, 6)
        print("Damage: ", damage)
        return damage

    def mirrorImages(self):
        rand = random.randint(1, 2)
        if (rand == 1):
            self.noDamage = 2
            print("No Damage for two rounds")
        else:
            print("Fail")

    def smallhealing(self):
        healing = random.randint(1, 4)
        self.live = self.live+healing
        print("Character healing ", healing)

    def attack(self):
        while (True):
            choise = input(
                "Which Attack? (1=Fireball, 2=MagicMissile, 3=MirrorImage, 4=SmallHealing): ")
            if (choise == "1"):
                if (self.charged == True):
                    self.charged = False
                    return self.fireball()
                else:
                    print("Fireball is charged")
                    self.charged = True
                    return 0
            if (choise == "2"):
                return self.magicMissile()
            if (choise == "3"):
                self.mirrorImages()
                return 0
            if (choise == "4"):
                if (self.heal == False):
                    self.heal = True
                    self.smallhealing()
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
        if (self.charged):
            print("Fireball is ready")
        else:
            print("Fireball is not ready")
        if (self.noDamage != 0):
            print("Schield for", self.noDamage, "Round/s")
        else:
            print("No Schield")

    def getDamage(self, damage):
        if (self.noDamage == 0):
            self.live = self.live-damage
        else:
            self.noDamage -= 1
