def p(x):
    flag=1
    for i in range(2,int(x/2)+1,1):
        if x%i==0:
            flag=0
            break
    if flag==1:
        print(x," is prime")
    else:
        print("Not prime")

d=int(input("Enter the number : "))
p(d)