class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

        def deposit(self, amount):
             self.account_balance += amount
             print("Deposited: ${amount:.2F}")
             print(f"Currnet balance:" , self.account_balance)

        def withdraw(self, amount): 
                if amount > self.balance:
                    print("Insufficient funds!")
                else:

                        
                    self.balance -= amount
                    print("Withdraw: ${amount:.2F}")
                    print(f"Current balance:" , self.account_balance)
                
                def display_balance(self):
                    print("Current Balance:" , self.account_balance)
                    def main():
                        account = BankAccount(250)
                        account.display_balance()

                        account.deposit(100)
                        account.withdraw(50)
                        account.display_balance()
                        




                                

                                     




