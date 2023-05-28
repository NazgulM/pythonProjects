#sum = 0
# number = 1

# while sum < 100:
#     number += 1
#     sum += number
#     print(sum)

sum = 0
list1 = []

while sum < 100:
    number = int(input("Enter the number: "))
    sum += number
    list1.append(number)
    print(sum)

print(f"Here is the list: {list1}")

