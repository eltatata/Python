# ----------------------------------------------------------------------------------------------------
# LIST utlizando list para crear una lista vacia

list = list()

print(list, "\n")

# asignado valores a lista
list = ["David", 6, "Andy", False, "Pepe", [1, 2, 3], 4.5, "User"]

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# LEN cuanta cuantos elementos hay detro de la lista

print(len(list), "\n")
# ----------------------------------------------------------------------------------------------------
# APEND agregar elementos a la lista

list.append("Add")

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# INSERT agregar un elemento en un indice indicado

list.insert(3, "Candy")

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# EXTEND agregar varios elementos a una lista

list2 = ["a", "b", "c"]

list.extend(list2)

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# POP eliminar un elemento en el indice indicado

list.pop(9)

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# REMOVE eliminar un elemento segun su valor

list.remove("Pepe")

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# SORT ordena de menor a mayor los elemento dentro de una lista

listNumbers = [1, 10, 6,0,7,9,2,3,4]

listNumbers.sort()

print(listNumbers, "\n")
# ----------------------------------------------------------------------------------------------------
# REVERSE invierte los valores de la lista

list.reverse()

print(list, "\n")
# ----------------------------------------------------------------------------------------------------
# SLICING
# mostrar los elementos de una lista / cadena desde n1 a n2

listaNames = ["David", "Pepe", "Jose", "Emilia"]
cadena = "123456789"

print(listaNames[:2], listaNames[2:], cadena[2:6])
# ----------------------------------------------------------------------------------------------------
# CLEAR elimina todos los elementos de una lista

list.clear()

print(list)