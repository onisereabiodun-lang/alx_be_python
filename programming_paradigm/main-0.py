import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100.00)  # ← you can change starting amount here

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands:")
        print("  deposit:<amount>")
        print("  withdraw:<amount>")
        print("  display")
        sys.exit(1)

    arg = sys.argv[1]
    parts = arg.split(':', 1)
    command = parts[0].lower().strip()

    amount = None
    if len(parts) > 1:
        try:
            amount = float(parts[1].strip())
        except ValueError:
            print("Error: Amount must be a valid number")
            sys.exit(1)

    if command == "deposit":
        if amount is None:
            print("Error: deposit needs an amount")
            sys.exit(1)
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:,.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    elif command == "withdraw":
        if amount is None:
            print("Error: withdraw needs an amount")
            sys.exit(1)
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:,.2f}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print(f"Unknown command: {command}")
        print("Valid commands: deposit:<amount>, withdraw:<amount>, display")

if __name__ == "__main__":
    main()