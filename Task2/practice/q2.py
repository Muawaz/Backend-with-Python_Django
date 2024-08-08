# Question 2: Tuple Sticing

# Write a Python program to create a tuple with elements 
# (5, 10, 15, 20, 25, 30, 35, 40) Slice the tuple to get a new tuple 
#  with elements from Index 2 to Index 5 (inclusive).

tup = tuple((5, 10, 15, 20, 25, 30, 35, 40))

tup2 = tup[1:5]

print("Tuple : ", tup)
print("new tuple : ", tup2)