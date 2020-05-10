# Write your code here
NOT_ENOUGH_WATER = "Sorry, not enough water!"
NOT_ENOUGH_COFFEE_BEANS = "Sorry, not enough coffee beans"
ENOUGH_RESOURCES = "I have enough resources, making you a coffee!"

action = input('Write action (buy, fill, take, remaining, exit):')


class CoffeeMachine:
    state = "choosing_action"

    def __init__(self):
        self.amount = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9

    def can_make_espresso(self):
        if self.water < 250:
            print(NOT_ENOUGH_WATER)
        elif self.coffee_beans < 16:
            print(NOT_ENOUGH_COFFEE_BEANS)
        return self.water >= 250 and self.coffee_beans >= 16

    def can_make_latte(self):
        if self.water < 350:
            print(NOT_ENOUGH_WATER)
        elif self.coffee_beans < 20:
            print(NOT_ENOUGH_COFFEE_BEANS)
        elif self.milk < 75:
            print("Sorry, not enough milk")
        return self.water >= 350 and self.coffee_beans >= 20 and self.milk >= 75

    def can_make_cappucino(self):
        if self.water < 200:
            print(NOT_ENOUGH_WATER)
        elif self.coffee_beans < 12:
            print(NOT_ENOUGH_COFFEE_BEANS)
        elif self.milk < 100:
            print("Sorry, not enough milk")
        return self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12

    def buy_coffee(self, item):
        if self.cups == 0:
            print("Sorry, not enough cups!")
        if item == 1 and self.can_make_espresso():
            print(ENOUGH_RESOURCES)
            self.water -= 250
            self.coffee_beans -= 16
            self.amount += 4
            self.cups -= 1
        elif item == 2 and self.can_make_latte():
            print(ENOUGH_RESOURCES)
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.amount += 7
            self.cups -= 1
        elif item == 3 and self.can_make_cappucino():
            print(ENOUGH_RESOURCES)
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.amount += 6
            self.cups -= 1

    def fill_coffee(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee
        self.cups += cups
        self.state = "choosing_action"

    def take_money(self):
        print(f"I gave you {self.amount}")
        self.amount = 0

    def print_details(self):
        print(f"""
        The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.cups} of disposable cups
        {self.amount} of money
        """)

    def take_action(self, action):
        if self.state == "choosing_action":
            if action == "buy":
                self.state = "type_of_coffee"
            elif action == "exit":
                self.state = "choosing_action"
            elif action == "fill":
                self.state = "filling_machine"
            elif action == "remaining":
                self.print_details()
            elif action == "take":
                self.take_money()
        elif self.state == "type_of_coffee":
            self.state = "choosing_action"
            if action != "back":
                coffee_type = int(action)
                self.buy_coffee(coffee_type)

    def get_state(self):
        return self.state


coffee_machine = CoffeeMachine()
while action != 'exit':
    coffee_machine.take_action(action)
    if coffee_machine.get_state() == "type_of_coffee":
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_machine.take_action(coffee)
    elif coffee_machine.get_state() == "filling_machine":
        add_water = int(input('Write how many ml of water do you want to add:'))
        add_milk = int(input('Write how many ml of milk do you want to add:'))
        add_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
        add_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        coffee_machine.fill_coffee(add_water, add_milk, add_coffee, add_cups)
    action = input('Write action (buy, fill, take, remaining, exit):')
