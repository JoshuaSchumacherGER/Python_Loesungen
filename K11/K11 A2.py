tel = {
  "arbeit": {"jan": 50, "Mark": 81},
  "private": {"julia": "013123342", "mark": "023123"}
 }

tel["private"]["mark"]= "39243248"
print(tel["private"]["mark"])

del tel["private"]["julia"]
del tel["private"]["mark"]

tel["private"].update({"murad": "39243248"})

print(tel["private"]["murad"])
print(tel)