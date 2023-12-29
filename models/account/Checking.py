from models.account.Account import Account


class Checking(Account):
    def __init__(self, account_number, customer_name, balance=0):
        super().__init__(account_number, customer_name, balance)

        def update_checking_account():
            pass

        def overdraft():
            pass
