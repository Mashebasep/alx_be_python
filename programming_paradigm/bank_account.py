class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
# Add the specified amount
        def deposit(self, amount):
             if amount > 0:
                  self.__account_balance += amount
                  print(f"Deposited: $ {amount:.2F}")
             else:
                  print("Deposit amount must be positive.")

                  def withdraw(self, amount):
                    if amount > self.account_balance:
                         print("Insufficient funds.")
                         return False
                    elif amount <= 0:
                        print("Withdrawal amount must be positive.")
                        return False
                    else:
                        self.account_balance -= amount
                        print(f"Withdrew: $ {amount:.2F}")
                        return True

                    def display_balance(self):
                        print(f"Current Balance: ${self.account_balance}")



                    







                                

                                     




