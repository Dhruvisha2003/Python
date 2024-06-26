list1 = [3,4,5,6,3,2,5,7,5]
list2 = [67,45,6,4,42]

a = list2.index(4)
print(a)
value = 4
for i in range(len(list2)) :
    if list2[i] == value :
        index = i
        break
print(index)