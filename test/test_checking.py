import unittest

from banking_system.controller.operation_page import Operation

'''
USE CircleCI to run tests
'''


class TestChecking(unittest.TestCase):

    def setUp(self):
        self.Operation = Operation()

    def test_deposit(self):
        # Deposit an amount to a test user's account
        self.Operation.deposit('Test User', 100)

        # Find the test user
        user, _ = self.Operation.find_user('Test User')

        # Assert that the user's deposit amount has been updated correctly
        self.assertEqual(user['deposit'], 100)

    def test_withdraw(self):
        # Withdraw an amount from a test user's account
        self.Operation.withdraw('Test User', 50)

        # Find the test user
        user, _ = self.Operation.find_user('Test User')

        # Assert that the user's deposit amount has been updated correctly
        self.assertEqual(user['deposit'], 50)

    #  CONTINUE FROM HERE
    # COME BACK TO THIS LATER
    def test_withdraw_insufficient_funds(self):
        # Set up initial user data and balance
        user_id = 'test_user'
        initial_balance = 100.00
        overdraft_fee = 25.00  # Example fee amount
        withdraw_amount = 150.00  # More than the initial balance

        # Add test user to the system
        self.add_user(user_id, {'balance': initial_balance})

        # Perform withdrawal operation
        self.withdraw(user_id, withdraw_amount)

        # Retrieve updated user data after withdrawal
        updated_user = self.find_user_by_id(user_id)
        updated_balance = updated_user['balance']

        # Calculate expected balance after withdrawal and overdraft fee
        expected_balance = initial_balance - withdraw_amount - overdraft_fee

        # Check if the updated balance matches the expected balance after withdrawal and overdraft fee
        assert updated_balance == expected_balance, f"Test failed: Expected balance to be {expected_balance}, but got {updated_balance}"

        # Clean up test user from the system (if necessary)
        self.remove_user(user_id)

# class TestCustomer(unittest.TestCase):
#     def test_generate_unique_id(self):
#         customer = Customer()
#         try:
#             id = customer.generate_unique_id()
#             self.assertTrue(10000 <= id <= 99999)  # Check if id is a 5-digit number
#         except Exception as e:
#             self.fail(f"Test failed due to exception: {str(e)}")
