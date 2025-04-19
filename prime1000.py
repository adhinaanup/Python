# Loop through numbers from 2 to 999
for num in range(2, 1000):
    is_prime = True  # Assume the number is prime

    # Check if num is divisible by any number from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False  # Not a prime number
            break  # Stop checking further

    if is_prime:
        print(num, end=" ")  # Print prime number
