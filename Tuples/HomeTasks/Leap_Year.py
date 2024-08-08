# Find Leap Year
# 6. Write a Python program that takes a year as input and 
# checks whether the year is a leap year. 
# 
# A leap year is exactly divisible by 4, except for years that are 
# exactly divisible by 100, but these centurial years are leap years 
# if they are exactly divisible by 400.

year = 1
while (True):
    year = int(input("\nEnter the 4-digit value of YEAR = "))
    num = year
    count = 0
    while(num > 0):
        num //= 10
        count += 1
    if(count != 4):
        print("\nYour input was not 4-digit value!---ENTER AGAIN\n")
    else:
        break


if((year % 100 == 0) and (year % 400 == 0)):
    print("\n===LEAP YEAR===\n")

elif((year % 4 == 0)):
    print("\n===LEAP YEAR===\n")
else:
    print("\n===NOT LEAP YEAR===\n")