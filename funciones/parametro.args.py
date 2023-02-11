# ARGS
# todos los parametros que se pasen se agruparan en uno solo

def suma(name, *numeros):
    return f"{name} la suma de tus numeros es: {sum(numeros)}"

print(suma("David",1,2,3,4,5,6,7,8,9,10.5), "\n")
# ----------------------------------------------------------------------------------------------------
# IMPRIMIR LOS ELEMENTOS DE UNA LISTA CON ARGS

listNums = [1,2,3,4,5,6,7,8,9,10.5]

# imprimir lista
print(listNums, "\n")

# imprimir los elementos sin nesesidad de el bucle for si no con (args)
print(*listNums)
