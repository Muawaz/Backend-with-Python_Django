# Question 2: Copy a File:
# Create a Python script that copies the content of a file source.txt to 
# another file called destination.txt.

reading = ''
with open("source.txt", 'r') as source:
    reading = source.read()
    print(reading)

writing = open("destination.txt", 'w')
writing.write(reading)
writing.close()




