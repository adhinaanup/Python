x=input('Enter the string :')
l=len(x)//2
print(l)
t1=x[:l-1:-1]
t2=x[l-1::-1]
print(t2+t1)
