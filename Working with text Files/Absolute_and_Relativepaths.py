# Absolute and Relative Paths in Python

f = open('settings.txt')

# example of absolute path:
# /Users/babararshad/python-projects/venv1/Working with text Files/settings.txt 

f = open('/Users/babararshad/python-projects/venv1/Working with text Files/settings.txt')

# this works in MAC but in windows, the path would look like this:
# C:\Users\babararshad\python-projects\venv1\Working with text Files\settings.txt 
#and due to the backslashes, we will see error. 
# To avoid this, we can use raw strings in Python by prefixing the string with 'r'. This tells Python to treat the backslashes as literal characters.


# f = open(r'C:\Users\babararshad\python-projects\venv1\Working with text Files\settings.txt')


# Relative paths - are paths that are relative to the current working directory. The current working directory is the directory from which the Python script is being executed.
# . - represents the current directory
# .. - represents the parent directory
# Example of relative path:
f = open('settings.txt')  # This will look for settings.txt in the current working directory.
# and if the file is in parrent directory, we can use:  
f = open('../test.txt')  # This will look for settings.txt in the parent directory.



