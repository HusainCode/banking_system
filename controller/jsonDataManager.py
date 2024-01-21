"""
@classmethod:

@property:

@<property_name>.setter:

@functools.cache or @functools.lru_cache (Python 3.9+ and 3.2+ respectively):
"""

import json

PATH = r"C:\Users\bsk14\OneDrive\Documents" \
       r"\SWAT\PYTHON\Banking System\banking_system\data\fake_users.json"


class JsonDataManager:
    def __init__(self):
        self.PATH = PATH

    def read_json_file(self):
        try:
            # Attempt to open the file located at self.PATH in read mode ('r')
            with open(self.PATH, "r") as file:
                # Load the JSON data from the file
                data = json.load(file)

                # Check if the data is a dictionary and has the 'users' key
                if not isinstance(data, dict) or 'users' not in data:
                    # If validation fails, raise a ValueError
                    raise ValueError("Invalid JSON file")
                return True

            # If everything is ok, return the data
            return data

        except (FileNotFoundError, json.JSONDecodeError) as e:
            # If the file is not found or the JSON data is invalid, print an error message
            print(f"An error occurred while reading the file: {e}")
            # Return None to indicate that the data loading was unsuccessful
            return None

    def find_user_by_fullname(self, filename, fullname):
        # Read the data from the JSON file
        data = self.read_json_file()

        # Find the user
        # 'next' is used to get the first match; if no match is found, it returns None
        user_fullname = next((user_fullname for user_fullname in data['users'] if user_fullname.get('fullname')
                              == fullname), None)

        return user_fullname

    def find_user_by_id(self, id):
        # Read the data from the JSON file
        data = self.read_json_file()

        # Find the user id
        user_id = next((user_id for user_id in data['users'] if user_id.get('id')
                        == id), None)

        return user_id

    def get_user_balance(self, balance):
        # Read the data from the JSON file
        data = self.read_json_file()

        # Find the user
        # 'next' is used to get the first match; if no match is found, it returns None
        user_balance = next((user_balance for user_balance in data['users'] if user_balance.get('balance')
                             == balance), None)

        return user_balance

    def get_user_account_type(self, account_type):
        # Read the data from the JSON file
        data = self.read_json_file()

        # Find the account type
        user_account_type = next(
            (user_account_type for user_account_type in data['users'] if user_account_type.get('account_type')
             == account_type), None)

        return user_account_type

    def get_user_password(self, password):
        # Read the data from the JSON file
        data = self.read_json_file()

        # Find the password
        user_password = next(
            (user_password for user_password in data['users'] if user_password.get('password')
             == password), None)

        return user_password

    def write_json_file(self, data):
        try:
            # Attempt to open the file located at self.PATH in write mode ('w')
            with open(self.PATH, 'w') as file:
                # Write the data to the file
                json.dump(data, file, indent=4)
                return True

        except IOError as e:
            # If the file is not found, print an error message
            print(f"An error occurred while writing to the file: {e}")
            # Return False to indicate that the data writing was unsuccessful
            return False
