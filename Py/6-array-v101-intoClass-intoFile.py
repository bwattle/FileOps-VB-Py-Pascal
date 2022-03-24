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
    Student("Min", 1.5, "M", 1998),
    Student("Ling", 1.6, "F", 1998)
]

if __name__ == "__main__":
    print(arrStud[0].name)
    print(arrStud[1].birthYear)
    
file = open("StudentData.txt", "w")
for i in range(0, len(arrStud)):
    line = arrStud[i].name + "," + arrStud[i].gender + "," + str(arrStud[i].birthYear) + "," + str(arrStud[i].height) + "\n"
    file.write(line)
print("done")
file.close()  # close file
