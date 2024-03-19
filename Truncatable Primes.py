import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True




def truncate(n):
    lol = str(n)
    for i in range(len(lol)):
        if not is_prime(int(lol[i:])) or not is_prime(int(lol[:i+1])):
            return False
    return True

        

lista = []
for i in range(10,1000000):
    if is_prime(i):
        if truncate(i):
            lista.append(i)
print(sum(lista))