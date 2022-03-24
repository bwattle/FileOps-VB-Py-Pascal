"""
This file creates a class with an "arrStud of records" - 3 data types
Thanks to Yr12 Student 2022, Aiden Gardner for the structure
"""

class Student:
    def __init__(self, name: str, height: float, gender: str, birthYear: int):
        self.name = name
        self.height = height
        self.gender = gender
        self.birthYear = birthYear



arrStud = [
    Student("Name", 0.0, "Gender", 2000)
]

with open("StudentData.txt") as file_object:
    arrLines = file_object.read().splitlines()

print(arrLines)
print(arrLines[0][2])

arr2D = [i.split(",") for i in arrLines]
arr2D.append("'Ling', 'F', '1998', '1.6'")
print(arr2D)
print(arr2D[0][2])
"""
for i in range(0, len(arr2D)):
    arrStud.append
    arrStud[i].name = arr2D[i][0]
    arrStud[i].gender = arr2D[i][1]
    """
if __name__ == "__main__":
    print(arrStud[0].name)
    #print(arrStud[1].birthYear)
    
file = open("StudentData.txt", "w")
for i in range(0, len(arrStud)):
    line = arrStud[i].name + "," + arrStud[i].gender + "," + str(arrStud[i].birthYear) + "," + str(arrStud[i].height) + "\n"
    file.write(line)
print("done")
file.close()  # close file