# Check Palindrome
# 8. Write a Python program that takes a string as input and 
# checks whether the string is a palindrome.
# A palindrome is a string that reads the same forwards and backwards.

pali = input("\nEnter the string to check Palindrom = ")

pali_rev = pali[::-1]

if(pali == pali_rev):
    print("Palindrom")
else:
    print("Not Palindrom")