years=int(input("Please enter the number of years: "))

unit = int(input("""Please pick which unit to convert to: 
                 1-days 
                 2-weeks 
                 3-months: """))
if unit == 1:
    print(f"{years * 365} days")

elif unit == 2:
    print(f"{years * 52} weeks")

elif unit == 3:
    print(f"{years * 12} months")

else:
    print("Pick the right choice!")