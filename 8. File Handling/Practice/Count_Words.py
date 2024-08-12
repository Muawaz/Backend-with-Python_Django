# Question 1: Count Words in a File:
# Write a Python script that reads a file called article.txt and 
# counts the number of words in it.


file = open("article.txt", 'w')
file.write("Hello, Write!")
file.close()

file = open("article.txt", 'r')
arr = file.read()
file.close()

temp_list = list(arr.split(" "))
print(len(temp_list))