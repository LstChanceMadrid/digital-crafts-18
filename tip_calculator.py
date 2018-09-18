total_amount = float(input("Enter the total amount: "))
tip_percentage_amount = float(input("Enter the tip percentage amount: "))

def tip_amount(total_amount, tip_percentage_amount):
    tip = total_amount * tip_percentage_amount / 100
    print("$" + str(tip))
    return tip
    

tip_amount(total_amount, tip_percentage_amount)