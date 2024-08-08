# Question 5:
# Write a Python program that takes a list of integers as input and
# removes all the duplicates, keeping only the unique elements in the list

this_list = [1, 2, 3, 1, 4, 5, 2, 3, 6, 7, 4, 5]

unique = []

for i in this_list:
    if i not in unique:
        unique.append(i)

print(unique)