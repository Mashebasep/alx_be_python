import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py<operatin> [amount]")
        return
    operation = sys.argv[1].lower()
    if operation == "deposit" and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        account.deposit(amount)
    elif operation == "withdraw" and len(sys.argv) == 3:
        amount = float(sys.argv[2])
    account.withdraw(amount)
    def display_balance(self):
        if operation == "display":
            account.display_balance()
        else:
            print("Invalid operation or missing amount.")







  




 









