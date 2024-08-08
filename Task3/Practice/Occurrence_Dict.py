# 2. Question: 
# Write a Python program to count the number of occurrences of each element 
# in a tuple (1, 2, 2, 3, 3, 3, 4, 4, 4, 4) and print the result as a dictionary


tup = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

# for i in tup:
#     print(i)

# this_dict = {
#     x : x for x in set(tup)
# }

# for i in this_dict.items():
#     print(i)

this_dict = dict.fromkeys(tup, 0)
# print(this_dict)

for i in tup:
    if(i in this_dict):
        this_dict[i] += 1

for i in this_dict.items():
    print(i)