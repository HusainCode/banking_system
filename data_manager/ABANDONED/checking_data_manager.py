# #############################################################################
#
#                               # ABANDONED CLASS
#
# #############################################################################
#
# from banking_system.data.ABANDONED.json_data_manager import JsonDataManager
#
#
# class CheckingDataManager(JsonDataManager):
#     def __init__(self):
#         super().__init__()
#
#     def get_checking_balance(self, balance):
#         return self.find_user_by_attribute('balance', balance)
#
#     def checking_add_deposit(self, user_id, deposit_amount):
#         if self.find_user_by_id(user_id) is False:
#             # Read the JSON file
#             data = self.read_json_file()
#
#             for user in data['users']:
#                 if user['id'] == user_id:
#                     user['balance'] += deposit_amount
#
#         return self.write_json_file(data)
#
#     def checking_process_withdrawal(self, user_id, withdrawal_amount):
#         if self.find_user_by_id(user_id) is False:
#             # Read the JSON file
#             data = self.read_json_file()
#
#             for user in data['users']:
#                 if user['id'] == user_id:
#                     user['balance'] -= withdrawal_amount
#
#         return self.write_json_file(data)
