import random
import time
Spieler1 = 0
Spieler2 = 0

InitiativeK2 = 0

        
LebenspunkteK2 = 0


def Krieger1():
    global InitiativeK  
    InitiativeK = random.randint(10,18) #Höhere Initiative = macht den ersten Angriff

    global LebenspunkteK
    LebenspunkteK = random.randint(1,10) #Lebenspunkte werden zufällig generiert

def Krieger_Faehigkeiten1():
    global SchwertschlagK1
    SchwertschlagK1 = random.randint(1,7) #Kann zwischen 1 und 7 Schaden machen.
    
    Schildblock = random.randint(1,4) #Veringert den Schaden des nächsten Angriffs des Gegners zwischen 1 und 4
    Heilung = random.randint(1,6) #Heilt den Charakter zwischen 1 und 6 Leben. Kann nur einmal verwendet werden.

def Magier1():
    global InitiativeM
    InitiativeM = random.randint(1,6) #Höhere Initiative = macht den ersten Angriff

    global LebenspunkteM
    LebenspunkteM = random.randint(1,6) #Lebenspunkte werden zufällig generiert

def Magier_Faehigkeiten1():

    Feuerball = random.randint(2,7) #Kann zwischen 2 und 7 Schaden machen. Bennötigt eine Runde zum aufladen. Kann in der zweiten Runde abgefeuert werden.
    Magic_Missle = random.randint(1,6) #Kann zwischen 1 und 6 Schaden machen.
    Spiegelbilder = random.randint(0,1) #Mit einer Wahrscheinlichkeit von 50% wird kein Schaden am Magier1 für 2 Angriffe verursacht.
    Kleine_Heilung = random.randint(1,4) #Heilt den Charakter zwischen 1 und 4 Leben. Kann nur einmal verwendet werden.

def Schurke1():
    global InitiativeS
    InitiativeS = random.randint(1,10) #Höhere Initiative = macht den ersten Angriff

    global LebenspunkteS
    LebenspunkteS = random.randint(1,8) #Lebenspunkte werden zufällig generiert

def Schurke_Faehigkeiten1():

    Sneak_Attack = random.randint(1,3) #Falls der Schurke1 zuerst angreift. Dann fügt der nächste Angriff zusätzlich 1d3 Schaden zu.
    Dolchangriff = random.randint(1,4) #2x 1d4 Schaden
    Schmutz = random.randint(0,1) #Der Schurke1 wirft dem Gegner Dreck in die Augen. Trifft er, verursacht der nächste Angriff keinen Schaden.
    Heilung = random.randint(1,6) #Heilt den Charakter zwischen 1 und 6 Leben. Kann nur einmal verwendet werden.

#-----------------------------------------------------------------------------------------#
#Spieler 2 Funktionen
def Krieger2():
    InitiativeK2 = random.randint(1,8) #Höhere Initiative = macht den ersten Angriff

    LebenspunkteK2 = random.randint(1,10) #Lebenspunkte werden zufällig generiert
 

def Krieger_Faehigkeiten2():

    Schwertschlag2 = random.randint(1,7) #Kann zwischen 1 und 7 Schaden machen.
    Schildblock2 = random.randint(1,4) #Veringert den Schaden des nächsten Angriffs des Gegners zwischen 1 und 4
    Heilung2 = random.randint(1,6) #Heilt den Charakter zwischen 1 und 6 Leben. Kann nur einmal verwendet werden.

def Magier2():
    global InitiativeM2
    InitiativeM2 = random.randint(1,6) #Höhere Initiative = macht den ersten Angriff

    global LebenspunkteM2
    LebenspunkteM2 = random.randint(1,6) #Lebenspunkte werden zufällig generiert

