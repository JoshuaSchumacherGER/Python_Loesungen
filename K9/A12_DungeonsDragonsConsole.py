""" ===========================
    $Creator: Matthias Stefan $
    =========================== """


import random
import abc
from os import system
 
class GameState:
    def __init__(self):
        self.running = False
        self.round = 0
        
        self.player = []
        self.first_player = None
        self.second_player = None

    def init_game(self):
        while self.player[0].initiative == self.player[1].initiative:
            self.player[0].change_initiative()
            self.player[1].change_initiative()
        if self.player[0].initiative > self.player[1].initiative:
            self.first_player = self.player[0]
            self.second_player = self.player[1]
        else:
            self.first_player = self.player[1]
            self.second_player = self.player[0]
        self.running = True

    def switch_player(self):
        temp = self.first_player
        self.first_player = self.second_player
        self.second_player = temp

    def select_class(self):
        system('cls')
        print("1: Warrior\n2: Mage\n3: Villain")
        for i in range(0, 2):
            valid_selection = False
            while valid_selection == False:
                selection = int(input())
                if selection == 1:
                    valid_selection = True
                    self.player.append(Warrior())
                elif selection == 2:
                    valid_selection = True
                    self.player.append(Mage())
                elif selection == 3:
                    valid_selection = True
                    self.player.append(Villain())
        system('cls')

    def end_game(self):
        if self.player[0].life_points <= 0:
            print(f"{self.player[1]} wins")
        else:
            print(f"{self.player[0]} wins")



class Dice:
    def roll(maxNumber: int) -> int:
        result = random.randint(1, maxNumber)
        return result

    def heads_or_tails() -> bool:
        result = random.randint(0, 1)
        return True if result == 1 else False




class Character(abc.ABC):
    def __init__(self, initiative, life_points):
        self.base_life_points = 10
        self.initiative = Dice.roll(initiative)
        self.life_points = self.base_life_points + Dice.roll(life_points)

    @abc.abstractmethod
    def start_action():
        pass

    @abc.abstractmethod
    def end_action() -> None: 
        pass

    @abc.abstractmethod
    def deal_damage() -> int:
        pass

    @abc.abstractmethod
    def take_damage(damage: int) -> None:
        pass 

    @abc.abstractmethod
    def print_skills() -> None:
        pass

    @abc.abstractmethod
    def change_initiative() -> None:
        pass 

    @abc.abstractmethod
    def drink_potion() -> None:
        pass

class Warrior(Character):
    def __init__(self):
        self.max_warrior_initiative = 8
        self.max_warrior_life_points = 10
        self.max_warrior_damage = 7
        self.max_warrior_shield = 4 

        self.effect_shield_block = False
        self.healing_potion = 1
        super().__init__(self.max_warrior_initiative, self.max_warrior_life_points)

    def start_action(self):
        valid_action = False
        while valid_action == False:
            action = int(input())
            if action == 1:
                valid_action = True
                return self.deal_damage()
            elif action == 2:
                valid_action = True
                self.effect_shield_block = True
            elif action == 3 and self.healing_potion > 0:
                valid_action = True
                self.drink_potion()

    def end_action(self) -> None:
        return

    def deal_damage(self) -> int:
        damage = Dice.roll(self.max_warrior_damage)
        print(f"Warrior tries to deal {damage} damage")
        return damage

    def take_damage(self, damage: int) -> None:
        if self.effect_shield_block == True:
            reduce_damage = Dice.roll(self.max_warrior_shield)
            damage -= reduce_damage
            self.effect_shield_block = False
        if damage > 0:
            self.life_points -= damage
        print(f"Warrior suffers {damage} damage")

    def print_skills(self) -> None:
        print(f"\nWarrior\ninitiative: {self.initiative}\nlife points: {self.life_points}\n1: sword strike\n2: shield block\n3: healthpotion ({self.healing_potion})\n-------------------")

    def change_initiative(self) -> None:
        self.initiative = Dice.roll(self.max_warrior_initiative)

    def drink_potion(self) -> None:
        self.life_points += Dice.roll(6)
        self.healing_potion -= 1


