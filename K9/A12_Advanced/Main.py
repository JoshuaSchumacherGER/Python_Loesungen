import player


def finish():
    if (playerOne.player.live <= 0):
        print("PlayerTwo Win !!!")
        return False
    if (playerTwo.player.live <= 0):
        print("PlayerOne Win !!!")
        return False
    return True


# Game
print("Player One:")
playerOne = player.Player()
playerOne.chose()

print("Player Two:")
playerTwo = player.Player()
playerTwo.chose()

play = False
if (playerOne.player.initiative > playerTwo.player.initiative):
    play = True

while (finish()):
    print()
    print("Player One:")
    playerOne.player.printData()
    print()
    print("Player Two:")
    playerTwo.player.printData()
    print()

    if (play):
        print("Player One Attack:")
        playerTwo.player.getDamage(playerOne.player.attack())
        play = False
    else:
        print("Player Two Attack:")
        playerOne.player.getDamage(playerTwo.player.attack())
        play = True
