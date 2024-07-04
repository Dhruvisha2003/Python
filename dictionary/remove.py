dict = {'name':'dhruvi','num':932}
keyname = 'num'
new_dict = {}
for i , value in dict.items():
    # print(i , value)
    if i != keyname :
        new_dict[i] = value

print(new_dict)