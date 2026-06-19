# Opening and reading files in Python
# To open a file, we can use the built-in open() function. It takes the file name as an argument and returns a file object.

# Example: Opening a file
file = open('configuration.txt', 'r')  # 'r' stands for read mode
content = file.read()  # Read the entire content of the file
print(content)  # Print the content of the file
print (file.closed)  # Check if the file is closed (should be False)
file.close()  # Close the file after reading
print (file.closed)  # Check if the file is closed (should be True)





