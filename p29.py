# to check if a string entered by the user is a palindrome or not#
s=input('Enter the string : ')
x=s[::-1]
#print(x)
if s==x:
    print('Palindrome')
else:
    print('Not palindrome')
