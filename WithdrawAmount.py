from PIL import Image
import random as r

print("Withdrew Your amount")
# Global variable for balance
balance = 10000

def display_image(image_path):
    try:
        print("Attempting to open image:", image_path)
        image = Image.open(image_path)
        if image:
            image.show()
        else:
            print("Error: Unable to open or display the image")
    except Exception as e:
        print("Error:", e)

def generate_otp():
    return ''.join(r.choices('0123456789', k=4))  # Generate a random 4-digit OTP

def send_otp(user_mobile_number, otp):
    print("OTP sent to", user_mobile_number, ":", otp)

def withdraw_amount():
    global balance
    user_name = input("Enter the Account User Name: ")
    user_acc = input("Enter the Account User Account Number:")
    user_mobile_number = input("Enter the User Mobile Number :")
    withdraw_date = input("Enter the Withdraw Date:")
    withdraw_amount = float(input("Enter the Withdraw Amount:"))

    atm_option = input("Do you want ATM option (yes or no): ")
    if atm_option.lower() == "yes":
        print("Please insert your ATM card and follow the instructions on the screen.")
        print("Your withdrawal is being processed. Please wait until your transaction is completed.")
        print("Thank you for using our ATM service.")
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\withraw_Amount.jpeg")
        show_balance()
    else:
        otp = generate_otp()
        send_otp(user_mobile_number, otp)
        entered_otp = input("Enter the OTP received on your mobile:")
        if entered_otp == otp:
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print("OTP verified. Successfully Withdrawn Amount:", withdraw_amount)
                print("Current balance:", balance)
                display_image("C:\\Users\\admin\PycharmProjects\\Bank Management System\\BMS\\withraw_Amount.jpeg")

            else:
                print("Insufficient balance.")
        else:
            print("OTP verification failed. Withdrawal unsuccessful.")


# Function to show balance
def show_balance():
    global balance
    print("Current balance:", balance)

withdraw_amount()  # Call the withdraw function
   # Call the function to show the balance
