class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
# Add the specified amount
        def deposit(self, amount):
             if amount > 0:
                  self.__account_balance += amount
                  print(f"Deposited: {amount}.")
                  print(f"Current: ${self.__account_balance:.2F}")
             else:
                  print("Invalid deposit amount")
                  def withdraw(self, amount):
                    if amount > 0:
                         self.account_balance -= amount
                         print(f"withdrew {amount}.")
                         return True
                    else:
                        print("Insufficient funds.")
                        return False

                    def display_balance(self):
                        print(f"Current Balance: ${self.account_balance}")



                    







                                

                                     




