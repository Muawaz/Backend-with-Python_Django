# 5. Question: 
# Given a list of tuples where each tuple contains 
# a person's name and their age: people = 
# [("John", 25), ("Jane", 30), ("Alice", 25), ("Bob", 30)]
# Write a Python program to group these people by their age into a dictionary 
# where each key is an age and each value is a list of names of people with that age.
# Answer:
# {25: ['John', 'Alice'], 30: ['Jane', 'Bob']}

my_list = [("John", 25), ("Jane", 30), ("Alice", 25), ("Bob", 30)]
my_tuple = tuple(my_list)
my_dictionary = {}

for i in my_tuple:
    if(i[1] in my_dictionary.keys()):
        this_list = list(my_dictionary[i[1]])
        this_list.append(i[0])
        my_dictionary[i[1]] = this_list
    else:
        my_dictionary[i[1]] = [i[0]]

for i in my_dictionary.items():
    print(i)