# Lets make the exception is a warning instead of an error

try:
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    c = a / b
    print('Result:', c)
except: 
    print('Warning: an error occurred')
# if we run the code and 20 and 10 it will print the result 2.0 but if we run the code and 20 and 0 it will print the warning message instead of throwing an error

else:
    print('No error occurred')
    print(f'Final Result: {c}') 
# we use else block when the try block does not raise any exception. The else block will be executed only if the try block is successful and no exceptions are raised.

finally:
    print('Execution completed') 
# The finally block will always be executed regardless of whether an exception was raised or not. It is typically used for cleanup actions that must be executed
