def divisores(n):
    lista = []
    suma = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            lista.append(i)
            suma += i
    return suma

def amicable(n):
    amicable_pairs = []
    for a in range(2, n):
        b = divisores(a)
        if b > a and divisores(b) == a:
            amicable_pairs.append((a, b))
    return amicable_pairs

pairs = amicable(10000)
for pair in pairs:
    print(pair)
