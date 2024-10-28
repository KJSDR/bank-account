## Bank Account Project

The goal of this project was to simulate a working bank account. We used the class "BankAccount" to make it work and assigned it multiple functions to allow the program to generate an account number, make a deposit, withdraw money, get your balance, add interest and had a print statement to give you feedback based on requests and inputs.

# Pseudo Code

***
-Class BankAccount
-- Make the account attributes
  -Set full_name
  -Set account_number
  -Set balance to 0

  -When making an account
    -CreateAccount(name, number = 0)
      -Set full_name to name
      -If number is 0 then
        -Set account number to GenerateRandomAccountNumber
      -Else
        -Set account_number to number

  -Generating random account number
    -GenerateRandomAccountNumber
      -Return random number between 10000000 and 99999999

  -Depositing money
    -Deposit(amount)
      -Add amount to balance
      -Print "You deposited $X"
      -Print "New balance $X"

  -Withdrawing money
    -Withdraw(amount)
      -If amount is great than balance then
        -Print "Not enough funds"
        -Substract 10 from balance
        -Print "Overdraft dee charged. New balance: $X"
      -Else
        -Substract amount from balance
        -Print "You withdraw $X"
        -Print "New Balance $X"

  -Get balance
    -ShowBalance
      -Print "Your balance is: $X"

  -Add interest to balance
    -AddInterest
      -Set intereset to balance * 0.00083
      -Add interest to balance
      -Print "Interest added: $X"
      -Print "New Balance: $X"

  -Print details
    -PrintStatement
      -Print "Account Holder: full_name
      -Print "Account number: **** and last 4 numbers of account_number
      -Print "Balance: $X"
***

  
