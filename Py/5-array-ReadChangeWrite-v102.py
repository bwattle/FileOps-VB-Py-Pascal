"""
This file makes a change to the 2D array, then updates to the file
It was originally written to assist in the response to the HSC 2016, Q33 
https://educationstandards.nsw.edu.au/wps/portal/nesa/resource-finder/hsc-exam-papers/2016/software-design-and-development-2016-hsc-exam-pack
Thanks to Yr12 student 2022, Minh Dang for the much tighter write code
The file "FoodData.txt" must be in the same folder. It can be found at: https://github.com/bwattle/FileOps-VB-Py-Pascal/blob/master/Py/FoodData.txt
The file "newfile.txt" will be created. If it exists, it will be overwritten.
"""

with open("FoodData.txt") as file_object:
    name_food_array = file_object.read().splitlines()

print(name_food_array)

name_food_array_sanitised = [i.split(",") for i in name_food_array]
print(name_food_array_sanitised)

for i in name_food_array_sanitised:
    print(f"{i[0]} likes{i[1]}")

name_food_array_sanitised[0][1] = " guacamole"
print(name_food_array_sanitised)

with open("newfile.txt", "w") as file_object:
    for i in name_food_array_sanitised:
        to_be_written = ",".join(i)
        print(to_be_written)
        file_object.write(to_be_written + "\n")
