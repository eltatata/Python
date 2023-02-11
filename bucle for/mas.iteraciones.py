frutas = ["banana", "manzana", "naranja", "kiwi", "tomate", "mango"]
# ----------------------------------------------------------------------------------------------------
# SALTAR UN ELEMENTO DE UNA LISTA CON CONTINUE

for fruta in frutas:
    
    # si la condicion se cumple saltarse esa fruta
    if fruta == "manzana":
        continue
    
    print(f"me comere: {fruta}")
    
print()
# ----------------------------------------------------------------------------------------------------
# TERMINAR EL BUCLE EN CIERTO ELEMENTO DE LA LISTA

for fruta in frutas:
    print(f"me comere: {fruta}")
    
    # si la condicion se cumple saltarse esa fruta
    if fruta == "tomate":
        break
    
print()
# ----------------------------------------------------------------------------------------------------
# ITERAR CADENAS DE TEXTO

cadena = "Cadena de texto"

for char in cadena:
    print(char)
    
print()
# ----------------------------------------------------------------------------------------------------
# FOR EN UNA SOLA LINEA DE CODIO

numeros = [1,2,3,4,5]

numeroDuplicados = [x * 2 for x in numeros]

print(numeroDuplicados)