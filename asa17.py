import tkinter as tk
from tkinter import *
import sys
def tkin():
   print("tkinter program")


# q1
c = tk.Tk()
l = Label(c, text="Hello World")
l.pack()
w = tk.Button(c, text="end",command=ends())
w.pack()
c.mainloop()

#Q2

p = tk.Button(c, text="Mark1",command=tkin())
p.pack()
c.mainloop()

#Q3
def change(w):
    w.configure(text="Mark42")
    w.grid()
r=tk.Tk()
f=tk.Frame(r)
f.pack()
w= Label(master=f,text="Change is ordinary")
w.grid(row=1)
b= Button(master=f,text="exit",command=sys.exit())
b.grid(row=2, column=1)
b2= Button(master=f, text="Custom message",command=change(w))
b2.grid(row=2, column=2)
r.mainloop()

#Q4
def other():
    res = w.get()
    fin.config(text=res)
    w.delete(0, END)

r=tk.Tk()
f=tk.Frame(r)
f.pack()
w=Entry(f)
w.bind()
enter = Button(r, text="Team iron man", command=other)
enter.pack()
fin = Label(r, text="", bg="red")
fin.pack()
r.mainloop()
