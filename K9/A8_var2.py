#Aufgabe K9 | A8: Schreibe eine Methode „cancel“, 
# die solange Eingaben vom Benutzer annimmt, bis dieser das Wort „Beenden“ eintippt. 
# Das Programm wird dann entsprechend beendet!
while(True):
    x=input("Gib etwas ein.")
    if(x=="Beenden"):
        print("Game Over")
        break