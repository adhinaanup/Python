n = int(input("Enter the number of elements: "))
li = [int(input("Enter element {}: ".format(i + 1))) for i in range(n)]
num = int(input("Enter the target sum: "))

seen= set()

for i in range(n):
    for j in range(i + 1, n):
        if li[i] + li[j] == num and (li[j], li[i]) not in seen:
            print([li[i], li[j]])
            seen.add((li[i], li[j]))