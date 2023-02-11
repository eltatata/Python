listNums = [12,3,5,82,10,9]
# ----------------------------------------------------------------------------------------------------
# MAX() para encontrar el numero mas grande

print(max(listNums), "\n")
# ----------------------------------------------------------------------------------------------------
# MAX() para encontrar el numero mas pequeño

print(min(listNums), "\n")
# ----------------------------------------------------------------------------------------------------
# ROUND() para redondear numeros decimales

print(round(10.6481632, 3), "\n")
# ----------------------------------------------------------------------------------------------------
# BOOL Flas -> vacio, False, ninguno

print(bool(), "\n")
# ----------------------------------------------------------------------------------------------------
# ALL() TRUE si todo los valores son verdaderos

print(all([1,2,"buenas", True])) #True
print(all([0,2,"buenas", False]), "\n") #False
# ----------------------------------------------------------------------------------------------------
# SUM() suma todos los valores dentro de una lista

print(sum(listNums), "\n")
# ----------------------------------------------------------------------------------------------------
# EVAL() evalua un string que contiene una opetacion matematica y devuelve el valor de ella

print(eval("(5 * 5) ** 0.5"))