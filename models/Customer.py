class Customer:
    """
        Initialize a new Customer with the given details.
    """
    def __init__(self, d, age, gender, address):
        self.name = name # Assigning the name of the customer
        self.address = address # Assigning the address of the customer
        self.age = age # Assigning the age of the customer
        self.gender = gender # Assigning the gender of the customer
        self.accounts = [] # List to store accounts associated with the customer

    def get_customer_name(self):
        return self.name

    def get_customer_address(self):
        return self.address

