import math
print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
function = input()
if function == "n":
    LoanPrincipal = int(input("Enter the loan principal:"))         #Основная сумма кредита (A)
    MonthlyPayment = int(input("Enter the monthly payment:"))       #Ежемесячный платеж
    LoanInterest = int(input("Enter the loan interest:"))           #проценты по кредиту

    MonthlyPercentage = LoanInterest/(100*12)              #i – номинальная(месячная) процентная ставка
    a = MonthlyPayment/(MonthlyPayment -  MonthlyPercentage * LoanPrincipal)
    b = 1+MonthlyPercentage
    n = math.ceil(math.log(a, b))
    years = n // 12
    month = n - years * 12
    print("It will take " + str(years) + " years and " + str(month) + " months to repay this loan!")
if function == "a":
    LoanPrincipal = int(input("Enter the loan principal:"))
    Number_Of_Periods = int(input("Enter the number of periods:"))
    LoanInterest = int(input("Enter the loan interest:"))
    MonthlyPercentage = LoanInterest/(100*12)
    monthly_payment = math.ceil(LoanPrincipal * (MonthlyPercentage * (1+MonthlyPercentage)**Number_Of_Periods) / ((1+MonthlyPercentage)**Number_Of_Periods - 1))
    print(monthly_payment)
if function == "p":
    AnnuityPayment = float(input("Enter the annuity payment:"))
    Number_Of_Periods = int(input("Enter the number of periods:"))
    LoanInterest = float(input("Enter the loan interest:"))
    MonthlyPercentage = LoanInterest/(100*12)
    LoanPrincipal = round(AnnuityPayment*(((1+MonthlyPercentage)**Number_Of_Periods - 1)/(MonthlyPercentage * (1+MonthlyPercentage)**Number_Of_Periods)))
    print("Your loan principal= " + LoanPrincipal)