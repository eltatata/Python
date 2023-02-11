# FUCION NORMAL

# def math(operacion, n1, n2):
#     if operacion == 1:
#         return n1 + n2
#     elif operacion == 2:
#         return n1 - n2
#     elif operacion == 3:
#         return n1 * n2
#     elif operacion == 4:
#         return n1 / n2
#     else:
#         return "No se econtro la operacion en el menu"
    
# operacionMenu = int(input("Menu operaciones: \n1. Suma\n2. Resta\n3. Multipliacion\n4. Divicion\n\n"))
# numero1 = int(input("\nDigite un numero: "))
# numero2 = int(input("Digite un numero: "))

# print(math(operacionMenu, numero1, numero2))
# ----------------------------------------------------------------------------------------------------
# FUNCION QUE RETORNA VARIOS VALORES

user = {
    'name': "David",
    'password': "123"
}

def login(password):
    if password == user['password']:
        return "Sesion iniciada", True
    else:
        return "Sesion fallida", False

passwordInput = input("Digite la contraseña: ")

# desempaquetado de la funcion
msg, bool = login(passwordInput)

if bool:
    print(msg, f":Bienvenido {user['name']}")
else:
    print(msg, ":contraseña incorrecta")
    