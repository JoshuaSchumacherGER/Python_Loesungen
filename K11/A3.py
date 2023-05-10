#K11 A3
#Dieses Funktion sucht auch Werte in einem Array weil why not.
#Die Funktion sucht auch Werte die in weiteren Dictionaries als auch arrays verborgen sind
def supersearch(d,value):
    isarray = False #Dieser Variable ist dazu da um ein Dictionarie von einem Array zu unterscheiden weil sonst funktioniert die for-schleife nicht.
    
    if type(d)!=type([]) and type({}) !=type(d): #damit man nur arrays und dictionaries eingeben kann
        return False
    
    if type(d)==type([]):
        isarray = True
        
    #Hier passiert dann das ganze durchlaufen also erstmal prüfen ob das array oder dictionary den Wert beinhalten.
    #zusätzlich wird geprüft ob der wert ein array oder dictonarie ist falls ja nochmal funktion aufrufen damit diese auch geprüft wird.
    for i in d:
        if isarray == True:
            if i == value:
                return True
            elif (type(i)==type([]) or type({}) ==type(i)):
                if supersearch(i,value) == True:
                   return True
                
        elif d[i] == value:
            return True
        
        elif (type(d[i])==type([]) or type({}) ==type(d[i])):
            if supersearch(d[i],value) == True:
                return True
            
    return False

#nur zum testen
test =  {'test1':'testt','test2':['test',{'array':3}],'test3':{'hallo':32,'Hello':'eaae'}}
print(supersearch(test,32))
