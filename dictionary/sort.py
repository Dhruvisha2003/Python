dict1 = {'b':67,'r':90,'q':8,'a':56,'t':14}
list1 = list(dict1.keys())
# print(list1)
length = len(list1)
# print(length)
for i in range(length-1):
    # print(i)
    for j in range(0 , length-i-1):
        # print(j)
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp


sorted_dict = {}
for i in list1 :
    sorted_dict[i] = dict1[i]

print(sorted_dict)



