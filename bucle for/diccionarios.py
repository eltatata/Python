# ----------------------------------------------------------------------------------------------------
# ITERAR DICTS

dict = {
    'nombre': "David",
    'apellido': "Tabares",
    'age': 18
}

print(type(dict), dict, "\n")

# iterar las claves
for key in dict:
    print(key)
    
print()

# iterar las claves con sus valores
for item in dict.items():
    print(f"La clave es: {item[0]} y el valor es: {item[1]}")