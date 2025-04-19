li1=[1,2,3,4,7,8]
li2=[3,4,5,6,7]
li3=[]
for i in li1:
    for j in li2:
        if i==j:
            li3.append(i)
print(li3)