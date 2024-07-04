d1 = {'a':2,'b':4,'c':6}
sum = 0
# for i in d1.items():
#    if type(i[1] == int) :
#         sum = sum + i[1]
# print(sum)

for i in d1.values():
    sum = sum + i
print(sum)