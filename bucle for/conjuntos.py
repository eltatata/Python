# # ----------------------------------------------------------------------------------------------------
# # ITERAR LISTAS

# animales = {"perro", "gato", "pajaro", "vaca"}

# for animal in animales:
#     print(animal)

# print()
# # ----------------------------------------------------------------------------------------------------
# # ZIP() ITERAR "n" LISTAS

# numeros = {1,2,3,4}
# animales = {"perro", "gato", "pajaro", "vaca"}
# nombres = {"Andy", "Candy", "Paloma", "Lola"}

# for numero, animal, nombre in zip(numeros, animales, nombres):
#     print(numero, animal, nombre)

# print()
# # ----------------------------------------------------------------------------------------------------
# # ZIP() EJEMPLO CON MATRICES

# alumnos = {"David", "Samuel", "Sebastian", "Julian"}

# notasAlumnos = {frozenset([3.0, 2.0, 5.0, 4.5, 5.0]),
#                 frozenset([5.0, 5.0, 3.0, 1.0, 2.9]),
#                 frozenset([3.0, 4.5, 5.0, 1.0, 1.0]),
#                 frozenset([3.0, 3.0, 5.0, 1.0, 2.2])}

# for alumno, notas in zip(alumnos, notasAlumnos):
#     print(f"{alumno}, notas: {notas}")
    
# print()
# # ----------------------------------------------------------------------------------------------------
# # ENUMERATE() FORMA OPTIMA DE RECORRER UNA LISTA POR INIDICES Y ENUMERAR

# alumnos = {"David", "Samuel", "Sebastian", "Julian"}

# for alumno in enumerate(alumnos):
#     print(alumno)
    
# # desempaquetando
# for i, alumno in enumerate(alumnos):
#     print(i, alumno)
    
# print()
# # ----------------------------------------------------------------------------------------------------
# # FOR ELSE

# numeros = {1,2,3,4}

# for numero in numeros:
#     print(numero)
# else:
#     print("el bucle termino")

