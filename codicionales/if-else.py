# IF ELSE
import time

# ejemplo de condicional con un diccionario:
#iniciar sesion con un usuario registrado en la DB

user = {
    '_id': "123321",
    'name': "Jose",
    'confirm': False
}

# como el usuario no ha confirmado su correo, no se iniciara sesion
if user['confirm']:
    print("Iniciando sesion...")
    time.sleep(1)
    print(f"{user['name']}, inicio sesion")
else:
    print(f"{user['name']}, debes de confirmar tu direccion de correo para iniciar sesion")
    
# ponemos la propiedad 'confirm' en 'True' para poder iniciar sesion
print("Confirmado el correo...")
time.sleep(2)
user['confirm'] = True

# como el usuario ya confirmo su correo, se iniciara sesion
if user['confirm']:
    print("Iniciando sesion...")
    time.sleep(1)
    print(f"{user['name']}, inicio sesion")
else:
    print(f"{user['name']}, debes de confirmar tu direccion de correo para iniciar sesion")