import json
import random


class Customer:
    """
        Initialize a new Customer with the given details.
    """

    used_id = set()
    ID_RANGE_START = 1000000  # Start of 7-digit numbers
    ID_RANGE_END = 9999999  # End of 7-digit numbers

    def generate_unique_id(self):
        data = self.read_json_file()

        attempt = 0
        max_attempt = 10  # To avoid infinite loop

        while attempt < max_attempt:
            new_id = random.randint(self.ID_RANGE_START, self.ID_RANGE_END)
            attempt += 1

            if new_id not in data["id"]:
                data["id"].append(new_id)

                with open("fake_users.json", "w") as file:
                    json.dump(data, file, indent=4)
                    print("New id added to the file")

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
