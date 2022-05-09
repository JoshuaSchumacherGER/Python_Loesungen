# Kapitel 18 | char creation
# Author: Ali Abas Arsalahn
# Datum: 11.03.2022

from Creature import introduce_yourself
from Mage import Mage
from Warrior import Warrior


def main() -> None:
    player = Warrior(100, 'Pluschie', 1.56, 50, 100)
    player2 = Mage(100, 'Vaselina', 1.69, 9999, 100)

    print(player.fist_hit())
    print(player2.fist_hit())

    introduce_yourself(player, player2)
    print(player.__repr__())


if __name__ == '__main__':
    main()
