# Equals (=) 
a = 10
print(a) # Output: 10

# Addition assignment (+=)
a += 5 # Equivalent to a = a + 5
print(a) # Output: 15

# Subtraction assignment (-=)
a -= 3 # Equivalent to a = a - 3
print(a) # Output: 12

# Multiplication assignment (*=)
a *= 2 # Equivalent to a = a * 2
print(a) # Output: 24

# Division assignment (/=)
a /= 4 # Equivalent to a = a / 4
print(a) # Output: 6.0

# Modulus assignment (%=)
a %= 5 # Equivalent to a = a % 5
print(a) # Output: 1.0  

# Floor division assignment (//=)
a //= 2 # Equivalent to a = a // 2
print(a) # Output: 0.0  

# Exponentiation assignment (**=)
a **= 3 # Equivalent to a = a ** 3
print(a) # Output: 0.0  

#Note that in Python there are also some built in functions that perform basic math operations.

# divmod() function
a, b = divmod(10, 3) # Returns the quotient and remainder
print(a, b) # Output: 3 1   

# pow() function
result = pow(2, 3) # Equivalent to 2 ** 3
print(result) # Output: 8   

#sum() function
numbers = [1, 2, 3, 4, 5, -6] # A list of numbers
total = sum(numbers) # Returns the sum of all elements in the list
print(total) # Output: 15

# or we can also write like this
print(sum([1, 2, 3, 4, 5])) # Output: 15

# max() function
max_value = max(numbers) # Returns the maximum value in the list
print(max_value) # Output: 5

# min() function
min_value = min(numbers) # Returns the minimum value in the list
print(min_value) # Output: 1

# round() function
rounded_value = round(3.14159, 2) # Rounds the number to 2 decimal places
print(rounded_value) # Output: 3.14 
b = round(rounded_value, 1) # Rounds the number to 1 decimal place
print(rounded_value, b) # Output: 3.14 3.1

