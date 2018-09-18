number = int(input("Enter an integer: "))

def fizz_buzz(number):
    if(number % 3 == 0 and number % 5 == 0):
        print("Fizz Buzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")

fizz_buzz(number)