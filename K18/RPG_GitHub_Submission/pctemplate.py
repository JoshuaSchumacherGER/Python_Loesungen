
class Pctemplate():
    def __init__(self, hp = 0, init = 0):
        self.hp = hp
        self.init = init
        self.defense = 0
        self.dmgmod = 1
    
    #def fist_hit(self, opponent):
    #    defense = opponent.get_defense
    #    dmg = random.randrange(1, 4) - defense
    #    opponent.set_hp(dmg)
    
    def get_healing(self, heal):
        self.hp += heal
        print(self.hp, " HP remaining.")
    
    def get_dmg(self, dmg):
        defense, mod = self.get_defstats()
        minus = mod * (dmg - defense)
        if minus < 0:
            minus = 0
        self.hp -= minus
        print(self.hp, " HP remaining.")
    
    def get_hp(self):
        return self.hp
    
    def get_defstats(self):
        return self.defense, self.dmgmod