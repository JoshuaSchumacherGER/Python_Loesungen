# Von Jonas Dinger

def read_every_line():
    file = open("A1.txt")
    for line in file:
        line = line.replace("\n", "")
        if "18" in line:
            print(line)


read_every_line()
