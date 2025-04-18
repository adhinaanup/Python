numbers = (3, -1, 4, -2, 0)

# Sort the tuple by their squares
sorted_by_squares = tuple(sorted(numbers, key=lambda x: x**2))

print("Original Tuple:", numbers)
print("Sorted by Squares:", sorted_by_squares)