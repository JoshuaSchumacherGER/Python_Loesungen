import random
from pctemplate import *

def charcreate():
    hp = random.randrange(1,10)
    init = random.randrange(1,8)
    return Warrior(hp, init)

class Warrior(Pctemplate):
    def __init__(self, hp = 0, init = 0):
        self.hp = hp
        self.init = init
        self.defense = 0
        self.dmgmod = 1
        self.pt = True
        self.pots = 1
        print("'Tis but a scratch!")
    
    
    def turn(self, opponent):

        action = {
            "Swordattack"  : self.swordattack,
            "Shieldblock"  : self.shieldblock,
            "Healthpotion" : self.healthpotion
        }

        self.defense = 0

        while True:
            print("Choose your action:")
            print("""
            Swordattack
            Shieldblock
            Healthpotion""")
            self.move = input()
            if self.move in ("Swordattack", "Shieldblock", "Healthpotion"):
                self.move = action.get(self.move)
                self.move(opponent)
                break
            else:
                print("Not a valid action")
    
        
    def swordattack(self, opponent):
        print("Swordattack")
        dmg =random.randrange(1,7)
        opponent.get_dmg(dmg)

    def shieldblock(self, opponent):
        print("Shieldblock")
        self.defense = random.randrange(1, 4)
        

    def healthpotion(self, opponent):
        print("Healthpotion")
        if self.pots > 0:
            self.pots -= 1
            self.get_healing(random.randrange(1,4))
        else:
            print("No more Pots")
            self.turn(opponent)