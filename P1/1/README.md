# Seriennummergenerator
Author: Ali Abas Arsalahn\
Das folgende Programm erstellt Seriennummern und sichert diese in eine .json Datei.\
Ebenfalls ermöglicht wird die validierung von erstellten Seriennummern.

### Anleitung
Das Programm lässt sich über eine Kommandozeile (PowerShell o. bsh/zsh) ausführen. 
Benötigt wird hierbei ein Python Interpreter. Zum Ausführen Python in die Kommandozeile (Python3 für macOS) eingeben und die unten spezifizierten Paramter eingeben

### Parameter
-h oder --help um alle verfügbaren befehle anzeigen zu lassen.\
-dg oder --digitalgenerator mit der Anzahl als Wert für nummerbasierte Schlüssel.\
-lg oder --lettergenerator mit der Anzahl als nummerischer Wert für buchstabenbasierte Schlüssel.\
-v oder --validate um erstellte Schlüssel zu validieren.\

### Optionale Parameter
-kr oder --keyrows um die Anzahl der erstellen Blöcke zu manipulieren. (Standardmäßg auf 4)\
-rl oder --rowlength um
-p oder --path um den Speicherort für erstelle Seriennummern anzugeben. Standardmäßig ist dies das Verzeichnis aus dem das Python Skript ausgeführt wird.
-fn oder --filename um den Namen der Datei zu bearbeiten die entweder mit Seriennummern beschrieben wird oder aus der Seriennummern gelesen werden

### Bemerkung
eine GUI wird (evtl.) noch nachgereicht. Ich habe mich bei der Erstellung des Projekts sehr darauf fixxiert ein Commandlinetool zu basteln (personal preference)