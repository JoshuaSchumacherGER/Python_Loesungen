typed_Zero = False
while(typed_Zero == False):
    zahl = input("Gib mir eine Zahl.")
    zahl = int(zahl)
    
    if(zahl == 0):
        typed_Zero = True