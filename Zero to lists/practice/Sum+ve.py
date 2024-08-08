# Question 4: 
# Write a Python program that takes a list of integers as input and 
# finds the sum of all the positive numbers in the list.

sum = 0
num = list(map(int, input("Enter numbers seperated by space : ").split()))

if(len(num) == 0):
    print("List is empty")
else:
    i = 0
    while i < len(num):
        if(num[i] > 0):
            sum += num[i]
        i += 1

print("\nThe sum of all the positive numbers in the list = ", sum, "\n")

