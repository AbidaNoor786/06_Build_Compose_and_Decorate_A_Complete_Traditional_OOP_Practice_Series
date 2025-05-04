# 1. Using self
#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Age: {self.age}")



student1 = Student("Abida Noor", 99, 30)
student1.display()
    