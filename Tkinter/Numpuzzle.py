from tkinter import *
import tkinter as tk
from random import shuffle

puzzle = Tk()
puzzle.title("Number Puzzle")
puzzle.geometry("400x300")
var = IntVar()
def random_num():
   numbers = list(range(1, 9)) 
   shuffle(numbers)
   for i in numbers:
      var.set(numbers[i])

label = Label(puzzle, text='Number Puzzle')
label.place(x=150, y=30)
b1 = Button(puzzle, width=6,font=16,textvariable=var)
b1.place(x=90, y=70)
b2 = Button(puzzle, width=6,font=16, textvariable=var)
b2.place(x=160, y=70)
b3 = Button(puzzle, width=6,font=16, textvariable=var)
b3.place(x=230, y=70)
b4 = Button(puzzle, width=6,font=16, textvariable=var)
b4.place(x=90, y=120)
b5 = Button(puzzle, width=6,font=16, textvariable=var)
b5.place(x=160, y=120)
b6 = Button(puzzle, width=6,font=16, textvariable=var)
b6.place(x=230, y=120)
b7 = Button(puzzle, width=6,font=16, textvariable=var)
b7.place(x=90, y=170)
b8 = Button(puzzle, width=6,font=16, textvariable=var)
b8.place(x=160, y=170)

b9 = Button(puzzle, width=6,font=16,textvariable=var)
b9.place(x=230, y=170)

btn = Button(puzzle, text='Start', command=random_num)
btn.place(x=170, y=220)

puzzle.mainloop()
