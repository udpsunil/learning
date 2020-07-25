import random

IIN = "400000"
account_details = {}


def print_menu_return_choice():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    return int(input())


def generate_account_number():
    random_account = random.randint(0, 999999999)
    return "{:09}".format(random_account)


def generate_luhn_number(temp_card_number):
    card_number = list(temp_card_number)
    print(temp_card_number)
    card_number = [i*2 if index % 2 ==0 else i for index, i in enumerate(map(int, card_number))]
    card_number = [i- 9 if i > 9 else i for i in card_number]
    return str((10 - sum(card_number) % 10) % 10)


def generate_card_number():
    temp_card_number = IIN + generate_account_number()
    luhn_number = generate_luhn_number(temp_card_number)
    return temp_card_number + luhn_number


def generate_pin_number():
    return "{:04}".format(random.randint(0, 9999))


def store_account_details(card_number, pin):
    account_details[card_number] = pin


def print_account_menu_return_choice():
    print("\n1. Balance")
    print("2. Log out")
    print("0. Exit")
    return int(input())


def handle_account():
    choice = print_account_menu_return_choice()
    while choice != 0:
        if choice == 1:
            print("Balance: {}".format(0))
        elif choice == 2:
            print("\nYou have successfully logged out!")
            return
        else:
            print("\nBye!")
        choice =print_account_menu_return_choice()
    if choice == 0:
        exit()


def get_account_details(card_number, pin):
    if (
        card_number not in account_details.keys()
        or card_number in account_details.keys()
        and account_details[card_number] != pin
    ):
        print("Wrong card number or PIN!")
    else:
        print("you have successfully logged in!")
        handle_account()


choice = print_menu_return_choice()
while choice != 0:
    if choice == 1:
        print("\nYour card has been created")
        print("Your card number:")
        card_number = generate_card_number()
        print(card_number)
        print("Your card PIN:")
        pin = generate_pin_number()
        print(pin)
        store_account_details(card_number, pin)
    elif choice == 2:
        print("\nEnter your card number:")
        card_number = input()
        print("Enter your PIN:")
        pin = input()
        get_account_details(card_number, pin)
    choice = print_menu_return_choice()
