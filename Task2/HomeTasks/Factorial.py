# Find Factorial
# 4. Write a Python program that takes a non-negative integer as input 
# and calculates its factorial. 
# The factorial of a number.n is the product of all positive integers 
# less than or equal to n

num = -1

while (num <= 0):
    num = int(input("\nEnter any positive number = "))
    if(num <=0 ):
        print("\nYour given number was non positve\nENTER AGAIN")

fact = 1
while (num > 0):
    fact *= num
    num -= 1

print("\nThe Factorial of the given positve number = ", fact, "\n")