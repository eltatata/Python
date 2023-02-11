dict = {
    'name': "Felix",
    'lastname': "Escobar",
    'age': 35,
    'single': True
}

print(dict)
for prop in dict:
    print(prop, end=" ")

print("\n")
# ----------------------------------------------------------------------------------------------------
# KEYS() -> devuelve las claves

print(dict.keys(), "\n")
# ----------------------------------------------------------------------------------------------------
# GET() -> devueñve el valor de cada clave

print(dict["name"])
print(dict.get('name'), "\n")
# ----------------------------------------------------------------------------------------------------
# POP() -> elimina un elemento

dict.pop('single')
print(dict, "\n")
# ----------------------------------------------------------------------------------------------------
# ITEMS() -> para iterar el direcctorio

print(type(dict.items()), dict.items())

for item in dict.items():
    print(type(item), item, item[0], item[1]) 
    
print()
# ----------------------------------------------------------------------------------------------------
# CLEAR() -> elimina todos los elementos

dict.clear()

print(dict)