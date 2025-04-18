address = {"state": "Texas", 'city': 'Houston'}
person = {'name': 'Jessa', 'company': 'Google', 'address': address}
for i in person:
    if i=='address':
        for j in address:
            print(j)