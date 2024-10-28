import random

class BankAccount: #This function defines bank account and gives it 3 attributes, fullname, account number and balance.
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = self.generate_account_number()
        self.balance = 0.0

    def generate_account_number(self): #This is used to generate a random account number by importanting from random.
        return random.randint(100000, 999999)