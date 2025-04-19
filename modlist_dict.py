numbers_list = [12, 45, 67, 89, 34, 23, 56, 78]
mod_value = int(input("Enter a divisor for modulus operation: "))
m={}
for i in range(len(numbers_list)):
    m[numbers_list[i]]=numbers_list[i]%mod_value

# Print the modulus results
print("Modulus results:",m)