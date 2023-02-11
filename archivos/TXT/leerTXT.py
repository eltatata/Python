# ----------------------------------------------------------------------------------------------------
# ABRIR UN ARCHIVO DE TEXTO

# "r": para dar permisos de lectura
# encoding="UTF-8": para que no hallan errores de codificacion

with open("archivos\\TXT\\texto.txt", "r", encoding="UTF-8") as texto:
    # ----------------------------------------------------------------------------------------------------
    # LEER EL CONTENIDO DENTRO DE UN ARCHIVO DE TEXTO
    content = texto.read()

    print(content)
    # ----------------------------------------------------------------------------------------------------
    # LEER LAS LINEAS DENTRO DE EL TEXTO
    # readlines() retorna un arreglo con todas la linea

    # lineas = texto.readlines()

    # print(lineas)
    # ----------------------------------------------------------------------------------------------------
    # LEER UNA SOLA LINEA DE TEXTO 
    "readline()"

    # linea = texto.readline()

    # print(linea)
