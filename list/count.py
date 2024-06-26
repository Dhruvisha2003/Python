counteven = 0
countodd = 0
numbers = [2,45,3,78,90,53,4,8,12,11]
for i in range(len(numbers)) :
    if numbers[i] % 2 == 0 :
        counteven = counteven + 1
    else : 
        countodd = countodd + 1

print('Even Numvers are : ',counteven)
print('Odd Numbers are :',countodd)