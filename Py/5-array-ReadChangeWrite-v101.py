# Python use "list" instead of "array"
# This program demonstrates how to read, ammend and write to text file using Python
# originally written to assist in the response to the HSC 2016, Q33
# Thanks to Yr12 student 2022, Minh Dang for the short "split" code and breakdown for write

# "with" block https://www.python.org/dev/peps/pep-0343/#examples.
# Read file
with open("FoodData.txt") as file_object:
    name_food_list = file_object.read().splitlines()

print(f"name_food_list 'array': {name_food_list}")
# 👉 ['Charlie, fish', 'Tim, meat', 'Max, tuna', 'Simon, rice']

# Split the string (format: "name, food") into 2 array element (format: ["name", "food"])
# List comprehension used: https://www.programiz.com/python-programming/list-comprehension
name_food_list_2D = [i.split(", ") for i in name_food_list]
print(f"name_food_list_2D 'array': {name_food_list_2D}\n")
# 👉 [['Charlie', ' fish'], ['Tim', ' meat'], ['Max', ' tuna'], ['Simon', ' rice']]

for i in name_food_list_2D:
    print(f"{i[0]} likes {i[1]}")

print(f"\n2nd person's name: {name_food_list_2D[1][0]}")
# 👉 'Tim'
print(f"\n1st person's food: {name_food_list_2D[0][1]}")
# 👉 'fish'

# Update value
name_food_list_2D[0][1] = "OtherFood"
print(f"\n1st person's UPDATED food: {name_food_list_2D[0][1]}")
# 👉 'OtherFood'

print("\nData saved to file 'FoodDataChanged.txt'")
# Write file (creates new file if file does not exist)
with open("FoodDataChanged.txt", "w") as file_object:
    # Loop through 2D array -> Turn child array into string, append string with newlines
    for i in name_food_list_2D:
        to_be_written = ", ".join(i)
        print(to_be_written)
        file_object.write(to_be_written + "\n")
