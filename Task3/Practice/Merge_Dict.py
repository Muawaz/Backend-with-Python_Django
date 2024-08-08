# 6. Merge Dictionaries with Custom Logic Question: 
# Given two dictionaries:
# dict1 = ('a': 10, 'b': 20}
# dict2 = {'b': 30, 'c': 40}
# Merge these dictionaries such that if a key exists in both dictionaries, 
# the value in the merged dictionary is the sum of the values from both dictionaries. 
# Print the resulting dictionary.

import itertools

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40, 'd': 50}

# merg_dict = {}

# for (i, j) in itertools.zip_longest(dict1.keys(), dict2.items()):
#     print("i", i)
#     print("j", j)
#     if(i[0] in merg_dict.keys()):
#         merg_dict[i[0]] += dict1[i[1]]
#         print("i")
#     if(j[0] in merg_dict.keys()):
#         merg_dict[j[0]] += dict2[j[1]]
#         print("j")
#     if(i in merg_dict and j in merg_dict):
#         print("hello")
#         merg_dict[i] = dict1[i] + dict2[j]

# print(merg_dict)

merg_dict = dict2.copy()

for name, age in dict1.items():
    if(name in merg_dict):
        merg_dict[name] += age
    else:
        merg_dict[name] = age

print(merg_dict)