def Magier_Faehigkeiten2():

    Feuerball2 = random.randint(2,7) #Kann zwischen 2 und 7 Schaden machen. Bennötigt eine Runde zum aufladen. Kann in der zweiten Runde abgefeuert werden.
    Magic_Missle2 = random.randint(1,6) #Kann zwischen 1 und 6 Schaden machen.
    Spiegelbilder2 = random.randint(0,1) #Mit einer Wahrscheinlichkeit von 50% wird kein Schaden am Magier1 für 2 Angriffe verursacht.
    Kleine_Heilung2 = random.randint(1,4) #Heilt den Charakter zwischen 1 und 4 Leben. Kann nur einmal verwendet werden.

def Schurke2():
    global InitiativeS2
    InitiativeS2 = random.randint(1,10) #Höhere Initiative = macht den ersten Angriff

    global LebenspunkteS2
    LebenspunkteS2 = random.randint(1,8) #Lebenspunkte werden zufällig generiert

def Schurke_Faehigkeiten2():

    Sneak_Attack2 = random.randint(1,3) #Falls der Schurke1 zuerst angreift. Dann fügt der nächste Angriff zusätzlich 1d3 Schaden zu.
    Dolchangriff2 = random.randint(1,4) #2x 1d4 Schaden
    Schmutz2 = random.randint(0,1) #Der Schurke1 wirft dem Gegner Dreck in die Augen. Trifft er, verursacht der nächste Angriff keinen Schaden.
    Heilung2 = random.randint(1,6) #Heilt den Charakter zwischen 1 und 6 Leben. Kann nur einmal verwendet werden.




print("D&D wird geladen...")
time.sleep(1)
print("Spieler 1. Welchen Charakter möchtest du wählen?")
time.sleep(1)

Auswahl = 0

while Auswahl != 1:
    Charakter_Spieler1 = input("Spieler 1. Du hast die Auswahl zwischen Magier, Schurke und Krieger!")
    if Charakter_Spieler1 == "Magier":
        print("Du hast den Charakter Magier ausgewählt!")
        Auswahl +=1
    elif Charakter_Spieler1 == "Schurke":
        print("Du hast den Charakter Schurke ausgewählt!")
        Auswahl +=1
    elif Charakter_Spieler1 == "Krieger":
        print("Du hast den Charakter Krieger ausgewählt!")
        Auswahl +=1
    else :
        print("Diesen Charakter gibt es nicht")

time.sleep(1)
print("------------------------------------")

print("Spieler 2. Welchen Charakter möchtest du wählen?")
time.sleep(1)

Auswahl2 = 0

while Auswahl2 != 1:
    Charakter_Spieler2 = input("Spieler 1. Du hast die Auswahl zwischen Magier, Schurke und Krieger!")
    if Charakter_Spieler2 == "Magier":
        print("Du hast den Charakter Magier ausgewählt!")
        Auswahl2 +=1
    elif Charakter_Spieler2 == "Schurke":
        print("Du hast den Charakter Schurke ausgewählt!")
        Auswahl2 +=1
    elif Charakter_Spieler2 == "Krieger":
        print("Du hast den Charakter Krieger ausgewählt!")
        Auswahl2 +=1
    else :
        print("Diesen Charakter gibt es nicht")

time.sleep(1)
print("------------------------------------")

K1 = 0 #Gewählter Charakter ==> Krieger1 Player 1
S1 = 0 #Gewählter Charakter ==> Schurke1 Player 1
M1 = 0 #Gewählter Charakter ==> Magier1 Player 1


K2 = 0 #Gewählter Charakter ==> Krieger1 Player 2
S2 = 0 #Gewählter Charakter ==> Schurke1 Player 2
M2 = 0 #Gewählter Charakter ==> Magier1 Player 2

time.sleep(1)
if Charakter_Spieler1 == 'Krieger':
    K1  += 1
    Krieger1()
    print("Deine Initiative beträgt: ",InitiativeK," Spieler 1.")
    time.sleep(1)
    print("Du hast: ",LebenspunkteK," Lebenspunkte."," Spieler 1.")
