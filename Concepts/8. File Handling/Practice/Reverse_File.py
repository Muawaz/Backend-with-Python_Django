# Question 4: Reverse the Content:
# Write a Python script that reads a file called poem.txt and writes its content
# in reverse order to a new file called reversed_poem.txt

import re

reading = ''
with open("poem.txt", 'r') as source:
    reading = source.read()

# rev_read = reading[::-1]

read_list = re.split(',|\n| ', reading)
print(read_list)

rev_read = ""
list_sentence = []
for line in read_list:
    if(line == ''):
        rev_read += str(list_sentence)
        rev_read += "\n"
        list_sentence = []
    else:
        list_sentence.insert(0, line)

print(rev_read)
    

writing = open("reversed_poem.txt", 'w')
writing.write(rev_read)
writing.close()