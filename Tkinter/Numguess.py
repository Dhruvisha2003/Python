from tkinter import *
from random import*
def checkguess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)

root=Tk()
root.geometry("500x400")
ranNum=randint(0, 10)
chance=5

var=IntVar()
disp=StringVar()

l=Label(root,text='Number Guessing Game',font=('sans-serif', 20))
l.pack()
e1=Entry(root,textvariable=var,font=('sans-serif',16))
e1.pack()
Btn = Button(root, text = "Submit", command=checkguess)
Btn.pack()
l2=Label(root,textvariable=disp,font=('sans-serif', 14))
l2.pack()

mainloop()