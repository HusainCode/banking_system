from banking_system.data.json_data_manager import JsonDataManager


# TO BE CHANGED

class SavingsDataManager(JsonDataManager):
    def __init__(self):
        super().__init__()

    def savings_add_deposit(self, user_id, deposit_amount):
        if self.find_user_by_id(user_id) is False:
            # Read the JSON file
            data = self.read_json_file()

            for user in data['users']:
                if user['id'] == user_id:
                    user['balance'] += deposit_amount

        return self.write_json_file(data)

    # TO BE CHANGED

    def savings_process_withdrawal(self, user_id, withdrawal_amount):
        if self.find_user_by_id(user_id) is False:
            # Read the JSON file
            data = self.read_json_file()

            for user in data['users']:
                if user['id'] == user_id:
                    user['balance'] -= withdrawal_amount

        return self.write_json_file(data)
