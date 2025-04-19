import random

# a. Create an empty dictionary stud
stud = {}

# b. Add details of 5 students (starting from roll number 3, circular list)
students_list = [
    (1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "David"), (5, "Eve"),
    (6, "Frank"), (7, "Grace"), (8, "Hannah"), (9, "Ian"), (10, "Jack")
]

start_roll = 3  # Starting roll number
for i in range(5):
    rno, name = students_list[(start_roll - 1 + i) % len(students_list)]
    stud[rno] = name

# c. Sort and print students by roll number
sorted_stud = sorted(stud.items())
print("Students sorted by roll number:", sorted_stud)

# d. Sort and print students by name
sorted_by_name = sorted(stud.items(), key=lambda x: x[1])
print("Students sorted by name:", sorted_by_name)

# e. Create a new dictionary with marks
stud1 = {}  # Empty dictionary
for rno, name in stud.items():
    mark = random.randint(30, 100)  # Assign random marks
    stud1[rno] = {'name': name, 'mark': mark}  # Store data
print("Student Records with Marks:", stud1)

# f. Find and print the highest scorer(s)
max_mark = max(stud1.values(), key=lambda x: x['mark'])['mark']
toppers = {rno: data for rno, data in stud1.items() if data['mark'] == max_mark}
print("Top Scorers:", toppers)

# g. Read a roll number and delete that student's details
del_rno = int(input("Enter roll number to delete: "))
if del_rno in stud1:
    del stud1[del_rno]
    print("Updated Student Records:", stud1)
else:
    print("Roll number not found.")

# h. Print students who passed (mark >= 50)
passed_students = {rno: data for rno, data in stud1.items() if data['mark'] >= 50}
print("Passed Students:", passed_students)
