# Question 1: 
# Write a generator function called even_numbers that yields even numbers
# starting from 0 up to a given number n.

def gen_even_numbers(num):
    for index in range(num+1):
        if index % 2 == 0:
            yield index


even_list = gen_even_numbers(20)
print("\n")
print(list(even_list))