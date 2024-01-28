from functools import reduce

def multiplicar(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result


def find_combinations(target):
    combinations = []
    lista = []
    for i in range(1, target):
        for j in range(1, target - i):
            k = target - i - j
            if k > 0:
                combinations.append([i, j, k])
    for l in range(len(combinations)):
        if combinations[l][0] ** 2 + combinations[l][1]**2 == combinations[l][-1]**2:
            lista.append(combinations[l])
    return lista

target = 1000

combinations = find_combinations(target)
lel = []
for combo in combinations:
    print(multiplicar(combo))
    