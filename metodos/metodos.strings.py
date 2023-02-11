string1 = "Hola Usuario"
string2 = "eres bienvenido"

# ----------------------------------------------------------------------------------------------------
# DIR ver todos los metodos que se puede aplicar a un dato

print(dir(string1), "\n")
# ----------------------------------------------------------------------------------------------------
# UPPER convertir a MAY

print(string1.upper(), "\n")
# ----------------------------------------------------------------------------------------------------
# UPPER convertir a MIN

print(string1.lower(), "\n")
# ----------------------------------------------------------------------------------------------------
# CAPITALIZE primera letra en MAY

print(string2.capitalize(), "\n")
# ----------------------------------------------------------------------------------------------------
# FIND buscar dentro de un string

print(string1.find("Hola"))
print(string1.find("Buenas"), "\n")
# ----------------------------------------------------------------------------------------------------
# INDEX buscar dentro de un string, pero si no ecuentran da una excepcion

print(string1.index("Hola"))
# print(string1.index("Buenas"))
print("")
# ----------------------------------------------------------------------------------------------------
# ISNUMERIC saber si es un numero

text = "123"

print(string1.isnumeric())
print(text.isnumeric(), "\n")
# ----------------------------------------------------------------------------------------------------
# ISALPHA saber si es alfa numerico

text = "Z"

print(string1.isalpha())
print(text.isalpha(), "\n")
# ----------------------------------------------------------------------------------------------------
# COUT saber cuanto ocurrencias(letras, texto) hay dentro de una cadena

print(string1.count("a"))
print(string1.count("Hola"), "\n")
# ----------------------------------------------------------------------------------------------------
# LEN cuenta el tamaño del string

print(len(string1), "\n")
# ----------------------------------------------------------------------------------------------------
#   STARTSWITH ENDSWITH
# saber como empieza / saber como termina

print(string1.startswith("Hola"))
print(string1.endswith("Usuario"), "\n")
# ----------------------------------------------------------------------------------------------------
# REPLACE remplaza un valor por otro
newText = string1.replace("Hola", "Buenas")

print(newText, "\n")
# ----------------------------------------------------------------------------------------------------
# SPLIT separa el string por el parametro dado

print(string1.split(" "), "\n")
# ----------------------------------------------------------------------------------------------------
# LIST volver el string en una lista
list = list(string1)

print(list)