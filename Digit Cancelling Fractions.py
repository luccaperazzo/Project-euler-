from fractions import Fraction
from math import gcd

def producto(fractions):
    # Calculate the product of numerators and denominators
    product_numerators = 1
    product_denominators = 1
    for fraction in fractions:
        product_numerators *= fraction[0]
        product_denominators *= fraction[1]
    
    # Calculate the greatest common divisor (GCD) of the products
    divisor = gcd(product_numerators, product_denominators)
    
    # Simplify the fraction by dividing both products by the GCD
    simplified_numerator = product_numerators // divisor
    simplified_denominator = product_denominators // divisor
    
    return simplified_denominator



def digits(numerator, denominator):
    num_str = str(numerator)
    denom_str = str(denominator)

    for digit in '0123456789':
        if digit in num_str and digit in denom_str:
            return True
    return False

def check(numerator, denominator):
    num_str = str(numerator)
    denom_str = str(denominator)

    for digit in num_str:
        if digit in denom_str and digit != '0':  # Exclude digit '0'
            simplified_num = int(num_str.replace(digit, '', 1))
            simplified_denom = int(denom_str.replace(digit, '', 1))
            if simplified_denom != 0 and numerator / denominator == simplified_num / simplified_denom:
                return num_str + '/'+  denom_str
    return False




lista = []

for i in range(10,99):
    for x in range(10,99):
        if (i / x) < 1:
            if digits(i,x) and str(i)[-1]!= '0' and str(x)[-1] !='0' :
                func = str(i) +'/'+ str(x)
                lista.append(func)
            else:
                continue
            
listaf = []         
for frac in lista:
    if check(int(frac[:2]),int(frac[3:])):
        listaf.append(check(int(frac[:2]),int(frac[3:])))
print(listaf)
fractions = [(16, 64), (19, 95), (26, 65), (49, 98)]

lel = producto(fractions)
print(lel)

        
        