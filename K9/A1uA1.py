inputNumber = int(input("Zahl?:"))


def easy(number):
    if (number <= 2):
        print("1")
    else:
        fiboOld = 0
        fibo = 1
        fiboNew = 1

        for x in range(2, number+1):
            fiboNew = fiboOld + fibo
            fiboOld = fibo
            fibo = fiboNew

        print("Easy:", fiboNew)


a = []
for x in range(0, inputNumber):
    a.append(0)


def rekursion(number):

    if (number <= 2):
        return 1
    if (a[number-1] == 0):
        a[number-1] = rekursion(number-1)+rekursion(number-2)
    return a[number-1]


easy(inputNumber)
print("Rek:", rekursion(inputNumber))
