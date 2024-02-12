#############################################################################

                     # ABANDONED CLASS

#############################################################################


import random


class Customer:
    """
        Initialize a new Customer with the given details.
    """

    ID_RANGE_START = 1000000  # Start of 7-digit numbers
    ID_RANGE_END = 9999999  # End of 7-digit numbers

    def __init__(self, customer_fullname: str = None, customer_id: int = None):
        self.customer_fullname = customer_fullname
        self.customer_id = customer_id
        self.new_id = self.generate_unique_id()

    # Come back to this later,see if you can make it more efficient
    def generate_unique_id(self):
        max_attempt = 10  # To avoid infinite loop

        for _ in range(max_attempt):
            customer_id = random.randint(self.ID_RANGE_START, self.ID_RANGE_END)

            if not self.data_manager.is_user_id_present(customer_id):
                return customer_id
            else:
                return False

        raise ValueError("Unable to generate a unique ID")

    def get_customer_unique_id(self):
        return self.customer_id

    def set_customer_name(self):
        self.customer_fullname = input("Enter your full name: ")

    def get_customer_name(self):
        return self.customer_fullname



cus = Customer()






#