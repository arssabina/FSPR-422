# 7 kyu
# These are not my grades! (Revamped !)

class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = list(grades) # копия списка как deep copy
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)

johnDoe=Student("John", "Doe")
janeDoe=Student("Jane", "Doe")
jamesSmith=Student("James", "Smith")
jennaSmith=Student("Jenna", "Smith")
students=(johnDoe, janeDoe, jamesSmith, jennaSmith)
firstAssesmentGrades=[63,92,82,75]


"""Вместо этого кода, напишем динамичный код с for циклом"""
# johnDoe.add_grade(firstAssesmentGrades[0])
# janeDoe.add_grade(firstAssesmentGrades[1])
# jamesSmith.add_grade(firstAssesmentGrades[2])
# jennaSmith.add_grade(firstAssesmentGrades[3])  

# Динамичный код:

for i, student in enumerate(students):
    # print(i, student.first_name)
    student.add_grade(firstAssesmentGrades[i])  # 0 1 2 3

print(johnDoe.grades)
print(janeDoe.grades)
print(jamesSmith.grades)
print(jennaSmith.grades)


