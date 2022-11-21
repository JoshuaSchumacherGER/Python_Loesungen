import warrior
import mage
import rouge


class Player:
    def __init__(self):
        self.player = None

    def chose(self):
        while (True):
            inputUser = (
                input("Which Chraracter you chose? (Warrior,Mage,Rouge): ")).lower()
            if (inputUser == "warrior"):
                self.player = warrior.Warrior()
                break
            if (inputUser == "mage"):
                self.player = mage.Mage()
                break
            if (inputUser == "rouge"):
                self.player = rouge.Rouge()
                break
            print("Wrong input")
