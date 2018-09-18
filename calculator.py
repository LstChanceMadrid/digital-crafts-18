first_number = float(input("Enter your first number: "))
operand = input("Enter an operand (+, - , * , /): ")
second_number = float(input("Enter your second number: "))

def calculate(first_number, operand, second_number):

    if (operand == "+") :
        result = first_number + second_number
        print(result)
    elif (operand == "-"):
        result = first_number - second_number
        print(result)
    elif (operand == "/"):
        result = first_number / second_number
        print(result)
    elif (operand == "*"):
        result = first_number * second_number
        print(result)
    else:
        print("Invalid input, try again.")


calculate(first_number, operand, second_number)