# Frozensets are immutable sets in Python. They are similar to regular sets but cannot be modified after they are created. This means that you cannot add or remove elements from a frozenset once it has been defined.
# most commmon use case of frozensets is to use them as keys in dictionaries or as elements of other sets, since regular sets are mutable and cannot be used in these contexts.

fs1 = frozenset([1, 2, 3, 'a', 'b'])  # Creating a frozenset from a list
print (fs1, type(fs1))  # Output: frozenset({1, 2, 3, 'a', 'b'}) <class 'frozenset'>

s1 = 'BABAR is an amazing person'
fs2 = frozenset(s1)  # Creating a frozenset from a string
print (fs2)


fs3 = frozenset() 

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
fs3 = fs1.intersection(fs2)  # Intersection of two frozensets
print(fs3)  # Output: frozenset({3, 4})

s1 = {4, 10, 20}
result1 = s1.intersection(fs1)
result2 = fs1 - s1

print (f'result1 type: {type(result1)}')  # Output: result1 type: <class 'set'>
print (f'result2 type: {type(result2)}')  # Output: result2 type: <class 'frozenset'>

