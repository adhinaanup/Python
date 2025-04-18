
#Basic Slicing
# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[1:4])

#Slicing with default parameters
# print(my_tuple[:3])
# print(my_tuple[2:])
# print(my_tuple[:])

#Using step
# print(my_tuple[::2])
# print(my_tuple[1::2])

#Negative Slicing
# print(my_tuple[-4:-1])
# print(my_tuple[::-1])

my_tuple = (10, 20, 30, 40, 50)
#Membership Test
if 20 not in my_tuple:
    print('Present')
else:
    print('Not resent')


