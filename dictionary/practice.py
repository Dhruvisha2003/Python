# s1 = {'Name':'Dhruvisha','Surname':'Vekariya','Number':'986469'}
# s1 = dict({'Name':'Dhruvisha','Course':'Python'})
# s1 = dict([('Name','Dhruvisha'),('Course','Python')])
s1 = {'Name':'Dhruvisha','Number':{34,56,78,23}}

# s1['age']=32

s1.update({'Age' : 67})
# s1.update({'Name':'Jinal'})
print(s1)
# for i in s1.items() :
#     # print(i ,':',s1[i])
#     print(i[0],':',i[1])

# s1['Course'] = 'Python'
# s1.update({'Fees':'60000'})

# print(s1.get('Name'))
# print(s1['Name'])
# print(s1.keys())
# print(s1.values())
# print(s1.items())

# for i in s1.items():
#     if(type(i[1])==list or type(i[1])==set):
#         for j in i[1]:
#             print(j)


# s1 = {'name':'jhxn','num':45678}
# s2={'num':'4rfvd'}
s1={"name":45,"number":3245546,"course":67,'fees':50000}
print(sorted(s1.keys()))
# s3 = {'name2':'jdfhcn'}
# s={**s1,**s2,**s3}
# print(s)
# s2 = s1.copy()
# print(s2)
# s1.pop('name')
# print(s1)

# s1.update({'name1':'ghcxd','name2':'ghcxd'})
# s1.update({})

# s1.popitem()
# del s1['name1']
# del s1
# print(s1)

# keyname = 'num'

# for i in s1.keys():
#     if i == keyname:
#         print(i)
#     else:
#         print('not found')