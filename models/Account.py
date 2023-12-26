class Account:
    def __init__(self, balance, amount, account_number, customer_name, account_type):
        self.balance = balance
        self.amount = amount
        self.account_number = account_number
        self.customer_name = customer_name
        self.account_type = account_type

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        return self.balance

