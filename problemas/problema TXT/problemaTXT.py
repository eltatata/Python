# ----------------------------------------------------------------------------------------------------
# CREAR UN TEXT UNIENDO LA INFORMACION DE LAS 2 LISTAS

names = ["David", "Luis", "Maria", "Ana", "Dulce", "Andy"]
lastnames = ["Tabares", "Tabares", "Seguro", "Giraldo", "Tabares", "Seguro"]

with open("problemas\\problema TXT\\problema_archivo.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Los datos son: \n")
    
    for name, lastname in zip(names, lastnames):
        archivo.writelines(f"\nName: {name}, Lastname: {lastname}\n---------------")
        
        