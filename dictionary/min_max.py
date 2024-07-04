dict1 = {'b':67,'r':90,'q':8,'a':56,'t':14}
list1 = list(dict1.values())
length = len(list1)
# print(list1)
min = list1[0]
for i in range(1,length):
    if list1[i] < min :
        min = list1[i]

print('Minimum Number is :',min)

max = list1[0]
for j in range(1,length):
    # print(list1[j])
    if list1[j] > max :
        max = list1[j]

print('Maximum Number is :',max)