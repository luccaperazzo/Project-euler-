def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

limit = 600851475143
prime_numbers = [num for num in range(2, limit + 1) if is_prime(num)]

print(max(prime_numbers))
