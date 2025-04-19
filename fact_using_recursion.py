def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

def nCr(n,r):
    return fact(n)//(fact(r)*(fact(n-r)))

n=int(input('Enter the n : '))
r=int(input('Enter r : '))

print(nCr(n,r))