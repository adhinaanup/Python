x=int(input('Enter the no : '))
s=""
while x>0:
    s=str(x%8)+s
    x=x//8
print('Octal no : ',s)