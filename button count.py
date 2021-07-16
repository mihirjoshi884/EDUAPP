import tkinter as tk
from tkinter import ttk


count = 0

def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1

    day1= list([count])
    day1.reverse()
    day1= day1[0]
    return day1
    


windows = tk.Tk()
windows.title("My Application")

label = tk.Label(windows, text="Hello World")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button = ttk.Button(windows, text="Click on me", command=clicked)
custom_button.grid(column=1, row=0)


windows.mainloop()
