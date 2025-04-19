x=input('Enter the string : ')
flag=0
j=""
for i in range(len(x)):
    if x[i]==" ":
        x=x.replace(" ","*")
        flag=1
if flag==0:
    j="$"+x+"$"
    print(j)
else:
    print(x)