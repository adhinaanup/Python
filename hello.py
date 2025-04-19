s=input('Enter : ')
l=len(s)//2
str1=""
str2=""
i=l-1
j=len(s)-1
while i>=0:
    str1+=s[i]
    i-=1
if len(s)%2!=0:
    str1+=s[l]
while j>=l+(len(s)%2):
    str2+=s[j]
    j-=1
str3=str1+str2
print(str3)
