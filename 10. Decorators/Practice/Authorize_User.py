# Question 3:
# Write a decorator called requires_auth that checks if a user is authorized before
# running a function.
# If the user is not authorized, print "Unauthorized access!" and 
# do not run the function.
# Use this decorator on a function that displays sensitive information.

def required_auth(original_function):
    def wrapper(access_arg):
        original_function(access_arg)
        if(access_arg[0] == True):
            password = "12348765"
            print(f"The password for this Personal Computer = {password}")
        else:
            print ("Unauthorized access!")
    return wrapper

@required_auth
def check_auth(access):
    password = int(input("Enter the PassCode = "))

    if(password == 1234):
        access[0] = True
    else:
        access[0] = False
    return access

access = [False]


check_auth(access)