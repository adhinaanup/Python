#take a string as an  input from the user and check if the string is a palindrom or not
x=input('Enter the string : ')
y=x[::-1]
if x==y:
    print('Palindrome')
else:
    print('Not palindrome')
# print(y)