from tkinter.filedialog import *
import tkinter as tk 
from tkinter import Frame, Text, END, INSERT, WORD

# canva
canvas=tk.Tk()
canvas.title("NotePad")
canvas.geometry("400x600")
canvas.config(bg="white")
top = Frame(canvas)
top.pack(padx=10, pady=5, anchor='nw')

# functions
def saveFile():
    new_file=asksaveasfile(mode='w', defaultextension=".txt", filetypes=[('text files','*.txt')])
    if new_file is None:
        text=str(entry.get(1.0,END))
        new_file.write(text)
        new_file.close()

def openFile():  
    file=askopenfile(mode='r', filetypes=[('text files','*.txt')])
    if file:
        content=file.read()
        entry.insert(INSERT,content) 
        file.close() 
        
def clearFile():
    entry.delete(1.0,END)     


# buttons
b1= tk.Button(canvas, text="Open", command=openFile)
b1.pack(in_=top, side='left', padx=5)

b2= tk.Button(canvas, text="Save", command=saveFile)
b2.pack(in_=top, side='left', padx=5)


b3= tk.Button(canvas, text="Clear", command=clearFile)
b3.pack(in_=top, side='left', padx=5)

b4= tk.Button(canvas, text="Exit", command=exit)
b4.pack(in_=top, side='left', padx=5)

entry= Text(canvas,bg = "#F9DDA4", wrap=WORD, font = ("poppins", 15))
entry.pack(padx=10, pady=5, expand=True, fill='both')



canvas.mainloop() 