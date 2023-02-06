"""
 Write  python program to perform following operations on tuples:
a) Create Set
b) Access Set elements
c) Update Set
d) Delete Set
"""
#a)Creating a Set

set1 = {1,2,3,4,5,6,7}

#b)Accessing Set Elements

for x in set1:
  print(x)

#c)Updating Set

set1.add(8)
print(set1)

#d)Deleting a Set

del set1
print(set1) # Throws an Error