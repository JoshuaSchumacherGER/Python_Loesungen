#Add Playerclasses-Folder to sys.path
import sys
sys.path.insert(0,'/home/dev/Git/Projekt--RPG-Fighting-Game/playerclasses')
#Inizialize Fight Mode
import json
import importlib

def read():
        with open("classes.json", "r") as infile:
            outfile = json.load(infile)
        return outfile

def game():

    #read out classes from classes.json
    classes = read()

    #import previously read classes
    for module in classes:
        importname = "playerclasses." + module
        globals()[module] = importlib.import_module(importname)

    #character creation Player1
    while True:
        p1class = input("Player 1 choose your class: ")
        if p1class in globals():
            p1class = globals()[p1class]
            player1 = p1class.charcreate()
            print(f"{player1.hp} and {player1.init}")
            break
        else:
            print("Not a valid class")
    
    #Charactercreation PLayer 2
    while True:
        p2class = input("Player 2 choose your class: ")
        if p2class in globals():
            p2class = globals()[p2class]
            player2 = p2class.charcreate()
            print(f"{player2.hp} and {player2.init}")
            break
        else:
            print("Not a valid class")

    #game start
    fight(player1, player2)

def fight(player1, player2):
    GAME = True

    #first turn for player 2 if his init is higher than player 1 init
    if player2.init > player1.init:
        print("Player 2 turn")
        player2.turn(player1)
        p1hp = player1.get_hp()
        if p1hp <= 0:
            print("Player 2 won!")
            GAME = False

    #Else here first turn
    while GAME:
        print("Player 1 turn")
        player1.turn(player2)
        p2hp = player2.get_hp()
        if p2hp <= 0:
            print("Player 1 won!")
            break
        print("Player 2 turn")
        player2.turn(player1)
        p1hp = player1.get_hp()
        if p1hp <= 0:
            print("Player 2 won!")
            break