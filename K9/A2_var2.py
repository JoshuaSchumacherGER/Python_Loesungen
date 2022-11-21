def iterfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    old = 0
    new = 1
    result = 0

    for i in range(0, n - 1):
        result = old + new
        old = new
        new = result

    return result


n = int(input("Für welches n willst du den Wert der Fibonacci Folge wissen?: "))
print(iterfib(n))
