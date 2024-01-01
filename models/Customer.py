import random


class Customer:
    """
        Initialize a new Customer with the given details.
    """
    used_id = set()
    id_range_start = 100000
    id_range_end = 999999

    def __init__(self, full_name: str, customer_id: int = 0):
        self.full_name = full_name  # Assigning the name of the customer
        self.customer_id = customer_id

    @classmethod
    def generate_unique_id(cls):
        while True:
            new_id = random.randint(cls.id_range_start, cls.id_range_end)
            if new_id not in cls.used_ids:
                cls.used_ids.add(new_id)
                return new_id

    def set_customer_name(self, full_name):
        self.full_name = full_name

        def get_customer_name(self):
            return self.name
