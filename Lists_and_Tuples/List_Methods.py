# # LIST METHODS 

# L1 = list() # create an empty list using the list() constructor
# # print(dir(L1)) # print the list of methods available for the list object
# #help(L1.append) # print the documentation for the append() method of the list object

# # Adding to the the list: Append(), Extend() and Insert()
# L1 = [1, 2.2, "three"] # create a list with different types of elements
# #1. Append() method
# L1.append(4) # append an integer to the end of the list
# print (L1) # print the modified list
# # L1.append(5, 6) # ERROR 
# L1.append([5, 6]) # append a list to the end of the list
# print (L1) # print the modified list

# #2. Extend() method
# L1.extend([7, 8]) # extend the list with another list
# print (L1) # print the modified list
# L1.extend("nine") # extend the list with a string (each character will be added as a separate element)
# print (L1) # print the modified list

# #3. Insert() method
# Years = [2020, 2022, 2023] # create a list of years
# Years.insert(1, 2021) # insert an element at a specific index (1)
# Years.insert(len(Years), 2024) # insert an element at the end of the list using the length of the list as the index
# print (Years) # print the modified list
# Years.insert(-1, 2025) # insert an element at the end of the list using a negative index
# print (Years) # print the modified list


# #4. List.clear() method
# Years.clear() # clear all elements from the list
# print (Years) # print the modified list (should be empty)

# #5. List.pop() method
# L2 = [1, 2, 3, 4, 5] # create a list of integers
# x = L2.pop() # remove and return the last element of the list
# print (x) # print the removed element
# print (L2) # print the modified list
# y = L2.pop(1) # remove and return the element at index 1
# print (y, L2) # print the removed element and the modified list
# # L2.pop(100) # ERROR: index out of range


# #6. List.remove() method
# L3 = [10, 20, 30, 40, 50, 20, 20, "Z"] # create a list with duplicate elements and a string
# L3.remove(20) # remove the first occurrence of the element 20 from the list 
# print (L3) # print the modified list

# while 20 in L3: # remove all occurrences of the element 20 from the list using a while loop
#     L3.remove(20)
# print(L3) # print the modified list (should not contain any 20s)

print("#" * 10 + " LIST METHODS - PART 2 " + "#" * 10) # print a separator line

# 7. List.index() method
names = ["Alice", "Bob", "Charlie", "David", "Eve"] # create a list of names
print (names.index("Charlie")) # find the index of the first occurrence of the element "Charlie" in the list (should return 2)
i = names.index("Bob") # find the index of the first occurrence of the element "Bob" in the list
print (f"Index of Bob: {i}" ) # print the index of "Bob"

#8. List.count() method
L4 = [1, 2, 3, 2, 4, 2, 5] # create a list with duplicate elements
N = L4.count(2) # count the number of occurrences of the element 2 in the list
print (f"Number of occurrences of 2: {N}") # print the count of the element 2 in the list   
print(2 in L4) # check if the integer 2 is in the list (should return True)

#9. List.reverse() method
L5 = [1, 3, "abc", 5.5] # create a list with different types of elements
L5.reverse() # reverse the order of the elements in the list
print(f'L5: {L5}') # print the modified list


# 10. List.sort() method
ages = [25, 30, 20, 35, 28] # create a list of ages
la = sorted(ages) # sort the list using the sorted() function (returns a new sorted list)
print (la, ages) # print the sorted list and the original list (should be unchanged)

n = ages.sort() # sort the list in place using the sort() method (modifies the original list)
print (n)
print (ages) # print the modified list (should be sorted)
ages.sort(reverse=True) # sort the list in reverse order using the sort() method with the reverse parameter
print (ages) # print the modified list (should be sorted in reverse order)

# Max() and Min() functions

L2 = [-10, 20, 5, 15, 30] # create a list of integers
print(f'Maximum value in L2: {max(L2)}') # find the maximum value in the list using the max() function
print(f'Minimum value in L2: {min(L2)}') # find the minimum value in the list using the min() function
print(f'sum of values in L2: {sum(L2)}') # find the sum of the values in the list using the sum() function

