# Input from user
num = int(input("Enter a number to find its factors: "))

# Initialize an empty list to store the factors
factors = []

# Loop through 1 to num and check if the number divides evenly
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

# Print the list of factors
print(f"The factors of {num} are: {factors}")
