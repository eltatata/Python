# ----------------------------------------------------------------------------------------------------
# SET() crear un conjunto con la funcion set()

conjunto = set(["dato1", "dato2"])

print(type(conjunto), conjunto, "\n")

# ----------------------------------------------------------------------------------------------------
# FROZENSET() meter un conjunto dentro de otro

conjunto1 = frozenset(["dato3", "dato4"])
conjunto2 = {conjunto1, "dato5", "dato6"}

print(type(conjunto2), conjunto2, "\n")
# ----------------------------------------------------------------------------------------------------
# TEORIA DE CONJUNTOS, issubset, issuperset

conjuntoPares = {2,4,6,8,10}
conjunto2Pares = {10,8,2}

conjuntoImpares = {1,3,5,7,9}
conjunto2Impares = {1,3,5}

# verificando si es un subconjunto
print(conjunto2Pares.issubset(conjuntoPares))
print(conjunto2Impares.issubset(conjuntoImpares))
print(conjuntoImpares.issubset(conjuntoPares), "\n")

# verificando si es un superconjunto
print(conjuntoPares.issuperset(conjunto2Pares))
print(conjuntoImpares.issuperset(conjunto2Impares))
print(conjuntoImpares.issuperset(conjuntoPares), "\n")
# ----------------------------------------------------------------------------------------------------
# ISDISJOINT verificar si hay un numero en comun, 
# si no tienen nada en comun /True
# si tienen un numero en comun /False

print(conjuntoPares.isdisjoint(conjunto2Pares))
print(conjuntoImpares.isdisjoint(conjunto2Impares))
print(conjuntoImpares.isdisjoint(conjuntoPares))