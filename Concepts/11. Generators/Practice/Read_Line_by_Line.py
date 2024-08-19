# Question 3:
# Write a generator function called read_large_file that reads a large file
# line by line without loading the entire file into memory.

def gen_read_large_file(file):
    with open(file, 'r') as source:
        for line in source:
            yield line.rstrip()


read_list = gen_read_large_file("sample.txt")
for i in read_list:
    print(i)
    print("\n\n")