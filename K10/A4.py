def selectionSort(L):
  n = len(L)
  for i in range(n):
    min_index = i

    for j in range(i+1, n):
      if (L[j] < L[min_index]):
        min_index = j

    temp = L[i]
    L[i] = L[min_index]
    L[min_index] = temp
    
  return L

array = [13, 4, 9, 5, 3, 16, 12]
print("Unsorted: ", array)
print("Sorted: ", selectionSort(array))