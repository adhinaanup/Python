li=[1,2,3,"None",5,6,"None",9]
count=0
for i in li:
    count+=1
    if i=="None":
        li.pop(count-1)
print(li)