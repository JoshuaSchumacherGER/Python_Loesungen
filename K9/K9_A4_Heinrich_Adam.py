# Eine Funktion "ende"
# die Zahlen vom Benutzer einliest,
# bis dieser eine 0 eingibt

def ende():

    x = 1

    while x != 0:
        x = int(input("Zahl eingeben (0 zum beenden): "))

    print("Programm beendet")


ende()
