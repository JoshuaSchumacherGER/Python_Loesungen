# Fibonacci-Folge rekursiv

def fib_re(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib_re(n-1) + fib_re(n-2)

for i in range(20):
    print(fib_re(i), end=" ")
