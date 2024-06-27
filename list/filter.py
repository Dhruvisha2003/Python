str_list = ['he', 'dr', 'dh', 'ji', 'd', 'rt', 'hr', 6, 7, 5]

new_list = []
i = 0
while i < len(str_list):
    current_str = str_list[i]
    if isinstance(current_str, str) and current_str[0] == 'd':
        new_list.append(current_str)
    i = i + 1

print(new_list)




# new_list = []
# i = 0
# while i < len(str_list) :
#     current_str = str_list[i]
#     if current_str[0] != 'd' :
#         str_list.remove(str_list[i])
#         # new_list.append(str_list)
#     i = i + 1

# print(str_list)