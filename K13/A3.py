# Von Jonas Dinger

def read_on_value():
    file = open("A1.txt")
    for line in file:
        line = line.replace("\n", "")
        for word in line.split(","):
            print(word)


read_on_value()
