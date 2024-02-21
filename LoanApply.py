from PIL import Image

print("Chose yor loan option pleas")
class Loan:
    def __init__(self, name, amount, interest_rate, duration):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration
        self.status = "Pending"

    def calculate_total_payment(self):
        total_interest = self.amount * (self.interest_rate / 100) * self.duration
        return self.amount + total_interest

    def approve_loan(self):
        self.status = "Approved"
        print("Loan approved!")
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\loan approved.jpg")

    def reject_loan(self):
        self.status = "Rejected"
        print("Loan rejected.")
        display_image("C:\\Users\\admin\\PycharmProjects\\Bank Management System\\BMS\\loan reject.jpg")

def display_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except FileNotFoundError:
        print("Error: Image file not found at the specified path.")
    except Exception as e:
        print(f"Error: {e}")

class PersonalLoan(Loan):
    def __init__(self, name, amount, interest_rate, duration, purpose):
        super().__init__(name, amount, interest_rate, duration)
        self.purpose = purpose

class HomeLoan(Loan):
    def __init__(self, name, amount, interest_rate, duration, property_type):
        super().__init__(name, amount, interest_rate, duration)
        self.property_type = property_type

class CarLoan(Loan):
    def __init__(self, name, amount, interest_rate, duration, car_model):
        super().__init__(name, amount, interest_rate, duration)
        self.car_model = car_model

def apply_for_loan(loan_type):
    print(f"Applying for a {loan_type} Loan")
    name = input("Enter your full name: ")
    amount = float(input("Enter loan amount: $"))
    interest_rate = float(input("Enter annual interest rate (%): "))
    duration = int(input("Enter loan duration (in years): "))

    if loan_type == "Personal":
        purpose = input("Enter loan purpose: ")
        loan = PersonalLoan(name, amount, interest_rate, duration, purpose)
    elif loan_type == "Home":
        property_type = input("Enter property type: ")
        loan = HomeLoan(name, amount, interest_rate, duration, property_type)
    elif loan_type == "Car":
        car_model = input("Enter car model: ")
        loan = CarLoan(name, amount, interest_rate, duration, car_model)
    else:
        print("Invalid loan type")
        return

    total_payment = loan.calculate_total_payment()
    print("\nLoan Details:")
    print("Name:", loan.name)
    print("Loan Amount: $", loan.amount)
    print("Total Payment: $", total_payment)

    decision = input("Do you want to approve or reject the loan? (approve/reject): ")
    if decision.lower() == "approve":
        loan.approve_loan()
    else:
        loan.reject_loan()

# Example usage:
loan_type = input("Enter the type of loan you want to apply for (Personal/Home/Car): ")
apply_for_loan(loan_type)
