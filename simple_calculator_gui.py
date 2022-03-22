# This is a simple calculator GUI made using the Python tKinter module

from tkinter import *

def add(num1, num2):
    "returns num1 + num2"
    result = num1 + num2
    print('Result => {}'.format(result))
    show = Toplevel(root)
    show.title('Result')
    msg = Message(show, text=('{} + {} = {}'.format(num1, num2, result)))
    msg.config(bg='pink', font=('times', 20, 'italic'))
    msg.pack(expand=YES, fill=BOTH)

def subtract(num1, num2):
    "returns num1 - num2"
    result = num1 - num2
    print('Result => {}'.format(result))
    show = Toplevel(root)
    show.title('Result')
    msg = Message(show, text=('{} - {} = {}'.format(num1, num2, result)))
    msg.config(bg='pink', font=('times', 20, 'italic'))
    msg.pack(expand=YES, fill=BOTH)

def multiply(num1, num2):
    "returns num1 * num2"
    result = num1 * num2
    print('Result => {}'.format(result))
    show = Toplevel(root)
    show.title('Result')
    msg = Message(show, text=('{} * {} = {}'.format(num1, num2, result)))
    msg.config(bg='pink', font=('times', 20, 'italic'))
    msg.pack(expand=YES, fill=BOTH)

def divide(num1, num2):
    "returns num1 / num2"
    result = num1 / num2
    print('Result => {}'.format(result))
    show = Toplevel(root)
    show.title('Result')
    msg = Message(show, text=('{} / {} = {}'.format(num1, num2, result)))
    msg.config(bg='pink', font=('times', 20, 'italic'))
    msg.pack(expand=YES, fill=BOTH)

root = Tk()

ent1 = Entry(root)
ent1.insert(0, 'enter first number')
ent1.pack(side=TOP, fill=X)

ent2 = Entry(root)
ent2.insert(0, 'enter second number')
ent2.pack(side=TOP, fill=X)

addbtn = Button(root, text='add', command=(lambda: add(float(ent1.get()), float(ent2.get()))))
addbtn.pack(side=LEFT, expand=YES, fill=BOTH)

subbtn = Button(root, text='subtract', command=(lambda: subtract(float(ent1.get()), float(ent2.get()))))
subbtn.pack(side=RIGHT, expand=YES, fill=BOTH)

mulbtn = Button(root, text='multiply', command=(lambda: multiply(float(ent1.get()), float(ent2.get()))))
mulbtn.pack(side=LEFT, expand=YES, fill=BOTH)

divbtn = Button(root, text='divide', command=(lambda: divide(float(ent1.get()), float(ent2.get()))))
divbtn.pack(side=RIGHT, expand=YES, fill=BOTH)

quitbtn = Button(root, text='Quit', bg='red', command=root.destroy)
quitbtn.pack(expand=YES)

root.mainloop()
