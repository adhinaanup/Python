# to change the wovels of a string to uppercase#
v='aeiouAEIOU'
s='Adhina'
result=''
for i in s:
    if i in v:
        result+=i.upper()
    else:
        result+=i
print(result)



# check if 2 strings are anagrams or not