class Mage(Character):
    def __init__(self):
        self.max_mage_initiative = 6
        self.max_mage_life_points = 6
        self.max_mage_fireball = 7
        self.max_mage_missile = 4 

        self.cast_fireball = False
        self.effect_mirror = 0
        self.healing_potion = 1
        super().__init__(self.max_mage_initiative, self.max_mage_life_points)

    def start_action(self):
        if self.cast_fireball == True:
            return self.deal_damage()
        valid_action = False
        while valid_action == False:
            action = int(input())
            if action == 1:
                valid_action = True
                return self.load_fireball()
            elif action == 2:
                valid_action = True
                return self.deal_damage()
            elif action == 3 and self.healing_potion > 0:
                valid_action = True
                self.drink_potion()
            elif action == 4:
                valid_action = True
                self.cast_mirror()
            
    def end_action(self) -> None:
        pass

    def deal_damage(self) -> int:
        if self.cast_fireball == True:
            damage = Dice.roll(self.max_mage_fireball)
            damage += Dice.roll(self.max_mage_fireball)
            self.cast_fireball = False
            print(f"Mage tries to deal {damage} damage")
            return damage
        else:
            damage = Dice.roll(self.max_mage_missile)
            print(f"Mage tries to deal {damage} damage")
            return damage

    def take_damage(self, damage: int) -> None:
        if self.effect_mirror != 0:
            anulate = Dice.heads_or_tails()
            if anulate == False:
                self.life_points -= damage
                print(f"Mage suffers {damage} damage")
        else:
            self.life_points -= damage
            print(f"Mage suffers {damage} damage")
    
    def print_skills(self) -> None:
        print(f"\nMage\ninitiative: {self.initiative}\nlife points: {self.life_points}\n1: fireball\n2: magic missile\n3: healthpotion ({self.healing_potion})\n4: magic mirror\n-------------------")

    def change_initiative(self) -> None:
        self.initiative = Dice.roll(self.max_mage_initiative)

    def drink_potion(self) -> None:
        self.life_points += Dice.roll(4)
        self.healing_potion -= 1

    def load_fireball(self) -> None:
        if self.cast_fireball == False:
            self.cast_fireball = True

    def cast_mirror(self) -> None:
        self.effect_mirror = 2


class Villain(Character):
    def __init__(self):
        self.max_villain_initiative = 10
        self.max_villain_life_points = 8
        self.max_villain_dagger = 4 

        self.sneak_attack = True
        self.protected = False
        self.healing_potion = 1
        super().__init__(self.max_villain_initiative, self.max_villain_life_points)

    def start_action(self):
        valid_action = False
        while valid_action == False:
            action = int(input())
            if action == 1:
                valid_action = True
                return self.deal_damage()
            elif action == 2:
                valid_action = True
                return self.throw_mud()
            elif action == 3 and self.healing_potion > 0:
                valid_action = True
                self.drink_potion()

    def end_action(self) -> None: 
        return

    def deal_damage(self) -> int:
        damage = Dice.roll(self.max_villain_dagger)
        damage += Dice.roll(self.max_villain_dagger)
        if self.sneak_attack == True:
            damage += Dice.roll(3)
            self.sneak_attack = False
        print(f"Villain tries to deal {damage} damage")
        return damage

    def take_damage(self, damage: int) -> None:
        self.sneak_attack = False
        if self.protected == False:
            self.life_points -= damage
        print(f"Villain suffers {damage} damage")

    def print_skills(self) -> None:
        print(f"\nVillain\ninitiative: {self.initiative}\nlife points: {self.life_points}\n1: dagger\n2: mud\n3: healthpotion ({self.healing_potion})\n-------------------")

    def change_initiative(self) -> None:
        self.initiative = Dice.roll(self.max_villain_initiative)

    def drink_potion(self) -> None:
        self.life_points += Dice.roll(6)
        self.healing_potion -= 1

    def throw_mud(self) -> None:
        hit = Dice.heads_or_tails()
        if hit == True:
            self.protected == True


if __name__ == '__main__':
    gameState = GameState()
    gameState.select_class()
    gameState.init_game()

    while gameState.running == True:
        gameState.round += 1
        for i in range(0, 2):
            active_player = gameState.first_player
            idle_player = gameState.second_player   
            active_player.print_skills()
            value = active_player.start_action()
            if value != None:
                idle_player.take_damage(value)
            if idle_player.life_points <= 0:
                gameState.running = False
                break
            gameState.switch_player()
        active_player.end_action()
        idle_player.end_action()
        system('cls')
    
    gameState.end_game()












        