# ----------------------------------------------------------------------------------------------------
# DICT() para crear in dict

dict = dict(name = "david", age = 18)

print(type(dict), dict, "\n")

for prop in dict:
    print(f"{prop}: {dict[prop]}")
    
print()
# ----------------------------------------------------------------------------------------------------
# FROMKEYS() crear dict con todos los valore en None o el que digamos

dict = dict.fromkeys(["name", "age"])

print(type(dict), dict, "\n")

dict = dict.fromkeys(["name", "age"], "----")

print(type(dict), dict, "\n")

dict = dict.fromkeys("ABCD", "----")