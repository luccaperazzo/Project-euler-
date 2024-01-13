a = 20  # Set a to a suitable initial value
found = False

while not found:
    contar = 0

    for x in range(1, 21):
        if a % x == 0:
            contar += 1

    if contar == 20:
        print(a)
        found = True
    else:
        a += 20  # Increment a by 20 since it needs to be divisible by all numbers from 1 to 20
