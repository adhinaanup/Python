# take a number as an input from the user and find the factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input('Enter the no : '))
print(fact(x))