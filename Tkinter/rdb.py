from tkinter import *

def clic():
    value = v.get()
    print(value)

a = Tk()
a.title("Example")
a.geometry("400x400")

v = IntVar()
v.set(1)
r1 = Radiobutton(a,text='Male',variable=v,value=1,command=clic)
r1.pack()
r2 = Radiobutton(a,text='Female',variable=v,value=2,command=clic)
r2.pack()
# Button = Button(a, text = "Submit", command=clic)
# Button.pack()
a.mainloop()