passwords = ["ababa","baab","sdiopc","ajkwei","bab"]
index = 0
for string in passwords:
    if(passwords[index].find("ab") != -1 or passwords[index].find("ba") != -1):
        print(passwords[index])
    index +=1

