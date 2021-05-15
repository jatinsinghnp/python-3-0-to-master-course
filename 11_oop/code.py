class Student:
    def __init__(self, name, grades, age):
        self.name = name

        self.grades = grades
        self.age = age

    # def __str__(self):
    #     return f"<person{self.name},{self.age} years old.>"

    def average(self):
        return sum(self.grades)/len(self.grades)

    def __repr__(self):  # use for representing the object
        return f"<person({self.name},{self.age})>"


obj = Student("jatin", (100, 23, 12, 145, 16, 7), 10)
print(obj.average())
print(obj)
