# with argument and without return

def fact(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print('Factorial of given num is : ',factorial)

fact(5)