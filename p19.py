# Generate square numbers between 1 and 30
square_numbers = [x**2 for x in range(1, 7) if x**2 <= 30]

# Get first and last 5 elements
first_last_five = square_numbers[:5]  # This will return the first 5 elements

# Print the result
print("First and last 5 square numbers between 1 and 30:", first_last_five)
