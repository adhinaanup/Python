# Program to process student data from a file

def create_data_file(filename):
    data = """1|aswith|30|40|50
2|john|45|35|40
3|emma|50|50|45
4|oliver|20|30|25
5|sophia|48|49|50"""
    with open(filename, 'w') as file:
        file.write(data)

def read_student_data(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            rno, name, m1, m2, m3 = int(parts[0]), parts[1], int(parts[2]), int(parts[3]), int(parts[4])
            total = m1 + m2 + m3
            students.append({'rno': rno, 'name': name, 'm1': m1, 'm2': m2, 'm3': m3, 'total': total})
    return students

def print_rank_list(students):
    students.sort(key=lambda x: x['total'], reverse=True)
    print("Rank List:")
    for student in students:
        print(student['rno'], student['name'], student['total'])

def print_passed_students(students):
    print("Passed Students:")
    for student in students:
        if student['m1'] >= 25 and student['m2'] >= 25 and student['m3'] >= 25:
            print(student['rno'], student['name'])

def print_pass_percentage(students):
    total_students = len(students)
    for i in range(1, 4):
        passed = sum(1 for student in students if student[f'm{i}'] >= 25)
        print(f"Pass percentage in Subject {i}: {passed / total_students * 100:.2f}%")

def print_top_students(students):
    print("Students with 80% or more in all subjects:")
    for student in students:
        if student['m1'] >= 40 and student['m2'] >= 40 and student['m3'] >= 40:
            print(student['rno'], student['name'])

filename = "students.txt"
create_data_file(filename)
students = read_student_data(filename)
print_rank_list(students)
print_passed_students(students)
print_pass_percentage(students)
print_top_students(students)
