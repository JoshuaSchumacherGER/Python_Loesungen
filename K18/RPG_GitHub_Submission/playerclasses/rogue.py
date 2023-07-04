import random
from pctemplate import *

def charcreate():
    hp = random.randrange(1,8)
    init = random.randrange(1, 10)
    return Rogue(hp, init)

class Rogue(Pctemplate):
    def __init__(self, hp, init):
        self.hp = hp
        self.init = init
        self.defense = 0
        self.dmgmod = 1
        self.pt = True
        self.pots = 1
        print("What doesn't kill you isn't finished yet.")
    
    
    def turn(self, opponent):

        action = {
            "Daggers"      : self.Daggers,
            "Dirt"         : self.Dirt,
            "Healthpotion" : self.Healthpotion
        }

        while True:
            print("Choose your action:")
            print("""
            Daggers
            Dirt
            Healthpotion""")
            self.move = input()
            if self.move in ("Daggers", "Dirt", "Healthpotion"):
                self.move = action.get(self.move)
                self.move(opponent)
                break
            else:
                print("Not a valid action")
    
    

    def Daggers(self, opponent):
        print("Daggers")

    def Dirt(self, opponent):
        print("Dirt")

    def Healthpotion(self, opponent):
        print("Healthpotion")
        if self.pots > 0:
            self.pots -=1
            self.get_healing(random.randrange(1,4))
        else:
            print("No more Pots")
            self.turn(opponent)