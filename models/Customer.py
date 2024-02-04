import random
import tkinter as tk
from banking_system.data.json_data_manager \
    import JsonDataManager


class Customer:
    """
        Initialize a new Customer with the given details.
    """

    ID_RANGE_START = 1000000  # Start of 7-digit numbers
    ID_RANGE_END = 9999999  # End of 7-digit numbers

    def __init__(self):
        self.data_manager = JsonDataManager()
        self.new_id = self.generate_unique_id()

    # Come back to this later,see if you can make it more efficient
    def generate_unique_id(self):
        max_attempt = 10  # To avoid infinite loop

        for _ in range(max_attempt):
            new_id = random.randint(self.ID_RANGE_START, self.ID_RANGE_END)

            if not self.data_manager.is_user_id_present(new_id):
                return new_id
            else:
                return False

        raise ValueError("Unable to generate a unique ID")

    def create_frames(self):
        self.frame_fullname = tk.Frame(self.main_window)
        self.frame_fullname.pack(padx=5, pady=2)

        self.frame_password = tk.Frame(self.main_window)
        self.frame_password.pack(padx=5, pady=2)

    def create_labels(self):
        # Label for Full Name
        label_fullname = tk.Label(self.frame_fullname, text="Full Name")
        label_fullname.grid(row=0, column=0, padx=5, pady=2, sticky='w')

        # Label for Password
        label_password = tk.Label(self.frame_password, text="Password")
        label_password.grid(row=0, column=0, padx=5, pady=2, sticky='w')

    def create_entries(self):
        # Entry for Full Name
        self.entry_fullname = tk.Entry(self.frame_fullname)
        self.entry_fullname.grid(row=0, column=1, padx=5, pady=2, sticky='e', ipadx=20)

        # Entry for Password
        self.entry_password = tk.Entry(self.frame_password, show="*")
        self.entry_password.grid(row=0, column=1, padx=5, pady=2, sticky='e', ipadx=20)

    def get_customer_unique_id(self):
        print("Number", self.new_id)

    def set_customer_name(self):
        self.customer_fullname = input("Enter your full name: ")

    def get_customer_name(self):
        pass


cus = Customer()
cus.get_customer_unique_id()
