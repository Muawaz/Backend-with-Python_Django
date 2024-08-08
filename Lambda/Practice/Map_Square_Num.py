# 3. 
# Use a lambda function inside the map function to square each number 
# in a given list of integers

my_list = [0,1,2,3,4,5,6,8,9,10]
squared_list = map((lambda x: x*x), my_list)

print(list(squared_list))
