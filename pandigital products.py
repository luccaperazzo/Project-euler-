def is_pandigital(number_str):
    return sorted(number_str) == [str(i) for i in range(1, 10)]

def sum_of_pandigital_products():
    products = set()

    for multiplicand in range(1, 100):
        for multiplier in range(100, 10000):
            product = multiplicand * multiplier
            concat_str = str(multiplicand) + str(multiplier) + str(product)
            if len(concat_str) == 9 and is_pandigital(concat_str):
                products.add(product)

    return sum(products)

# Calculate the sum of all pandigital products
result = sum_of_pandigital_products()
print("Sum of all pandigital products:", result)
