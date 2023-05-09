# Kapitel 11 Aufgabe 5
# Schreibe eine Funktion foo(number), die eine ganze Zahl nimmt und überprüft ob diese positiv,
# negativ, gerade, ungerade oder gar keine Integer ist. 
# Die Ausgabe soll in Form eines Dictionaries erfolgen.
def foo(number):
    dic = {}
    if number < 0:
        dic["vorzeichen"] = "negativ"
    elif number >= 0:
        dic["vorzeichen"] = "positiv"
    if number % 2 == 0:
        dic["parität"] = "gerade"
    elif number % 2 != 0:
        dic["parität"] = "ungerade"
    if number % 1 != 0:
        dic["parität"] = "kein Integer"
    return dic

print(foo(-2))
print(foo(-1))
print(foo(0))
print(foo(1))
print(foo(2))
print(foo(0.1))