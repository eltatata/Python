# ----------------------------------------------------------------------------------------------------
# MANEJO DE EXCEPCIONES CON TRY

def suma():
    while True:
        try:
            a = input("Numero 1: ")
            b = input("Numero 2: ")
            
            res = int(a) + int(b)
        except Exception as e:
            print(f"Valores ingresados no validos, Error: {e}")
        else:
            break
        # finally:
        #     print("Lo que esta dentro de finally se ejecuta siempre")

    return res
print(suma())