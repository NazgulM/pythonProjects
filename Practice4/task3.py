print("=====Task1======")
sum = 0
for i in range(0,101):
    sum += i
print(sum)

print("=====Task2=======")

for num in range(100, 0, -1):
    print(num)

print("======task3=====")

list1=[0,1,2,3,4,5,6,7,8,9,10]

for a in list1:
    if a % 2 == 0 and a != 0:
        print(a)

print("====Task4====")

number_user = int(input("Please enter the number: "))

for b in range(0, 11):
    print(f"{number_user} * {b} = {number_user*b}")