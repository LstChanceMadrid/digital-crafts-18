#first_number = float(input("Enter your first number: "))
#operand = input("Enter an operand (+, - , * , /): ")
print("***---------***---------***---------***")
print("---***---***---***---***---***---***---")
print("------***---------***---------***------")
print("Hello, your calculator is ready!")
print("You may press 'q' at anytime to quit.")
print("------***---------***---------***------")
print("---***---***---***---***---***---***---")
print("***---------***---------***---------***")

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
        print("---***---***---***---***---***---***---")
        print("Invalid operand, try again")
        print("---***---***---***---***---***---***---")
        return False

            


def add(first_number, second_number):
    result = first_number + second_number
    print("Your sum is {0}".format(result))

def subtract(first_number, second_number):
    result = first_number - second_number
    print("Your difference is {0}".format(result))

def multiply(first_number, second_number):
    result = first_number * second_number
    print("Your product is {0}".format(result))

def divide(first_number, second_number):
    result = first_number / second_number
    print("Your quotient.remainder is {0}".format(result))



while True:
    try:
        first_number = input("Enter your first number: ")
        if (first_number.lower() == 'q'):
            break
        first_number_t = float(first_number)
        operand = input("Enter an operand (+, - , * , /): ")
        if (operand == 'q'):
            break  
        second_number = input("Enter your second number: ")
        if (second_number == 'q'):
            break
        second_number_t = float(second_number)
        calculate(first_number_t, operand, second_number_t)          

        
    except:

        if ValueError:
            print("---***---***---***---***---***---***---")
            print("Invalid number, try again")
            print("---***---***---***---***---***---***---")





