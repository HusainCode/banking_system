import tkinter as tk
from tkinter import messagebox

from banking_system.controller.account_creation_page import AccountCreation
from banking_system.controller.gui import GUI
from banking_system.models.Customer import Customer
from banking_system.data.json_data_manager import JsonDataManager

"""
REFACTOR BEFORE FINALIZING 
"""


class LoginRegistrar(GUI):
    def __init__(self):
        super().__init__()
        self.setup_window()  # Call the setup_window method from GUI
        self.data_manger = JsonDataManager()
        self.main_window.title("Login/Register")

        """
        'ew': Stretches the widget horizontally.
        'ns': Stretches the widget vertically.
        'nsew': Stretches the widget both horizontally and vertically
        'w': Aligns the widget to the left side of the cell (west).
        'e': Aligns the widget to the right side of the cell (east).
        'n': Aligns the widget to the top side of the cell (north).
        's': Aligns the widget to the bottom side of the cell (south).
        """

    ############################### CLEAN THIS FUCKERY ##################################
    def create_frames(self):
        # Frame for the fullname field, centered and adjacent to the password frame
        self.frame_fullname = tk.Frame(self.main_window)
        self.frame_fullname.grid(row=1, column=0, padx=5, pady=(0, 5), sticky='nsew')

        # Frame for the password field, directly below the fullname field, centered and adjacent to the button frames
        self.frame_password = tk.Frame(self.main_window)
        self.frame_password.grid(row=2, column=0, padx=5, pady=(0, 0), sticky='nsew')

        # Frame for the login button, positioned below the password field, centered and adjacent to the register button frame
        self.login_button_frame = tk.Frame(self.main_window)
        self.login_button_frame.grid(row=3, column=0, padx=5, pady=(0, 0), sticky='nsew')

        # Frame for the register button, positioned directly below the login button, centered
        self.register_button_frame = tk.Frame(self.main_window)
        self.register_button_frame.grid(row=4, column=0, padx=5, pady=(0, 5), sticky='nsew')

    # REFACTOR THIS(DRY)
    def create_labels(self):
        # Label for Full Name
        label_fullname = tk.Label(self.frame_fullname, text="Full Name")
        label_fullname.grid(row=0, column=0, padx=5, pady=2, sticky='w')  # Reduced pady here as well

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


    def navigate_to_operation(self):
        pass

    def create_login_button(self):
        # ADD COMMAND LATER
        self.login_button = tk.Button(self.login_button_frame,
                                      text="Login",
                                      command=self.on_login,
                                      width=30)

        # Pack the login button at the bottom
        self.login_button.pack(side='bottom', padx=5, pady=5)

    def on_login(self):
        # Retrieve values from the entries
        fullname = self.entry_fullname.get()
        password = self.entry_password.get()

        user = self.data_manger.find_user_by_fullname(fullname, password)

        if user:
            self.navigate_to_operation()
        else:
            messagebox.showerror("Login Failed", "User not found. Please register.")

    def create_register_button(self):
        # ADD COMMAND LATER
        self.register_button = tk.Button(self.register_button_frame,
                                         text="Register",
                                         command=self.navigate_to_account_creation,
                                         width=30)

        # Pack the register button at the bottom
        self.register_button.pack(side='bottom', padx=5, pady=5)

    def navigate_to_account_creation(self):
        # Destroy all widgets
        for widget in self.main_window.winfo_children():
            widget.destroy()

        # Create an instance of the AccountCreationPage
        account_creation_page = AccountCreation(self.main_window)
        account_creation_page.create_frames()








LR = LoginRegistrar()
LR.create_frames()
LR.create_labels()
LR.create_entries()
LR.create_login_button()
LR.create_register_button()
LR.run()
