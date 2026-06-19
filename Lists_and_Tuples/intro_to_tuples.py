# PYTHON TUPLES
# main difference between lists and tuples is that tuples are immutable, they can not be changed.
# Tuples are faster and more efficient then Lists. 
# Tuples are Safer than Lists.
# Tuples can be used as keys in dictionaries. 
# Storage effeciency. 

t1 = tuple()
t2 = ()
print(type(t1), type(t2)) # <class 'tuple'> <class 'tuple'>

t3 = (1, 3.4, 'Hello', True)
print(t3)
# we can not change the value of a tuple, but we can concatenate two tuples together to create a new tuple.

t4 = (10) # this is not a tuple, it is an integer
print(type(t4)) # <class 'int'>

t5 = (10,) # this is a tuple with one element
print(type(t5)) # <class 'tuple'>

t6 = 6.9, True, 'World', 10 # this is also a tuple, we can omit the parentheses
print(type(t6))

t7 = tuple([1, 2, 3, 4])
t8 = tuple ('hello')
print(type(t7), type(t8))

l1 = list(t6)
print(l1)

print(t6[0])
# t6[0] = 'X' # this will create error because the TUPLES are immutable