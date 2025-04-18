# update set1 by adding the elements from set2 except common elements
set1 = {10, 20, 30, 40, 50}#
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)