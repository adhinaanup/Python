x = input("Enter the binary number: ")  # Take input as a string
s = 0
i = 0
while i < len(x):
    s = s * 2 + int(x[i])
    i += 1
print("Decimal:", s)
