# SET METHODS

set1 = {1,2,3}
set2 = {3,2,1}
print(set1 == set2) # True
print(set1 is set2) # False

# However, that's not the applicable to list, str and tuple
# for example, if we have a list
print([1,2,3] == [3,2,1] ) 

# 1. set.add(item)
s1 = {1,2,3}
s1.add('a')
s1.add(4.5)
print(s1)
s1.add(1) # it does nothing because 1 is already in the set
print(s1)


# 2. set.remove(item)
s1.remove(3) 
print(s1)
# s1.remove(3) # ERROR becasue 3 is not in the set

# 3. set.discard(item)
s1.discard('a')
print(s1)
s1.discard('X') # it does nothing because X is not in the set
print(s1)

#4. set.pop()
x = s1.pop()
print(x, s1) 

s2 = set('abc')
s3 = s2 
s3.add('x')
print(s2) 

# 5. set.clear()
s3.clear()
print(f's2: {s2}, s3: {s3}')

# 6. set.copy()
s4 = s1.copy()
print(f's1: {s1}, s4: {s4}')
