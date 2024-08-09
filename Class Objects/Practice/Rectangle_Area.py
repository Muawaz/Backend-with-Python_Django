# Question 1: 
# Create a class called Rectangle with attributes width and height. 
# Implement a method calculate_area that returns the area of the rectangle. 
# Instantiate an object of the class and calculate its area.

class MyRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def cal_area(self):
        area = self.width * self.width
        print("\nThe area of the defined rectangele =", area, "\n")
        return area

rect_obj = MyRectangle(5, 6)
rect_obj.cal_area()