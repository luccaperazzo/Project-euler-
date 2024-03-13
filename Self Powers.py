lista = []
for i in range(1,1001):
    lista.append(i**i)
lol = sum(lista)
print(str(lol)[-10:])