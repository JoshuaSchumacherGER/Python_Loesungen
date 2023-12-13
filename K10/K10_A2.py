#maria
unsorted = [23,63,1,435,6]

def bubble_sort(list):
    length = len(list)
    for x in range (length):
        for num in range (length - 1):
            if list[num] > list[num+1]:
                list[num], list[num+1] = list[num+1], list[num] 
    
    return list
                
print(unsorted)
print(bubble_sort(unsorted))
            
