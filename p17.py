n=int(input('Enter the length : '))
li=['apple','banana','cherry','pineapple']
y=[i for i in li if len(i)<=n]
print(y)