#Aufgabe K11 | A1: Folgendes Dictionary ist gegeben:

tel = {
'arbeit': {'Jan': '50', 'Mark': '81'},
'private': {'Julia': '0151438924' , 'Mark': '016932834'}
}

#Welche Ausgaben liefern folgende Befehle:
"""
len(tel)                              #1. Ausgabe => 2    | in tel befinden sich 2 x Key/Value - arbeit , private , auch wenn diese selbst nochmal Dictionarys sind.
len(tel['arbeit'])                    #2. Ausgabe => 2    | in arbeit befinden sich 2 x Key/Value
tel['arbeit'].get('Mark')             #3. Ausgabe => 81   | ruft aus 'arbeit' den Value '81' zum Key 'Mark' auf
'Jan' in tel['arbeit']                #4. Ausgabe => True | prüft ob Jan in 'arbeit' vorkommt
list(tel['private'].values())         #5. Ausgabe => ['0151438924', '016932834'] | nennt alle Values von 'private'
tel['private'].copy()                 #6. Ausgabe => {'Julia': '0151438924', 'Mark': '016932834'} | Kopie des Dictionary.
"""

#_____________ A2 _____________

#Ändere nachträglich die interne Durchwahl von Mark zu 80.

arbeit1 = {'Mark':'80'}
tel['arbeit'].update(arbeit1)

print(list(tel['arbeit'].values()))          #Zeile nicht notwendig, nur zum prüfen ob es funktioniert hat.

#Lösche den Eintrag von Julia inkl. Handynummer

tel['private'].pop('Julia')

print(tel['private'])           #Zeile nicht notwendig, nur zum prüfen ob es funktioniert hat.

#Ändere den Namen Mark im privaten Bereich in „Murad“
tel['arbeit'].pop('Mark')
arbeit2 = {'Murad':'80'}
tel['arbeit'].update(arbeit2)

print(list(tel['arbeit'].items()))  ##Zeile nicht notwendig, nur zum prüfen ob es funktioniert hat.