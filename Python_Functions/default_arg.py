# DEFAULT ARGUMENTS

# In the last section, we learned about POSITIONAL AND KEYWORD ARGUMENTS, 
# and how to use them in function calls. In this section, we will learn about DEFAULT ARGUMENTS.
# The main idea behind default arguments is that we can provide a default value for a parameter in a function definition.

# for example, in the world of IT networking, we can define a function to connect to a server with a default port number. If the user does not provide a port number, the function will use the default value.

# Here is an example of a function that connects to a server with a default port number:

def connect_to_server(host, port=80):
    print(f"Connecting to {host} on port {port}...")

# We can call this function with or without specifying the port number:
connect_to_server("example.com")  # Uses default port 80
connect_to_server("example.com", 443)  # Uses specified port 443

# In this example, the function connect_to_server has two parameters: host and port. The port parameter has a default value of 80. If the user does not provide a value for port, the function will use the default value of 80.

# Default arguments must be placed after non-default arguments in the function definition. If we try to define a function with a default argument before a non-default argument, Python will raise a SyntaxError.

# For example, the following function definition is invalid:
# def connect_to_server(port=80, host):
#     print(f"Connecting to {host} on port {port}...")


