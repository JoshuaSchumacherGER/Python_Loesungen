#Dion Abel
#Liest eine Datei namens text.txt und gibt alles aus in der Console

def read_every_line(f):
  fileObject = open(f, "r")
  data = fileObject.read()
  print(data)
  
read_every_line("text.txt")