from banking_system.models.account.Account import Account


class Checking(Account):

    OVERDRAFT_FEE = 35 # Defining the overdraft fee as a class constant
    def __init__(self, balance: float = 0, amount: float = 0):
        super().__init__("checking", balance, amount)

        def withdraw(self, amount: float) -> None:
            # check if the user has sufficient funds
            if amount <=0:
                return "insufficient funds"

            # handling any potential overdraft
            if  amount > self.balance:
                overdrafted_balnce = self.calculate_overdrafted_balance()
                print("You have over drafted your account, your new balance is:", overdrafted_balnce)
            else:
                self.balance -= amount
                return f"Withdrwal successful. Your new balance is: {self.balance}"


        def deposit(self, amount: float) -> None:
            pass

        def get_balance(self) -> float:
            return self.balance


          def calculate_overdrafted_balance(self) -> float:
            return self.balance - self.OVERDRAFT_FEE # the 35 is the overdraft fee
