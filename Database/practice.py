import mysql.connector as conn
con = conn.connect(host="localhost",user="root",password="",database='student_detail')
if con.is_connected():
    print('connected')
else:
    print('not')

mycursor = con.cursor()

# --------------insert------------
# name = input('Enter Name:')
# contact = input('Enter Contact:')
# email = input('Enter Email:')
# password = input('Enter Password:')
# query = "insert into register(name,contact,email,password) values(%s,%s,%s,%s)"
# val = [('ankit',8596589658,'ak12@gmail.com','ankit456'),('kunj',5426589325,'kunj@gmail.com','123456')]

#--------------select------------
# query= 'select * from register'
# query = 'select * from register where name="jinal"'
# query = 'select name from register order by name desc'
# query = 'select * from register limit 2'
query = 'select * from register limit 2 offset 2'

#------------delete-----------
# query = 'delete from register where name="ankit"'
# query = 'drop table register'
#  query = 'drop table if exist register'


#-------------update-----------
# query = "update register set name='mohitkumar' where id='3'"

mycursor.execute(query)
# con.commit()
result = mycursor.fetchall()
for i in result:
    print(i)
# print(mycursor.rowcount,'record deleted')
# print(mycursor.rowcount,'record selected')
# print(mycursor.rowcount,'record updated')
# mycursor.close()