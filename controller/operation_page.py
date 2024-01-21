import json
from abc import ABC

from banking_system.controller.gui import GUI
from banking_system.models.Customer import Customer
import tkinter as tk


class Operation(GUI, ABC):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.display_customer_name()

        self.main_window.title("Operation")

    def withdrawal(self):
        pass

    def deposit(self, fullname, amount):
        # Find the user
        user, data = self.find_user(fullname)

        if user:
            # Update the user's deposit amount
            user['deposit'] += amount

            # Write the updated data back to the JSON file
            with open('banking_system/data/fake_users.json', 'w') as file:
                json.dump(data, file, indent=4)

    # def get_customer_name_numer(self):

    def display_customer_name(self):
        print(Customer.get_customer_name())

    def display_customer_number(self):
        pass

    def display_current_balance(self):
        pass

    def create_labels(self):
        # Call the read_json_file method and pass the path to the JSON file
        data = self.read_json_file('banking_system/data/fake_users.json')

        # Extract the fullname of the first user
        fullname = data['users'][0]['fullname']

        # Create a label and set its text to the fullname
        label_fullname = tk.Label(self.main_window, text=fullname)

        # Pack the label to display it on the GUI
        label_fullname.pack()

    def create_entries(self):
        pass



app = Operation()
app.main_window.mainloop()
