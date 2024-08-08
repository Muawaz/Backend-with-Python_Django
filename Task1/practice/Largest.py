# Question 3: 
# Write a Python program that takes a list of numbers as input and 
# finds the largest number using a while loop.


max = 0
num = list(map(int, input("Enter numbers seperated by space : ").split()))

if(len(num) == 0):
    print("List is empty")
else:
    i = 0
    while i < len(num):
        if(num[i] > max):
            max = num[i]
        i += 1

print("\nThe largest number from input list = ", max, "\n")
