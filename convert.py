# suppose we take 4000 as seconds
# take // for decimal number

seconds = int(input('Enter Seconds : '))
hours = seconds//3600  # 4000/3600=1 1 hr = 3600 sec. 
hours1 = seconds%3600  # 400 
minutes = hours1//60   # 400/60 = 6
seconds1 = hours1%60   # 400%60 = 40
print(hours,':',minutes,':',seconds1)

# print(21+34)