# x = 23425
# temp_arr = 0;
# temp2 = x


# while (temp2 > 0):
#     temp_arr *= 10
#     temp_arr += temp2 % 10
#     temp2 //= 10
    
# print(temp_arr)


num = int(input("Enter the number : "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(reverse)
