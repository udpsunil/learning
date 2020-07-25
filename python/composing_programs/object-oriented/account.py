class Account:
    """A bank account that has a non-negative balance """
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals"""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_charge)


# Multiple Inheritance
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return super().deposit(amount-self.deposit_charge)

class AsSeenOnTvAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.balance = 1