# to delete the wovels in a string#
s='Adhina'
v='aeiouAEIOU'
result=''
for i in s:
    if i in v:
        result+=i.replace(i,' ')
    else:
        result+=i
print(result)