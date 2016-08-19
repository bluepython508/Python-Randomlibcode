#!/bin/python3
from RandomEvents import *
from tkinter import *
from pyautogui import *

def update(string):
	alert(text=string, title="Event", button='OK')
def rolled():
	try:
		number = int(prompt(text="How many dice would you like to roll?(1-15)", title="Dice"))
		if number or number == 0:
			if number < 1 or number > 15:
				number = 1
			results = roll(number)
			update(results)
		else:
			alert(title="Error", text="ERROR: Please enter a number between 1 and 15", button="OK")
	except ValueError:
		alert(title="Error", text="ERROR: Please enter a number between 1 and 15", button='OK')
def flip():
	results = flipcoin()
	update(results)
def quitprog():
	if confirm(title="QUIT", text="Are you sure?", buttons=['Quit','Cancel'])== "Quit":
		tk.destroy()

def main():
	global tk
	tk = Tk()
	tk.title("Random Event Generator")
	canvas = Canvas(tk, width=1000, height=700)
	canvas.grid(row=1, column=0)
	frame = Frame(tk)
	frame.grid(row=2, column=0)
	canvas.create_text(500, 50, text='Random Event Generator', fill="red" )
	canvas.create_text(500, 70, text='-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', fill="green" )
	quitbutton = Button(frame, text="QUIT", fg='red',bg='green', command=quitprog)
	flipbutton = Button(frame, text="Flip a Coin", command=flip)
	rollbutton = Button(frame, text="Roll some Dice", command=rolled)
	flipbutton.grid(row=0, column=0)
	rollbutton.grid(row=0, column=2)
	quitbutton.grid(row=0, column=5)
	tk.mainloop()
if __name__ == "__main__":
	main()
