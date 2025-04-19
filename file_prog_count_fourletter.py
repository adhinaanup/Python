f = open('hello.txt', 'r')
count = 0
c = f.read()
f.close()

w = c.split()  # Corrected: Splitting on all whitespace

for i in w:
    if len(i) == 4:
        count += 1

print('Count:', count)
