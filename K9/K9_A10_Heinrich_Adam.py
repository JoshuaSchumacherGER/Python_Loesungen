# Ein Programm "QuestionAnswer",
# welches dem Benutzer 3 Fragen stellt
# und für jede richtige Antwort einen Punkt
# vergibt.

def question_answer():
    richtig = 0
    print("3 Fragen, 3 Antworten, ...\n")

    print("Was is die Anwort auf Alles im Universum?")
    answer = int(input("Deine Anwort: "))
    if answer == 42:
        print("Richtig! Hier haste nen Gute-Nudel-Stern [.*.]")
        richtig += 1
    else:
        print("Falsch!")

    print("\nWieviele Eichhörnchen braucht man um eine Glühbirne zu wechseln?")
    answer = int(input("Deine Anwort: "))
    if answer == 42:
        print("Richtig! Hier haste nen Gute-Nudel-Stern [.*.]")
        richtig += 1
    else:
        print("Falsch!")

    print("\nWas ist die Wurzel aus 1764")
    answer = int(input("Deine Anwort: "))
    if answer == 42:
        print("Richtig! Hier haste nen Gute-Nudel-Stern [.*.]")
        richtig += 1
    else:
        print("Falsch!")

    print("\nDu hast insgesamt", richtig, "Gute-Nudel-Sterne gesammelt!")
    print("\nProgramm Ende")

question_answer()
