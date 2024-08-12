# Question 1:
# You are tasked with writing a Python program that reads Integers from a list and
# divides a constant number by each or these integers. 

# The program should handle the following exceptions:
#     ZeroDivisionError: Occurs when attempting to divide by zero.
#     ValueError: Occurs when a value in the list is not an integer.
#     TypeError: Occurs when the input list contains a type other than an integer
#                 or float.

# Write a function called safe_division that takes a list of numbers as input. 
# The function should attempt to divide a constant number, say 100, by each number
# in the list. For each exception, the function should print an appropriate error
# message and continue processing the remaining numbers.
#     Example:
#         my_List = [25, 0, 'a', 5, 2.5, None]
#         Expected_Output:
#         100/25 = 4.0
#         Cannot divide by zero. Skipping value: 0
#         Invalid type: a. It must be a number.
#         100/5 = 20.0
#         100/2.5 = 40.0
#         Invalid type: None. It must be a number

import math


def safe_division (input_list):
    const = 25
    for index in input_list:
        try:
            print(const,"/", int(index), " = ", const / int(index))
        except ZeroDivisionError:
            print("Cannot divide by zero. Skipping value: 0")
        except TypeError:
            print (f"Invalid type: '{index}'. It must be a number.")
        except ValueError:
            print(f"Invalid Value: '{index}'. Expected int/float value for division")

my_List = [25, 0, 'a', 5, 2.5, None]
safe_division(my_List)

