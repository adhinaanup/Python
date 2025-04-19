# Recursive function to find the sum of digits
def sum_of_digits(n):
    if n == 0:  # Base case: when number is 0, sum is 0
        return 0
    return (n % 10) + sum_of_digits(n // 10)  # Recursive case

# Input: Number from user
num = int(input("Enter a number: "))

# Compute and print the sum of digits
print(f"Sum of digits of {num} is: {sum_of_digits(num)}")
