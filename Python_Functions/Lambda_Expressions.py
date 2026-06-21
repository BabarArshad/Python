# A lambda expression is a small anonymous (unnamed) function. It is mainly used when you need a simple function for a short period of time.

# Normal Function
def square(x):
    return x * x

print(square(5))

# Output:25

# Lambda Function
square = lambda x: x * x

print(square(5))

# Output:25

# Lambda functions are A tiny functions, If your logic needs multiple lines, use a normal function.