# IMPORTAR UN MODULO

import moduloSaludar

msgRes = moduloSaludar.saludar("David")
print(msgRes, "\n")
# ----------------------------------------------------------------------------------------------------
# IMPORTAR DE EL MODULO "moduloMath" SU FUNCION "math" Y RENOMBRAR CON "as"

from moduloMath import math as m

mathRes = m("((1 * 100) / 50) * 2")
print(mathRes, "\n")
# ----------------------------------------------------------------------------------------------------
# IMPORTAR CIERTAS FUNCIONES DE UN MODULO

from moduloLists import sort_and_reverse, join_list

list = [1,5,6,0,-2,10,4]
list2 = ["Hola", "Mundo"]

listsRes = sort_and_reverse(list)
listsRes2 = join_list(list2)

print(listsRes, listsRes2, "\n")
# ----------------------------------------------------------------------------------------------------
# dir() A UN MODULO

print(dir(moduloSaludar), "\n")
# ----------------------------------------------------------------------------------------------------
# ENRUTAMIENTO / MODULOS DENTRO DE OTRA CARPETA

from modulosExtra.saludarExtra import extraSaludo

print(extraSaludo("David"))