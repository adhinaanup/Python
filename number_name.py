dic={'0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
    '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"}
output=''
n=int(input('Enter the no : '))
for i in str(n):
    output+=dic[i]+' '
print(output)