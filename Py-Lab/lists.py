# Here,we'll learn about lists and its various functions in Py
names = ['Rohit', 'Sourav', 'Akash', 'Vivek', 'Ayush']
print(names)  # Prints exactly int he list form

# Accessing index-element in list
print(names[0], ",", names[-4], ",", names[0:2], "|", names[2:])
# Modifying elements according to Index
names[3] = 'Kundan'
print(names[0:5])


# Probie-----------------------------------------------------------------
# Find largest number in list
nums = [1, 5, 0, 6, 3, 14]
maxI = nums[0]
for num in nums:
    if num > maxI:
        maxI = num
print(f"The largest no. in the list is: {maxI}")


# 2-D_LIST_____________________________
# [ 123
#   345
#   903 ] 3x3
appy = [
    [1, 2, 3],
    [5, 9, 14],
    [24, 28, 26]
]
# Accessing individual items in 2-D list
print(appy[1][0])
appy[2][1] = 19
print(appy[2][1])

for row in appy:
    for item in row:
        print(item, end=" ")
    print()
# -----------------------------------------------------


# List-Methods__________________________________________
feasty = [5, 9, 36, 14]
feasty.append(19)
print(feasty)

feasty.insert(1, 45)  # Index & val
print(feasty)

feasty.remove(9)
print(feasty)

# feasty.clear() - returns empty list
feasty.pop()
print(feasty)  # Pops out last el

print(feasty.index(14))  # Returns index of given el
# print(feasty.index(264))  # IOB condition

print(19 in feasty)  # Bool val for checking
print(feasty.count(14))  # Counting the els in list

# Sorting the list
feasty.sort()
print(feasty)

# Reversing the list
feasty.reverse()
print(feasty)

# Cpoying the lsit
kulfi = feasty.copy()
feasty.append(264)
print(kulfi, "\n", feasty)


# Probie----------------------------------------------------
# Remove duplicates in list
quyi = [1, 2, 9, 2, 0, 1, 0, 5]
res = []
for i in quyi:
    if i not in res:
        res.append(quyi)
print(res)
