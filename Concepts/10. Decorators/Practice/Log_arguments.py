# Question 2:
# Create a decorator called log_execution that logs the arguments and then
# return value of a function. Apply it to a function that adds two numbers.

def log_execution(original_function):
    def wrapper(num1, num2):
        print(f"\nThe first argument given = {num1}")
        print(f"The second argument given = {num2}\n")
        original_function(num1, num2)
    return wrapper



@log_execution
def add_num(input1, input2):
    print(f"The sum of the given numbers = {input1 + input2}")

add_num(10, 14)