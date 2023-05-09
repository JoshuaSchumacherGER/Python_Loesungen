#hochgeladen von Moritz E.
def super_fun(number):
    for i in range(1, number+1):
        filename = "file" + str(i) + ".txt"
        with open(filename, "w") as f:
            f.write("This is file " + str(i))

