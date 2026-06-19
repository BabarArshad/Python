# Python List Gotchas
#1
L1 = [1, 2, 3]
L2 = L1  # This creates a reference to the same list, not a copy
L2[0] = 10  # Modifying L2 will also modify L1
L2.append(4)  # This will also affect L1
print(f"L2: {L2}")  # Output: L2: [10, 2, 3, 4]
print(f"L1: {L1}")  # Output: L1: [10, 2, 3, 4]
print(id(L1))  # Output: Memory address of L1
print(id(L2))  # Output: Memory address of L2 (same as L1)
L1.remove(2)  # This will also affect L2
print(f"L2: {L2}")  # Output: L2: [10, 3, 4]

L3 = L1.copy()  # This creates a shallow copy of the list
L3.append(5)  # Modifying L3 will not affect L1
print(f"L3: {L3}")  # Output: L3: [10, 3, 4, 5]
print(f"L1: {L1}")  # Output: L1: [10, 3, 4]
print(id(L3))  # Output: Memory address of L3 (different from L1)       

#2

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 7, 9]
#imaging we need to remove all the numbers below 5 from the list. 
#This is wrong!! 

for n in nums:
    if n < 5:
        nums.remove(n)  # Modifying the list while iterating can lead to unexpected behavior

print(nums)  # Output may not be as expected due to the modification during iteration

# The correct way to remove items from a list while iterating is to create a new list or use a list comprehension:

new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)
print(new_list)  # Output: [5, 6, 7, 8, 9, 10, 7, 9]

# Using a list comprehension to create a new list with only the desired elements
filtered_nums = [n for n in nums if n >= 5]
print(filtered_nums)




