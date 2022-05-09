# Kapitel 18 | ABC: Creature
# Author: Ali Abas Arsalahn
# Datum: 11.03.2022


from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, hp: int, name: str, size: float, gold: int):
        self.hp = hp
        self.name = name
        self.size = size
        self._gold = gold

    def __repr__(self) -> str:
        rep = f"{self.name}, {str(self.size)}, {str(self.gold)}"
        return rep

    def __str__(self) -> str:
        pass

    @abstractmethod
    def roll_dice(self):
        pass

    @abstractmethod
    def fist_hit(self):
        pass

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        if value < 0:
            self.gold = 0
        elif value > 10000:
            self.gold = 10000
        else:
            self.gold = value


def introduce_yourself(*args: object) -> None:
    for object in args:
        object.introduction()
