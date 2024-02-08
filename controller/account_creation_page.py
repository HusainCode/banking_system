"""

1- REFACTOR BEFORE FINALIZING
"""

import tkinter as tk
from tkinter import messagebox
from banking_system.controller.gui import GUI
from banking_system.models.Customer import Customer


class AccountCreation(GUI):
    def __init__(self):
        super().__init__()
        self.setup_window()  # Call the setup_window method from GUI
        self.main_window.title("Account Creation")  # Set a specific title for AccountCreation
        self.create_ui_elements()

    def create_ui_elements(self):
        self.customer.create_frames()
        self.customer.create_labels()
        self.customer.create_entries()
        self.create_submit_button()

    def on_submit(self):
        # Retrieve values from the entries
        fullname = self.entry_fullname.get()
        password = self.entry_password.get()

        customer = Customer()

        # Assuming a method to generate a unique ID for the new user
        user_id = customer.generate_unique_id()

        new_user = {
            "fullname": fullname,
            "password": password,
            "id": user_id,
            "balance": 0  # Setting balance to zero as requested
        }

        del customer  # Delete the customer object

    def create_submit_button(self):
        '''
        TODO this button should submit the data to the json file
        '''
        # Button to create account
        # COME BACK TO THIS LATER TO ADD COMMAND
        submit_button = tk.Button(self.main_window,
                                  text="Submit",
                                    command=self.on_submit,
                                  width=20)
        submit_button.pack()












  # REFACTOR THIS(DRY)

    # def create_checkbox(self):
    #     # Frame to contain the checkboxes
    #     frame_checkboxes = tk.Frame(self.main_window)
    #     frame_checkboxes.pack(padx=5, pady=5)
    #
    #     # Initialize integer variables to track the state of each checkbox.
    #     self.var_savings = tk.IntVar()
    #     self.var_checking = tk.IntVar()
    #
    #     # Checkbutton for Savings account
    #     cb_savings = tk.Checkbutton(frame_checkboxes,
    #                                 text="Savings",
    #                                 variable=self.var_savings,
    #                                 command=lambda: self.var_checking.set(0))
    #
    #     cb_savings.pack(side=tk.LEFT, padx=5, pady=5)
    #
    #     # Checkbutton for Checking account
    #     cb_checking = tk.Checkbutton(frame_checkboxes,
    #                                  text="Checking",
    #                                  variable=self.var_checking,
    #                                  command=lambda: self.var_savings.set(0))
    #
    #     cb_checking.pack(side=tk.RIGHT, padx=5, pady=5)
    #
    #     # Store the checking or savings value
    #     account_type = self.var_checking.get()
    #     account_type = self.var_savings.get()


   # def validate_checkboxes_inputs(self):
    #     # Check if the 'Savings' checkbox is selected
    #     if self.var_savings.get() == 1:
    #         account_type = "Savings"
    #     # Check if the 'Checking' checkbox is selected
    #     elif self.var_checking.get() == 1:
    #         account_type = "Checking"
    #     # If nothing is selected
    #     else:
    #         raise ValueError("You must select an account type")


