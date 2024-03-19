from itertools import permutations

def generate_permutations():
    digits = '0123456789'
    all_permutations = permutations(digits)
    permutations_list = [''.join(permutation) for permutation in all_permutations]
    return permutations_list

# Example usage:
permutations_list = generate_permutations()
print("Total permutations:", len(permutations_list))
print(permutations_list[999999])
