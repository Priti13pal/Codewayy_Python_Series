# Methods of List in Python : 

# Python list methods
My_List = [6, 2, 4, 6, 1, 3, 7]

print(My_List)

# Output: 0
print(My_List.index(6))

My_List.append(8)

# Output : [6, 2, 4, 6, 1, 3, 7, 8]
print(My_List)


# Output: 2
print(My_List.count(6))

My_List.sort()

# Output: [1, 2, 3, 4, 6, 6, 7, 8]
print(My_List)

My_List.reverse()

# Output: [8, 7, 6, 6, 4, 3, 2, 1]
print(My_List)

My_List.remove(6)

#output: [8, 7, 6, 4, 3, 2, 1]
print(My_List)


My_List.clear()
print(My_List)

