# Python

1. What is Python?
=> Python is a high-level ,interpreted and general-purpose programming language.
=> Python is scripting language


[datastructure type]

1. list
 => it is same as array and written with square brackets.
 => List items are ordered, changeable, and allow duplicate values.

2. tupple 
 => Tuples are written with round brackets.
 => Tuples are unchangable.
 
3. dictionary
4. set
 => Set are written with curly brackets
 => Set is the collection of the unordered items.
 => Set items are unchangeable, but you can remove items and add new items.


[How to take data of list from user]

list1 = []
element = int(input('Enter Number Of elements : '))
for i in range(element) :
     arr = int(input())
     list1.append(arr)
print(list1)

list = [2,4,3,2,4,5]
list[0] = 2 
list[-1] = 5

[mysql queries]

suppose,Here we Create stud database and register name table
we can create database and table from admin panel or like this,..
1. Create database
CREATE DATABASE stud;
2. Create table
CREATE TABLE register (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) , email VARCHAR(50), password VARCHAR(30), phone VARCHAR(30)/BIGINT)
3. Insert data
INSERT INTO register (name, email, password, phone) VALUES ('John', 'john@example.com
, '123456', 1234567890)
4. Select data
SELECT * FROM register;
SELECT name from register where id=1
5. Delete data
DELETE FROM register WHERE id=1;
6. Update data
UPDATE register SET name='John' WHERE id=1;
