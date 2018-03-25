import tkinter
from tkinter import ttk

window = tkinter.Tk()

name = tkinter.StringVar()

ttk.Label(window, width=12, text="Sample entry").grid(column=1, row=0)
ttk.Entry(window, width=12, textvariable=name)

window.mainloop()