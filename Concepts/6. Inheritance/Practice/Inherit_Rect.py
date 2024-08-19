# Question 1:
# Create a base class called Shape with attributes width and height and 
# a method calculate_area() that calculates and returns the area of the shape.
# Create a derived class called Rectangle that inherits from Shape and overrides
# the calculate_area() method to calculate the area of the rectangle. Instiate
# an object of the Rectanle class, set the width and height, and call the 
# calculate_area() method


class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        pass
    

class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calculate_area(self):
        return self.base * self.height
    

rect_obj = Rectangle(12, 6)
area = rect_obj.calculate_area()
print("The area of the rectangle = ", area)