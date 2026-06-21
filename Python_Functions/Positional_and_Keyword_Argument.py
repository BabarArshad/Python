# Lets start with FUNCTION ARGUMENTS

# There are a total of 4 types of function arguments in Python:
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable-length Arguments (*args and **kwargs)


# 1. Positional Arguments
# Positional arguments are the most common type of arguments. They are passed to a function in the order in which they are defined in the function. The number of positional arguments passed to a function

# must match the number of parameters defined in the function.

def difference(a, b):
    result = a - b
    print(result)

difference(10, 5)  # Output: 5

# PARAMETERS VS ARGUMENTS
# Parameters are the variables that are defined in the function definition. They act as placeholders for the values that will be passed to the function when it is called. Arguments, on the other hand,
# are the actual values that are passed to the function when it is called. In the example above, 'a' and 'b' are parameters, while '10' and '5' are arguments.


# 2. Keyword Arguments
# Keyword arguments are a type of function argument that allows you to specify the name of the parameter

def func1(x, y, z):
    print(f'1st parameter of x is {x}')
    print(f'2nd parameter of y is {y}')
    print(f'3rd parameter of z is {z}')

func1(z=30, x=10, y=20) # Output:
# 1st parameter of x is 10
# 2nd parameter of y is 20
# 3rd parameter of z is 30

# However, if we type 
func1(10, 20, 30) # this will also give the same output as above. However, in this case, we are using positional arguments, and the order of the arguments matters. In the first example, we are using keyword arguments, and the order of the arguments does not matter as long as we specify the parameter names.

# In the above example, we have defined a function 'func1' that takes three parameters: 'x', 'y', and 'z'. When we call the function, we can specify the name of the parameter along with its value. This allows us to pass the arguments in any order we want, as long as we specify the parameter names.


# Positional VS Keyword Arguments
# There no differnce when defining the fuction. However, there is difference when calling the function. In positional arguments, the order of the arguments matters, while in keyword arguments, the order does not matter as long as we specify the parameter names.

func1(6, z=1, y=9) # Output:
# 1st parameter of x is 6
# 2nd parameter of y is 9
# 3rd parameter of z is 1  

#However, if we try 
#func1(X=6, 1, Z=9) # this will give an error because we are trying to pass a positional argument after a keyword argument. In Python, positional arguments must be passed before keyword arguments.