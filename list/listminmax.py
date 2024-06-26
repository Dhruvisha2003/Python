#list

list1 = [3, 5, 8, 10, 67, 34, 64, 48]
min = list1[0]
for i in range(1 , len(list1)) :
    if(list1[i] < min) :
        min = list1[i]
        list1[i] = min
print('Minimum Number is',min)

max = list1[1]
for i in range(2 , len(list1)) :
    if(list1[i] > max) :
        if list1[i] != min :
            max = list1[i]
            list1[i] = max
print('Maximum Number is',max)