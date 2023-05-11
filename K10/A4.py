#Selectionsort in place
meineListe=[14,112,13,14,374,7457,2,46346,7,3,73,26,5,3,8,9]
def meinSort(meineListe):
    
    for i in range(len(meineListe)):
        minindex=i
        for j in range(minindex+1,len(meineListe)):
            if meineListe[minindex]>meineListe[j]:
                minindex=j
        
        meineListe[i], meineListe[minindex]= meineListe[minindex], meineListe[i]
    return meineListe   

print(meinSort(meineListe))