import json
from abc import ABC
from banking_system.controller.json_data_manager import JsonDataManager

from banking_system.controller.gui import GUI
from banking_system.models.Customer import Customer
import tkinter as tk


class Operation(GUI, ABC):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.data_manager = JsonDataManager()
        # self.display_customer_name()

        self.main_window.title("Operation")

    def create_frames(self):
        self.frame_fullname = tk.Frame(self.main_window)
        self.frame_fullname.pack(padx=5, pady=2)

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

    def display_customer_number(self):
        pass

    def display_current_balance(self):
        pass

    def create_labels(self):
        # Call the read_json_file method and pass the path to the JSON file
        data = self.data_manager.read_json_file()

        # Extract the fullname of the first user
        fullname = data['users'][0]['fullname']
        customer_id = data['users'][0]['id']

        # Create a label and set its text to the fullname
        label_fullname = tk.Label(self.frame_fullname, text=fullname)
        label_customer_id = tk.Label(self.frame_fullname, text=customer_id)

        # Grid the label to display it on the GUI
        label_fullname.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        label_customer_id.grid(row=1, column=0, padx=(40,5), pady=2, sticky='w')

    def display_customer_name(self):
        pass

    def create_entries(self):
        pass


app = Operation()
app.create_frames()
app.create_labels()
app.main_window.mainloop()