elif Charakter_Spieler1 == 'Schurke':
    S1 += 1
    Schurke1()
    print("Deine Initiative beträgt: ",InitiativeS," Spieler 1.")
    time.sleep(1)
    print("Du hast: ",LebenspunkteS," Lebenspunkte."," Spieler 1.")
else :
    M1 += 1
    Magier1()
    print("Deine Initiative beträgt: ",InitiativeM," Spieler 1.")
    time.sleep(1)
    print("Du hast: ",LebenspunkteM," Lebenspunkte."," Spieler 1.")

print("------------------------------------------------------------")
time.sleep(1)

if Charakter_Spieler2 == 'Krieger':
    K2 += 1
    Krieger2()
    print("Deine Initiative beträgt: ",InitiativeK2," Spieler 2.")
    time.sleep(1)
    print("Du hast: ",LebenspunkteK2," Lebenspunkte."," Spieler 2.")
elif Charakter_Spieler2 == 'Schurke':
    S2 += 1
    Schurke2()
    print("Deine Initiative beträgt: ",InitiativeS2," Spieler 2.")
    time.sleep(1)
    print("Du hast: ",LebenspunkteS2," Lebenspunkte."," Spieler 2.")
else :
    M2 += 1
    Magier2()
    print("Deine Initiative beträgt: ",InitiativeM2," Spieler 2.")
    time.sleep(1)
    print("Du hast: ",LebenspunkteM2," Lebenspunkte."," Spieler 2.")

time.sleep(1)

Spieler1 =  0
Spieler2 =  0

if K1 == 1: #Charakter Krieger 1 wurde ausgewählt
    if K2 == 1:
        if InitiativeK == InitiativeK2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            KK = random.randint(0,1)
            time.sleep(1)
            if KK == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1
        elif InitiativeK > InitiativeK2:
            Spieler1 += 1
        else:
            Spieler2 += 1
    elif S2 == 1:
        if InitiativeK == InitiativeS2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            KS = random.randint(0,1)
            time.sleep(1)
            if KS == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.") 
                Spieler2 += 1
        elif InitiativeK > InitiativeS2:
            Spieler1 += 1
        else:
            Spieler2 +=1                   
    elif M2 == 1:
        if InitiativeK == InitiativeM2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            KM = random.randint(0,1)
            time.sleep(1)
            if KM == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1
        elif InitiativeK > InitiativeM2:
            Spieler1 += 1
        else:
            Spieler2 += 1
elif S1 == 1: #Charakter Schurke1 wurde ausgewählt
    if K2 == 1:
        if InitiativeS == InitiativeK2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            SK = random.randint(0,1)
            time.sleep(1)
            if SK == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1
        elif InitiativeS > InitiativeK2:
            Spieler1 += 1
        else:
            Spieler2 += 1
    elif S2 == 1:
        if InitiativeS == InitiativeS2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")  
            SS = random.randint(0,1)
            time.sleep(1)
            if SS == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")  
                Spieler2 += 1    
        elif InitiativeS > InitiativeS2:
            Spieler1 += 1
        else:
            Spieler2 += 1    
    elif M2 == 1:
        if InitiativeS == InitiativeM2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            SM = random.randint(0,1)
            time.sleep(1)
            if SM == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1
        elif InitiativeS > InitiativeM2:
            Spieler1 += 1
        else:
            Spieler2 += 1   
