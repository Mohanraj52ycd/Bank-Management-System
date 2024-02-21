from PIL import Image
import random as r
print("Deposit your Amount")
# Global variable for balance
balance = 10000

def display_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print("Error:", e)

def generate_otp():
    return ''.join(r.choices('0123456789', k=4))  # Generate a random 4-digit OTP

def send_otp(user_mobile_number, otp):
    print("OTP sent to", user_mobile_number, ":", otp)

def deposit_amount():
    global balance
    user_name = input("Enter the Account Holder Name:")
    user_acc_no = input("Enter the Account No:")
    user_mobile_number = input("Enter the Account Mobile Number:")
    deposit_Amount = float(input("Enter the amount you want to deposit:"))
    atm_option = input("Do you want ATM Option? (yes or no):")

    if atm_option.lower() == "yes":
        print("Please insert your card and follow the instructions on the screen.")
        print("Your deposit will be processed once your transaction is completed.")
        print("Thank you for using the ATM service.")
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\deposit.jpeg")
        show_balance()
    else:
        otp = generate_otp()
        send_otp(user_mobile_number, otp)
        entered_otp = input("Enter the OTP received on your mobile:")

        if entered_otp == otp:
            balance += deposit_Amount
            print("OTP verified. Successfully deposited:", deposit_Amount)
            print("Current balance:", balance)
            display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\deposit.jpeg")
        else:
            print("OTP verification failed. Deposit unsuccessful.")

# Function to show balance
def show_balance():
    global balance
    print("Current balance:", balance)

deposit_amount()  # Call the deposit function
