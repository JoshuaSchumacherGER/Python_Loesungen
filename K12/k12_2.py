import re


# K12 Aufgabe 1

def is_included(given_text, searched_word):
    included_word = re.search(searched_word, given_text)
    return True if included_word else False


text = "Mein Python-Projekt funktioniert"

print(is_included(text, "funktioniert"))


# K12 A2

def nur_ungerade(nummer_list):
    return [x for x in nummer_list if x % 2 != 0]


print(nur_ungerade([1, 3, 2, 19, 12, 3, 8]))

# BS-FI 22-A Dimitar Dimitrov
