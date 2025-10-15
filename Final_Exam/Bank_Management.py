
import random
import string
class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_limit = 2

    def generate_account_number(self):
        account_number = ''.join(random.choices(string.digits, k=6))
        return account_number

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} taka")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal amount exceeded"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount} taka")
            return f"Withdraw {amount} taka"

    def check_balance(self):
        return f"Available balance: {self.balance} taka Account_Number:{self.account_number}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < self.loan_limit:
            self.loan_taken += amount
            self.balance += amount
            self.transaction_history.append(f"Took a loan of {amount} taka")
            return f"Loan of {amount} taka granted"
        else:
            return "Maximum number of loans taken"

    def transfer(self, amount, other_account):
        if amount > self.balance:
            return "Not Send Amount"
        elif not isinstance(other_account, User):
            return "Account does not exist"
        else:
            self.balance -= amount
            other_account.balance += amount
            self.transaction_history.append(f"Transferred {amount} taka to {other_account.name}")
            return f"Transferred {amount} taka to {other_account.name}"


class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        self.users.append(new_user)
        return new_user

    def delete_account(self, user):
        self.users.remove(user)

    def get_all_accounts(self):
        return self.users

    def get_total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        return f"Total balance in the bank: {total_balance} taka"

    def get_total_loan_amount(self):
        total_loan_amount = sum(user.loan_taken for user in self.users)
        return f"Total loan amount in the bank: {total_loan_amount} taka"

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        if self.loan_feature_enabled:
            return "Loan feature enabled"
        else:
            return "Loan feature disabled"


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, user):
        self.bank.delete_account(user)

    def get_all_accounts(self):
        return self.bank.get_all_accounts()

    def check_total_balance(self):
        return self.bank.get_total_balance()

    def check_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def toggle_loan_feature(self):
        return self.bank.toggle_loan_feature()
    
    def find_user_by_name(name):
        for user in bank.users:
            if user.name.lower() == name.lower():
                return user
        return None

def user_menu(user):
    while True:
        print("\nUser Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            user.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            print(user.withdraw(amount))
        elif choice == "3":
            print(user.check_balance())
        elif choice == "4":
            print(user.check_transaction_history())
        elif choice == "5":
            amount = float(input("Enter the amount of loan: "))
            print(user.take_loan(amount))
        elif choice == "6":
            amount = float(input("Enter the amount to transfer: "))
            recived_name = input("Enter recipient's name: ")
            recived = Admin.find_user_by_name(recived_name)
            if recived:
                print(user.transfer(amount, recived))
            else:
                print("Recipient not found.")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. View All User Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type ( savings, current): ")
            admin.create_account(name, email, address, account_type)
        elif choice == "2":
            name = input("Enter user's name: ")
            user = Admin.find_user_by_name(name)
            if user:
                admin.delete_account(user)
                print("User account deleted.")
            else:
                print("User not found.")
        elif choice == "3":
            accounts = admin.get_all_accounts()
            for account in accounts:
                print(f"Name: {account.name}, Email: {account.email}, Address: {account.address}, Balance: {account.balance} Account_Number: {account.account_number}")
        elif choice == "4":
            print(admin.check_total_balance())
        elif choice == "5":
            print(admin.check_total_loan_amount())
        elif choice == "6":
            print(admin.toggle_loan_feature())
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


bank = Bank()
admin = Admin(bank)
Run=True
while Run:
    print("\n Welcome to Bank Management System")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    user_type = input("Enter user type: ")

    if user_type == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type ( savings, current): ")
        user = bank.create_account(name, email, address, account_type)
        user_menu(user)
    elif user_type == "2":
        admin=input("Enter usrname: ")
        password=input("Enter passord: ")
        if admin=="admin" and password=="12345":
             admin_menu(admin)
        else:
            print("Worng Entry.Place Try agian")
    elif user_type == "3":
        break
    else:
        print("Invalid choice.")

