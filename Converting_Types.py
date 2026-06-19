# # Converting Types
# # Lets make a sinple code to convert miles into kilometers. 
# # 1 mile = 1.60934 kilometers
# miles = input("Enter distance in miles: ")
# # print(type(miles))  # This will be a string

# # since its not permitted to multiply strings, we need to convert it to a number (float or int)
# miles = float(miles)  # Convert the string input to a float
# Km = miles * 1.60934 
# print("Total distance in kilometers:", Km)
# # Alternatively, we can do the conversion in one line without storing the miles variable
# # Km = float(input("Enter distance in miles: ")) * 1.60934
# # print("Total distance in kilometers:", Km)


a = 10 # This is an integer
b = 3.1 # This is a float
C = "5" # This is a string 

# lets convert int to float
a_float = float(a) # This will convert the integer 10 to a float 10.0
print("a:", type(a)) # Output: a: <class 'int'>
print("a_float:", type(a_float)) # Output: a_float: <class 'float'>

# lets convert float to int
b_int = int(b) # This will convert the float 3.1 to an integer 3 (it truncates the decimal part)
print("b:", type(b)) # Output: b: <class 'float'>
print("b_int:", type(b_int)) # Output: b_int: <class 'int'> 

# lets convert float to string 
b_str = str(b) # This will convert the float 3.1 to a string "3.1"
print("b:", type(b)) # Output: b: <class 'float'>
print("b_str:", type(b_str)) # Output: b_str: <class 'str'> 

# Lets convert string to float 
C_float = float(C) # This will convert the string "5" to a float 5.0
print("C:", type(C)) # Output: C: <class 'str'>
print("C_float:", type(C_float)) # Output: C_float: <class 'float'>     

# Lets convert string to integer
C_int = int(C) # This will convert the string "5" to an integer 5
print("C_int:", type(C_int)) # Output: C_int: <class 'int'>         







