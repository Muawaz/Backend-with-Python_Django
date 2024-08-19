# Question 1: 
# Write a decorator called time_it that measures the execution time of a function.
# Apply it to a function that calculates the factorial of a number.

from datetime import datetime
import time

def time_it(original_function):
    def wrapper(n):
        start_time = datetime.now()
        # start_time = time.time()
        original_function(n)
        end_time = datetime.now()
        # end_time = time.time()

        print("Start_time = ", str(start_time).split(" ")[1])
        print("End_time = ", str(end_time).split(" ")[1])

        print("time = ", end_time - start_time)
    return wrapper

@time_it
def factorial(n):
    time.sleep(2)
    fact = 1
    for num in range(1, n+1):
        fact *= num

    print(f"Factorial of {n} = {fact} \n")
    # return fact

factorial(10)
