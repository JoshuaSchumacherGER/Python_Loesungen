 # Fibonacci-Folge iterativ

def fib_it(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    sum = 0
    m1 = 1
    m2 = 0

    for i in range(2, n+1):
        sum = m1 + m2
        m2 = m1
        m1 =sum

    return sum

for i in range(20):
    print(fib_it(i), end=" ")
