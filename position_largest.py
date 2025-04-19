max=0
n=int(input('Enter the no : '))
length=len(str(n))
print(length)
while n>0:
    d=n%10
    if d>max:
        max=d
        a=length
    length=length-1
    n=n//10
print(max,' ',a)
