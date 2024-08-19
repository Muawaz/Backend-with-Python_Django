# Check Prime Number or Not
# 9. Write a Python program that takes a number as input and 
# checks whether the number is a prime number. 
# A prime number is a number greater than 1 that has no positive divisors 
# other than 1 and itself

num = int(input("Enter the number to check for = "))
count = 0
for i in range(num + 1):
    if(i != 0 and num % i == 0):
        count += 1

if(count == 2):
    print("\n===PRIME===\n")
else:
    print("\n==NOT PRIME===\n")