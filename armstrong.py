s=0
n1=int(input('Enter the no : '))
n=n1
while n>0:
    d=n%10
    s+=d**len(str(n1))
    n//=10
print(s)
print(n)
if s==n1:
    print('Armstrong')
else:
    print('Not')
