
while True: 
    age  = int(input("Enter the age: "))
    if age < 13: 
        print("Sorry, you are not allowed")
    elif age >= 13 and age < 18:
        print("Please call your legal guardian")
    elif age >= 18:
        print("Welcome!")
    
