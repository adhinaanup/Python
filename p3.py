s=input('Enter the string : ')
count=0
count1=0
vowels='aeiouAEIOU'
for i in s:
    if i in vowels:
        count+=1
    else:
        count1+=1

print('The no of vowels: ',count)
print('The no of consonants : ',count1)
