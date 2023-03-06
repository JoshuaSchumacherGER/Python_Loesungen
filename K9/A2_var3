"""
Aufgabe	K9	|	A1 Implementiere	diese	Aufgabe	iterativ! (Fibonacci-Folge)
"""

inp = int(input("Give a number: "))

nums = [inp]
auxArray = []
sum = []

while len(nums) > 0:
    for num in nums:
        if num == 0:
            continue
        if num == 1 or num == 2:
            sum.append(1)
            continue
        auxArray.append(num - 1)
        auxArray.append(num - 2)
    nums = auxArray
    auxArray = []

print(len(sum))
