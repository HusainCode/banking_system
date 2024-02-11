from banking_system.controller.gui import GUI
import tkinter as tk

from banking_system.data_manager.user_manager import UserManager


class Operation(GUI):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.data_manager = UserManager()
        self.main_window.title("Operation")


#   I STOPPED HERE
    def labels_source(self):
        # Customer Name at the top
        self.customer_name_label = tk.Label(self.main_window, text="Customer Name")
        self.customer_name_label.grid(row=0, column=0, padx=5, pady=(5, 5), sticky="w")

        # Customer ID right below Customer Name
        self.customer_id_label = tk.Label(self.main_window, text="Customer ID")
        self.customer_id_label.grid(row=1, column=0, padx=5, pady=(5, 5), sticky="w")

        # Current Balance at the bottom of the GUI
        self.current_balance_label = tk.Label(self.main_window, text="Current Balance")
        self.current_balance_label.grid(row=2, column=0, padx=5, pady=(5, 5), sticky="w")

        self.current_balance_value = tk.Label(self.main_window, text="$0.00")
        self.current_balance_value.grid(row=2, column=1, padx=5, pady=(5, 5), sticky="ew")

    def create_entries(self):
        self.deposit_entry = tk.Entry(self.main_window)
        self.deposit_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.withdrawal_entry = tk.Entry(self.main_window)
        self.withdrawal_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    def create_deposit_button(self):
        deposit_button = tk.Button(self.main_window, text="Deposit", width=8)
        deposit_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_withdrawal_button(self):
        withdrawal_button = tk.Button(self.main_window, text="withdrawal", width=8)
        withdrawal_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")


app = Operation()
app.labels_source()
app.create_entries()
app.create_deposit_button()
app.create_withdrawal_button()

app.main_window.mainloop()
