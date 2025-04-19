import math

def factorial(num):
    """Calculate factorial of a number."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sine_series(x, n):
    """Compute sine series expansion."""
    sin_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_x += term
    return sin_x

# Read input from user
x = float(input("Enter value of x in radians: "))
n = int(input("Enter number of terms n: "))

# Calculate sine series
result = sine_series(x, n)

# Print result
print(f"Sin({x}) using {n} terms = {result}")
print(f"Math library sin({x}) = {math.sin(x)}")
