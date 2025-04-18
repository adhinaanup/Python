
input_list = input("Enter a list of elements separated by spaces: ").split()
input_list = [int(i) if i.isdigit() else i for i in input_list]
result_list = [item for item in input_list if input_list.count(item) == 1]
print(f"List after removing elements that occur more than once: {result_list}")