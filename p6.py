x=int(input('Enter the no : '))
rev=0
while x>0:
    n=x%10
    rev=rev*10+n
    x=x//10
print('Reverse is : ',rev)