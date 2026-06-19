# With statement 

with open('configuration.txt', 'r') as file:
    content = file.read()
    print(content)

# The with statement automatically closes the file after the block of code is executed, even if an error occurs. This ensures that resources are properly managed and prevents potential memory leaks or file corruption.

print(file.closed)  # Output: True

# You can also use the with statement to write to a file:
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a test file.\n')
# The output.txt file will contain the following content:
# Hello, World!
# This is a test file.  

