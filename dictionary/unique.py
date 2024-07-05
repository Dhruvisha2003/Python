dict1 = {'b':67, 'r':90, 'q':8, 'a':56, 't':14, 'e':8, 'y':67}

new_dict = {}
for key ,value in dict1.items():
    if value not in new_dict.values() :
        new_dict[key] = value
        
print(new_dict)