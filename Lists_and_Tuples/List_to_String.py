# Split() and Join() are two string methods in Python that are used to manipulate strings and lists.
# The split() method is used to split a string into a list of substrings based on a specified delimiter.
# The join() method is used to join a list of strings into a single string, with a specified delimiter between each string.     
# both are string method and not list method, but they are commonly used to convert between strings and lists.

# Example of split() method
string = "Hello, World!"
list_of_strings = string.split(", ")
print(list_of_strings)  # Output: ['Hello', 'World!']   

# Example of join() method
list_of_strings = ['Hello', 'World!']
string = ", ".join(list_of_strings)
print(string)  # Output: "Hello, World!"    

