# merge 2 dictionaries into one#
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
m={**dict1,**dict2}
print(m)