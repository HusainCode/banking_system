import json
import random
from banking_system.controller.json_data_manager\
    import JsonDataManager, path_to_file


class Customer:
    """
        Initialize a new Customer with the given details.
    """

    ID_RANGE_START = 1000000  # Start of 7-digit numbers
    ID_RANGE_END = 9999999  # End of 7-digit numbers

    def __init__(self):
        self.data_manager = JsonDataManager(path_to_file)


    # Come back to this later,see if you can make it more efficient
    def generate_unique_id(self):

        attempt = 0
        max_attempt = 10  # To avoid infinite loop

        while attempt < max_attempt:
            new_id = random.randint(self.ID_RANGE_START, self.ID_RANGE_END)
            attempt += 1

         # CONTINUE FROM HERE

                return new_id

    def get_customer_unique_id(self):
        print("Number", self.new_id)

    def set_customer_name(self):
        self.customer_fullname = input("Enter your full name: ")

    @staticmethod
    def get_customer_name():
        PATH = r"C:\Users\bsk14\OneDrive\Documents\SWAT\PYTHON\Banking System\banking_system\data\fake_users.json"
        with open(PATH, "r") as file:
            data = json.load(file)
            return data["users"][0]["fullname"]


cus = Customer()
cus.generate_unique_id()
