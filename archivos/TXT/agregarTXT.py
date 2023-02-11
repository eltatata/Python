# ----------------------------------------------------------------------------------------------------
# AGREGAR TEXTO EN UN ARCHIVO DE TEXTO

# "w": para dar permisos de escritura

with open("archivos\\TXT\\texto.txt", "a", encoding="UTF-8") as texto:
    # ----------------------------------------------------------------------------------------------------
    # SOBREESCRIBIR EL ARCHIVO

    texto.write("\n\nNuevas linea de texto:\n")
    # ----------------------------------------------------------------------------------------------------
    # CREAR NUEVAS LINEAS DE TEXTO

    for i in range(5): 
        texto.writelines([f"{i}. Creando", "nuevas", "lineas", "de texto\n"])
