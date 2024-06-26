# num = int(input('Enter a Number : '))

# if num % 2 == 0 :
#     print('Number is Even')
# else :
#     print('Number is Odd')   


#----------table------------
# num = int(input('Enter any Number : '))
# for i in range(1 , 11) :
#     print(num,'X', i, '=', num*i)

# i = 1
# while i<=10 :
#     print(num,'X', i, '=', num*i) 



#---------fibonacci----------
# n1 = 0
# n2 = 1
# num = int(input('Enter Number : '))
# print(n1)
# print(n2)
# for i in range(2 , num) :
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3 
#     print(n3)

# i = 2
# while i < num :
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3)
#     i+=1


#---------------Armstrong-------------
# num = int(input('Enter Number : '))
# number = num
# sum = 0
# while number > 0 :
#     rem = number % 10
#     sum += rem*rem*rem
#     number = int(number/10)

# if num == sum :
#     print(num, 'is Armstrong')
# else :
#     print(num, 'is not Armstrong')



#-------palindrome------
# num = int(input('Enter Number : '))
# temp = num
# rev = 0
# while temp > 0 :
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp = int(temp / 10)
# if num == rev :
#     print (num,'is Palindrome')
# else :
#     print(num,'is not Palindrome')


# num = int(input('Enter Number : '))
# temp = num
# ans = str(temp)
# rev = 0
# for i in range(len(ans)) :
#       rem = temp % 10
#       rev = rev * 10 + rem
#       temp = int(temp / 10)
#       print(rev) 

# if rev == num :
#     print (num,'is Palindrome')
# else :
#     print(num,'is not Palindrome')



#-----------prime----------
# num = int(input('Enter Number : '))
# if num <= 1 :
#     print('Enter Number Greater then 1')
# else :
#     for i in range(2 , num) :
#         Isprime = num % i == 0
#         # print(Isprime)
#         break
# if Isprime :
#     print(num,'is not Prime')
# else :
#     print(num,'is Prime')


# i = 2
# while i<=num :
#     Isprime = num % i == 0
#     break

# if Isprime :
#     print(num,'is not Prime')
# else :
#     print(num,'is Prime')
