"""
@classmethod:

@property:

@<property_name>.setter:

@functools.cache or @functools.lru_cache (Python 3.9+ and 3.2+ respectively):
"""

import json
import functools
from pathlib import Path

path_to_file = r"C:\Users\bsk14\OneDrive\Documents" \
               r"\SWAT\PYTHON\Banking System\banking_system\data\fake_users.json"


class JsonDataManager:
    def __init__(self):
        self.path = Path(path_to_file)

    def read_json_file(self):
        try:
            # Attempt to open the file located at self.path in read mode ('r')
            with self.path.open("r") as file:
                # Load the JSON data from the file
                data = json.load(file)

                # Check if the data is a dictionary and has the 'users' key
                if not isinstance(data, dict) or 'users' not in data:
                    # If validation fails, raise a ValueError
                    raise ValueError("Invalid JSON file")

                # If everything is ok, return the data
                return data

        except (FileNotFoundError, json.JSONDecodeError) as e:
            # If the file is not found or the JSON data is invalid, print an error message
            print(f"An error occurred while reading the file: {e}")
            # Return None to indicate that the data reading was unsuccessful
            return None

    def find_user_by_attribute(self, attribute, value):
        data = self.read_json_file()
        if data is None:
            return None

        users = data.get('users', [])
        # 'next' is used to get the first match; if no match is found, it returns None
        return next((user for user in users if user.get(attribute) == value), None)

    def is_user_id_present(self, id):
        # Return True if the user id is present in the database
        return self.find_user_by_attribute('id', id) is not None

    def find_user_by_fullname(self, filename, fullname):
        return self.find_user_by_attribute('fullname', fullname)

    def find_user_by_id(self, id):
        return self.find_user_by_attribute('id', id)

    def get_user_account_type(self, account_type):
        return self.find_user_by_attribute('account_type', account_type)

    def get_user_balance(self, balance):
        return self.find_user_by_attribute('balance', balance)

    def get_user_password(self, password):
        return self.find_user_by_attribute('password', password)

    def write_json_file(self, data):
        try:
            # Attempt to open the file located at self.PATH in write mode ('w')
            with self.path.open('w') as file:
                # Write the data to the file
                json.dump(data, file, indent=4)
                return True

        except IOError as e:
            # If the file is not found, print an error message
            print(f"An error occurred while writing to the file: {e}")
            # Return False to indicate that the data writing was unsuccessful
            return False


 # def add_user_to_jason(self, fullname, password, account_type):
    #     new_user = {
    #         "fullname": fullname,
    #         "password": password,
    #         "account_type": account_type,
    #     }
    #
    #     try:
    #         with open("fake_users.json", "r") as file:
    #             data = json.load(file)
    #     except FileNotFoundError:  # If the file is not found
    #         data = {"users": []}
    #
    #     # Checking if the user already exist
    #     for customer in data["users"]:
    #         if customer["fullname"] == fullname:
    #             return "Customer already exist"
    #
    #     # Add the new customer
    #     data["users"].append(new_user)
    #
    #     # Write the data back to the file
    #     with open("fake_users.json", "w") as file:
    #         json.dump(data, file, indent=4)

# json_data_manager = JsonDataManager(path_to_file)
