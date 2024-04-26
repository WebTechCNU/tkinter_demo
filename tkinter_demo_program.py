from tkinter import *
from math import *

window = Tk()

def addition(label_output):
    result = int(entry_x.get()) + int(entry_y.get())
    label_output.destroy()
    label_output = Label(window, text=result)
    label_output.grid(row=1,column=2, padx=10, pady=10)
    return label_output

def substraction(label_output):
    result = int(entry_x.get()) - int(entry_y.get())
    label_output.destroy()
    label_output = Label(window, text=result)
    label_output.grid(row=1,column=2, padx=10, pady=10)
    return label_output

def multiplication(label_output):
    result = int(entry_x.get()) * int(entry_y.get())
    label_output.destroy()
    label_output = Label(window, text=result)
    label_output.grid(row=1,column=2, padx=10, pady=10)
    return label_output

def division(label_output):
    if(int(entry_y.get()) == 0):
        label_output.destroy()
        label_output = Label(window, text="Do not divide by zero please")
        label_output.grid(row=1,column=2)
        return 0
    result = int(entry_x.get()) / int(entry_y.get())
    label_output.destroy()
    label_output = Label(window, text=result)
    label_output.grid(row=1,column=2, padx=10, pady=10)
    return label_output

def root(label_output):
    if(int(entry_x.get()) < 0):
        label_output.destroy()
        label_output = Label(window, text="Sqrt from negative!")
        label_output.grid(row=1,column=2, padx=10, pady=10)
        return 0
    result = sqrt(int(entry_x.get()))
    label_output.destroy()
    label_output = Label(window, text=result)
    label_output.grid(row=1,column=2)
    return label_output

text_label = 'SUPER CALCULATOR'
label = Label(window, text=text_label)
entry_x = Entry(window, textvariable=IntVar())
entry_y = Entry(window, textvariable=IntVar())
label_output = Label(window, text="")

button_addition = Button(window, text='+', command=lambda: addition(label_output), 
                         bg='azure1', height=2, width=5)
button_substraction = Button(window, text='-', command=lambda: substraction(label_output), 
                             bg='azure1', height=2, width=5)
button_multiplication = Button(window, text='*', command=lambda: multiplication(label_output), 
                               bg='azure1', height=2, width=5)
button_division = Button(window, text='/', command=lambda: division(label_output), 
                         bg='azure1', height=2, width=5)
button_root = Button(window, text='sqrt', command=lambda: root(label_output), 
                     bg='azure1', height=2, width=5)

label.grid(row=0,column=0, padx=10, pady=10)
entry_x.grid(row=1,column=0, padx=10, pady=10)
entry_y.grid(row=2,column=0, padx=10, pady=10)
button_addition.grid(row=1,column=1, padx=10, pady=10)
button_substraction.grid(row=2,column=1, padx=10, pady=10)
button_multiplication.grid(row=3,column=1, padx=10, pady=10)
button_division.grid(row=4,column=1, padx=10, pady=10)
button_root.grid(row=5,column=1, padx=10, pady=10)

label_output.grid(row=1,column=2, padx=10, pady=10)

window.mainloop()
