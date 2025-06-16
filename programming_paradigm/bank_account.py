import sys


class BankAccount:
    def __init__(self, account_balance=0.00):
        self.account_balance = float(account_balance)
    
    def deposit(self,amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")



def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

#file path     "C:\Users\ItsAl\Desktop\ALX\programming_paradigm\bank_account.py"
