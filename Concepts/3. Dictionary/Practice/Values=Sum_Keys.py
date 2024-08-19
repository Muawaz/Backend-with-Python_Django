# Question : 1. 
# Write a Python program to create a dictionary where the keys are tuples 
# representing coordinates (x, y) and the values are the sum of x and y. 
# Use the tuples (1, 2), (3, 4), and (5, 6) as keys.


tup = ((1, 2), (3, 4), (5, 6))

dictionary = dict.fromkeys(tup)

for i in dictionary.keys():
    dictionary[i] = i[0] + i[1]

for i in dictionary.items():
    print(i)