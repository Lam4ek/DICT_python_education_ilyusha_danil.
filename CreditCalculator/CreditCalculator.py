import math
credit_amount = int(input("Enter the loan principal:"))
print("What do you want to calculate?")
print('type "m" – for number of monthly payments,')
print('type "p" – for the monthly payment:')
function = input()
a = int(input('Enter the monthly payment:'))
b = math.ceil(credit_amount/a)
lastpayment = credit_amount-(a-1) * b
while True:
    if function == "m":
        print("It will take " + str(b) + " months to repay the loan")
    elif function == "p" and a%2 == 0:
        print("Your monthly payment = " + str(b))
    else:
        print("Your monthly payment = " + str(b) + " and the last payment = " + str(lastpayment))
    break

    
