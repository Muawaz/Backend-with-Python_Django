# Question 2: 
# Write a Python program that calculates the sum of all the numbers from 1 to 100 
# using a for loop.

sum = 0
end_point = 100

for i in range(end_point + 1):
    sum += i

print("\nSum of number between 1 to 100 = ", sum, "\n")