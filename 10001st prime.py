def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


contar = 0
lista = []
while contar < 10001:
    if contar == 10001:
        break
    for i in range(1,1000000):
      if is_prime(i) == True:
          lista.append(i)
          contar+=1
    
print(lista[10000])