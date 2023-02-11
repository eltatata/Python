# serie de fibonacci

def fibonacci(num):
    if num <= 0:
        return  []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 2]
    else:
        listFibonacci = [0, 1]
        
        for i in range(2, num):
            print(listFibonacci[i-1], listFibonacci[i-2])
            
            listFibonacci.append(listFibonacci[i-1] + listFibonacci[i-2])
            
        return listFibonacci
    
print(fibonacci(5))
