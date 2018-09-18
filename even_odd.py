number = int(input("Enter an integer: "))

def even_or_odd(number):
    if (number % 2 == 0):
        print("Your integer is Even")
    else:
        print("Your integer is Odd")

even_or_odd(number)