# 1. 
# Given a list of tuples where each tuple contains a name and an age. 
# Use a lambda function to sort the list by age in ascending order.
# people = [("John", 25), ("Anna", 22), ("Mike", 30), ("Sophia", 27)]
# output:
# [('Anna', 22), ('John', 25), ('Sophia', 27), ('Mike', 30)]


people = [("John", 25), ("Anna", 22), ("Mike", 30), ("Sophia", 27)]
sorted_people = sorted(people, key=lambda age: age[1])
print(sorted_people)
