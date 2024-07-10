# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# add = [i+1 for i in numbers]
# print(add)         


# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'orange']
# output = [x.upper() for x in fruits]
# print(output)

# vowels = ['a','e','i','o','u']
# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'orange']
# output = [x for x in fruits if   in x]
# print(output)


# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'orange']
# output = [x for x in fruits if len(x) > 5]
# output = [x for x in fruits if len(x) == 5]
# output = [x for x in fruits if len(x) < 5]
# print(output)


# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'orange']
# output = [len(x) for x in fruits]
# output = [x for x in fruits if 'a' in x]
# print(output)


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# even = [i for i in numbers if i%2==0]
# print(even)
# odd = [i for i in numbers if i%2==1]
# print(odd)
# positive = [i for i in numbers if i>0]
# print(positive)
# negative = [i for i in numbers if i<0]
# print(negative)
# square = [i**2 for i in numbers]
# print(square)
# odd_negative = [i for i in numbers if i%2==1 and i<0]
# print(odd_negative)
# number_plus5 = [i+5 for i in numbers]
# print(number_plus5)
# prime = [x for x in numbers if all(x%y!=0 for y in range(2,x))]
# print(prime)