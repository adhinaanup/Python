f=open('integers.txt','r')
count=0
avg=0.0
sum=0
for i in f:
    count+=1
    sum+=int(i)
avg=sum/count
print('Average of numbers : ',avg)
f.close()