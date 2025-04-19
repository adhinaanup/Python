x=input('Enter : ')
s=''
for i in range(len(x)):
    s=s+x[len(x)-i-1]
print(s)

if(s==x):
    print('P')
else:
    print('Not')