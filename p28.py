# to check if a digit is present in a string and find the sum of digits#
s='Adhi1na23'
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)
