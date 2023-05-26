years  = int(input("Please enter the number of years: "))
choice = int(input("""Pick your choice: 
                      1 - days
                      2 - weeks
                      3- months
                      4- hours:  """))
def convert_days(day=365):
    day_in_year = years * day
    return day_in_year

# total_days = convert_days(day=365)
# print(convert_days(day=365))
# print(f"'total_days = convert_days(day=365)': {total_days}")
# print(50* "-")

def convert_weeks(week=52):
    week_in_year = years * week
    return week_in_year

# total_weeks = convert_weeks(week=52)
# print("As convert_weeks(week=52)", convert_weeks(week=52))
# print(f"'total_weeks = convert_weeks(week=52)': {total_weeks}")
# print(50* "-")

def convert_months(month=12):
    months_in_year = years * month
    return months_in_year

def convert_hours(hour=8766):
    hours_in_year = years * hour
    return hours_in_year

# total_hours = convert_hours(hour=8766)
# print(f"'convert_hours(hour=8766)': {convert_hours(hour=8766)}")
# print(f"'total_hours=convert_hours(hour=8766)': {total_hours}")
# print(50* "-")

if choice == 1:
    day = convert_days()
    print(day, " days in year")

elif choice == 2: 
    week = convert_weeks()
    print(week, "weeks in year")

elif choice == 3:
    month= convert_months()
    print(month, "months in year")

elif choice == 4:
    hour = convert_hours()
    print(hour, "hours in year")

else:
    print("Please enther the right number!")
