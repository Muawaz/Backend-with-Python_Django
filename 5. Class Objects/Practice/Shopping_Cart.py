# Question 4: 
# Create a class ShoppingCart with attributes items (a list to hold items 
# in the cart) and total_price. 
# Implement methods add item to add an item with its price to the cart, 
# remove_item to remove an item by name, and checkout to calculate and 
# return the total price of items in the cart.
# Expected Output:
# Added Laptop to the cart.
# Added Headphones to the cart.

class ShoppingCart:
    def __init__(self,):
        self.item = []
        # self.item.append(item)
        self.total_price = 0

    def add_item(self, name, price):
        item_tuple = (name, price)
        self.item.append(item_tuple)
        self.total_price += price
        print(self.item[len(self.item) - 1][0], " added to the list\n")

    def remove_item(self, name):
        for item in self.item:
            # print(item[0])
            if name == item[0]:
                self.total_price -= item[1]
                print(item[0], " removed from the list\n")
                self.item.remove(item)

    def checkout(self):
        print("====Checking out your Cart====")
        print (f"Items: {self.item}\nPrice: ${self.total_price}\n")
        return f"Items: {self.item}\nPrice: ${self.total_price}\n"

cart_obj = ShoppingCart()

cart_obj.add_item("Keyboard", 150)
cart_obj.add_item("Mouse", 80)
cart_obj.add_item("Laptop", 830)
cart_obj.add_item("Headphones", 470)

cart_obj.remove_item("Keyboard")
cart_obj.checkout()

