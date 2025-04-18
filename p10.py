def fact(x):
    f=1
    i=1
    while i<=x:
        f=f*i
        i=i+1
    print("Factorial is : ",f)
x=int(input("Enter the no : "))
fact(x)