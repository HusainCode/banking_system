class Account:
    """
        Initialize a new account with the provided details.
    """
    def __init__(self, amount, account_number,
                 customer_name, account_type, balance=0):
        self.balance = balance # Current balance in the account.Defaults to 0.
        self.amount = amount # Initial transaction amount
        self.account_number = account_number # Unique account number
        self.customer_name = customer_name # Name of the account holder
        self.account_type = account_type  # Savings or Checking

    # Implementation of deposit
    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount: The amount to be deposited. Must be greater than 0.

        Raises:
            ValueError: If the deposit amount is not greater than 0.
        """
        # Check if the deposit amount is less than 0
        if amount < 0:
            # If the deposit amount is 0 or less, give an error message
            raise ValueError("Deposit amount must be greater than 0.")

        # If deposit amount is valid , add to balance
        self.balance += amount

    # Implementation of withdraw
    def withdraw(self, amount):
         """
         Withdraws a specified amount from the balance.

         Args:
             amount: The amount to be withdrawn. Must be greater than 0.

        Raises:
            ValueError: If the withdrawal amount is not greater than 0 or if there's insufficient balance.
        """
         # Check if the withdrawal amount is less than or equal to 0
         if self.amount == 0:
             raise ValueError("You can't withdraw just $0.")

         ## Check if the withdrawal amount is greater than the account balance
         if self.balance < amount:
             raise ValueError("Insufficient balance.")

         # Withdraw the specified amount from the account's balance
        self.balance -= amount

    # Implementation of balance inquiry
    def check_balance(self):
        """
        Returns the current balance of the account.

        """
        # Return the current balance
        return self.balance

    # Functions related to Customer
    def add_account(self, account):
        pass

    def remove_account(self, account):
        pass


