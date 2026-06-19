# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Key is usually imutable like string, number or tuple. But value can be of any type and can be duplicated. However, the value can be a list, a tuple, another dictionary or any other data type.


Person = { 'Name': 'John', 'Age': 30, 'City': 'New York' }
print(type(Person))  # Output: <class 'dict'>
print(Person)  # Output: {'Name': 'John', 'Age': 30, 'City': 'New York'}
# d1 = dict(Name='John', Age=30, City='New York') # example of creating a dictionary using the dict() constructor
# d2 = {} # example of creating an empty dictionary using curly braces, However, since SETS are also created using curly braces, it is recommended to use the dict() constructor to create an empty dictionary.


