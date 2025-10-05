class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
# Add the specified amount
        def deposit(self, amount):
             if amount > 0:
                  self.__account_balance += amount
                  print(f"Deposited: ${amount}")
                  print(f"Current: ${self.__account_balance:.2F}")
             else:
                  print("Invalid deposit amount")
                  def withdraw(self, amount):
                    if 0 <amount <= self.__account_balance:
                         self.__account_balance -= amount
                         print(f"Withdrew: ${amount}")
                         print(f"Current balance: ${amount}")
                    else:
                         print("Invalid deposit amount.")
                         return True
                    if amount <= 0:
                        print("Invalid withdrawal amount.")
                        return False
                    else:
                        print("Insufficient funds.")
                        return False
                    def display_balance(self):
                        print(f"Current Balance: ${amount}")
                    # Create an instance to test
                    account = BankAccount(100)
                    account.display_balance()
                    account.deposit(50)
                    account.display_balance()
                    account.withdraw(20)
                    account.display_balance()


                    







                                

                                     




