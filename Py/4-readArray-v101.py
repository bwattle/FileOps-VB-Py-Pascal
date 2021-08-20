# this file splits the fields - written by Michael Kennedy in 2020
# written to assist in the response to the HSC 2016, Q33 
data = open('FoodData.txt', 'r')
lines = data.readlines()
for line in lines:
    student = ''
    food = ''
    done_student = False
    for char in line:
        if char == ',':
            done_student = True
        elif char == ' ' or char == '\n':
            pass
        elif done_student:
            food += char
        else:
            student += char
    print(f"{student} likes {food}")
