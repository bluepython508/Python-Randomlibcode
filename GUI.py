from RandomEvents import *
from tkinter import *
tk = Tk()
tk.title("Random Event Generator")
canvas = Canvas(tk, width=1000, height=700)
canvas.grid(row=1, column=0)
frame = Frame(tk)
frame.grid(row=2, column=0)
canvas.create_text(500, 50, text='Event Generator', fill="red" )
canvas.create_text(500, 70, text='-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', fill="green" )
def update(string):
    messagebox.showinfo("Event", string)
def rolled():
    tk2 = Tk()
    #tk.wait_window(tk2)
    tk2.title("dice")
    
    def close():
        try:
            number = int(num.get())
            tk2.destroy()
            if number < 1 or number > 15:
                number = 1
            results = roll(number)
            update(results)
        except ValueError:
            messagebox.showerror("Error", "Try Again")
    num = Entry(tk2)
    num.bind("<Return>", close)
    label = Label(tk2, text="How many dice?")
    done = Button(tk2, text="Done",command=close)
    done.pack(side=BOTTOM)
    num.pack(side=RIGHT)
    label.pack(side=LEFT)
    tk2.mainloop()
def flip():
    results = flipcoin()
    update(results)
def quitprog():
    if messagebox.askokcancel(title="QUIT", message="Are you sure?"):
        tk.destroy()
quitbutton = Button(frame, text="QUIT", fg='red',bg='green', command=quitprog)
flipbutton = Button(frame, text="Flip a Coin", command=flip)
rollbutton = Button(frame, text="Roll some Dice", command=rolled)
flipbutton.grid(row=0, column=0)
rollbutton.grid(row=0, column=2)
quitbutton.grid(row=0, column=1)
tk.mainloop()

    
