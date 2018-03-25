import tkinter
from tkinter import ttk

window = tkinter.Tk()

ttk.Label(window, text="A Label").grid(column=0, row=0)

window.mainloop()