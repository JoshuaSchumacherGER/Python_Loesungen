para = input("Wert ")

def switch(para):
    list2 = {
        1:"Stein",
        2:"Schere",
        3:"Papier"
    }
        
    print (list2.get(para, "Weder noch..."))
    
switch(para)