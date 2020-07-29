import math


def compute_months(payment):
    return math.ceil(credit_principal / payment)


def compute_payments(month):
    return math.ceil(credit_principal / month)


def compute_last_payment(payment, month):
    return credit_principal - (month - 1) * payment


def handle_choice(choice):
    if choice == 'm':
        payment = int(input("Enter monthly payment:"))
        months = compute_months(payment)
        print("It takes {} {} to repay the credit".format(months, lambda x: "month" if x <= 1 else months))
    elif choice == 'p':
        months = int(input("Enter count of months:"))
        payment = compute_payments(months)
        last_payment = compute_last_payment(payment, months)
        print("Your monthly payment = {} with last month payment = {}.".format(payment, last_payment))


credit_principal = int(input('Enter the credit principal:'))
print("""
What do you want to calculate?
type "m" - for count of months,
type "p" - for monthly payment:
""")
choice = input()

handle_choice(choice)

final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print(credit_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)
