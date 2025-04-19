# List of (roll number, name) tuples
L = [(1, 'Aswith'), (3, 'Rharles'), (2, 'Bibit')]

# Sort by roll number (default sorting based on first value in tuple)
L_sorted_by_rno = sorted(L)

# Sort by name (sorting based on second value in tuple)
L_sorted_by_name = sorted(L, key=lambda x: x[1])

# Print sorted lists
print("Sorted by Roll Number:", L_sorted_by_rno)
print("Sorted by Name:", L_sorted_by_name)
