# ----------------------------------------------------------------------------------------------------
# ESCRIBIR EN UN ARCHIVO DE TEXTO

# "w": para dar permisos de escritura

with open("archivos\\TXT\\texto.txt", "w", encoding="UTF-8") as texto:
    # ----------------------------------------------------------------------------------------------------
    # SOBREESCRIBIR EL ARCHIVO
    
    texto.write("Linea de texto creadas desde un programa de python")
    # ----------------------------------------------------------------------------------------------------
    # CREAR NUEVAS LINEAS DE TEXTO
    
    texto.writelines(["\nBuenas", "\nTardes"])
    texto.writelines(["\nBuenas", "\nNoches"])
