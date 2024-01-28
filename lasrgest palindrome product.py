lista = []
for i in range(100,999):
    for x in range(100,999):
        lel = i*x
        if str(lel) == str(lel)[::-1]:
            lista.append(lel)
for lol in lista:
    lol = int(lol)
print(max(lista))