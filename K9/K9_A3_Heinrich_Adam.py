# Eine Funktion "countdown"
# die von 10 bis zur 0 herunterzählt

from time import sleep


def countdown():
    for i in range(11):
        print(10 - i)
        sleep(1)


countdown()
