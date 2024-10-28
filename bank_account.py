import random

class BankAccount: #This function defines bank account and gives it 3 attributes, fullname, account number and balance.
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = self.generate_account_number()
        self.balance = 0.0

    def generate_account_number(self): #This is used to generate a random account number by importanting from random.
        return random.randint(10000000, 99999999)

    def deposit(self, amount): #Here we define the deposite function and how it is updated
        self.balance += amount
        print(f"Deposit Amount: ${amount:.2f} Balance: ${self.balance:.2f}") #The .2f portion of the code specifies to only show the last 2 digits and rounds up. example 43.71927 turns into 43.72

    def withdraw(self, amount): #Function for withdrawing and if you take too much money out get charged a fee for overdrafting.
        if amount > self.balance: #Says that if the amount you are trying to withdraw is more than you have it will print "Insufficient funds and charge you a $10 fee"
            print("Insufficient funds.")
            self.balance -= 10
            print(f"Overdraft fee is charged. Your new balance is: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:2f} New balance: ${self.balance:.2f}") # If the amount you want to withdraw is less than or equal to your balance it lets you withdrawn and prints out a message.  

    def get_balance(self): #This function retrieves your current calance and prints it out.
        print(f"Your balance is: ${self.balance:.2f}")
        return self.balance
    
    def add_interest(self): #Function to add interest, given is 0.083% a month so we multiple balance by 0.00083.
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest: ${interest:.2f} Balance: ${self.balance:.2f}")
    
    def print_statement(self): #This prints the accounts name and hidden version of the account number that only shows the last four numbers.
        print(f"{self.full_name}\nAccount No.: ****{self.account_number % 10000:04d}\nBalance: ${self.balance:.2f}")

if __name__ == "__main__":
    mitchell_account = BankAccount("Mitchell", account_number="03141592")

    mitchell_account.deposit(400000)

    mitchell_account.print_statement()

    mitchell_account.add_interest()

    mitchell_account.print_statement()

    mitchell_account.withdraw(150)

    mitchell_account.print_statement()


    