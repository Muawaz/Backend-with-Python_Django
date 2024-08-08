# 2. 
# Write a Python program that uses a lambda function 
# within the filter function to filter out all even numbers from a list.

my_list = [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]

even_list = (filter((lambda x: True if x%2==0 else False), my_list))

print(list(even_list))