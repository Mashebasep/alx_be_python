class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

        def deposit(self, amount):
             self.account_balance += amount
             print("Deposited: ${amount:.2F}")

        def withdraw(self, amount): 
                if amount <= self.account_balance:
                    self.account_balance -= amount
                    print("Withdraw:"  , amount)
                    return True
                else:
                    print("Insufficient funds.")
                    return False
                
                def display_balance(self):
                    print("Current Balance:" , self.account_balance)


                                

                                     




