# take a string as an input from the user and print the number of vowels and the number of consonants
count=0
count1=0
vowels='aeiouAEIOU'
x=input('Enter the string : ')
for i in x:
    if i in vowels:
        count+=1
    else:
        count1+=1
print('The no of vowels  : ',count)
print('The no of consonants : ',count1)
