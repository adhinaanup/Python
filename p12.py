def l(x,y,z):
    if x>=y and x>=z:
        print(x," is largest")
    elif y>=x and y>=z:
        print(y," is largest")
    else:
        print(z," is largest")

x=int(input("Enter no 1 :"))
y=int(input("Enter no 2 :"))
z=int(input("Enter no 3 :"))
l(x,y,z)