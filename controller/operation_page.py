from banking_system.controller.gui import GUI
from banking_system.models.Customer import Customer


class Operation(GUI):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.display_customer_name()

        self.main_window.title("Operation")

    def withdrawal(self):
        pass

    def deposit(self):
        pass

    # def get_customer_name_numer(self):

    def display_customer_name(self):
        print(Customer.get_customer_name())

    def display_customer_number(self):
        pass

    def display_current_balance(self):
        pass


app = Operation()
app.main_window.mainloop()

