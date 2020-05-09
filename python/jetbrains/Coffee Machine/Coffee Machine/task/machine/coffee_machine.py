# Write your code here
amount = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9


def buy_coffee():
    global amount, water, milk, coffee_beans, cups
    item = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'))
    if item == 1:
        water -= 250
        coffee_beans -= 16
        amount += 4
        cups -= 1
    elif item == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        amount += 7
        cups -= 1
    elif item == 3:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        amount += 6
        cups -= 1


def fill_coffee():
    global amount, water, milk, coffee_beans, cups
    add_water = int(input('Write how many ml of water do you want to add:'))
    water += add_water
    add_milk = int(input('Write how many ml of milk do you want to add:'))
    milk += add_milk
    add_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
    coffee_beans += add_coffee
    add_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
    cups += add_cups


def take_money():
    global amount
    print(f"I gave you {amount}")
    amount = 0


print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{amount} of money
""")

action = input('Write action (buy, fill, take):')

if action == 'buy':
    buy_coffee()
elif action == 'fill':
    fill_coffee()
elif action == 'take':
    take_money()

print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{amount} of money
""")
