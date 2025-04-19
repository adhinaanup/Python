# Program to manipulate personal details using a list

def personal_details():
    stud = []  # a. Create an empty list

    stud += [12345]  # b. Add roll number using + operator

    stud.append("John Doe")  # c. Append name

    stud.extend(["New York", "10001", "9876543210"])  # d. Extend with place, pin, and mobile number
    print(stud)
    stud.insert(0, "KTU123456")  # e. Insert KTU-ID at index 0

    print("KTU-ID:", stud[0], "Name:", stud[1])  # f. Print KTU-ID and name

    if isinstance(stud[1], str):  # Ensure the name is a string before finding length
        print("Number of characters in name:", len(stud[1]))  # g. Print length of name

    if isinstance(stud[-1], str) and stud[-1].isdigit():  # Ensure the phone number is a string
        print("Last 5 digits of phone number:", stud[-1][-5:])  # h. Print last 5 digits of phone number

    stud.reverse()  # i. Reverse the list
    print("Reversed list:", stud)

    if "John Doe" in stud:  # Check if name exists before finding the index
        print("Index of name:", stud.index("John Doe"))  # j. Find index of name
    else:
        print("Name not found in list.")


personal_details()
