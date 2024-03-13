longitud = 0
listaxd = 0
lista = []
suma = 0
limit = 1000000

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(2, limit):
    if is_prime(i):
        lista.append(i)
        suma = sum(lista)

        while suma > limit:
            lista.pop(0)
            suma = sum(lista)

        if is_prime(suma) and len(lista) > longitud:
            longitud = len(lista)
            listaxd = suma

print(listaxd)

