class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

        def deposit(self, amount):
             self.account_balance += amount
             print("Deposited: ${amount}")
             self.display_balance()

        def withdraw(self, amount): 
                if amount <= self.account_balance:
                    self.account_balance -= amount
                    print(f"Withdrew: ${amount}")
                    self.display_balance()
                    return True
                else:
                    print("Insufficient funds.")

                # Display
                def display_balance(self):
                    print(f"Current Balance: ${self.accout_balance}")
                    print(f"Deposited amount: ${amount}")
                    print(f"Withdrew amount: ${amount}")
                    







                                

                                     




