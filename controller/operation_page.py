from banking_system.controller.gui import GUI


class Operation(GUI):
    def __init__(self):
        super().__init__()
        self.setup_window()

        self.main_window.title("Operation")

    def withdrawal(self):
        pass

    def deposit(self):
        pass

    def display_customer_name(self):
        pass

    def display_customer_number(self):
        pass

    def display_current_balance(self):
        pass


oper = Operation()
oper.run()
