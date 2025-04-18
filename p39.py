# create a file and first write the content to the file and then read the first 8 cahracters
f=open('adhina',"a")
f.write('Hello World!')
f=open('adhina',"r")

print(f.readline(8))