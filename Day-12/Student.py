## Build a class called Student that:

## Takes name, age, and marks (a list) in __init__
## Has a method average() that returns the average of marks
## Has a method grade() that returns "A" if average ≥ 80, "B" if ≥ 60, else "C"
## Has a __str__ that prints something like: Riya (Age 15) — Grade: A

class InvalidMarksError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EmptyMarksError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


    def average(self):
        if len(self.marks) == 0:
            raise EmptyMarksError('There is no list of marks.')
        return sum(self.marks)/len(self.marks)
       
       
    def grade(self):
        avg = self.average()
        if avg >= 80:
            return 'A'
        elif avg >= 60:
            return 'B'
        else:
            return 'C'
    
    
    def add_mark(self, new_mark):
        if not isinstance(new_mark, (int, float)):
            raise InvalidMarksError("Marks must be a number!")
        if new_mark < 0 or new_mark > 100:
            raise InvalidMarksError(f"Mark {new_mark} is out of range (0–100)!")
        self.marks.append(new_mark)
        print(f"Mark {new_mark} added successfully.")


    def __str__(self):
        return f"{self.name} (Age {self.age}) - Grade: {self.grade()}"
    
    
    def __gt__(self, other):
        return self.average() > other.average()
        
        
    def __lt__(self, other):
        return self.average() < other.average() 


student1 = Student('Priya', 17, [33, 45, 56, 78 , 76])
print(student1.grade())
print(student1.average())
print(student1)

s1 = Student('Riya', 15, [80, 90, 85])
s2 = Student('Arjun', 16, [70, 65, 72])

print(s1 > s2)
print(s1 < s2)

try:
    s = Student("Riya", 15, [])
    print(s.average())

    s3 = Student("Arjun", 16, [70, 80])
    s3.add_mark(150)
    s3.add_mark("ninety")
    s3.add_mark(95)
    print(s3)

except InvalidMarksError as e:
    print(e)

except EmptyMarksError as e:
    print(e)

except Exception as e:
    print(f"Something unexpected: {e}")
