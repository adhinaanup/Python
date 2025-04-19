def sqrt_newton(number):
    guess = number  # Start with the number itself
    while abs(guess * guess - number) > 1e-6:  # Continue until close enough
        guess = (guess + number / guess) / 2  # Newton's formula
    return guess

# Get user input
num = float(input("Enter a number: "))

# Compute and print the square root
print(f"Square root of {num} ≈ {sqrt_newton(num)}")
