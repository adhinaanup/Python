# 1. List comprehension to create a list of odd numbers less than 50
odd_numbers = [x for x in range(50) if x % 2 != 0]

# 2. Using lambda and map() to find the cube of numbers in the list
cubes = list(map(lambda x: x**3, odd_numbers))

# 3. Using lambda and filter() to find numbers divisible by 3
div_by_3 = list(filter(lambda x: x % 3 == 0, odd_numbers))

# Print the results
print("Odd Numbers less than 50:", odd_numbers)
print("Cubes of Odd Numbers:", cubes)
print("Numbers Divisible by 3:", div_by_3)
