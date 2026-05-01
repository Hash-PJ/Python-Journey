## Build a class called Student that:

## Takes name, age, and marks (a list) in __init__
## Has a method average() that returns the average of marks
## Has a method grade() that returns "A" if average ≥ 80, "B" if ≥ 60, else "C"
## Has a __str__ that prints something like: Riya (Age 15) — Grade: A

class Student:
    def __init__(self, name, age, marks):
        self. name = name
        self.age = age
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
       
    def grade(self):
        grade = ''
        avg = self.average()
        if avg >= 80:
            grade = 'A'
        elif avg >= 60:
            grade = 'B'
        else:
            grade = 'C'
        self.grade = grade
        return grade

    def __str__(self):
        return f"{self.name} (Age {self.age}) - Grade: {self.average}"


student1 = Student('Riya', 15, [33, 45, 56, 78 , 76])
print(student1.grade())
print(student1.average())
print(student1)
