# Find Largest Number
# 5. Write a Python program that takes a list of numbers as input 
# and finds the largest number in the list.

input_list = list(map(int, input("\nEnter the number seperated by space = ").split()))

max = input_list[0]
for i in input_list:
    if(i > max):
        max = i

print("\nThe largest number from the given input list = ", max, "\n")