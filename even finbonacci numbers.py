lista = [1,2]
numero = 0
while numero < 4000000:
    numero = lista[-1] + lista[-2]
    if numero > 4000000:
        break
    else:
        lista.append(numero)
lista2 = []
for i in lista:
    if i % 2 == 0:
        lista2.append(i)
print(sum(lista2))