import sys
from bank_account import BankAccount
def main():
    print("welcome to the Bank Account program!")
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
        command, *params = sys.argv[1].split('.')
        amount = float(params[0]) if params else None
        print("Invalid amount please enter a valid number")
        sys.exit(1)

        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
            account.display_balance()
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
                account.display_balance()
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")
    
    while True:
        print("n/Bank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")


    



















  




 









