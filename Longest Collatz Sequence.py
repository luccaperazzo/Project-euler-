def odd(numero):
    formula = 3 * numero + 1
    return formula

def even(numero):
    formula = numero / 2
    return formula

lista = []
lista2 = []
for lol in range(1, 1000000): 
    listatemp = [lol]
    lista2.append(lol)
    while lol != 1:
        if lol % 2 != 0:
            lol = odd(lol)
        else:
            lol = even(lol)
        listatemp.append(lol)
    lista.append(len(listatemp))


print(lista2[837798])


