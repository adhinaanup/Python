# Program to process student names

def process_student_names():
    students = input("Enter student names separated by space: ").split()

    # a) Sort names in alphabetical order
    sorted_names = sorted(students)
    print("Sorted Names:", sorted_names)

    # b) Find the name with the largest length
    longest_name = max(students, key=len)
    print("Longest Name:", longest_name)

    # c) Print names starting with letter 'A'
    names_starting_with_A = [name for name in students if name.startswith('A')]
    print("Names starting with A:", names_starting_with_A)

    # d) Print names in reverse alphabetical order with all names in uppercase
    reverse_sorted_upper = sorted(students, reverse=True, key=str.upper)
    print("Names in reverse alphabetical order (uppercase):", [name.upper() for name in reverse_sorted_upper])

    # e) Print names in order of length
    sorted_by_length = sorted(students, key=len)
    print("Names sorted by length:", sorted_by_length)


process_student_names()
