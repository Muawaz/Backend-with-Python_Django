# Question 2:
# Create a base class Animal with a method speak() that prints a generic message
# like "Animal makes a sound". Then, create derived classes Dog and Cat that 
# inherit from Animal and override the speak() methid to print "Dog barks" and 
# "Cat meows" respectively. Instantiate objects of Dog and Cat and call the speak()
# method on each

class Animal:
    def __init__(self):
        pass

    def speak(self):
        print("---Animal makes a sound---\n")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("---Dog Barks---\n")

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("---Cat Meows---\n")

animal_obj = Animal()
animal_obj.speak()

dog_obj = Dog()
dog_obj.speak()

cat_obj = Cat()
cat_obj.speak()