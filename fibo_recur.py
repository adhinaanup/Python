# Recursive function to calculate nth Fibonacci number
def fibonacci(n):
    if n <= 0:  # Base case for invalid input
        return "Invalid input"
    elif n == 1:  # Base case: Fibonacci(1) = 0
        return 0
    elif n == 2:  # Base case: Fibonacci(2) = 1
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Function to print Fibonacci series up to n terms
def print_fibonacci_series(n):
    for i in range(1, n + 1):
        print(fibonacci(i), end=" ")

# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Print Fibonacci series
print("Fibonacci Series:")
print_fibonacci_series(n)
