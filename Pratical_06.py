"""
Write python program to perform following operations on Lists:
a) Create list
b) Access list
c) Update list (Add item, Remove item)
d) Delete list

"""

# a) Create list
list1 = ["banana ", "Chiku", "WaterMelon", "Pineapple", "Stawberry"]

# b) Access list
print(list1)

# c) Update list
list1.append("apple")  # Add item
print(list1)
list1.remove("apple")  # Remove item
print(list1)
# d) Delete list
del list1
"""Here the list is deleted if you want to verify , type 'print(list1)' , this will give an error named as "NameError: 
 name 'list1' is not defined. Did you mean: 'list'?"
"""
