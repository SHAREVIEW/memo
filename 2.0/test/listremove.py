data = [
    {'id': 1},
    {'id': 2},
    {'id': 3}
]

for each in data:
    if each['id'] == 1:
        data.remove(each)

print data
