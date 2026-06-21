# RETURN STATEMENT
# A return statement is used to send a value back to the caller of the function. When a function is called, it can perform some operations and then return a value using the return statement. The returned value can be stored in a variable or used directly in expressions.

# returning and printing a value are different actions. 

# in the world of IT networking, a return statement is like a response from a server to a client. When a client sends a request to a server, the server processes the request and sends back a response. Similarly, when a function is called, it processes the input and sends back a value using the return statement.

# lets see and example of return statement

def add(a, b):
    result = a + b
    return result

# We can call this function and store the result in a variable:
result = add(10, 5)
print(result)  # Output: 15

# In this example, the function add takes two parameters: a and b. The function returns the sum of a and b using the return statement. The returned value is then stored in the variable result and printed.


n = len([1, 2, 3, 4, 5])
print(n)  # Output: 5
# In this example, the len function returns the length of the list [1, 2, 3, 4, 5], which is 5. The returned value is stored in the variable n and printed.

def add1(a, b):
    print(f'sum: {a + b}')
# In this example, the function add1 takes two parameters: a and b. The function prints the sum of a and b but does not return any value. If we try to store the result of add1 in a variable, it will be None because the function does not have a return statement.

def add2(a, b):
    s = a + b
    return s
# In this example, the function add2 takes two parameters: a and b. The function calculates the sum of a and b, stores it in the variable s, and then returns s using the return statement. This allows us to store the result of add2 in a variable and use it

add1(10, 20)  # Output: sum: 30
my_sum = add2(5, 2)
print(my_sum)  # Output: 7
# In this example, we call the add1 function with the arguments 10 and 20. The function prints the sum of 10 and 20, which is 30. However, since add1 does not return any value, if we try to store its result in a variable, it will be None.

def func1():
    pass # The pass statement is a placeholder that does nothing. It is used when we want to define a function that we haven't implemented yet. The function func1 does not return any value, so if we try to store its result in a variable, it will be None.]
x = func1()
print(x)  # Output: None

# also 
print(add1(1, 2))  # Output: sum: 3 and None
# In this example, we call the add1 function with the arguments 1 and 2. The function prints the sum of 1 and 2, which is 3. However, since add1 does not return any value, the print statement will output None after printing the sum.


# a function can resturn more then one value. 
# example: 
def my_func(x): 
    return x, x**2, x**3, x**4
print(my_func(3))  # Output: (3, 9, 27, 81) # we notice its a tuple.

# we can keep it as it or we can do tuple unpacking.
a, b, c, d = my_func(10)
print(a, b, c, d)  # Output: 10 100 1000 10000 - I got the values in separate variables.

x, *y = my_func(4)
print(x, y)  # Output: 4 [16, 64, 256] - I got the first value in x and the rest in a list y.



