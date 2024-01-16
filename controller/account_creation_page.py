"""
TODO
1- REFACTOR BEFORE FINALIZING
"""

import tkinter as tk
from abc import ABC, abstractmethod
import json

from banking_system.controller.gui import GUI


class AccountCreation(GUI):
    def __init__(self, window_width=500, window_height=150):
        super().__init__(window_width, window_height)

        self.setup_window()

        self.create_frames()
        self.create_labels()
        self.create_entries()
        self.create_checkbox()
        self.create_submit_button()

    def setup_window(self):
        super().create_window()  # Call the GUI's create_window
        super().window_size()
        super().window_position()

        self.main_window.title("Account Creation")  # Customize the title

    def create_frames(self):
        self.frame_fullname = tk.Frame(self.main_window)
        self.frame_fullname.pack(padx=5, pady=2)

        self.frame_password = tk.Frame(self.main_window)
        self.frame_password.pack(padx=5, pady=2)

    def create_labels(self):
        # Label for Full Name
        label_fullname = tk.Label(self.frame_fullname, text="Full Name")
        label_fullname.grid(row=0, column=0, padx=5, pady=2, sticky='w')  # Reduced pady here as well

        # Label for Password
        label_password = tk.Label(self.frame_password, text="Password")
        label_password.grid(row=0, column=0, padx=5, pady=2, sticky='w')  # Reduced pady here as well

    def create_entries(self):
        # Entry for Full Name
        self.entry_fullname = tk.Entry(self.frame_fullname)
        self.entry_fullname.grid(row=0, column=1, padx=5, pady=2, sticky='e', ipadx=20)

        # Entry for Password
        self.entry_password = tk.Entry(self.frame_password, show="*")
        self.entry_password.grid(row=0, column=1, padx=5, pady=2, sticky='e', ipadx=20)

    def create_checkbox(self):
        # Frame to contain the checkboxes
        frame_checkboxes = tk.Frame(self.main_window)
        frame_checkboxes.pack(padx=5, pady=5)

        # Initialize integer variables to track the state of each checkbox.
        self.var_savings = tk.IntVar()
        self.var_checking = tk.IntVar()

        # Checkbutton for Savings account
        cb_savings = tk.Checkbutton(frame_checkboxes,
                                    text="Savings",
                                    variable=self.var_savings,
                                    command=lambda: self.var_checking.set(0))
        cb_savings.pack(side=tk.LEFT, padx=5, pady=5)

        # Checkbutton for Checking account
        cb_checking = tk.Checkbutton(frame_checkboxes,
                                     text="Checking",
                                     variable=self.var_checking,
                                     command=lambda: self.var_savings.set(0))
        cb_checking.pack(side=tk.RIGHT, padx=5, pady=5)

        # Store the checking or savings value
        account_type = self.var_checking.get()
        account_type = self.var_savings.get()

    def create_submit_button(self):
        '''
        TODO this button should submit the data to the json file
        '''
        # Button to create account
        btn_create = tk.Button(self.main_window,
                               text="Submit",
                               width=20)
        btn_create.pack()

        def handle_submission(self):

            # Check if the 'Savings' checkbox is selected
            if self.var_savings.get == 1:
                account_type = "Savings"

            # Check if the 'Checking' checkbox is selected
            elif self.var_checking.get() == 1:
                account_type = "Checking"

            else:
                raise ValueError("You must select an account type!")

                # Validate full name and password
            if not self.entry_fullname.get().strip():
                raise ValueError("You must enter a fullname")

            if not self.entry_password.get().strip():
                raise ValueError("You must enter a password")


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


app1 = AccountCreation()
app1.run()
