x=input('Enter the string : ')
flag=1
for i in range(len(x)//2):
    if x[i]!=x[len(x)-i-1]:
        flag=0
if flag==1:
    print('Palindrome')
else:
    print('Not palindrome')