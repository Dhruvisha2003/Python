list1 = [2,4,6,4,8,3,3]
length = len(list1)

for i in range(length) :
    for j in range(i+1 , length) :
        if list1[i] == list1[j] :
            list1[j] = list1[j+1]
            length = length - 1

for i in range(length):
    print(list1[i])     


# i = 0
# while i < length :
#     j = i + 1
#     while j < length :
#         if list1[i] == list1[j] :
#             list1[j] = list1[j+1]
#             length = length - 1
#         else:
#             j = j + 1
#     i = i + 1