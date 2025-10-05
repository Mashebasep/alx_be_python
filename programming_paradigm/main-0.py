import sys
from bank_account import BankAccount
def get_float_input(prompt):
    while True:
        return float(input(prompt))
    print("Invalid input. Please enter a number.")

def main():
    account = BankAccount(100)
    while True:
        print("/nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice:")
        # Prompt user to input choice


        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print(f"Deposited amount: ${amount}")
        elif choice =="2":
            amount = float(input("Enter amount to withdraw: "))
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")



















  




 









