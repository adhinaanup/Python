def f(x):
    return lambda d:d*x
a=f(4)
print(a(5))