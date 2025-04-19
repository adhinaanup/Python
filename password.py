x=input('Enter the password : ')
length=len(x)
no='0123456789'
sc='@#$'
a=0
b=0
c=0
d=0
for i in x:
    if(i>='A' and i<='Z'):
        a=1
    if(i>='a' and i<='z'):
        b=1
    if i in no:
        c=1
    if i in sc:
        d=1
if (a==1 and b==1 and c==1 and d==1 and length>=6):
    print('strong')
else:
    print('not strong')

