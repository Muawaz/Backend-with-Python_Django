# 4. Question: 
# Write a Python program to create an empty dictionary and 
# add entries "name": "Bob", "age": 25. 
# Then, update the "age" value to 26 and print the updated dictionary.

this_dict = {}

this_dict["name"] = "Bob"
this_dict["age"] = 25

print(this_dict)

this_dict.update({"age": 26})

print(this_dict)