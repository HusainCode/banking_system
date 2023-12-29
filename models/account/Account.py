from abc import ABC, abstractmethod
from typing import Optional, Union

from models.account.Checking import Checking
from models.account.Savings import Savings


class Account(ABC):
    def __init__(self, account_number: int, customer_name: str, balance: float = 0) -> None:
        self._balance = balance
        self._account_number = account_number
        self._customer_name = customer_name

    @staticmethod
    def create_account() -> Union['Checking', 'Savings', None]:
        """
            Static method to create and return a new Checking or Savings account
            based on user input, or return None if the account creation is canceled
            or fails due to invalid input.
            """
        while True:
            try:
                # Prompt the user to choose an account type
                account_type = input("Choose account type (checking/savings): ").lower()

                # Validate the chosen account type
                if account_type not in ["checking", "savings"]:
                    raise ValueError("Invalid account type. Please choose 'checking' or 'savings'.")

                # Get account number from the user
                account_number = input("Enter account number: ")

                # Create and return the appropriate account object
                if account_type == "checking":
                    return Checking(account_number)
                else:  # savings
                    return Savings(account_number)

            except ValueError as e:
                # Catch and print any ValueError
                print(f"Error: {e}")
                retry = input("Do you want to try again? (yes/no): ").lower()
                # Ask the user if they wish to retry after the error
                if retry != "yes":
                    # If the user doesn't want to retry, cancel account creation and exit
                    print("Account creation cancelled.")
                    return None

    @staticmethod
    def set_customer_name(account, customer_name):
        # Set the customer's name for the given account, if the account exists
        if account:
            account.set_customer_name(customer_name)

    @staticmethod
    def set_initial_balance(account, initial_balance):
        # Try to set the initial balance for the given account
        try:
            if account:
                balance = float(initial_balance)  # Convert balance input to float
                account.set_balance(balance)  # Set the balance if account exists
        except ValueError:
            # Handle the case where the balance input is not a valid number
            print("Invalid balance. Please enter a numeric value.")

    def deposit(self, amount: float) -> None:
        # Check if the deposit amount is valid (greater than 0)
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        # Add the amount to the account's balance
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        # Check if the withdrawal amount is valid (greater than 0)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        # Check if the account has enough balance for the withdrawal
        if self._balance < amount:
            raise ValueError("Insufficient balance.")

        # Subtract the amount from the account's balance
        self._balance -= amount

    def get_balance(self) -> float:
        # Return the current balance of the account
        return self._balance
