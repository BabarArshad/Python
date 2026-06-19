# Identity Operators:
# is - Returns True if both variables are the same object
# is not - Returns True if both variables are not the same object

x = 5
y = 5
z = [5]

print(x is y)  # Output: True
print(x is not y)  # Output: False
print(x is z)  # Output: False

# Mutable: Lists, Dictionaries, Sets
# Immutable: Integers, Floats, Strings, Tuples  
# Mutable: values can be changed 
# Immutable: values cannot be changed

print(id(x))  # Output: 140712345678912 (example ID)
print(id(y))  # Output: 140712345678912 (same ID as x)
print(id(z))  # Output: 140712345678944 (different ID)

# Mutable example
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))  # Output: 140712345678976 (example ID)
print(id(list2))  # Output: 140712345678976 (same ID as list1)
print(list1 is list2)  # Output: True
list1.append(100)
print(list1)  # Output: [1, 2, 3, 100]
print(id(list1))  # Output: 140712345678976 (same ID as before  because list1 is mutable

number = list1.copy() # creates a copy of list1
print(id(number))  # Output: 140712345679008 (different ID from list1)
print(number == list1) # Output: True
print(number is list1) #  but the identity operator returned false because they are saved at different addresses.

# Immutable example
str1 = "Hello"
str2 = "Hello"
str3 = "Hello1"
print(id(str1))  # Output: 140712345678912 (example ID)
print(id(str2))  # Output: 140712345678912 (same ID as str1)
print(str1 is str2)  # Output: True     
print(str1 is not str3)  # Output: True



