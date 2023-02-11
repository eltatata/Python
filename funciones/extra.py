# FORZAR PARAMETROS
# meter los parametros en diferente orden pero sin alterar el resultado 

def saludar(name, lastname, group):
    return f"Hola {name} {lastname}, Bienvenido a {group}"

msg = saludar(group="11-H", lastname="Tabares", name="David")

print(msg)