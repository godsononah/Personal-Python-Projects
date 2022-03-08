# A simple python script for running java source files
"A simple python script for running java source files"

import os
os.chdir(r'C:\MyJava')              # change the current working directory to where the java file is located 

def main():
    "the main function"
    filename = input('Enter java file name: ')  # input the java source file name e.g Example.java
    compiler(filename)
    executer(filename)

def compiler(filename):
    "compiles the java source code into a .class file"
    os.system('javac {}'.format(filename))

def executer(filename):
    "runs the compile .class java file"
    os.system('java {}'.format(filename.split('.')[0]))

if __name__ == '__main__':                  # runs only when the file is executed but not when it is imported 
    main()