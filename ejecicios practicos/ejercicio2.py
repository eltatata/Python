def calculateTime(str):
    time = float(len(str.split(" ")) / 2)
    
    return time

def countWords(str):
    count = len(str.split(" ")) 
    
    return count
    
text = input("Ingrese in texto real: ")

time = calculateTime(text)
count = countWords(text)

if time > 60:
    print(f"\nla cantidad de palabras son muchas: {count}")
else:
    print(f"\nla cantidad de palabras es: {count}, Una persona promedio lo diria en: {time}seg")
    print(f"Dalto lo diria en {(30 * time) / 100}seg")