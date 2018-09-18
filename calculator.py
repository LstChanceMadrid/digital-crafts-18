first_number = float(input("Enter your first number: "))
operand = input("Enter an operand (+, - , * , /): ")
second_number = float(input("Enter your second number: "))

def calculate(first_number, operand, second_number):

    if (operand == "+"):
        add(first_number, second_number)
    elif (operand == "-"):
        subtract(first_number, second_number)
    elif (operand == "*"):
        multiply(first_number, second_number)
    elif (operand == "/"):
        divide(first_number, second_number)
    else:
        invalid(first_number, operand, second_number)


def add(first_number, second_number):
    result = first_number + second_number
    print(result)

def subtract(first_number, second_number):
    result = first_number - second_number
    print(result)

def multiply(first_number, second_number):
    result = first_number * second_number
    print(result)

def divide(first_number, second_number):
    result = first_number / second_number
    print(result)

def invalid(first_number, operand, second_number):
    print("Invalid input, try again.")

calculate(first_number, operand, second_number)


