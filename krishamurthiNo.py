import math as m
n1=int(input('Enter the no : '))
n=n1
f=0
while n>0:
    d=n%10
    f=f+m.factorial(d)
    print(f)
    n=n//10
print(f)
