# Question 3: 
# Create a class called Car with attributes make, model, and year. 
# Implement methods start_engine and stop_engine that print messages 
# indicating the engine's state. 
# Instantiate an object of the class, start the engine, and then stop it.

class MyCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine = False

    def start_engine(self):
        if self.engine == False:
            self.engine = True
            print("Vroom, Vroooom,\n The Engine has started successfully\n")
        elif self.engine == True:
            print("The Engine is Running already !\n")

    def stop_engine(self):
        if self.engine == True:
            self.engine = False
            print("Brrrrum, rummm, mm,\n The Engine has stopped successfully\n")
        elif self.engine == False:
            print("The Engine is Stopped already !\n")

car_obj = MyCar("ToytaFord", "Fogg", "2025")
car_obj.start_engine()
car_obj.start_engine()

car_obj.stop_engine()
car_obj.stop_engine()
