# A simple python GUI for running java source files
"A simple python GUI for running java source files"

import os, sys
from tkinter import *

def main():
    "the main function"
    dirname = os.path.split(ent.get())[0] 
    os.chdir('{}'.format(dirname))                               # change the current working directory to where the java file is located 
    filename = os.path.split(ent.get())[1]

    def compiler(filename):
        "compiles the java source code into a .class file"
        os.system('javac {}'.format(filename))

    def executer(filename):
        "runs the compile .class java file"
        os.system('java {}'.format(filename.split('.')[0]))

    compiler(filename)
    executer(filename)



root = Tk()
root.title('Running java source file...')

row = Frame(root)
row.pack(side=TOP, fill=BOTH)              
label = Label(row, text='Enter java file path')
label.pack(side=LEFT)
ent = Entry(row)
ent.pack(side=RIGHT, expand=YES, fill=X)

row2 = Frame(root)
row2.pack(side=TOP, expand=YES, fill=BOTH)
runbutton = Button(row2, text='run file', command=main)
runbutton.config(height=3, width=15, font=('times', 10, 'bold'), bg='green', fg='black')
runbutton.pack(side=LEFT, expand=YES, fill=X, padx=20, pady=20)              
quitbutton = Button(row2, text='quit', command=sys.exit)
quitbutton.config(height=3, width=15, font=('times', 10, 'bold'), bg='red', fg='black')
quitbutton.pack(side=RIGHT, expand=YES, fill=X, padx=20, pady=20)

if __name__ == '__main__':
    root.mainloop()
