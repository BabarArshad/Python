# DICTIONARY OPERATIONS AND METHODS

person = {'name': 'John', 'age': 30, 'location': 'USA'}

friend = person 

# Modifying the friend's dictionary will also affect the original person dictionary
friend['age'] = 25

print(person)  # Output: {'name': 'John', 'age': 25, 'location': 'USA'}
print(friend)  # Output: {'name': 'John', 'age': 25, 'location': 'USA'}

# To create a copy of the dictionary, you can use the copy() method
neighbor = person.copy()
person['location'] = 'Europe'
print(neighbor, person)  # Output: {'name': 'John', 'age': 25, 'location': 'USA'} {'name': 'John', 'age': 25, 'location': 'Europe'}

# To update a dictionary with another dictionary, you can use the update() method
countries = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}
countries.update({'Germany': 'Berlin', 'India': 'New Delhi'})
print(countries)  # Output: {'USA': 'Washington, D.C.', 'France: 'Paris', 'Japan': 'Tokyo', 'Germany': 'Berlin', 'India': 'New Delhi'}      

person.clear()  # Removes all items from the dictionary
print(person, friend)


# PART 2 

# dict.key() - Returns a view object that displays a list of all the keys in the dictionary
person = {'name': 'Alice', 'age': 28, 'city': 'New York'}

k = person.keys()
print(k)  # Output: dict_keys(['name', 'age', 'city'])
print(type(k))  # Output: <class 'dict_keys'>
my_keys = list(k)
print(my_keys)  # Output: ['name', 'age', 'city']

# dict.values() - Returns a view object that displays a list of all the values in the dictionary
print(person.values())  # Output: dict_values(['Alice', 28, 'New York']
print(list(person.values()))  # Output: ['Alice', 28, 'New York']

# dict.items() - Returns a view object that displays a list of dictionary's key-value tuple pairs
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 28), ('city', 'New York')])

print('name' in person)  # Output: True
print(10 in person.keys())  # Output: False
print('New York' in person.values())  # Output: True
print(('age', 28) in person.items())  # Output: True

d1 = {10: 'a', 20: 'b', 30: 'c'}
v = d1.values()
d1[10] = 'x'
print(v)  # Output: dict_values(['x', 'b', 'c']) # this is because the view object reflects the current state of the dictionary, so when we change the value associated with key 10, it updates the view object as well.

d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'}
k1 = d1.keys()
k2 = d2.keys()
print(k1, k2)  # Output: dict_keys([10, 20]) dict_keys([20, 30]) # The keys view objects are separate and do not affect each other, so modifying one dictionary does not change the keys view of the other dictionary.

print (k1 & k2)  # Output: {20} # This will give us the common keys between the two dictionaries, which is 20 in this case.
print (k1 | k2)  # Output: {10, 20, 30} # This will give us the union of keys from both dictionaries, which includes all unique keys from both dictionaries.    

for k in person.keys():
    print(f'Key is {k}')  # Output: Key is name, Key is age, Key is city

for v in person.values():
    print(f'Value is {v}')  # Output: Value is Alice, Value is 28, Value is New York

for k in person.keys():
    print(f'Key is {k} and the value is {person[k]}')  # Output: Key is name and the value is Alice, Key is age and the value is 28, Key is city and the value is New York  

for k, v in person.items():
    print(f'Key is {k} and the value is {v}')  # Output: Key is name and the value is Alice, Key is age and the value is 28, Key is city and the value is New York  


    

