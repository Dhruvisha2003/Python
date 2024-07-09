# With argument and with return

def sum1(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
    
print('Sum is : ',sum1((45,6,8,92,12,39)))