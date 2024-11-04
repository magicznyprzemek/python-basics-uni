class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_mark = sum(self.marks) / len(self.marks)
        return average_mark > 50

student1 = Student("A", [70, 65, 80])
student2 = Student("B", [40, 45, 35])

print(student1.is_passed())
print(student2.is_passed())
