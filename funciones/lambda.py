# LAMBDA CREAR FUCIONES ANONIMAS 
# QUE DESPUES SE PUEDEN ALMACENAR COMO POR EJEMPLO EN UNA VARIABLE

multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5), "\n")
# ----------------------------------------------------------------------------------------------------
# ejemplo con funcion lamda

listNums = [1,2,3,4,5,6,7,8,9]

numerosPares = filter(lambda num:num%2==0, listNums)

print(list(numerosPares))