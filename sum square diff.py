n = 100

# Calculate the sum of squares
sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6

# Calculate the square of the sum
square_of_sum = ((n * (n + 1)) // 2) ** 2

# Calculate the difference
difference = sum_of_squares - square_of_sum

print("Difference:", difference)
