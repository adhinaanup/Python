my={}
x=input('Enter string : ')
w=x.split(" ")
for i in w:
    if i in my:
        my[i]+=1
    else:
        my[i]=1
print(my)
print(max(my.items()))