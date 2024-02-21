from PIL import Image

# WELCOME TO BANK MANAGEMENT SYSTEM
# CREATE NEW USER ACCOUNT
print("CREATE NEW USER ACCOUNT")


class CurrentAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Current Account Balance:", self.balance)


class SavingAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Savings Account Balance:", self.balance)


# Create account
def Create_Account():
    Name = input('Enter the Account Holder Name:')
    MobileNumber = str(input("Enter the Account User Mobile Number:"))

    if len(MobileNumber) == 10:
        print('Mobile number verified')
        EmailAddress = input("Enter the Account User Email Address:")
        Account_Type_Validation = input("Enter the Account Types (Saving or Current):")
        Signature = input("Enter the Account User Signature: ")
        Minimum_Balance = int(input("Enter the Account User Minimum Balance:"))

        if len(Name) > 60:
            print("Account creation failed. Name should be less than or equal to 60 characters.")
        elif len(EmailAddress) > 60:
            print("Account creation failed. Email Address should be less than or equal to 60 characters.")
        elif len(Account_Type_Validation) > 20:
            print("Account creation failed. Account Type should be less than or equal to 20 characters.")
        elif len(Signature) > 60:
            print("Account creation failed. Signature should be less than or equal to 60 characters.")
        elif not (1000 <= Minimum_Balance <= 5000):
            print("Account creation failed. Minimum balance should be between 1000 to 5000.")
        else:
            print("Account Created Successfully")

            # Assuming you have a balance for the newly created account
            if Account_Type_Validation.lower() == "current":
                account = CurrentAccount(Minimum_Balance)
            elif Account_Type_Validation.lower() == "saving":
                account = SavingAccount(Minimum_Balance)

            account.show_balance()

            i = Image.open('C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\bank acc open.jpeg')
            i.show()
    else:
        print('Please enter a valid 10-digit mobile number')


Create_Account()
