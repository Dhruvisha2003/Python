import tkinter as tk
from tkinter import *
calc = tk.Tk()
calc.title("Calculator")
calc.geometry("300x280")

dis = tk.StringVar()

a = Entry(calc,textvariable=dis,width=45)
a.place(x=10,y=10)

def displaydata(event):
    text = event.widget.cget("text")
    current_value = dis.get()
    new_value = current_value + text
    dis.set(new_value)
   
def result():
    value = dis.get()
    result = eval(value)
    dis.set(result)

b1 = Button(calc,text='AC',width=5)
b1.place(x=30,y=50)
b1.bind("<Button-1>",displaydata)

b2 = Button(calc,text='C',width=5)
b2.place(x=90,y=50)
b2.bind("<Button-1>",displaydata)

b3 = Button(calc,text='%',width=5)
b3.place(x=150,y=50)
b3.bind("<Button-1>",displaydata)

b4 = Button(calc,text='/',width=5)
b4.place(x=210,y=50)
b4.bind("<Button-1>",displaydata)

b5 = Button(calc,text='7',width=5)
b5.place(x=30,y=90)
b5.bind("<Button-1>",displaydata)

b6 = Button(calc,text='8',width=5)
b6.place(x=90,y=90)
b6.bind("<Button-1>",displaydata)

b7 = Button(calc,text='9',width=5)
b7.place(x=150,y=90)
b7.bind("<Button-1>",displaydata)

b8 = Button(calc,text='*',width=5)
b8.place(x=210,y=90)
b8.bind("<Button-1>",displaydata)

b9 = Button(calc,text='4',width=5)
b9.place(x=30,y=130)
b9.bind("<Button-1>",displaydata)

b10 = Button(calc,text='5',width=5)
b10.place(x=90,y=130)
b10.bind("<Button-1>",displaydata)

b11 = Button(calc,text='6',width=5)
b11.place(x=150,y=130)
b11.bind("<Button-1>",displaydata)

b12 = Button(calc,text='-',width=5)
b12.place(x=210,y=130)
b12.bind("<Button-1>",displaydata)

b13 = Button(calc,text='1',width=5)
b13.place(x=30,y=170)
b13.bind("<Button-1>",displaydata)

b14 = Button(calc,text='2',width=5)
b14.place(x=90,y=170)
b14.bind("<Button-1>",displaydata)

b15 = Button(calc,text='3',width=5)
b15.place(x=150,y=170)
b15.bind("<Button-1>",displaydata)

b16 = Button(calc,text='+',width=5)
b16.place(x=210,y=170)
b16.bind("<Button-1>",displaydata)

b17 = Button(calc,text='0',width=13)
b17.place(x=30,y=210)
b17.bind("<Button-1>",displaydata)

b18 = Button(calc,text='.',width=5)
b18.place(x=150,y=210)
b18.bind("<Button-1>",displaydata)

b19 = Button(calc,text='=',width=5)
b19.place(x=210,y=210)
b19.bind("<Button-1>",result)

mainloop()