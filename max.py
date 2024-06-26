a = input('Enter A : ')
b = input('Enter B : ')
c = input('Enter C : ')
d = input('Enter D : ')
e = input('Enter E : ')

if a > b :
    if a > c :
        if a > d :
            if a > e :
                print('A is max')
            else :
                print('E is max')
        else : 
            if d > e :
                print('D is max')
            else :
                print('E is max')
    else : 
        if c > d :
            if c > e :
                print('C is max')
            else :
                print('E is max')
        else :
            if d > e :
                print('D is max')
            else :
                print('E is max')
else :
    if b > c :
        if b > d :
            if b > e :
                print('B is max')
            else :
                print('E is max')
        else :
            if d > e :
                print('D is max')
            else :
                print('E is max')
    else :
        if c > d :
            if c > e :
                print('C is max')
            else :
                print('E is max')
        else :
            if d > e :
                print('D is max')
            else :
                print('E is max')