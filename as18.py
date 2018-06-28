import tkinter as tk
from tkinter import *

#Q1
dictn = {'Gaurav': '123456', 'Saurav': '789564', 'Mariam': '789895', 'Bob': '159753', 'Sanyukta': '693596',
        'Ayushkar': '852258'}
seek = tk.Tk()
frm = Frame(master=seek)
frm.pack()
scroll_ = Scrollbar(master=frm)
scroll_.pack(fill=Y, side=RIGHT)
lst = Listbox(f, yscrollcommand=scroll_.set)
lst.pack()
for i in dictn:
    lst.insert(END, '{}'.format(i))



#Q2
def update():
    dict.update({a.get(): b.get()})
    for k in dict.keys():
        print(k)
    i = k
    l.insert(END, i)

bt = Button(master=f, text="Insert", command=add)
bt.pack()
lab = Label(f,text="Name and Contact")
lab.pack()
a = Entry(f, text="Name")
b = Entry(f, text="Contact")
a.pack()
b.pack()
c.mainloop()
