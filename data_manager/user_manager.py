import random


class UserManager:
    ID_RANGE_START = 1000000  # Start of 7-digit numbers
    ID_RANGE_END = 9999999  # End of 7-digit numbers

    def __init__(self):
        pass

    # Come back to this later,see if you can make it more efficient
    def generate_unique_id(self):
        max_attempt = 10  # To avoid infinite loop

        for _ in range(max_attempt):
            customer_id = random.randint(self.ID_RANGE_START, self.ID_RANGE_END)

            if not self.is_id_present(customer_id):
                return customer_id
            else:
                return False

        raise ValueError("Unable to generate a unique ID")

    def get_customer_new_id(self):
        return self.generate_unique_id()

    def add_new_user(self, user):
        self.users.append(user)

    def find_by_attribute(self, attribute, value):
        for user in self.users:
            if user.get(attribute) == value:
                return user
        return None

    def display_balance(self, balance):
        return self.find_by_attribute('balance', balance)

    def find_user_by_fullname(self, filename, fullname):
        return self.find_by_attribute('fullname', fullname)

    def is_id_present(self, user_id):
        return "User exists" if self.find_by_attribute('id', user_id) is not None else False

    # I stopped here, I will come back to this later

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def display_customer_name(self, user_id):
        user = self.find_user_by_id(user_id)
        return user['fullname'] if user else 'User not found'

    def deposit(self, user_id, amount):
        user = self.find_user_by_id(user_id)
        if user:
            user['balance'] += amount
            return f"Deposit successful. New balance: {user['balance']}"
        else:
            return "User not found"

    def _initialize_users(self):
        return [
            {"fullname": "Husain Alshaikhahmed", "password": "pass1", "id": "7362516", "balance": 1000},
            {"fullname": "Sanji V Smoke", "password": "pass1", "id": "2333517", "balance": 10000000},
            {"fullname": "Ronro Zoro", "password": "pass1", "id": "1362518", "balance": 11000000},
            {"fullname": "Luffy D Monkey", "password": "pass1", "id": "9362219", "balance": 3000000000},
            {"fullname": "Nami", "password": "pass1", "id": "7362520", "balance": 30000000},
            {"fullname": "Usopp", "password": "pass1", "id": "5562521", "balance": 1000},
            {"fullname": "Tony Tony Chopper", "password": "pass1", "id": "5362522", "balance": 1000},
            {"fullname": "Nico Robin", "password": "pass1", "id": "1362523", "balance": 1000},
            {"fullname": "Franky", "password": "pass1", "id": "3362524", "balance": 1000},
            {"fullname": "Brook", "password": "pass1", "id": "2362525", "balance": 1000},
            {"fullname": "Jinbei", "password": "pass1", "id": "4362526", "balance": 1000},
            {"fullname": "Portgas D Ace", "password": "pass1", "id": "7362527", "balance": 1000},
            {"fullname": "Sabo", "password": "pass1", "id": "1362528", "balance": 1000},
            {"fullname": "Boa Hancock", "password": "pass1", "id": "9362529", "balance": 1000},
            {"fullname": "Buggy", "password": "pass1", "id": "7362530", "balance": 1000},
            {"fullname": "Dracule Mihawk", "password": "pass1", "id": "3362531", "balance": 1000},
            {"fullname": "Donquixote Doflamingo", "password": "pass1", "id": "7362532", "balance": 1000},
            {"fullname": "Bartholomew Kuma", "password": "pass1", "id": "6362533", "balance": 1000}
        ]
