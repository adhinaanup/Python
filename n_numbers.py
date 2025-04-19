li=[]
n=int(input('Enter the limit : '))
for i in range(n):
    j=int(input('Enter the no : '))
    li.append(j)
print(li)
sum=0
for i in li:
    sum+=i
li.sort()
print("Sum : ",sum)
print("Average : ",(float)(sum/n))
print("Maximum : ",li[-1])
print('Minimum  : ',li[0])
print('Sorted list : ',li)
