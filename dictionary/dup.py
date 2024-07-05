dict1 = {'b': 67, 'r': 90, 'q': 8, 'a': 56, 't': 14, 'e': 8, 'y': 67,'w':60,'i':56}

set1 = set()

list1= []
for key, value in dict1.items():
    if value in set1:
        list1.append(key) 
    else:
        set1.add(value) 

for key in list1:
    del dict1[key]

print(dict1)
print(set1)
print(list1)

