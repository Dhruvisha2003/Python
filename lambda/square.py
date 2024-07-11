list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 =[]
square = lambda x:list2.append(x**3)
for i in list1:
    square(i)

print(list2)