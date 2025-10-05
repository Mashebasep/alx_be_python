class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
# Add the specified amount
        def deposit(self, amount):
             self.account_balance += amount
             print(f"Deposited: ${amount:.2F}")
             print(f"Current balance: ${self.account_balance}")
             self.display_balance()
# Deduct the amount
        def withdraw(self, amount): 
                if amount > self.account_balance:
                    print("Insufficient funds.")
                    return False
                
                    self.account_balance -= amount
                    print(f"Withdrew: ${amount:.2F}")
                    print(f"Current balance: ${self.account_balance}")
                    return True
                # Print the current balance
                def display_balance(self):
                    print(f"Current Balance: ${self.accout_balance:.2F}")
                    # Create an instance to test
                    account = BankAccount(100)
                    account.display_balance()
                    account.deposit(50)
                    account.display_balance()
                    account.withdraw(20)
                    account.display_balance()
                    

                    







                                

                                     




