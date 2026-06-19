# PYTHON SETS 

s1 = {1,2,3,'a','b', 4, 5, 6}
print(s1)# we notice on every print the set is unordered

# print(s1[0]) # ERROR set are immutable

# SETS ARE Mutable
s1.add((1,2,3))
print(s1) 

s1.remove('a')
print(s1)

l1 = [1, 2] 
# s1.add(l1) # TypeError: cannot use 'list' as a set element (unhashable type: 'list')

s2 = set()
s3 = {} # this is not a set, it is a dictionary
print(type(s2))
print(type(s3))


# str => set
s4 = set('helooooooo') # you will notice the identical letters are not repeated
print(s4)

# tuple => set
s5 = set((1,2,3,4,5,6,7,8,9,10))
print(s5)

# list => set
s6 = set((1,2,3,4,'abr'))
print(s6)

# lets do a small exercise to remove duplicate mac addresses, we have a list with some duplicate mac addresses. 
macs = ['00:0a:95:9d:68:16', '00:0a:95:9d:68:16', '00:0a:95:9d:68:16', '00:0a:95:9d:68:30']
macs_addresses  = set(macs)
print(macs_addresses)

print (len(macs_addresses)) # we can use len buit in function with ses too. 

# if you need a list and not a set, call the list constructor with a set as an argument
macs = ['00:0a:95:9d:68:16', '00:0a:95:9d:68:16', '00:0a:95:9d:68:16', '00:0a:95:9d:68:30']
macs_addresses  = list (set(macs))
print(macs_addresses)

for item in s4:
    print(item)


print('x' in s4) # to see if an item is in a set, we see false because X is not in the set

