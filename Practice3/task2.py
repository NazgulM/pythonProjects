print("""Task 2: Create a calculator program with 4 functions that either adds, subtracts
        multiplies,divides, 2 numbers from user input""")

a = float(input("Please enter the 1st number: "))
b = float(input("Please add the 2nd number: "))
choice = (input("""Please choose:
                       + - addition
                       - - subtraction
                       * - multiplication
                       / - division: """))
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiple(a,b):
    return a * b

def divide(a,b):
    return a / b

if choice == "+":
    addition = add(a,b)
    print("Addition: ", addition)

elif choice == "-":
    substraction = subtract(a,b)
    print("Subtraction: ", substraction)

elif choice == "*":
    multiplication = multiple(a,b)
    print("Multiplication: ", multiplication)

elif choice == "/":
    division = divide(a,b)
    print("Division: ", division)

else:
    print("Please pick right choice!")

