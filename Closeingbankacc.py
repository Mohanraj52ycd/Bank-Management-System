from PIL import Image
import random as r


def image_display(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except FileNotFoundError:
        print("Error: Image file not found at the specified path.")
    except Exception as e:
        print(f"Error: {e}")


def otp_generation():
    return str(r.randint(1000, 9999))


def bank_close():
    User_Name = "mohan"
    User_Account_Number = "1226120000041"  # Make account number a string
    User_Mobile_Number = "8903797751"  # Make mobile number a string
    print("Bank Account Closing")
    use_name = input("Enter the Account Holder Name: ")
    use_Account_number = input("Enter the Account Number Please: ")
    use_mobile_number = input("Enter the Account Holder Mobile Number: ")

    # Validate user input
    if (User_Name == use_name and User_Account_Number == use_Account_number and
            User_Mobile_Number == use_mobile_number):
        print("User Account successfully Open : ")
        otp = otp_generation()
        print("Generated OTP:", otp)
        entered_otp = input("Enter the mobile OTP please: ")
        print("Entered OTP:", entered_otp)
        if entered_otp == otp:
            print("OTP verified. You can proceed to update your account.")
            while True:
                print("\nReason Option:")
                print("1. Poor Customer Service")
                print("2. Interest Rate are High")
                print("3. Negative Balance")
                print("4. Change at the New Bank ")
                print("5. Local Branches have Shutdown")
                print("6. You are Moving to a New City")
                print("7. Fake mitten details in bank ")
                print("8. Over Charge the Service Fees")
                print("9. Exit...")

                choice = input('Enter your choice please (1-9): ')
                if choice == "1":
                    print("Poor Customer Service")
                elif choice == "2":
                    print("Interest Rate are High")
                elif choice == "3":
                    print("Negative Balance")
                elif choice == "4":
                    print("Change at the New Bank ")
                elif choice == "5":
                    print("Local Branches have Shutdown")
                elif choice == "6":
                    print("You are Moving to a New City")
                elif choice == "7":
                    print("Fake mitten details in bank ")
                elif choice == "8":
                    print("Over Charge the Service Fees")
                elif choice == "9":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 9.")
        else:
            print("Your OTP is Invalid. Update Process aborted.")
    else:
        print("Invalid Account details. Update process aborted.")
    image_display("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\bank  acc close.jpeg")
    print("Bank account successfully closed.")




bank_close()
