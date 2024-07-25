from tkinter import *
import tkinter as tk
from random import shuffle

puzzle = Tk()
puzzle.title("Number Puzzle")
puzzle.geometry("400x300")

def random_num():
   numbers = list(range(1, 9)) 
   shuffle(numbers)
   var1.set(numbers[0])
   var2.set(numbers[1])
   var3.set(numbers[2])
   var4.set(numbers[3])
   var5.set(numbers[4])
   var6.set(numbers[5])
   var7.set(numbers[6])
   var8.set(numbers[7])

label = Label(puzzle, text='Number Puzzle')
label.place(x=150, y=30)

var1 = IntVar()
b1 = Button(puzzle, width=6,font=16,textvariable=var1)
b1.place(x=90, y=70)

var2 = IntVar()
b2 = Button(puzzle, width=6,font=16, textvariable=var2)
b2.place(x=160, y=70)

var3 = IntVar()
b3 = Button(puzzle, width=6,font=16, textvariable=var3)
b3.place(x=230, y=70)

var4 = IntVar()
b4 = Button(puzzle, width=6,font=16, textvariable=var4)
b4.place(x=90, y=120)

var5 = IntVar()
b5 = Button(puzzle, width=6,font=16, textvariable=var5)
b5.place(x=160, y=120)

var6 = IntVar()
b6 = Button(puzzle, width=6,font=16, textvariable=var6)
b6.place(x=230, y=120)

var7 = IntVar()
b7 = Button(puzzle, width=6,font=16, textvariable=var7)
b7.place(x=90, y=170)

var8 = IntVar()
b8 = Button(puzzle, width=6,font=16, textvariable=var8)
b8.place(x=160, y=170)

b9 = Button(puzzle, width=6,font=16)
b9.place(x=230, y=170)

btn = Button(puzzle, text='Start', command=random_num)
btn.place(x=170, y=220)

puzzle.mainloop()