elif M1 == 1: #Charakter Magier1 wurde ausgewählt
    if K2 == 1:
        if InitiativeM == InitiativeK2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            MK = random.randint(0,1)
            time.sleep(1)
            if MK == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1
        elif InitiativeM > InitiativeK2:
            Spieler1 += 1
        else:
            Spieler2 += 1   
    elif S2 == 1:
        if InitiativeM == InitiativeS2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            MS = random.randint(0,1)
            time.sleep(1)
            if MS == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1  
        elif InitiativeM > InitiativeS2:
            Spieler1 += 1
        else:
            Spieler2 += 1            
    elif M2 == 1:
        if InitiativeM == InitiativeM2:
            print("Die Initiative der beiden Charaktere ist gleich.")
            print("Es wird neu ermittelt welcher Charakter anfängt.")
            MM = random.randint(0,1)
            time.sleep(1)
            if MM == 0:
                print("Spieler 1 fängt an.")
                Spieler1 += 1
            else:
                print("Spieler 2 fängt an.")
                Spieler2 += 1
        elif InitiativeM > InitiativeM2:
            Spieler1 += 1
        else:
            Spieler2 += 1 

def Zug_P1():
    Zug = 0
    print("Spieler 1. Du hast den ersten Zug!")
    while(Zug != 1):
        FähigkeitK1= int(input("Du kanst Schwertschlag mit 1 wählen: "))
        if FähigkeitK1 == 1:
                Krieger_Faehigkeiten1()
                print(SchwertschlagK1) 
                Zug += 1
                if K2 == 1:
                    if LebenspunkteK2 < SchwertschlagK1 or LebenspunkteK2 == SchwertschlagK1:
                        LebenspunkteK2 = 0
                        print("Der Schwertschlag von Spieler 1 hat dich getroffen. Du hast "+SchwertschlagK1+" Lebenspunkte verloren" )
                        print("Der Schwertschlag hat dir mehr Schaden gemacht als du besitzt.")
                    else:
                        SchwertschlagK1 - LebenspunkteK2
                        print("Der Schwertschlag von Spieler 1 hat dich getroffen. Du hast ",SchwertschlagK1," Lebenspunkte verloren" )
                        print("Du hast noch ",LebenspunkteK2," übrig")


                elif M2 == 1:
                    if LebenspunkteM2 < SchwertschlagK1:
                        LebenspunkteM2 = 0
                        print("Der Schwertschlag von Spieler 1 hat dich getroffen. Du hast "+SchwertschlagK1+" Lebenspunkte verloren" )
                        print("Der Schwertschlag hat dir mehr Schaden gemacht als du besitzt.")
                    else:
                        SchwertschlagK1 - LebenspunkteM2
                        print("Der Schwertschlag von Spieler 1 hat dich getroffen. Du hast "+SchwertschlagK1+" Lebenspunkte verloren" )
                        print("Du hast noch "+LebenspunkteM2+" übrig")
                elif S2 == 1:
                    if LebenspunkteS2 <= SchwertschlagK1:
                        LebenspunkteM
                        LebenspunkteS2 = 0
                        print("Der Schwertschlag von Spieler 1 hat dich getroffen. Du hast "+SchwertschlagK1+" Lebenspunkte verloren" )
                        print("Der Schwertschlag hat dir mehr Schaden gemacht als du besitzt.")
                    else:
                        SchwertschlagK1 - LebenspunkteS2
                        print('Der Schwertschlag von Spieler 1 hat dich getroffen. Du hast '+SchwertschlagK1+'Lebenspunkte verloren')
                        print("Du hast noch "+LebenspunkteS2+" übrig")
                
                

        else:
            print("Diese Fähigkeit gibt es nicht")
        #if Charakter_Spieler1 == K1:
           # while FähigkeitK1 != 1:
                #FähigkeitK1= input("Du kanst Schwertschlag mit 1 wählen")
            #if FähigkeitK1 == 1:
            #    print(SchwertschlagK1)    
        #elif Charakter_Spieler1 == M1:
        #    print("Maier 1")
        #elif Charakter_Spieler1 == S1:
        #    print("Schurke 1")

if Spieler1 == 1:
    print(Zug_P1())

elif Spieler2 == 1:
    print("Spieler 2. Du hast den ersten Zug!")

    


time.sleep(3)
print("Programm wird beendet.")
time.sleep(0.2)
print(".")
for x in range(1,10):
            time.sleep(0.1)
            print(x*".")

