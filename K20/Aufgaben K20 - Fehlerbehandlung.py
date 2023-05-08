def Aufgaben():
    print("A1: Fehlerbehandlung")
    print("----------------------------------------------------------------------------")

Aufgaben()
print("Welche Aufgabe soll ausgegeben werden?")
Aufgabe = input()
print("----------------------------------------------------------------------------")

if Aufgabe == "A1":
    # A1
    print("Aufgabe A1:")
    try:
        with open('test.txt', 'r') as file:
            # Dateioperationen durchführen
            print("Done")
    except FileNotFoundError:
        print("Die angegebene Datei konnte nicht gefunden werden. Überprüfen Sie den Pfad und den Dateinamen.")
    except PermissionError:
        print("Sie haben keine Berechtigung, auf die angegebene Datei zuzugreifen. Stellen Sie sicher, dass Sie die erforderlichen Berechtigungen besitzen.")
    except IsADirectoryError:
        print("Sie haben versucht, ein Verzeichnis statt einer Datei zu öffnen. Stellen Sie sicher, dass Sie die richtige Datei auswählen.")
    except UnicodeDecodeError:
        print("Die Datei ist nicht im erwarteten Format codiert. Wählen Sie das richtige Dateiformat oder geben Sie eine geeignete Codierung an.")
#####
#####
#####
else:
    print("Diese Aufgabe steht nicht zur Auswahl")
