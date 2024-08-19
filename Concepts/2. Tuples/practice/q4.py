# Question 4:

# Write a Python program to create a nested tuple 
# ((1, 2, 3), ("a", "b", "c"), (True, False, True)). 
# Access and print the element 'b' from the second inner tuple and 
# the element False from the third inner tuple.


tup1 = ((1, 2, 3), ("a", "b", "c"), (True, False, True))

print("Second inner tuple: ", tup1[1][1])
print("Third inner tuple : ", tup1[2][1])
