import array as arr
a=arr.array('i',[])
n=int(input('enter n='))
for i in range(n):
    a.append(int (input()))
for i in range(n):
    print('a[',i,']=',a[i])
a.reverse()
print(a)
