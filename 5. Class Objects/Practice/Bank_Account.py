# Question 2: 
# Create a class called Bank with attribute name and an empty list accounts. 
# Implement methods add_account and remove account that add or remove a bank account 
# from the list. 
# Instantiate an object of the class, add multiple accounts, 
# and then remove one of them.

class MyBank:
    def __init__(self, name, account):
        self.name = name
        self.account = []
        self.account.append(account)

    def add_account(self, acc_num):
        self.account.append(acc_num)
        print("Account added successfuly")

    def remove_account(self, acc_num):
        if acc_num in self.account:
            self.account.remove(acc_num)
            print("Account remove successfuly")
        

    def __str__(self):
        return f"\nObjectInformation::\n{self.name}({list(self.account)})\n"

acc_obj = MyBank("Muawaz", 123456)
print(acc_obj)
acc_obj.add_account("987654")
print(acc_obj)
acc_obj.add_account("01001223")
print(acc_obj)
acc_obj.remove_account("987654")
print(acc_obj)
