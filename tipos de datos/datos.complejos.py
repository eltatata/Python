# LISTAS

# list = ["David", "Maria", "Rocio", "Emilia", "Guillermo", True, 5]

# # saber el tipo de dato
# print(type(list))

# # imprimir la lista completa
# print(list)

# # imprimir un elemento especifico dentro de la lista
# print(list[0])

# # saber el tipo de dato de los elementos dentro de la lista
# for element in list:
#     if isinstance(element, str):
#         print(f"string: {element}")
#     elif isinstance(element, bool):
#         print(f"bool: {element}")
#     elif isinstance(element, (int, float, complex)):
#         print(f"number: {element}")
#     else:
#         print(f"{element}, no se indentifico el tipo de dato")
# ----------------------------------------------------------------------------------------------------
# TUPLAS en las tuplas no se pueden modificar los datos

# tupla = ("David", "Maria", "Rocio", "Emilia", "Guillermo", True, 5)

# # saber el tipo de dato
# print(type(tupla))

# # imprimir la tupla completa
# print(tupla)

# print(tupla[1])

# # saber el tipo de dato de los elementos dentro de la tupla
# for element in tupla:
#     if isinstance(element, str):
#         print(f"string: {element}")
#     elif isinstance(element, bool):
#         print(f"bool: {element}")
#     elif isinstance(element, (int, float, complex)):
#         print(f"number: {element}")
#     else:
#         print(f"{element}, no se indentifico el tipo de dato")
# ----------------------------------------------------------------------------------------------------
# SET conjunto 
# en los conjuntos no se pueden modificar los datos ni acceder por su indice
# y tampoco se pueden tener elementos o datos repetidos
# y sus datos estan en posiciones desordenadas

# conjunto = {"David", "David", "Maria", "Rocio", "Emilia", "Guillermo", True, 5}

# # saber el tipo de dato
# print(type(conjunto))

# # imprimir el conjunto
# print(conjunto)

# # saber el tipo de dato de los elementos dentro del conjunto
# for element in conjunto:
#     if isinstance(element, str):
#         print(f"string: {element}")
#     elif isinstance(element, bool):
#         print(f"bool: {element}")
#     elif isinstance(element, (int, float, complex)):
#         print(f"number: {element}")
#     else:
#         print(f"{element}, no se indentifico el tipo de dato")
# ----------------------------------------------------------------------------------------------------
# DICCIONARIOS

persona = {
    'nombre': "david",
    'edad': 18,
    'casado': False
}

# saber el tipo de dato
print(type(persona))

# imprimir el diccionario
print(persona)

# imprimir unna propiedad del diccionario
print(persona['nombre'])
