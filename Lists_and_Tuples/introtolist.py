# Python Lists 
print("#" * 10 + " Simple list with List slicing example " + "#" * 10) # print a separator line
L1 = [1, 2.5, "python", True, ["abc", 123], (10, 20, 30)]
print (len(L1)) # length of the list
print (L1[0]) # access first element
print (L1[2]) # access third element
print (L1[4]) # access fifth element
print (L1[4][0]) # access first element of the fifth element (which is a list)
print (L1[5][1]) # access second element of the sixth element (which is a tuple)
print (L1[-1]) # access last element
print (L1[-2]) # access second last element
print (L1[1:4]) # access elements from index 1 to 3
print (L1[:3]) # access first three elements
print (L1[3:]) # access elements from index 3 to the end
print (L1[::2]) # access every second element
print (L1[::-1]) # access elements in reverse order 
L1[0:2] = [100, "B"] # modify the first two elements of the list
print (L1) # print the modified list
L1[0:2] = [100, "D", 3.5] # modify the first two elements of the list with a new list of different length
print (L1) # print the modified list

print ("##############################################")
L2 = [] # create an empty list
L3 = list() # create an empty list using the list() constructor
print (L2) # print the empty list
print (L3) # print the empty list
print ("##############################################")
L4 = list("abcd") # create a list using the list() constructor
print (L4) # print the list
print (id(L4)) # print the memory address of the list
L4[0] = "x" # change the first element of the list
L4.append("100") # add a new element to the end of the list
print (L4) # print the modified list
print (id(L4)) # print the memory address of the modified list (should be the same as before)

