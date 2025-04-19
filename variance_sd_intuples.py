import math

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Calculate the mean (average)
mean = sum(numbers) / len(numbers)

# Calculate the variance
variance = 0.0
for x in numbers:
    variance += (x - mean) ** 2

variance /= len(numbers)  # Variance is the average of the squared differences

# Calculate the standard deviation
std_deviation = math.sqrt(variance)

# Print the results
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
