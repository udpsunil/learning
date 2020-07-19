import math
import sys


def compute_differentiated_payments(principal, periods, interest):
    interest = interest/(12 * 100.0)
    accumulated_diff_amount = 0
    for period in range(periods):
        diff_amount = math.ceil(principal / periods + interest * (principal - (principal * period / periods)))
        accumulated_diff_amount += diff_amount
        print("Month {}: paid out {}".format(period + 1, math.ceil(diff_amount)))

    overpayment = accumulated_diff_amount - principal
    print("\nOverpayment = {}".format(overpayment))


def handle_diff(args):
    first_param, principal = args[0].split("=")
    second_param, periods = args[1].split("=")
    third_param, interest = args[2].split("=")
    if first_param == "--principal" and second_param == "--periods" and third_param == "--interest":
        compute_differentiated_payments(float(principal), int(periods), float(interest))
    else:
        print("incorrect parameters")


def compute_annuity_payments(principal, periods, interest):
    i = interest / (12 * 100.0)
    annuity_payment = math.ceil(principal * i * ((1+i)**periods / ((1+i)**periods -1)))
    overpayment = annuity_payment*periods - principal
    print("Your annuity payment = {}!".format(math.ceil(annuity_payment)))
    print("Overpayment = {}".format(math.ceil(overpayment)))


def compute_annuity_principal(payment, periods, interest):
    i = interest / (12 * 100.0)
    principal = payment / (i * (1+i)**periods /((1+i)**periods-1))
    print("Your credit principal = {}".format(math.ceil(principal)))


def compute_annuity_periods(principal, payment, interest):
    i = interest / (12 * 100.0)
    n = int(math.ceil(math.log((payment / (payment - i * principal)), (1+i))))
    years = n // 12
    months = n % 12
    message = 'You need '
    if years > 1:
        message += str(years) + ' years and '
    message += str(months) + ' months to repay this credit'
    print(message)
    overpayment = payment*n - principal
    print("Overpayment = {}".format(math.ceil(overpayment)))


def handle_annuity(args):
    first_param, first_value = args[0].split("=")
    second_param, second_value = args[1].split("=")
    third_param, third_value = args[2].split("=")
    if first_param == "--principal" and second_param == "--periods" and third_param == "--interest":
        compute_annuity_payments(float(first_value), int(second_value), float(third_value))
    elif first_param == "--payment" and second_param == "--periods" and third_param == "--interest":
        compute_annuity_principal(float(first_value), int(second_value), float(third_value))
    elif first_param == "--principal" and second_param == "--payment" and third_param == "--interest":
        compute_annuity_periods(float(first_value), float(second_value), float(third_value))
    else:
        print("4 Incorrect parameters")


def parse_arguments(args):
    first_param, first_value = args[1].split("=")
    if len(args) > 4 and first_param == "--type" and first_value == "diff":
        handle_diff(args[2:])
    elif len(args) > 4 and first_param == "--type" and first_value == "annuity":
        handle_annuity(args[2:])
    else:
        print("Incorrect parameters")


parse_arguments(sys.argv)
