def palin(n):
    lol = str(n)[::-1]
    return lol == str(n)

def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]  
    return binary_representation

lista = []
for i in range(1, 1000000):
    decimal_str = str(i)
    binary_str = decimal_to_binary(i)
    if palin(decimal_str) and palin(binary_str):
        lista.append(i)

print(sum(lista))
