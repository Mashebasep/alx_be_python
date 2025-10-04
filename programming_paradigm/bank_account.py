class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

        def deposit(self, amount):
            if amount > 0:
                 self.__account_balance += amount
                 print(f"Deposited ${amount:.2F}. New balance is ${self.__accout_balance:.2F}")
            else:
                 print("Invalid deposit amount.")


            def withdraw(self, amount):
                    if 0 < amount <=self.__account_balance:
                        self.__account_balance -= amount
                        print(f"Withdrew ${amount:.2F}. New balance is ${self.__account_balance:.2F}") 
                        return True
                    elif amount <= 0:
                        print("Invalid withdrawal amount.")
                        return False
                    else:
                        print("Insufficient funds.")
                        return False
            def display_balance(self):
                 print(f"Balance: ${self.__account_balance:.2F}")
                 def main():
                      account = BankAccount(1000)
                      while True:
                           print("/nBanking Menu:")
                           print("1. Deposit")
                           print("2. Withdraw")
                           print("3. Display Balance")
                           print("4. Exit")
                           choice = input("Enter your choice:")
                           if choice == '1':
                                amount = float(input("Enter amount to deposit: "))
                                account.deposit(amount)
                           elif choice == '2':
                                amount = float(input("Enter amount to withdraw: "))
                                account.withdraw(amount)
                           elif choice == '3':
                                account.display_balance()
                           elif choice == '4':
                                print("Exiting program.")
                                break
                           else:
                                print("Invalid choice. Please try again.")

                                

                                     




