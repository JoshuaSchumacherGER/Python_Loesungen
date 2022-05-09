# Kapitel 18 | Class: Warrior
# Author: Ali Abas Arsalahn
# Datum: 11.03.2022

from Creature import Creature, introduce_yourself
from random import randrange


class Warrior(Creature):

    MAX_RAGE = 100
    fist_range = 4

    def __init__(self, hp: int, name: str, size: float, gold: int, rage: int):
        super().__init__(hp, name, size, gold)
        self._rage = rage

    def roll_dice(self, range: int) -> int:
        return randrange(1, range)

    def fist_hit(self) -> int:
        damage = self.roll_dice(self.fist_range)
        return damage

    def introduction(self) -> None:
        print(f"Hi. My name is {self.name}. I'm the strongest!")

    @property
    def rage(self):
        return self._rage

    @rage.setter
    def rage(self, value):
        if value < 0:
            self._rage = 0
        elif value > self._rage:
            self._rage = self.MAX_RAGE
