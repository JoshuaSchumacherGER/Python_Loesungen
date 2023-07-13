import random
from pctemplate import *

def charcreate():
    hp = random.randrange(1,6)
    init = random.randrange(1,6)
    return Mage(hp, init)

class Mage(Pctemplate):
    def __init__(self, hp, init):
        self.hp = hp
        self.init = init
        self.defense = 0
        self.dmgmod = 1
        self.pt = True
        print("You're a wizard, Harry.")

    def turn(self, opponent):

        action = {
            "Fireball"      : self.Fireball,
            "Magic Missile" : self.Magic_Missile,
            "Mirror Images" : self.Mirror_Images,
            "Heal"          : self.Heal
        }

        while True:
            print("Choose your action:")
            print("""
            Fireball
            Magic Missile
            Mirror Images
            Heal""")
            if self.pt:
                self.move = input()
                if self.move in ("Fireball", "Magic Missile", "Mirror Images", "Heal"):
                    self.move = action.get(self.move)
                    self.move(opponent)
                    break
                else:
                    print("Not a valid action")
            else:
                self.move(opponent)
                break
            

    def Fireball(self, opponent):
        print("Fireball")
        if self.pt:
            self.pt = False
        else:
            self.pt = True
            dmg = random.randrange(1, 7) + random.randrange(1, 7)
            opponent.get_dmg(dmg)

    def Magic_Missile(self, opponent):
        print("Magic Missile")
        dmg = random.randrange(1, 6)
        opponent.get_dmg(dmg)

    def Mirror_Images(self, opponent):
        print("Mirror Images")
        self.dmgmod = 0

    def Heal(self, opponent):
        print("Heal")
        self.get_healing(random.randrange(1, 4))