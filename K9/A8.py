def cancel():
    typed_End = False
    while(typed_End == False):
        user_Input = input("Schreib was.")
        if user_Input == "Beenden":
            typed_End = True

cancel()