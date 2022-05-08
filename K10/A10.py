#K10|A10 Schreibe eine Funktion „print_it(number), die eine Zahl nimmt und jede Zahl von 0 bis zu dieser Zahl in 0.1 Schritten ausgibt.
def print_it():
    number = int(input("Gib eine Zahl ein."))
    null = 0

    while(null<number):
        print(null)
        null += 0.1

print_it()
