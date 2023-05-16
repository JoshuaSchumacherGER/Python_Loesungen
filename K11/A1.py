#K11 A1
tel={
    "Arbeit":{"Jan":"50","Mark":"81"},
    "private":{"Julia":"0151438924","Mark":"061932834"}
}

print(len(tel))                             #Dieser Befehl gibt die Anzahl der Schlüsselwert-Paare aus.
print(len(tel["Arbeit"]))                   #Dieser Befehl gibt die Anzahl der Elemente mit dem Schlüssel "Arbeit" aus.
print(tel["Arbeit"].get("Mark"))            #Dieser Befehl gibt den Wert des Elements "Mark" im Schlüssel "Arbeit" aus.
print("Jan" in tel["Arbeit"])               #Dieser Befehl checkt ob der Wert "Jan" im Schlüssel "Arbeit" vorhanden ist.
print(list(tel["private"].values()))        #Dieser Befehl gibt die Werte des Schlüssels "private" aus
print(tel["private"].copy())                #Dieser Befehl kopiert die Werte des Schlüssels "private"