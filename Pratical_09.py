"""
Write python program to perform following operations on
Dictionaries:
a) Create Dictionary
b) Access Dictionary elements
c) Update Dictionary
d) Delete Set
e) Looping through Dictionary


"""
#a) Create Dictionary
my_dict = {'name': 'Adnan Qureshi', 'age': 19, 'gender': 'Male', 'Nationality':'Indian'}

#b) Access Dictionary elements

print(my_dict)

#c) Update Dictionary

my_dict['age'] = 21
print(my_dict['age'])

#d) Delete Set
# Deleting element from Dictionary
del my_dict['age']

#e) Looping through Dictionary
for key in my_dict:
    print("Looping statement: ",key, my_dict[key])