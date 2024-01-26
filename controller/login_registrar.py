import tkinter as tk

from banking_system.controller.gui import GUI

"""
REFACTOR BEFORE FINALIZING 
"""


class LoginRegistrar(GUI):
    def __init__(self):
        super().__init__()
        self.setup_window()  # Call the setup_window method from GUI
        self.main_window.title("Login/Register")

    def create_login_button(self):
        login_button_frame = tk.Frame(self.main_window)
        login_button_frame.pack(padx=5, pady=2)

        # ADD COMMAND LATER
        login_button = tk.Button(login_button_frame,
                                 text="Login",
                                 width=20)

        # Pack the login button at the bottom
        login_button.pack(side='bottom', padx=5, pady=5)

    def create_register_button(self):
        register_button_frame = tk.Frame(self.main_window)
        register_button_frame.pack(padx=5, pady=2)

        # ADD COMMAND LATER
        register_button = tk.Button(register_button_frame,
                                    text="Register",
                                    width=20)

        # Pack the register button at the bottom
        register_button.pack(side='bottom', padx=5, pady=5)

    def create_entries(self):
        pass

    def create_labels(self):
        pass


LR = LoginRegistrar()
LR.create_login_button()
LR.create_register_button()
LR.run()
