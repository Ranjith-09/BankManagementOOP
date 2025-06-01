class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account: {self.account_number} | Name: {self.name} | Balance: ₹{self.balance}")

# Store accounts in a dictionary
accounts = {}

def create_account():
    acc_no = input("Enter account number: ")    
    if acc_no in accounts:
        print("Account already exists.")
        return
    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial deposit: "))
    accounts[acc_no] = BankAccount(acc_no, name, balance)
    print("Account created successfully.")

def access_account():
    acc_no = input("Enter account number: ")
    account = accounts.get(acc_no)
    if not account:
        print("Account not found.")
        return

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\n=== BANK MENU ===")
        print("1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            create_account()
        elif option == "2":
            access_account()
        elif option == "3":
            print("Thanks for using the system. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
