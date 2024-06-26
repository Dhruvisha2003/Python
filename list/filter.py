str_list = ['he','dr','dh','ji','ho','d','rt']
new_list =[]
i = 0
while i < len(str_list) :
    current_str = str_list[i]
    if current_str[0] == 'd' :    
        new_list.append(current_str)
    i = i + 1

print(new_list)
