flag=0
x=int(input('Enter the no : '))

for i in range(2,int(x/2)+1):
    if x%i==0:
        flag=1
        break

if flag==0:
    print('It is prime')
else:
    print('Not prime')