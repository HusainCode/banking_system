class Checking(Account):
    def __init__(self, amount, account_number, customer_name, balance=0):
        super().__init__(amount, account_number, customer_name, "checking", balance)
