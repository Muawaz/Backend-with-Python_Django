# Tables Generator
# 7. Write a Python program that takes a number as input and 
# prints its multiplication table up to 10.

num = int(input("\nEnter the number to print table upto 10 = "))

for i in range(11):
    print(num, " * ", i, " = ", num*i)