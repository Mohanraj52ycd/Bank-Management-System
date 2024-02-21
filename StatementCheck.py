from PIL import Image
import random as r

print("Statement Checking")


def display_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except:
        print("Error: Unable to open or display the image.")


username: str = "mohan"
user_passward = "mohan123"


def Bank_statement_Enquiry():
    User_Name = input("Enter the  Account User Name:")
    User_Password = input("Enter the Account User Password:")
    if username == User_Name and user_passward == User_Password:
        print(" Statement Successfully Open:")
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\statement1.PNG")
    else:
        print("User Data is incorrect Try Again Please")


Bank_statement_Enquiry()
