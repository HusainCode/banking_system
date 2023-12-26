class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_customer_name(self):
        return self.name

    def get_customer_address(self):
        return self.address
