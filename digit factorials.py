import math


def fact(number):
    digits = [int(digit) for digit in str(number)]
    total_factorial = sum(math.factorial(digit) for digit in digits)
    
    return total_factorial


lista = []

for i in range(10,10000000):
    if fact(i) == i:
        lista.append(i)
    
print(lista)