liste = [4,1,3,2,0,-1]

def meineSort(li):
    sorted = []
    while(len(li) > 0):
        temp = min(li)
        sorted.append(temp)
        i = 0
        index = 0
        temp2 = li[0]
        while(i < len(li) - 1):
            if temp2 > li[i+1]:
                index = i+1
                temp2 = li[i+1]
            i += 1
        li.pop(index)             
    print(sorted)    
              
meineSort(liste) 