import json
import os
def save():
    classes = []
    count = 0

    for playerclass in os.listdir("./playerclasses"):
        if playerclass.endswith(".py"):
            if playerclass in "pctemplate.py":
                continue
            count += 1
            playerclass = playerclass[:-3]
            classes.append(playerclass)

    classes_json = json.dumps(classes, indent=count)
    with open("classes.json", "w") as outfile:
        outfile.write(classes_json)

    print(classes)