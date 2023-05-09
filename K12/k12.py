# BSFI-22-A Marc Subat

import re

#K12_A1
def is_included(txt,word_to_find): 
    x = re.search(word_to_find, txt)
    if(x):
        return True
    else:
        return False

#K12_A2
def nur_ungerade(list):
    U = [x for x in list if x % 2 != 0]
    return U

#Test
txt = "The rain in Spain funktioniert"  
print(is_included(txt,"funktioniert"))

liste = [0,1,2,3,4,5,6,7]
print(nur_ungerade(liste))