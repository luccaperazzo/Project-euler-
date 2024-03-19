def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_circular_primes(limit):
    count = 0
    for n in range(2, limit):
        digits = str(n)
        if is_prime(n):
            is_circular = True
            for _ in range(len(digits)):
                digits = digits[1:] + digits[0]
                if not is_prime(int(digits)):
                    is_circular = False
                    break
            if is_circular:
                count += 1
    return count

print(f"The number of circular primes below one million is: {count_circular_primes(1000000)}")