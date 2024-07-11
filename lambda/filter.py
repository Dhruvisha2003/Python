list1 = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []

filtr = lambda x:even.append(x) if x%2==0 else odd.append(x)
for i in list1:
    filtr(i)

print('Even numbers are :',even)
print('Odd numbers are :',odd)


