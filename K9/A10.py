def question ():
    fragen = ['Was ist die Antwort auf alles im Universum?','Welche Farbe ensteht aus Rot und Blau?','Welche Farbe hat der Himmel']
    antworten = ['42','violett','blau']
    punkte = 0

    for i in range(0, len(fragen), 1):
        print(fragen[i],"\n")
        answer = str.lower((input("Deine Antwort: ")))
        if answer == antworten[i]:
            print("Richtige Antwort\n")
            punkte += 1
        else:
            print("Leider falsche Antwort\n")

    print("\nDu hast insgesamt", punkte, "Punkte gesammelt!")
    print("\nProgramm Ende")

question()