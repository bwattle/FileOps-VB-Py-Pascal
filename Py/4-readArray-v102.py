# this file splits the fields - written by Minh Dang in 2022 - clever!
# written to assist in the response to the HSC 2016, Q33 
# shorter that v1.01, but not as easy to see what's happening

with open("FoodData.txt") as file_object:
    _array = file_object.read().splitlines()

print(_array) # to check the single array with 4 elements

arr2D_elements = [i.split(",") for i in _array]
print(arr2D_elements) # check array of 4 arrays, each with 2 elements

for i in arr2D_elements:
    print(f"{i[0]} likes{i[1]}") # f for format. Spaces automatic

print("") # blank line
print(arr2D_elements[1][0]) # print 2nd person
print(arr2D_elements[0][1]) # print 1st food
print(arr2D_elements[3][1]) # print 4th food