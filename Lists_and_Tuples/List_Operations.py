# List Concatenation

L1 = [1, 2, 3]
print (L1, id(L1)) # print the list and its memory address
L1 = L1 + [4, 5] # concatenate the list with another list
print (L1, id(L1)) # print the modified list and its memory address (should be different from before)
###############################################
L1 += [6, 7] # concatenate the list with another list using the += operator
print (L1, id(L1)) # print the modified list and its memory address (should be the same as before)  
L1.extend([8, 9]) # extend the list with another list
print (L1, id(L1)) # print the modified list and its memory address (should be the same as before)
###############################################

# append VS extend

L1.append(["a", "b"]) # append a list to the end of the list
print (L1) # print the modified list
L1.extend(["c", "d"]) # extend the list with another list
print (L1) # print the modified list    
L1.append(20) # append an integer to the end of the list
L1.extend([20]) # extend the list with a list containing an integer
print (L1) # print the modified list
# L1.extend(20) # extend the list with an integer (should raise an error)


# Repitition of Lists
L2 = list("abc") # create a list using the list() constructor
L3 = L2 * 3 # repeat the list three times
print (L3) # print the repeated list

# List Iteration

print ("#" * 10 + " List Iteration example " + "#" * 10) # print a separator line
L4 = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "10.0.0.1"] # create a list
for i in L4: # iterate over the list using a for loop
    print (f'connecting to {i} ...') # print each element of the list

print ("192.168" in L4) # check if an element is in the list (should return True)
print ("10.0.0.2" in L4) # check if an element is in the list (should return False)
print ("192" not in L4) # check if an element is not in the list (should return True)


