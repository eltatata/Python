# promedio de duracion
actual = 1.5
min = 2.5
prom = 4
max = 7

# duracion de crudos
crudoProm = 5
crudoActual = 3.5

def findPercentage(portion, total):
    return f"{round(100 - ((portion / total) * 100), 1)}%"

# ver diferecias de duracion
print(f"El curso actual dura un {findPercentage(actual, min)} menos que el mas rapido")
print(f"\nEl curso actual dura un {findPercentage(actual, max)} menos que el mas lento")
print(f"\nEl curso actual dura un {findPercentage(actual, prom)} menos que el promedio")

print(f"\nUn curso promedio elimina un {findPercentage(prom, crudoProm)} de tiempo vacio")
print(f"\nEl curso actual elimina un {findPercentage(actual, crudoActual)} de tiempo vacio")

print(f"\nver 10 horas de este curso equivale a ver {round((prom/actual) * 10, 2)} de otro curso")