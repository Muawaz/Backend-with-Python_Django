# Question 2:
# Create a generator function called fibonacci that yields the Fibonacci sequence
# up to a certain number of terms.
# example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,


def gen_fibonacci(terms):
    last_term = 1
    second_last_term = 0
    counter = 2

    yield second_last_term
    yield last_term
    
    while (counter <= terms):
        next_term = second_last_term + last_term
        yield next_term
        second_last_term = last_term
        last_term = next_term
        counter += 1

fibonacci_list =  gen_fibonacci(9)
print(list(fibonacci_list))
    
