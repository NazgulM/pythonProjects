limit = int(input("Enter limit: "))
first_value = 0
second_value = 1

next_value = first_value + second_value

while next_value <= limit:
    print(next_value)

    first_value = second_value
    second_value = next_value

    next_value = first_value + second_value

