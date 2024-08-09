def print_alphabets():
    Z = 26
    alpha = ""
    for i in range(97, 97 + Z):
        alpha += chr(i)
        alpha += " "

    print(alpha)


# print_alphabets()