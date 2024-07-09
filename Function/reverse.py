# Without Aurgument and with return

def reverse():
    string = input ('Enter any string : ')
    reverse_string = ''
    length = len(string)
    while length > 0 :
        reverse_string += string[length - 1]
        length = length - 1
    return reverse_string   
    
print('Reverse String is : ',reverse())