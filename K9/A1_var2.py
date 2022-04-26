n=int(input("Welche Zahl möchtest du mit der Fibonacci Folge berechnen?"))  #Zeile nicht essenziel, Variable n auch direkt in 6 Zeile eingebar
def fibo(n):
    if n > 1:
        return fibo(n-1) + fibo(n-2)
    return n
print(fibo(n))



#Optional wenn man die Fibonacci Folge nachvollziehen möchte
"""
for x in range(n):
    print(fibo(x))
"""