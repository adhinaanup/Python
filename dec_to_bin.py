x=int(input('Enter the no : '))
s=""
while x>0:
    s=str(x%2)+s
    x=x//2
print(s)