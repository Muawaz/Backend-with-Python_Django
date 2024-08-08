this_list = list(("apple", "banana", 123))
print(this_list)

this_list = [1, 2, 3, 1, 4, 5, 2, 3, 6, 7, 4, 5]

unique = []

# for i in this_list:
#     if i not in unique:
#         unique.append(i)

# print(unique)

print(this_list)
index = len(this_list) - 1
i = 0
j = 0
while i < index:
    j = 0
    while j < index:
        if (this_list[j] == this_list[i]) & (j != i):
                print(this_list[j])
            #     this_list.remove(j)
            #     index-=1
        j+=1
    i+=1

print(this_list)



# for i in this_list:
#     for j in this_list:
#         if j == i & (this_list.index(j) != this_list.index(i)):
#             this_list.remove(j)


# print(this_list)
