def get_student_details(n):
    student_list = []
    for _ in range(n):
        rno = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        marks = float(input("Enter marks out of 50: "))
        student_list.append((rno, name, marks))
    return student_list

def search_student(student_list, rno):
    for student in student_list:
        if student[0] == rno:
            return student
    return None

def delete_student(student_list, rno):
    for student in student_list:
        if student[0] == rno:
            student_list.remove(student)
            return True
    return False

def display_descending(student_list):
    student_list.sort(key=lambda x: x[2], reverse=True)
    print("\nStudent details in descending order of marks:")
    for student in student_list:
        print("Roll No: ",student[0], "Name:", student[1], "Marks:", student[2])

def display_failed_students(student_list):
    print("\nList of failed students (marks < 25):")
    for student in student_list:
        if student[2] < 25:
            print(f"Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

# Main program
n = int(input("Enter the number of students: "))
student_list = get_student_details(n)

# Search for a student by roll number
rno_to_search = int(input("\nEnter roll number to search: "))
student = search_student(student_list, rno_to_search)
if student:
    print(f"\nStudent found: Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2]}")
else:
    print("Student not found.")

# Delete a student by roll number
rno_to_delete = int(input("\nEnter roll number to delete: "))
if delete_student(student_list, rno_to_delete):
    print(f"Student with roll number {rno_to_delete} deleted.")
else:
    print("Student not found to delete.")

# Display the list of students in descending order of marks
display_descending(student_list)

# Display list of failed students (marks < 25)
display_failed_students(student_list)
