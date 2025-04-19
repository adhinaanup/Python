x=int(input('Enter the no : '))
s=""
d="0123456789ABCDEF"
while x>0:
    r=x%16
    s=d[r]+s
    x=x//16
print("Hexa : ",s)

