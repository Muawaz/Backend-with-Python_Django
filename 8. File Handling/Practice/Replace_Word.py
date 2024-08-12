# Question 3: Find and Replace:
# Write a Python script that opens a file called notes.txt, 
# finds all occurrences of a specific word (e.g., "old") and 
# replaces it with another word (e.g., "new"). 
# Save the result in a new file called updated_notes.txt.

reading = ''
with open("notes.txt", 'r') as source:
    reading = source.read()
    # print(reading)

# reading = reading.split(" ", ",", ".")
reading = reading.replace('old', 'new')
reading = reading.replace('Old', 'New')

print(reading)

file = open("updated_notes.txt", 'w')
file.write(reading)
file.close()