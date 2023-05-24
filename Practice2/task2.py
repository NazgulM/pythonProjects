# Create tuples
foods_tuple = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin")
calories_tuple = (52, 96, 62, 60, 33, 68, 50)

print(foods_tuple)
print(calories_tuple)

# Convert from tuples to list:
foods_list = ["apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry"]
calories_list = [52, 96, 62, 60, 33, 68, 50, 33]

# print out the strawberry with caloric value:
print(f"{foods_list[4]}: {calories_list[4]}")

# Print out the second last output and its caloric value
print(f"{foods_list[-2]}: {calories_list[-2]}")

# Print all the uniique foods in the list:
print(f"{set(foods_list)}: {set(calories_list)}")

# Create a dict with their unique values 

dict_food = {"apple": "kcal", "banana": "96 kcal", "orange": "62 kcal", "mango": "60kcal", 
             "strawberry": "33 kcal", "grape": "68 kcal", "mandarin": "50 kcal"}

dict_food["tomato"] = "60 kcal"

print(dict_food)

# Replace the caloric value of a grape to 50 from the dictionary, print out the value

dict_food["grape"] = "50 kcal"

print(dict_food)