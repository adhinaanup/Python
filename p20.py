from functools import reduce
li=[1,2,3,4,5]
x=lambda a,b:a*b
print(reduce(x,li))