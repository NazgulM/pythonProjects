age  = int(input("Please enter the age of the person: "))

if age < 13:
    print("The user is a child!")

elif age >= 13 and age < 18: 
    print("The user is a teenager!")

elif age >= 18 and age <= 65:
    print("The user is an adult!")

elif age > 65:
    print("The user is an elder person!")


# Task2

tip = int(input("Please enter the tip percentage: "))

if tip == 15 :
    print("Standard")

elif tip == 18:
    print("Good!")

elif tip == 20:
    print("Great!")

elif tip > 20:
    print("My hero")

else:
    print("Please enter 15, 18, 20 or greater")