from functools import reduce

def multi(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)

lista = []
for i in range(1,100):
    lista.append(i)
    
lol = multi(lista)
lista2= []
for x in str(lol):
    lista2.append(int(x))
print(sum(lista2))