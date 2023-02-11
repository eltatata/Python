# funcion que devuelve los numeros primos entre el 0 y el parametro indicado

# verificar si un numero es primo
def prime(num):
    if num <= 1: return False
    
    # verificar eque el numero no se divida entro 2
    for i in range(2, num):
        if num%i == 0: return False
        
    # si se termina el bucle, es numero es primo
    return True

# funcion que retorna una lista con la cantidad de primos hasta el numero indicado
def primes_nums(num):
    primes = list()
    
    for i in range(3, num+1):
        res = prime(i)
        
        if res: primes.append(i)
        
    return primes

res = primes_nums(13)

print(res)