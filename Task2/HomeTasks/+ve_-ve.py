# Check Number Positive or Negative
# 2. Write a Python program that takes a number as input 
# and checks whether the number is positive, negative, or zero.


num = float(input("Enter the number = "))

if(num == 0):
    print("\nThe given number is ZERO\n")
elif(num > 0):
    print("\nThe given number is POSITIVE\n")
else:
    print("\nThe given number is NEGATIVE\n")