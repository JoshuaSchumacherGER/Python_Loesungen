#K11
#A2
tel={
    "Arbeit":{"Jan":"50","Mark":"81"},
    "private":{"Julia":"0151438924","Mark":"061932834"}
}
#Nummer 1
del tel["private"]["Julia"]

#Nummer 2
tel["Arbeit"]["Mark"]= "80"

#Nummer 3
NeuerMark=tel["private"]["Mark"]
tel["private"]["Murad"]=NeuerMark

print (tel)