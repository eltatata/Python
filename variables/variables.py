# nombre = "David"
# edad = 18
# civil = True

# print(f"Nombre de la persona: {nombre}, edad: {edad}, estado civil: {civil}")

# nombre = "Rocio"
# edad = 53
# civil = True

# print(f"Nombre de la persona: {nombre}, edad: {edad}, estado civil: {civil}")
# ----------------------------------------------------------------------------------------------------
# "del" operador para borrar datos que esta alojados en la memoria

# nombre = "Rocio"
# edad = 53
# civil = True

# del nombre
# del edad
# del civil

# print(f"Nombre de la persona: {nombre}, edad: {edad}, estado civil: {civil}")
# ----------------------------------------------------------------------------------------------------
# "in" para saber si hay algo dentro de un dato

nombre = "David"
edad = 18
civil = True

infoPersona = f"Nombre de la persona: {nombre}, edad: {edad}, estado civil: {civil}"

print("David" in infoPersona) #True
print("Rocio" in infoPersona) #False
print("Rocio" not in infoPersona) #True