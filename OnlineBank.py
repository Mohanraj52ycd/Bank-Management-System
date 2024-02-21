import time
from PIL import Image
import webbrowser
def display_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except FileNotFoundError:
        print("Error: Image file not found at the specified path.")
    except Exception as e:
        print(f"Error: {e}")

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful.")
        self.display_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
            self.display_balance()
        else:
            print("Insufficient funds.")
            self.display_balance()


def online_operations(account):
    while True:
        print("\nATM Operations:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            account.display_balance()
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
            display_image('C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\withraw_Amount.jpeg')  # Display withdrawal image
        elif choice == "3":
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
            display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\deposit.jpeg")  # Display deposit image
        elif choice == "4":
            print("Exiting ...")
            display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\bank exit image.png")  # Display exit imag
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def open_account_online_process():
    print("Welcome to the Online Banking  Process")
        # Gather customer information
    name = input("Enter your full name: ")
    account_number = input("Enter account number: ")
    initial_deposit = float(input("Enter initial deposit amount: $"))

    # Create a new bank account
    new_account = BankAccount(name, account_number, initial_deposit)
    print("\nCongratulations! Your account has been successfully opened online.")
    print("Account Details:")
    print("Name:", new_account.name)
    print("Account Number:", new_account.account_number)
    new_account.display_balance()

    # Perform ATM operations
    print("\nWelcome to Online Operations")
    online_operations(new_account)


# Example usage:
open_account_online_process()
