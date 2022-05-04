def blablub(lis,obj):
    index = len(lis)
    while index > 0:
        index -= 1  
        if(lis[index] == obj):
            return(lis)  
    lis.append(obj) 
    return(lis) 

liste = ["lisa","klaus","franz","peter","amelie"]
print(liste)
objekt = "jens"
print(blablub(liste, objekt))