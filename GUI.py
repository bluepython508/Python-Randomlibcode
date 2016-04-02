from RandomEvents import *
from tkinter import *

tk = Tk()
tk.title("Random Event Generator")
canvas = Canvas(tk, width=1000, height=700)
canvas.pack()
canvas.create_text(500, 50, text='Event Generator', fill="red" )
canvas.create_text(500, 70, text='-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', fill="green" )
def rolled():
    print("hello")
flip = Button(tk, text="Flip a Coin", command=flipcoin)
roll = Button(tk, text="Roll some Dice", command=rolled)
flip.pack(side="top")
roll.pack(side="top")
