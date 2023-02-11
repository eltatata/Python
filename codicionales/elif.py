# ELIF

# se generara un numero de el 1 al 3 aleatoriamente, 
# y con el programa se abra cual de los tres numeros se genero

import random

random_number = random.randint(1, 3)

print(random_number)

if random_number == 1:
    print(f"el numero aletorio es: {random_number}")
elif random_number == 2:
    print(f"el numero aletorio es: {random_number}") 
elif random_number == 3:
    print(f"el numero aletorio es: {random_number}")
else:
    print("no se identifico el numero")