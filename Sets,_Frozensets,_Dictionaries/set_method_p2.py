# SET METHIODS PART 2 


set1 = {1, 3, 5}
set2 = {5, 7, 9}

# 1. set.intersection() # The intersection() method returns a set that contains the similarity between two or more sets.
set3 = set1.intersection(set2)
print(f'set3: {set3}')  # Output: set3: {5}
set3 = set1&set2 # can also use '&' operator to find the intersection of two sets
print(f'set3: {set3}')  # Output: set3: {5}


# 2. set.difference() # The difference() method returns a set that contains the difference between two or more sets.
set4 = set1.difference(set2)
print(f'set4: {set4}')  # Output: set4: {1, 3}
set4 = set1-set2 # can also use '-' operator to find the difference of two sets
print(f'set4: {set4}')  # Output: set4: {1, 3}

# set4 = set1.difference([1, 2, 3, 4, 5]) # can also use a list to find the difference of two sets
# set4 = set1 - [1, 2, 3, 4, 5] # ERROR: unsupported operand type(s) for -: 'set' and 'list'

# 3. set.symmetric_difference() # The symmetric_difference() method returns a set that contains all items from both sets, except items that are present in both sets.
set5 = set1.symmetric_difference(set2)
print(f'set5: {set5}')  # Output: set5: {1, 3, 7, 9}
set5 = set1^set2 # can also use '^' operator to find the symmetric difference of two sets
print(f'set5: {set5}')  # Output: set5: {1, 3, 7, 9}

# 4. set.union() # The union() method returns a set that contains all items from both sets, duplicates are excluded.
set6 = set1.union(set2)
print(f'set6: {set6}')  # Output: set6: {1, 3, 5, 7, 9}
set6 = set1|set2 # can also use '|' operator to find the union of two sets
print(f'set6: {set6}')  # Output: set6: {1, 3, 5, 7, 9}

# 5. set.isdisjoint() # The isdisjoint() method returns True if two sets have a null intersection, otherwise it returns False.
s1 = {1, 3, 5}
s2 = {5, 6, 7}
print(f's1.isdisjoint(s2): {s1.isdisjoint(s2)}')  # Output: s1.isdisjoint(s2): False
s3 = {8, 9}
print(f's1.isdisjoint(s3): {s1.isdisjoint(s3)}')  # Output: s1.isdisjoint(s3): True

# <, <=, >, >=, ==, != operators can also be used to compare sets
print({1, 3} < {1, 3, 5})  # Output: True

# These are some of the examples of SET there any many more methods available in SETS. You can check the official documentation for more information. 