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
        self.main_window.mainloop()

    def create_ui_elements(self):
        self.create_frames()
        self.create_labels_and_entries()
        self.create_submit_button()

    def create_frames(self):
        # Use an outer frame to hold all content and center it
        self.center_frame = tk.Frame(self.main_window)
        self.center_frame.pack(expand=True)

        # Frame for the fullname field
        self.frame_fullname = tk.Frame(self.center_frame)
        self.frame_fullname.pack(padx=5, pady=(0, 5), fill='x')

        # Frame for the password field
        self.frame_password = tk.Frame(self.center_frame)
        self.frame_password.pack(padx=5, pady=(0, 5), fill='x')

        # Frame for the button
        self.frame_button = tk.Frame(self.center_frame)
        self.frame_button.pack(padx=5, pady=(0, 5), fill='x')

    def create_labels_and_entries(self):
        # Combine label and entry creation to minimize redundancy
        self.entry_fullname = tk.Entry(self.frame_fullname)
        label_fullname = tk.Label(self.frame_fullname, text="Full Name", width=20)
        label_fullname.grid(row=0, column=0)
        self.entry_fullname.grid(row=0, column=1)

        self.entry_password = tk.Entry(self.frame_password, show="*")
        label_password =  tk.Label(self.form_frame, text="Password:", width=20, anchor="e").grid(row=1, column=0, padx=5, pady=5)
        label_password.grid(row=0, column=0)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5, sticky="ew")



        # Label for Password

        self.entry_password = tk.Entry(self.form_frame, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5, sticky="ew")



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

        # Pyhon have garbage collector, however, it is a good practice to delete the object
        del customer  # Delete the customer object

    def create_submit_button(self):
        '''
        TODO this button should submit the data to the json file
        '''
        # Button to create account
        # COME BACK TO THIS LATER TO ADD COMMAND
        submit_button = tk.Button(self.frame_button,
                                  text="Submit",
                                  command=self.on_submit,
                                  width=20)
        submit_button.pack()


account_creation = AccountCreation()

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
