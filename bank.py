import hashlib
import datetime

class BankAccount:
    def __init__(self, owner_name, password, account_type="checking", initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_type = account_type
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should be positive.")
        self.balance += amount
        self.transaction_history.append((datetime.datetime.now(), f"Deposited ${amount:.2f}"))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount should be positive.")
        
        if self.account_type == "savings" and self.balance - amount < 1000:
            raise ValueError("Savings account must maintain a minimum balance of $1000.")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        
        self.balance -= amount
        self.transaction_history.append((datetime.datetime.now(), f"Withdrew ${amount:.2f}"))
        return self.balance

    def get_balance(self):
        return self.balance

    def verify_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def display_transaction_history(self):
        for date, transaction in self.transaction_history:
            print(f"{date} - {transaction}")

    def __str__(self):
        return f"Account of {self.owner_name} ({self.account_type}) has a balance of ${self.balance:.2f}"


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, owner_name, password, account_type, initial_balance=0):
        account = BankAccount(owner_name, password, account_type, initial_balance)
        self.accounts.append(account)

    def get_account(self, owner_name, password):
        for account in self.accounts:
            if account.owner_name == owner_name and account.verify_password(password):
                return account
        return None


def main():
    bank = BankSystem()

    while True:
        print("\n--- Bank System ---")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            owner_name = input("Enter owner name: ")
            password = input("Enter a password: ")
            account_type = input("Enter account type (checking/savings): ")
            initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
            
            bank.create_account(owner_name, password, account_type, initial_balance)

        elif choice == 2:
            owner_name = input("Enter your name: ")
            password = input("Enter your password: ")
            
            account = bank.get_account(owner_name, password)

            if not account:
                print("Invalid credentials or account not found.")
                continue

            while True:
                print(f"\nWelcome, {owner_name}")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Logout")
                
                action = int(input("Choose an action: "))
                
                if action == 1:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print(f"Deposited ${amount:.2f}")
                
                elif action == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    try:
                        account.withdraw(amount)
                        print(f"Withdrew ${amount:.2f}")
                    except ValueError as e:
                        print(e)
                
                elif action == 3:
                    print(account)
                
                elif action == 4:
                    account.display_transaction_history()

                elif action == 5:
                    break

        elif choice == 3:
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
