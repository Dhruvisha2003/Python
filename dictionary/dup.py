dict1 = {'b':67, 'r':90, 'q':8, 'a':56, 't':14, 'e':8, 'y':67}
my_list = list(dict1.values())
new_dict = {}
for value in my_list:
    if value != new_dict.values():
        new_dict[value] = value

new_list = list(new_dict.values())
print(new_list)
