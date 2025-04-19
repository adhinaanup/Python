x=input('Enter the string : ')
d='0123456789'
v='aeiouAEIUO'
vowels=0
consonants=0
digits=0
blanks=0
for i in x:
    if i in v:
        vowels+=1
    elif i in d:
        digits+=1
    elif i in " ":
        blanks+=1
    else:
        consonants+=1
print("Vowels : ",vowels,"\nConsonants : ",consonants,"\nBlanks : ",blanks,"\nDigits :",digits)

