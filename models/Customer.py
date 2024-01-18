import json
import random


class Customer:
    """
        Initialize a new Customer with the given details.
    """

    used_id = set()
    id_range_start = 100000
    id_range_end = 999999

    def generate_unique_id(self):
        while True:
            new_id = random.randint(self.id_range_start, self.id_range_end)
            if new_id not in self.used_id:
                self.used_id.add(new_id)
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




