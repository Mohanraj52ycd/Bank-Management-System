import random as r
from PIL import Image


def display_image(image_path):
    image = Image.open(image_path)
    if image:
        image.show()

    else:
        print("Error:  Unable to open or display the image.")


def otp_generate():
    return str(r.randint(1000, 9999))


def send_otp(mobile_number, otp):
    print(f"OTP sent to {mobile_number}: {otp}")


def Update_Acc(pan_card=None, aadhar_card=None):
    user_Name = "mohan"
    user_Acc = 1226120000041
    user_Mobile_Number = 9443308552

    print("Update User Bank Account")
    User_Name = input("Enter the Account Holder Name:")
    User_Acc = int(input("Enter the User Account Number:"))
    entered_mobile_number = int(input("Enter the User Mobile Number"))


    if User_Name == user_Name and User_Acc == user_Acc and entered_mobile_number == user_Mobile_Number:
        print("User Account successfully Open  ")
        otp = otp_generate()
        send_otp(entered_mobile_number, otp)
        entered_otp = input("Enter the mobile OTP please:")

        if entered_otp == otp:
            print("OTP verified. You can proceed to update your account.")
            while True:
                print("\nOptions:")
                print("1. Change Your New Mobile Number")
                print("2. Change Your New Address")
                print("3. Change Your Account Saving Acc or Current Acc ")
                print("4. Change Your New Branch Address")
                print("5. Change Your New Email Address ")
                print("6. Update Your PAN code ")
                print("7. Exit")

                choice = input("Enter your choice please (1-7): ")

                if choice == "1":
                    old_mobile_number = entered_mobile_number
                    new_mobile_number = input("Enter your new mobile number: ")
                    print(f"Mobile number updated from {old_mobile_number} to {new_mobile_number}")
                elif choice == "2":
                    old_address = input("Enter your old address: ")
                    new_address = input("Enter your new address: ")
                    print(f"Address updated from {old_address} to {new_address}")
                elif choice == "3":
                    old_account_type = input("Enter your old account type (Saving/Current): ")
                    new_account_type = input("Enter your new account type (Saving/Current): ")
                    print(f"Account type updated from {old_account_type} to {new_account_type}")
                elif choice == "4":
                    old_branch_address = input("Enter your old branch address: ")
                    new_branch_address = input("Enter your new branch address: ")
                    print(f"Branch address updated from {old_branch_address} to {new_branch_address}")
                elif choice == "5":
                    old_email = input("Enter your old email address: ")
                    new_email = input("Enter your new email address: ")
                    print(f"Email address updated from {old_email} to {new_email}")
                elif choice == "6":
                    pan_code = input("Enter your new PAN code: ")
                    print(f"PAN code updated to {pan_code}")
                elif choice == "7":
                    print("Exiting...")
                    display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\Update Acc Details.jpeg")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
        else:
            print("Incorrect OTP. Update process aborted.")
    else:
        print("Invalid account details. Update process aborted.")


Update_Acc()