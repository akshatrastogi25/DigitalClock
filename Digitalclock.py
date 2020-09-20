import time
from tkinter import *
root = Tk()
root.title("Digital Clock")
root.geometry("250x100+0+0")
root.resizable(0,0)
label = Label(root, font=("Arial", 25, 'italic'), bg="black", fg="grey", bd =30)
label.grid(row =0, column=1)
def clock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, clock)
clock()
root.mainloop()