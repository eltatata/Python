# EXPRESIONES REGULARES

# modulo para trabajar con expresiones regulares
import re

text = """Hello world, Welcome to Python 2022, ¿how are you?
have a nice day.
You are amazing, see you soon.
"""
# ----------------------------------------------------------------------------------------------------
# SEARCH() retorna la coincidencia encontrada

res = re.search("Hello", text)

print(res, "\n")
# ----------------------------------------------------------------------------------------------------
# SEARCH() retorna todas las coincidencias encontradas

res = re.findall("you", text, flags=re.IGNORECASE)

print(res, "\n")
# ----------------------------------------------------------------------------------------------------
# "\d" BUSCA DIGITOS NUMERICOS DE EL 0 AL 9

def find_nums_in_text(txt):
    res = re.findall(r"\d", txt)
    
    if res == []: return "La cadena de texto no tiene numeros"
    else: return f"Los numeros dentro de la cadena de texto es: {res}"
    
print(find_nums_in_text(text))

withoutNums = "text without nums"

print(find_nums_in_text(withoutNums), "\n")
# ----------------------------------------------------------------------------------------------------
# "\D" BUSCA TODO MENOS DIGITOS NUMERICOS

res = re.findall(r"\D", text)

print(res, "\n") 
# ----------------------------------------------------------------------------------------------------
# "\w" BUSCA CARACTERES ALFANUMERICOS [a - z, A - Z, 0 - 9, _]
# "\w" BUSCA TODO MENOS CARACTERES ALFANUMERICOS [a - z, A - Z, 0 - 9, _]

res = re.findall(r"\w", text)
print(res) 

res = re.findall(r"\W", text)
print(res, "\n") 
# ----------------------------------------------------------------------------------------------------
# "\s" BUSCA ESPACIOS EN BLANCO
# "\S" BUSCA TODO MENOS ESPACIOS EN BLANCO

res = re.findall(r"\s", text)
print(res) 

res = re.findall(r"\S", text)
print(res, "\n") 
# ----------------------------------------------------------------------------------------------------
# "\n" BUSCA ESPACIOS EN LINEA
# "." BUSCA TODO MENOS ESPACIOS EN LINEA

res = re.findall(r".", text)
print(res) 

res = re.findall(r"\n", text)
print(res, "\n") 
# ----------------------------------------------------------------------------------------------------
# "\" BUSCAR PUNTOS

res = re.findall(r"\.", text)
print(res, "\n")
# ----------------------------------------------------------------------------------------------------
# "^" BUSCAR EL COMIENZO DE UNA CADENA DE TEXTO

def know_start_of_string(txt, start):
    res = re.findall(fr"^{start}", txt)
    
    if res == []: return f"La cadena de texto no comienza con: {start}"
    else: return f"Si, la cadena de texto comienza con: {start}"
    
print(know_start_of_string(text, "Hello"))
print(know_start_of_string(text, "Hola"), "\n")
# ----------------------------------------------------------------------------------------------------
# "^" BUSCAR EL COMIENZO DE TODAS LAS LINEAS

res = re.findall(r"^have", text, flags=re.M)
print(res, "\n")
# ----------------------------------------------------------------------------------------------------
# "$" BUSCAR EL FINAL DE TODAS LAS LINEAS

res = re.findall(r"soon.$", text, flags=re.M)
print(res, "\n")
# ----------------------------------------------------------------------------------------------------
# "{n}" BUSCA "n" CANTIDAD DE VECES EL VALOR INIDICADO

res = re.findall(r"\d{1,3}", text)
print(res)