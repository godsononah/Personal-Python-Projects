# This is a simple calculator program.

def add(num1, num2):
    "returns num1 + num2"
    return num1 + num2

def subtract(num1, num2):
    "returns num1 - num2"
    return num1 - num2

def multiply(num1, num2):
    "returns num1 * num2"
    return num1 * num2

def divide(num1, num2):
    "returns num1 / num2"
    return num1 / num2

def square(num1):
    "returns num ** 2"
    return (num1 ** 2)

def square_root(num1):
    "returns num ** 0.5"
    return (num1 ** 0.5)

def power(num1, num2):
    "returns num1 ** num2"
    return (num1 ** num2)

def percent(num1, num2=1):
    "returns (num1 / num2) * 100"
    return (num1 / num2) * 100


def main():
    "This is the main loop."
    
    print("Welcome to Onah's Simple Calculator!")
    print("""
    Using this calculator,
    you can perform some simple calculations
    on up to 2 numbers.""")
    print("""
    You will be required to input 2 numbers,
    followed by the math sign of the math operation
    that will be carried out.
    You can press Enter to skip the input of the second
    number, if your math operation does not require it.\n
    You can perform the following math operations (the signs
    for the operations are shown in the parentheses):
    addition(+), subtraction(-), multiplication(*),
    division(/), percentage(%), square of a number(**),
    square root of a number(*/), and power(^).""")
    
    while True:
        print("\nDo you want to calculate something?")
        check = input("Enter y or n: ")
        
        if check == 'n':
            print("\nThank you for using Onah's Simple Calculator.")
            print("Goodbye!")
            break
        
        elif check == 'y':
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number or press 'Enter' to skip it: ")
            sign = input("Enter the math operation sign: ")
            if sign == '+':
                result = add(float(num1), float(num2))
            elif sign == '-':
                result = subtract(float(num1), float(num2))
            elif sign == '*':
                result = multiply(float(num1), float(num2))
            elif sign == '/':
                result = divide(float(num1), float(num2))
            elif sign == '**':
                result = square(float(num1))
            elif sign == '*/':
                result = square_root(float(num1))
            elif sign == '^':
                result = power(int(num1), int(num2))
            elif sign == '%':
                result = '{}%'.format(percent(float(num1), float(num2)))
            else:
                print("You inputted an incorrect sign!")

            sign_list = ['+', '-', '*', '/', '**', '*/', '^', '%']
            if sign in sign_list:
                print(result)
        else:
            print("You entered an incorrect answer!\n")

if __name__ == '__main__':
    main()
