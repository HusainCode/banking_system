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
        pass

    def test_withdraw_insufficient_funds(self):
        pass

# class TestCustomer(unittest.TestCase):
#     def test_generate_unique_id(self):
#         customer = Customer()
#         try:
#             id = customer.generate_unique_id()
#             self.assertTrue(10000 <= id <= 99999)  # Check if id is a 5-digit number
#         except Exception as e:
#             self.fail(f"Test failed due to exception: {str(e)}")
