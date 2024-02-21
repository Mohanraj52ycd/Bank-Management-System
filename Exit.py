from PIL import Image

def display_image(image_path: object) -> object:
    image = Image.open(image_path)
    if image:
        image.show()
    else:
        print("Error: Unable to open or display the image.")

def Bank_acc_Exit():
    print("1. Poor")
    print("2. Unsatisfactory")
    print("3. Satisfactory")
    print("4. Very Satisfactory")
    print("5. Outstanding")
    choice = input("Enter your Choice (1-5): ")
    if choice == "1":
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\rating poor image.jpg")
        print("Thank you for your Rating")
    elif choice == "2":
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\rating Unsatisfactory imoji.jpeg")
        print("Thank you for your Rating")
    elif choice == "3":
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\rating imoji Satisfactory.jpg")
        print("Thank you for your Rating")
    elif choice == "4":
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\rating Very Satisfactory.png")
        print("Thank you for your Rating")
    elif choice == "5":
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\raring Outstanding imoji.jpg")
        print("Thank you for your Rating")

Bank_acc_Exit()


