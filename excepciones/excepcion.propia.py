# CREAR UNA PROPIA EXCEPCION

# heredar la clase "Excepcion"
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"El error que ocasionastes es el siguiente: {err}")
        
try:
    # "raise" es la palanra clave para lanzar una excepcion
    raise MiExcepcion("Metistes la cuchara en el microondas")
except:
    print("Tremendo lo que acabas de hacer mi rey")