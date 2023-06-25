# Python_Skript_v_1.11.pdf, Kapitel 22 Aufgabe 7
# Von Sascha Meissner / meissa.bsawis22     | 2023.06.25

# Arbeitsauftrag:
# Programmiere das Spiel Tic-Tac-Toe in einer GUI nach. Hierzu benötigst du das
# Spielfeld und 9 Buttons. Nacheinander können die Spieler jeweils ein X oder O setzen. Sofern ein Spieler
# gewinnt, soll das Spiel automatisch mit einer entsprechenden Nachricht beendet werden. Sind alle
# Buttons betätigt worden, aber kein Spieler hat gewonnen, erscheint die Nachricht „unentschieden“

# Hinweis: Im Folgenden kommentiere ich aus Gewohntheit vom Betrieb auf Englisch.

import tkinter as tk
from tkinter import messagebox as msgB

# Function for the player move. The function is called, whenever a player makes a move
# Returns: NONE
def player_move(row, column):
    global current_player, game_board
    
    # Check if the field is still free to be taken
    if game_board[row][column] != " ":
        return

    # Setting the game logic and text for the button to be displayed to the player(s)
    game_board[row][column] = current_player
    buttons[row][column].config(text = current_player)

    # Checking wheather or not the current player has won
    if check_win(current_player):
        msgB.showinfo("Spielende", "Spieler " + current_player + " hat gewonnen!")
        reset_game()
    # Checking if any field is still free to be taken
    elif check_draw():
        msgB.showinfo("Spielende", "Unentschieden!")
        reset_game()
    else:
        # Change the current player. Here the player is switched to the corresponding opponent
        current_player = "X" if current_player == "O" else "O"

# Function to check for a winner. The function takes the 
def check_win(player):
    for x in range(3):
        if game_board[x][0] == game_board[x][1] == game_board[x][2] == player:  # If 3 are set vertically by the player specified, return true
            return True
        if game_board[0][x] == game_board[1][x] == game_board[2][x] == player:  # If 3 are set horizontally by the player specified, return true
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player:      # If 3 are set across (left top to right bottom) by the player specified, return true
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == player:      # If 3 are set across (right top to left bottom) by the player specified, return true
        return True
    return False                                                                # Returns False if the player has not won

# Function to check for a draw.
# The function simply checks wheather or not any field is still empty
# Returns: BOOL
def check_draw():
    for row in game_board:      # Check every field in "game_board"
        if " " in row:          # Check wheather or not the field is empty
            return False
    return True                 # If no field is free to be set, the game has ended in a draw and the function therefor returns True

# Function to reset the game
# Returns: NONE
def reset_game():
    global current_player, game_board                           

    current_player = "X"                                        # Resets the current_player
    game_board = [[" " for _ in range(3)] for _ in range(3)]    # Reseting the game_board variable to have empty " " as values again
    for x in range(3):                                          # Resets the text for every textbox on the screen to " "
        for y in range(3):
            buttons[x][y].config(text=" ")

# Creating the tkinter window_main
window_main = tk.Tk()                                                # Creating the Tkinter-object using the default constructor Tk()
window_main.title("2023 TicTacToe")                                  # Since x already labeled the file "2023_TicTacToe.py", x decided for this title

# Initializing game variables
current_player = "X"                                            # Char variable saving the current player using X or O as symbol
game_board = [[" " for _ in range(3)] for _ in range(3)]        # 2d array consisting of 3x3 fields to save the player to, who took the field

# Creating the buttons for the game
buttons = [[0 for _ in range(3)] for _ in range(3)]             # 2d array consisting of 3x3 fields to save the buttons of tkinter to.
for x in range(3):
    for y in range(3):
        buttons[x][y] = tk.Button(window_main, text=" ", width=10, height=5, command=lambda row=x, column=y: player_move(row, column))
        buttons[x][y].grid(row=x, column=y)

# Reset button for the game
reset_button = tk.Button(window_main, text="Spiel zurücksetzen", command=reset_game) # Creates a button with the text "Spiel zurücksetzen". The button will use the already existing function "reset_game"
reset_button.grid(row=3, columnspan=3)                                          # Sets the button in the fourth row (3) and makes the button span 3 columns

window_main.mainloop()   # Tkinter mainloop

    



