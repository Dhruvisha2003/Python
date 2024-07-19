# import array
# a=array.array('i',[12,13,14])
# print(a[0])
# we can not print full array like print(a) but we can access value with index number or we can print full array with iteration

# from array import *
# a=array('i',[12,13,14])
# print(a[0])

import array as arr
a = arr.array('i',[])
num = int(input('Enter Values:'))
for i in range(num):
    a.append(int(input()))
for i in range(num):
    print('a[',i,']=',a[i])