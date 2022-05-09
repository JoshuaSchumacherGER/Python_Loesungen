# Kapitel 18 | Mage
# Author: Ali Abas Arsalahn
# Datum: 11.03.2022


from Creature import Creature, introduce_yourself
from random import randrange


class Mage(Creature):

    MAX_MANA = 100
    fist_range = 3

    def __init__(self, hp: int, name: str, size: float, gold: int, mana: int):
        super().__init__(hp, name, size, gold)
        self._mana = mana

    def roll_dice(self, range: int) -> int:
        return randrange(1, range)

    def fist_hit(self) -> int:
        damage = self.roll_dice(self.fist_range)
        return damage

    def introduction(self) -> print:
        print(f"Hi. My name is {self.name}. I'm the smartest!")

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        try:
            value = int(value)
        except ValueError:
            pass
        finally:
            self._mana = value
