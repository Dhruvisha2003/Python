str_list = ['he', 'dr', 'dh', 'ji', 'd', 'rt', 'hr', 6, 7, 5]
new_list = []
i = 0
for i in str_list :
    if type(i) == str and i[0] == 'd' :
        new_list.append(i)
print(new_list)