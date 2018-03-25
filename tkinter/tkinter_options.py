import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# background="..." doesn't work...
ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
ttk.Style().configure('green/black.TButton', foreground='green', background='black')

label = ttk.Label(root, text='DEMO!', style='green/black.TLabel')
label.pack()

button = ttk.Button(root, text='Click Me!', style='green/black.TButton')
button.pack()

root.mainloop()