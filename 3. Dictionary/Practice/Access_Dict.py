# 3. Question: 
# Write a Python program to create a dictionary with keys 
# "name", "age", and "city", and corresponding values 
# "Alice", 30, and "New York". 
# Access and print the value associated with the key "city"

this_dict = {
    "name" : "Alice",
    "age" : 30,
    "city" : ("Germany", "France")
}

if("city" in this_dict):
    my_list = list(this_dict["city"])

my_list[0] = "Bangladesh"
print(my_list)

if("city" in this_dict):
    this_dict["city"] = tuple(my_list)

print(this_dict)