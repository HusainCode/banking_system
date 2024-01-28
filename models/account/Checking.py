from banking_system.controller import json_data_manager
from banking_system.models.account.Account import Account
import json


class Checking(Account):
    OVERDRAFT_FEE = 35  # Defining the overdraft fee as a class constant

    def __init__(self, balance: float = 0, amount: float = 0):
        super().__init__("checking", balance, amount)
        self.data_manager = json_data_manager.JsonDataManager()

        def withdraw(self, amount: float) -> None:
            pass

        def deposit(self) -> None:
            self.data_manager.add.deposit(self.amount)

        def get_balance(self) -> float:
            return self.data.manger.get_user_balance(self.balance)

        def calculate_overdrafted_balance(self) -> float:
            return self.balance - self.OVERDRAFT_FEE  # the 35 is the overdraft fee
