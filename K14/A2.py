def writecsv():
    f = open("my_first_numbers.csv", "a") #Append fügt Werte hinzu ohne andere zu überschreiben.
    f.write("1,2,3,4,5,6,7,8,9,10")
    f.close()

writecsv()