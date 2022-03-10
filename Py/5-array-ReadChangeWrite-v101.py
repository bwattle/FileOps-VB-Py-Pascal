""" 
This file makes a change to the 2D array, then does 2 updates to the file:
   the first is line by line
   the 2nd is as a block of text
Originally written to assist in the response to the HSC 2016, Q33: 
https://educationstandards.nsw.edu.au/wps/portal/nesa/resource-finder/hsc-exam-papers/2016/software-design-and-development-2016-hsc-exam-pack
Thanks to Yr12 student 2022, Minh Dang for the short "split" code and breakdown for write
The file "FoodData.txt" must be in the same folder. It can be found at: https://github.com/bwattle/FileOps-VB-Py-Pascal/blob/master/Py/FoodData.txt
The file "FoodDataChanged.txt" will be created. If it exists, it will be overwritten.
"""

with open("FoodData.txt") as file_object:
    _array = file_object.read().splitlines()

print(_array) # to check the single array with 4 elements

arr2D_elements = [i.split(",") for i in _array]
print(arr2D_elements) # check array of 4 arrays, each with 2 elements

for i in arr2D_elements:
    print(f"{i[0]} likes{i[1]}") # f for format. Spaces automatic

print("")
print(arr2D_elements[1][0]) # print 2nd person
print(arr2D_elements[0][1]) # print 1st food
arr2D_elements[0][1] = "OtherFood" # change - space left out
print(arr2D_elements[0][1]) # print 1st food, now changed

# write (w) changed array to a different text file
file = open("FoodDataChanged.txt", "w")
arrChanged = "\n" + "words written as a block:" + "\n" + "\n" # just for demo. Normally ""
print("")
for i in range(0, len(arr2D_elements)):
    line = arr2D_elements[i][0] + "," + arr2D_elements[i][1] + "\n"
    arrChanged = arrChanged + line
    file.write(line) # this writes to the file line by line
print("")
print("")
file.write(arrChanged) 
file.close()  # close text file
print(arrChanged) # just for demo