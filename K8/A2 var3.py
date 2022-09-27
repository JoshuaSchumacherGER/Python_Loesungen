numbers = []

while (len(numbers) < 3):
    enteredNumber = input("Enter a number: ")
    numbers.append(enteredNumber)

numbers.sort()

print(numbers)
