from tkinter import *
import tkinter as tk
from random import *

puzzle = Tk()
puzzle.title("Number Puzzle")
puzzle.geometry("400x300")

display = tk.IntVar()

# arr = []
def random_num():
   numbers = list(range(1,9))
   shuffle(numbers)
#    print(numbers)
   return numbers

def output(event):
    shuffled_numbers = random_num()
    entries = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for i,entry in enumerate(entries):
        if i < len(entries):
            #  entry.config(text=shuffled_numbers[i])
            text = shuffled_numbers[i]
            display.set(text)
            

label = Label(puzzle,text='Number Puzzle',)
label.place(x=150,y=30)

b1 = Button(puzzle,width=6,textvariable=display)
b1.place(x=90,y=70)

b2 = Button(puzzle,width=6,textvariable=display)
b2.place(x=160,y=70)

b3 = Button(puzzle,width=6,textvariable=display)
b3.place(x=230,y=70)

b4 = Button(puzzle,width=6,textvariable=display)
b4.place(x=90,y=120)

b5 = Button(puzzle,width=6,textvariable=display)
b5.place(x=160,y=120)

b6 = Button(puzzle,width=6,textvariable=display)
b6.place(x=230,y=120)

b7 = Button(puzzle,width=6,textvariable=display)
b7.place(x=90,y=170)

b8 = Button(puzzle,width=6,textvariable=display)
b8.place(x=160,y=170)

b9 = Button(puzzle,width=6,textvariable=display)
b9.place(x=230,y=170)

btn = Button(puzzle,text='start')
btn.place(x=170,y=220)
btn.bind('<Button-1>',output)
puzzle.mainloop()