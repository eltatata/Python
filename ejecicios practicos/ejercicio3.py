alummnos = list()

# crear la clase alumnos para crear instancias
class Alumno:
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
# preguntar numero de alumnos
cant = int(input("Cual es la cantidad de alumnos: "))   
    
# iniciar bucle y crear instancias
for i in range(cant):
    nombre = input("\nCual es el nombre de el alumno: ")
    edad = int(input("Cual es la edad de el alumno: "))
    
    # guardar las instancias dentro de la lista en forma de "dict()"
    alummnos.append(Alumno(nombre, edad).__dict__)

print(f"\nLista de alumnos: {alummnos}")

# ordenar la lista de los estudiantes por las edades de los alumnos

# obtener una copia de la lista original ordenada con "sorted()"
# alummnosSort = sorted(alummnos, key=lambda e:e['age'])

# ordenar la lista original
alummnos.sort(key=lambda e:e['age'])

print(f"\nLista de alumnos ordenada: {alummnos}")

# hallar el estudiante con la mayor edad en la lista
alumnoProfesor = max(alummnos, key=lambda e:e['age'])
# hallar el estudiante con la menor edad en la lista
alumnoAsistente = min(alummnos, key=lambda e:e['age'])

print(f"\nProfesor: {alumnoProfesor['name']}\nAsistente: {alumnoAsistente['name']}")