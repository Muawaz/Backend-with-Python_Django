# Question 3:
# Create a base class Person with attributes name and age. Write a method
# display_info() that prints the name and age. 
# Create a derived class Student that inherits from Person and adds an attribute 
# student_id. 
# Override the display_info() method to include the student_id when printing. 
# Instantiate an object of Student, and demonstrate how the constructor of the base 
# class is called automatically.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}\nAge:{self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"{super().display_info()}\nId:{self.student_id}"
    

student_obj = Student("Muawaz", 100, 3)
info = student_obj.display_info()
print(info)